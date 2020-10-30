import requests
import webbrowser
import urllib.parse
import json
import http.client
import urllib.request

#from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

import re
import json

from getpass import getpass
#JP is a big bot

class Mario_GetToken:
    
    client_id = "07CCF41A-C82C-4411-A8A1-58CFB9A254A0" #Working one
    state = "user1"
    scope = "vso.build_execute vso.code_full vso.graph_manage vso.loadtest_write vso.profile_write vso.project_manage vso.release_manage vso.test_write vso.tokenadministration vso.work_full"
    callback_URL = "https://dev.azure.com/adasupershi" #Good one
    
    clientSecret = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im9PdmN6NU1fN3AtSGpJS2xGWHo5M3VfVjBabyJ9.eyJjaWQiOiIwN2NjZjQxYS1jODJjLTQ0MTEtYThhMS01OGNmYjlhMjU0YTAiLCJjc2kiOiI5MGVjOTNjMS00MWZiLTQ2NjctOTJiOS00MjQ0OWNlZWUzY2EiLCJuYW1laWQiOiI3ODJkNDVhMy05ZGY0LTQ3NjAtYjRkNi1hMWMxZTNiMjRlZDUiLCJpc3MiOiJhcHAudnN0b2tlbi52aXN1YWxzdHVkaW8uY29tIiwiYXVkIjoiYXBwLnZzdG9rZW4udmlzdWFsc3R1ZGlvLmNvbSIsIm5iZiI6MTU4ODg4NDg1MCwiZXhwIjoxNzQ2NjUxMjUwfQ.vqhNHkmgNPrYHYjZfuIqA5f26j7CEiiK_oUFItED742a_-aoLYPvz_FKfy-tg7uGCVuk1MdkR9bcUNHxG_YiA9mUSHbvyWIZuDTGROfkLMiFEcsshCjyqI6z0_PNWCLZ7lK38KOUjZrp2y66-BYfWbjZ3yEqfNmhv_ILZAb5sLXjbA12uJNP4Ln8s6mY3dImoAmutDTyUb-AYzOYiVULINN3UFo2X_sxaJZRixLgUJEkQbU752utxOT52A7mcCIoG1R6Xa-NPxCyZyZYPldj0gWYoCyXyOEQAq5-2zJPne_QjGzDIJo1eDZKFCsN1YiaXxWyFvjxnSr9neKSqyMq4A"
        
    refreshingToken = ""
    
    def get_authenticated(self):

        # Azure DevOps Services authorization endpoint
        Auth_URL = "https://app.vssps.visualstudio.com/oauth2/authorize?client_id=" + self.client_id + "&response_type=Assertion&state=" + self.state + "&scope=" + self.scope + "&redirect_uri=" + self.callback_URL
        
        #This opens the link to Authenticate
        webbrowser.open(Auth_URL)
        
        str = input("Paste here the URL(To paste right click): ")
        result = re.search('code=(.*)&state=', str)
        
        code11 = result.group(1)
        
        self.get_token(code11)  #Pass in the code
        
    def get_token(self, codenite):
        API_ENDPOINT = "https://app.vssps.visualstudio.com/oauth2/token"
        
        #Client secret
        first = self.clientSecret
        second = codenite
        
        urlEncodeFirst = urllib.parse.quote_plus(first)
        urlEncodeSecond = urllib.parse.quote_plus(second)
        
        
        data = {
            "client_assertion_type":"urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion":urlEncodeFirst,
            "grant_type":'urn:ietf:params:oauth:grant-type:jwt-bearer',
            "assertion":urlEncodeSecond,
            "redirect_uri":self.callback_URL
        }
        
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        
        r = requests.post(url = API_ENDPOINT, data = data, headers = headers).json()
        
        
        json_data = json.dumps(r)  #Transfer json to string ;)
        print(json_data)
        
        parsed_json = json.loads(json_data)
        
        token11 = parsed_json['access_token']
        refreshToken = parsed_json['refresh_token']
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("//////////REFRESH TOKEN WILL BE AFTER THIS/////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE REFRESH TOKEN: " + refreshToken)
        
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("////////////TOKEN WILL BE AFTER THIS///////////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE TOKEN: " + token11)
        
        self.getRefreshedToke(refreshToken)
      
    def getRefreshedToke(self, refreshToken1):
        API_ENDPOINT = "https://app.vssps.visualstudio.com/oauth2/token"
        
        #Client secret
        first = self.clientSecret
        #Refresh Token obtained when you got the token.
        second = refreshToken1
        
        urlEncodeFirst = urllib.parse.quote_plus(first)
        urlEncodeSecond = urllib.parse.quote_plus(second)
        
         
        data = {
            "client_assertion_type":"urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion":urlEncodeFirst,
            "grant_type":'refresh_token',
            "assertion":urlEncodeSecond,
            "redirect_uri":self.callback_URL
        }
        
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        
        r = requests.post(url = API_ENDPOINT, data = data, headers = headers).json()
        
        
        json_data = json.dumps(r)  #Transfer json to string ;)
        
        
        parsed_json = json.loads(json_data)
        
        accessToken = parsed_json['access_token']
        refreshToken = parsed_json['refresh_token']
        
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("////////////NEW TOKEN WILL BE AFTER THIS///////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE TOKEN: " + accessToken)


def main():
    obj = Mario_GetToken()
    obj.get_authenticated()


 
main()
