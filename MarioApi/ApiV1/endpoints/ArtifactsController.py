from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .ArtifactsCaller import ArtifactsCaller
from django.http import HttpResponse 
from django.http import HttpRequest
from http import HTTPStatus
import json


#How to retrieve artifacts
def get_ArtifactData(request : HttpRequest):
    """
    This gets all of the artifacts for a 
    specific drive type and test environment.
    Can select artifacts via name or all artifacts.
    Parameters:
        request (HttpRequest) : The request from the front end
    Returns:
        HttpResponse: The list of artifacts or if none where found 
        an empty array of values with count zero is returned.
    """
    emptyResponse = { "count" : 0, "value" : []}
    defaultResponse = HttpResponse(status=HTTPStatus.BAD_REQUEST)

    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    if request.method == "GET":
        jsonbody = json.loads(request.body);
        token = request.headers['azure']
        organization = request.headers['organization']
        project = jsonbody['project']
        driveType = jsonbody['driveType']
        testEnv = jsonbody['testEnv']
        util = Utilities(token, organization)
        ac = ArtifactsCaller(util)
        dbCaller = DatabaseCaller()
        buildId = dbCaller.buildIDs_get(driveType, testEnv)

        if buildId == None:
            return HttpResponse(status=HTTPStatus.OK, reason="Could not find a build with specified parameters")
        if 'name' in jsonbody:
            artifact_name = jsonbody['name']
            data = ac.get_ArtifactByName(project, buildId, artifact_name)
            if data == HTTPStatus.NOT_FOUND:
                response = HttpResponse(json.dumps(emptyResponse), content_type="application/json", status=HTTPStatus.OK)
                response["Access-Control-Allow-Origin"] = "*"
                return response
            else:
                response = HttpResponse(data, content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                return response
        else:
            data = ac.get_ListOfArtifacts(project, buildId)
            if data == HTTPStatus.NOT_FOUND:
                response = HttpResponse(json.dumps([]), content_type="application/json", status=HTTPStatus.OK)
                response["Access-Control-Allow-Origin"] = "*"
                return response
            response = HttpResponse(data, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            return response
    else:
        return defaultResponse
