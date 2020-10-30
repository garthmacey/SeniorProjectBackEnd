from .GitCaller import GitCaller
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from django.http import HttpResponse
from .FileTreeBuilder import FileTreeBuilder
import json
import http
import os


def GetFileNames(request):
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
    repoResponse = json.loads(git_caller.get_fileNames(project, repo))
    if repoResponse == '-1':
        response = HttpResponse(status=http.HTTPStatus.NOT_FOUND, content="Repo not found")
        response["Access-Control-Allow-Origin"] = "*"
        return response

    parsedFileNames = ParseFileNames(repoResponse['value'])
    data = {'files': parsedFileNames}
    response = HttpResponse(status=http.HTTPStatus.OK, content=json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def GetTestFrameworkBranches(request):
    # Get list of test framework branches.
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
    gitCaller = GitCaller(util)

    branchJson = gitCaller.get_listOfBranches(project, repo)
    branches = ParseBranchData(branchJson)

    data = {'branches': branches}
    response = HttpResponse(status=http.HTTPStatus.OK, content=json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def GetRepos(request):
    # Returns a list of repos for the given project.
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response

    token = request.headers['azure']
    organization = request.headers['organization']
    project = request.GET["project"]

    util = Utilities(token, organization)
    gitCaller = GitCaller(util)

    repoJson = gitCaller.get_listOfRepos(project)
    repos = ParseRepos(repoJson)

    data = {'repos': repos}
    response = HttpResponse(status=http.HTTPStatus.OK, content=json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def GetFileTreeStructure(request):
    # Returns a json node tree object that is formatted for the material-ui tree component.
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
    gitCaller = GitCaller(util)
    fileTreeBuilder = FileTreeBuilder()
    # grabs the items in the repo and builds a Tree Structure from it
    items_response = json.loads(gitCaller.get_fileNames(project, repo))
    
    data = fileTreeBuilder.build_tree_structure(items_response)[0]
    treeData = {"treeData": data}
    response = HttpResponse(status=http.HTTPStatus.OK, content=json.dumps(treeData))
    response["Access-Control-Allow-Origin"] = "*"
    return response


# Private Helpers

#
# fullPathsList: A list of file paths in json format.
# Returns an array of filename.filetype strings.
#
def ParseFileNames(fullPathsList):
    # parse file names from the list of full file paths
    fileList = []
    for filePath in fullPathsList:
        if 'isFolder' in filePath:  # isFolder attribute only exists on folder paths, so we have to check for existence instead of true/false
            continue
        fileList.append(os.path.basename(filePath['path']))
    return fileList


#
# branchData: A list of branch metadata in json format.
# Returns an array of branch names.
#
def ParseBranchData(branchData):
    branchjson = json.loads(branchData)['value']
    branches = []
    for branch in branchjson:
        branchName = branch['name'].split('/')[2]
        branches.append(branchName)
    return branches


def ParseRepos(fullRepoList):
    repojson = json.loads(fullRepoList)['value']
    repos = []
    for repo in repojson:
        repoName = repo['name']
        repos.append(repoName)
    return repos
