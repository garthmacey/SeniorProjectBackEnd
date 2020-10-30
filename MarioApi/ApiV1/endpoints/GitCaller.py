import json
import requests
from .Utilities import Utilities

#This class calls Azure's Git Api
class GitCaller:
       
    def __init__(self, util):
        self.util = util
    
    #This method returns the Repo List given the organization and project ID, in json string form.
    def get_listOfRepos(self, project):
        url = "/" + project + '/_apis/git/repositories'
        return self.util.getRequest(url)


    #This method returns the branch list, given the organization, project ID and Repo Name, in json string form.
    def get_listOfBranches(self, project, repo):
        url = "/" + project + '/_apis/git/repositories/{0}/refs'.format(
            repo)
        return self.util.getRequest(url)

    #Find repo that matches provided repo name
    def get_RepoId(self, project, repo):
        url = "/{0}/_apis/git/repositories".format(project)
        repoList = json.loads(self.util.getRequest(url))['value']
        for repoTemp in repoList:
            if repoTemp["name"] == repo:
                return repoTemp["id"]
        return -1

    def get_fileNames(self, project, repo):
        repoId = self.get_RepoId(project, repo)
        if repoId == -1:
            return repoId #If the repo was not found, return -1 and let controller do error handling and do not send next request to azure.

        url = "/{0}/_apis/git/repositories/{1}/items?includeContentMetadata=true&recursionLevel=full".format(project, repoId)
        return self.util.getRequest(url)