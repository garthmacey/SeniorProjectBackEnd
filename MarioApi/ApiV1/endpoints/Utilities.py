import json
import requests

# Utility Class containing common methods for API Callers and Controllers
from .ProjectCaller import ProjectCaller

class Utilities:

    def __init__(self, token, organization):
        self.token = token
        self.organization = organization

    def getRequest(self, url, args={}):
        """
        :param url: HTTP URL to be called
        :param args: Optional additional arguments
        :return: HTTP status code
        """
        fullURL = self.__getURL(url, args)
        response = requests.get(url=fullURL, headers=self.__getHeader())
        if response.status_code == 200:
            return json.loads(json.dumps(response.content.decode('utf-8')))
        return response.status_code

    def postRequest(self, url, data, args=dict()):
        """
        :param url: HTTP URL to be called
        :param args: Optional additional arguments
        :return: HTTP status code
        """
        fullURL = self.__getURL(url, args)
        response = requests.post(url=fullURL, data=data, headers=self.__getHeader())
        return response.status_code

    def deleteRequest(self, url, args={}):
        """
        :param url: HTTP URL to be called
        :param args: Optional additional arguments
        :return: HTTP status code
        """
        fullURL = self.__getURL(url, args)
        response = requests.delete(url=fullURL, headers=self.__getHeader())
        return response.status_code

    def __getHeader(self):
        """
        :return: Header including authorization token and content type
        """
        return {"Authorization": "Bearer {}".format(self.token), "Content-Type": "application/json"}

    def __getURL(self, url, args):
        """
        :return: Constructed url given the organization, url, and optional arguments
        """
        fullURL = "https://dev.azure.com/" + self.organization + url
        c = "?"
        for key, value in args.items():
            fullURL = fullURL + c + key + "=" + value
            c = "&"
        return fullURL

    def checkParams(self, jsonbody, optionalParams):
        """
        This goes through a json object and checks each
        parameter specified in the optionalParams list of strings.
        If the parameter does not exist, create one with a
        value of None.
        Parameters:
            jsonbody (json) : The json object to edit.
            optionalParams (str []) : The list of parameters to check
        """
        for parameter in optionalParams:
            try:
                jsonbody[parameter]
            except:
                jsonbody[parameter] = None

    def securityCheck(self):
        pcaller = ProjectCaller(self)
        check = pcaller.get_listOfProjects()
        if type(check) == int:
            return check
        else:
            return 200
