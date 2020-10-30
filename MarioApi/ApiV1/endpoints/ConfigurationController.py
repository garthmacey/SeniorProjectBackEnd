# -*- coding: utf-8 -*-
from .GitCaller import GitCaller
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from django.http import HttpResponse
from django.http import HttpRequest
from .ProjectCaller import ProjectCaller
from http import HTTPStatus
import json
from django.views.decorators.csrf import csrf_exempt


def get_DevData(request):
    """
    Obtains a list of the drive types and environments
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response

    token = request.headers['azure']
    organization = request.headers['organization']
    project = request.GET["project"]
    repo = request.GET["repo"]

    util = Utilities(token, organization)
    git_caller = GitCaller(util)
    database = DatabaseCaller()
    branchdata = git_caller.get_listOfBranches(project, repo)
    if type(branchdata) == int:
        response = HttpResponse(status=branchdata)
    else:
        branches = parseBranchData(branchdata)

        drive_types = database.drive_types_get()
        environments = database.environments_get()

        data = {"TestEnv": environments, "DriveType": drive_types, "Branches": branches}
        response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


def getProjectsInOrganization(request):
    """
    Obtains projects from the organization.
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response

    token = request.headers['azure']
    organization = request.headers['organization']

    util = Utilities(token, organization)

    projectCaller = ProjectCaller(util)

    rawProjects = projectCaller.get_listOfProjects()
    if type(rawProjects) == int:
        response = HttpResponse(status=rawProjects)
    else:
        projectsJson = json.loads(rawProjects)

        projectNames = []

        for projects in projectsJson['value']:
            projectNames.append(projects['name'])

        data = {"Projects": projectNames}
        response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


def parseBranchData(request):
    """
    Helper function to parse through a JSON body containing the branches and returns a list
    """
    branchjson = json.loads(request)['value']
    branches = []
    for branch in branchjson:
        branchName = branch['name'].split('/')[2]
        branches.append(branchName)
    return branches


@csrf_exempt
def endpoint_configmap(request : HttpRequest):
    """
    Configuration map handling method. Checks the request type and passes it to the correct method.
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, DELETE, PATCH"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    util = Utilities(token, organization)
    check = util.securityCheck()
    if check == 200:
        dbCaller = DatabaseCaller()
        jsonbody = json.loads(request.body)
        if request.method == "GET":
            if 'configid' not in jsonbody:
                return get_all_configurations(dbCaller, jsonbody)
            else:
                return get_configuration(dbCaller, jsonbody)
        elif request.method == "PATCH":
            return patch_configuration(dbCaller, jsonbody)
        elif request.method == "DELETE":
            return delete_configuration(dbCaller, jsonbody)
        elif request.method == "POST":
            return post_configuration(dbCaller, jsonbody)
    else:
        response = HttpResponse(status=check)
        response["Access-Control-Allow-Origin"] = "*"
        return response


def post_configuration(db, jsonbody):
    """
    Obtains the information from the configuration page and creates a new configuration record in the database table.
    """
    configID = jsonbody["configid"]
    buildID = jsonbody["buildid"]
    applicationID = jsonbody["applicationid"]
    firmwareID = jsonbody["firmwareid"]
    powercardID = jsonbody["powercardid"]
    success = db.configurations_insert(configID, buildID, applicationID, firmwareID, powercardID)
    if success:
        response = HttpResponse(status=HTTPStatus.OK)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST, reason="Failed to insert data.")
        response["Access-Control-Allow-Origin"] = "*"
        return response


def delete_configuration(db, jsonbody):
    """
    Deletes any given configuration from the database table, given the ID.
    """
    configID = jsonbody["configid"]
    success = db.configurations_delete(configID)
    if success:
        response = HttpResponse(status=HTTPStatus.OK)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST, reason="Failed to delete data")
        response["Access-Control-Allow-Origin"] = "*"
        return response


def patch_configuration(db, jsonbody):
    """
    Updates the configuration with any new data, given the ID and new updated attributes.
    """
    configID = jsonbody["configid"]
    buildID = jsonbody["buildid"]
    applicationID = jsonbody["applicationid"]
    firmwareID = jsonbody["firmwareid"]
    powercardID = jsonbody["powercardid"]
    success = db.configurations_update(configID, buildID, applicationID, firmwareID, powercardID)
    if success:
        response = HttpResponse(status=HTTPStatus.OK)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST, reason="Failed to patch data")
        response["Access-Control-Allow-Origin"] = "*"
        return response


def get_configuration(db, jsonbody):
    """
    Returns a list of the id and attributes of a given configuration record.
    """
    
    configInfo = db.configurations_get(jsonbody['configid'])
    response = HttpResponse(json.dumps(configInfo), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_all_configurations(dbCaller, jsonbody):
    """
    Returns a list of all configurations in the table
    """
    configNames = dbCaller.configurations_get_names()
    configurations = []
    for configName in configNames:
        success = dbCaller.configurations_get(configName)
        if not success:
            response = HttpResponse(status=HTTPStatus.INTERNAL_SERVER_ERROR, reason="Internal Database Error")
            response["Access-Control-Allow-Origin"] = "*"
            return response
        jsonified = {
            'configID': configName,
            'buildid' : success[0], 
            'drivetype' : success[1],
            'environment' : success[2],
            'applicationid' : success[3],
            'firmwareid' : success[4],
            'powercardid' : success[5],
            }
        configurations.append(jsonified)
    jsonOut = {
        'count' : str(len(configurations)),
        'configurations' : configurations
    }
    response = HttpResponse(json.dumps(jsonOut), status=HTTPStatus.OK, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
