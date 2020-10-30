import json
import http
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .BuildsCaller import BuildsCaller
from .TestRunsCaller import TestRunCaller
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import time


@csrf_exempt
def queue_build(request):
    """
    Given a drive type, environment, and artifacts, will queue a build on the project.
    :return: HTTP response with number of failed responses, number of runs ran, and response code
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    jsonbody = json.loads(request.body)
    util = Utilities(token, organization)
    buildcaller = BuildsCaller(util)

    project = jsonbody["project"]
    testEnv = jsonbody["testEnv"]
    driveType = jsonbody["driveType"]
    pcArtifacts = None
    appArtifacts = None
    ccArtifacts = None
    if 'PCArtifacts' in jsonbody and "APPArtifacts" in jsonbody and "CCArtifacts" in jsonbody:
        pcArtifacts = jsonbody["PCArtifacts"] #develop
        appArtifacts = jsonbody["APPArtifacts"] 
        ccArtifacts = jsonbody["CCArtifacts"]
    numberOfRuns = jsonbody["numberOfRuns"]
    branchSelections = ""#jsonbody[""]
    
    dbCaller = DatabaseCaller()
    buildId = dbCaller.buildIDs_get(driveType, testEnv)
    build_responses = []

    for num in range(0, numberOfRuns):
        build = buildcaller.queue_build(project, buildId, pcArtifacts, appArtifacts, ccArtifacts)
        build_responses.append(build)

    failedResponses = 0
    responseNotFound = False
    for build in build_responses:
        if build != 200:
            failedResponses += 1
        if build == 404:
            responseNotFound = True
    response = HttpResponse(status= http.HTTPStatus.OK)
    if responseNotFound == True:
        response = HttpResponse(status=http.HTTPStatus.NOT_FOUND)
    if failedResponses > 0:
        response = HttpResponse(status= http.HTTPStatus.BAD_REQUEST)

    response["Access-Control-Allow-Origin"] = "*"
    body = json.dumps({"failedResponses": failedResponses, "numberOfRuns": numberOfRuns, "buildResponse": response.status_code})
    response.content = body
    return response

def list_of_builds(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response

    token = request.headers["azure"]
    organization = request.headers["organization"]
    project = request.GET["project"]
    #lastWeek = datetime.now() - timedelta(days=7)

    util = Utilities(token, organization)
    buildCaller = BuildsCaller(util)
    tCaller = TestRunCaller(util)
    rawTestData = tCaller.get_allTestRuns(project)
    if type(rawTestData) == int:
        response = HttpResponse(status=rawTestData)
    else:
        testData = json.loads(rawTestData)['value']
        testArray = {}
        for test in testData:
            id = str(test['build']['id'])
            try:
                testArray[id]
            except:
                testArray[id] = {}
                testArray[id]['totalTests'] = 0
                testArray[id]['passedTests'] = 0
            testArray[id]['totalTests'] += test['totalTests']
            testArray[id]['passedTests'] += test['passedTests']

        #buildParams = {"minTime": str(lastWeek.isoformat())}
        rawBuildData = buildCaller.get_listOfBuilds(project) #, buildParams)
        if type(rawBuildData) == int:
            response = HttpResponse(status=rawBuildData)
        else:
            buildData = json.loads(rawBuildData)['value']

            buildsList = []
            for build in buildData:
                if build['status'] == 'completed':
                    result = build['result']
                    finishTime = build['finishTime']
                    finishTime = finishTime[0:19]
                    finishTime = datetime.strptime(finishTime, "%Y-%m-%dT%H:%M:%S").strftime('%m/%d/%Y %I:%M%p')
                    #ratio = list_of_test_runs(util, build['id'], project)
                    id = str(build['id'])
                    try:
                        ratio = str(testArray[id]['passedTests']) + "/" + str(testArray[id]['totalTests'])
                    except:
                        ratio = "No Tests"
                else:
                    result = 'inProgress'
                    finishTime = 'inProgress'
                    ratio = "No Tests"

                queuedTime = build['queueTime']
                queuedTime = queuedTime[0:19]
                queuedTime = datetime.strptime(queuedTime, "%Y-%m-%dT%H:%M:%S").strftime('%m/%d/%Y %I:%M%p')
                author = build['requestedBy']
                authors = author['displayName']

                buildsList.append({"id": build['id'], "buildNumber": build['buildNumber'], "finishedTime": finishTime,
                                   "status": build['status'], "author": authors, 'tags': build['tags'], 'results': result,
                                   'queuedTime': queuedTime, 'ratio' : ratio})
            data = {'builds': buildsList}
            response = HttpResponse(json.dumps(data), content_type="application/json")

    response["Access-Control-Allow-Origin"] = "*"
    return response


def getLastBuild(request):
    """
    Retrieves the most recently ran build that was queued.
    :param request:
    :return: HTTP response containing the last build information
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    project = request.GET['project']
    nameId = request.GET['nameId']
    util = Utilities(token, organization)
    buildcaller = BuildsCaller(util)
    lastBuild = buildcaller.get_latestBuild(project, 1, nameId)
    response = HttpResponse(lastBuild, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def list_of_test_runs(util, buildId, project):
    """
    Retrieves the list of runs and finds the ratio of passed to total tests for the latest run
    :param util: Utilities object
    :param buildId: unique build ID number
    :param project: project name
    :return: Ratio of passed tests to total tests on that build id
    """
    testRunsCaller = TestRunCaller(util)
    testRunData = json.loads(testRunsCaller.get_list_of_runs(project, buildId))['value']
    if not testRunData:
        return 'No Tests'
    totalTests = []
    passedTests = []
    for test in testRunData:
        totalTests.append(test['totalTests'])
        passedTests.append(test['passedTests'])
    # incompleteTests = testRun['incompleteTests']
    # completedTests = totalTests - incompleteTests
    ratio = str(passedTests.pop()) + '/' + str(totalTests.pop())
    return ratio
