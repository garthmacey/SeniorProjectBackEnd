from ProjectCaller import ProjectCaller
import json


class ProjectCallerStub(ProjectCaller):
    jsonListTest = {
        "count": 3,
        "value": [
            {
                "id": "eb6e4656-77fc-42a1-9181-4c6d8e9da5d1",
                "name": "Fabrikam-Fiber-TFVC",
                "description": "Team Foundation Version Control projects.",
                "url": "https://dev.azure.com/fabrikam/_apis/projects/eb6e4656-77fc-42a1-9181-4c6d8e9da5d1",
                "state": "wellFormed"
            },
            {
                "id": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "name": "Fabrikam-Fiber-Git",
                "description": "Git projects",
                "url": "https://dev.azure.com/fabrikam/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "state": "wellFormed"
            },
            {
                "id": "281f9a5b-af0d-49b4-a1df-fe6f5e5f84d0",
                "name": "TestGit",
                "url": "https://dev.azure.com/fabrikam/_apis/projects/281f9a5b-af0d-49b4-a1df-fe6f5e5f84d0",
                "state": "wellFormed"
            }
        ]
    }

    def listAPICaller(self, organization):
        return json.dumps(self.jsonListTest)