import os
import json

json_data = {
    "count": 57,
    "value": [
        {
            "objectId": "a6220c86aa9b661418062497e9cb5af653b27714",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/d5a809eb-7f7b-45cd-ae75-8360371b0bf2/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items?path=%2F&versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "894a44cc066a027465cd26d634948d56d13af9af",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/.gitignore",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//.gitignore?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "777afa1a61a908a959935ab92d93e9fca5f473e7",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "fee0f8150d97dfe3ee2fa6badad8b6308cb6b025",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "2d7fa485463805a2499a61a95511357e7566a471",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/UnitTests",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/UnitTests?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/UnitTests/__init__.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/UnitTests/__init__.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "9ac73a2b3b5574edc579264a38a083bc8bd999bb",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/UnitTests/stubs",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/UnitTests/stubs?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "123a21fc5752b5b4365358011638ef0953058778",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/UnitTests/stubs/ConfigurationControllerStubs.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/UnitTests/stubs/ConfigurationControllerStubs.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "4b7c4319f98ef459d29358cacc6ae5eeee48201b",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/UnitTests/testConfigurationController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/UnitTests/testConfigurationController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "8c38f3f3dad51e4585f3984282c2a4bec5349c1e",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/admin.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/admin.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "f6be17c8fb267225bd34cc5256941432cf96cf56",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/apps.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/apps.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "6f7d698f6fd74710488f436eca5a0562e3a8c9e8",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "008dc8bc36901c96199c896332c6b1be52028742",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ArtifactsCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ArtifactsCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "edeb80895102ee91bca5d013bfe451d55f753e17",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ArtifactsCallerStub.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ArtifactsCallerStub.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "5e4fabd3dffce75e85ae4b9d803d1b5f825f3b07",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ArtifactsCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ArtifactsCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "5b0ce50999a97b278c944385d3904f1adbdba18b",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/BuildsCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/BuildsCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "70ee9471c75e2e881f0cc4e41bd1df5e7aacf134",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/BuildsCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/BuildsCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "354a13f42df44a59ddb9785998c4aa0f7a54637d",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/BuildsController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/BuildsController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "f660dd2614271ad74c527efbb953637ec87d8456",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ConfigurationController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ConfigurationController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "9a0dec0e4a41fdb943e6585876e520f9fafe162c",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/DatabaseCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/DatabaseCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "072a107c65c9dacc24574fddb136cf0acc117181",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/DatabaseCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/DatabaseCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "4055b2e4b7cd59f87c540fe012f1be981d6029f8",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/DatabaseCallerTestInit.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/DatabaseCallerTestInit.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "0f39411761b0bfa5c04d828b4245c0581166fb2f",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/DatabaseInit.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/DatabaseInit.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "071bc3b60171cb3a2cb45a89206b793c9424dcf1",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/DemoScript.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/DemoScript.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "7ab3f789d41f85bae14005ace3ab290733ba4eb3",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/GitCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/GitCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "8e41b272df82aa1e04922b27e3a20d9be0fff96d",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/GitCallerStub.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/GitCallerStub.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "21065b7077c4640e9cd491d213addbf6b3e4ca96",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/GitCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/GitCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e9b46aa304da084a3fcdb1f289dc9d5fe8b2913b",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/GitController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/GitController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e887386b3957531d899a3b78568ae342c4370f22",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/GitControllerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/GitControllerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e4ab8319a1641ccf375f17bc909a3a79a15617d8",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ProjectCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ProjectCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e03e8e319e6a36ef180dd4e8772a62dc689baba8",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ProjectCallerStub.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ProjectCallerStub.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "fc3f52ac5c00e268aa74557b0129cfc69bab2125",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ProjectCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ProjectCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "43ebe95c41c76d564f30055a8bc444190594ed85",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ProjectController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ProjectController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "b2ede701bba4c704beda0aeaf7bd95e0f882b578",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/ProjectControllerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/ProjectControllerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "c875bf3ffc81252a93fbae99b647d7d76168ac6a",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/QueueCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/QueueCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "9df61ec96677244cc99e28ceb2ea0b23be6f8949",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/QueueCallerStub.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/QueueCallerStub.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "ffd2220e2763bf9ad301ccfd9c3e3167c9cde523",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/QueueCallerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/QueueCallerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "5d5957fd8ab2916c3936058fa237106a73980062",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/QueueController.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/QueueController.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "3ebddc734db2a5bad2d97768c7aaae6bb686f242",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/QueueControllerTest.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/QueueControllerTest.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "f08144f28e35c085d1735a7bac40222ccfcad023",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/TestDatabaseCaller.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/TestDatabaseCaller.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "f0dddc614afa5d34b3c3066a69d0bbe1f1960781",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/endpoints/Utilities.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/endpoints/Utilities.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "9d1dcfdaf1a6857c5f83dc27019c7600e1ffaff8",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/migrations",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/migrations?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/migrations/__init__.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/migrations/__init__.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "71a836239075aa6e6e4ecb700e9c42c95c022d91",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/models.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/models.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "adc773cd618b58c5c90b98306cca5f85a9977f66",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/tests.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/tests.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "b264f921b8b247f48ad77b12a8eaa20d0546cbca",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/urls.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/urls.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "91ea44a218fbd2f408430959283f0419c921093e",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/ApiV1/views.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/ApiV1/views.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "03f3a99de04a37da033a35eac7273a67f747a915",
            "gitObjectType": "tree",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/MarioApi",
            "isFolder": True,
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/MarioApi?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/MarioApi/__init__.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/MarioApi/__init__.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "3b9ac59c3cb8d17d5eeab7fcf876fca079d7c860",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/MarioApi/settings.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/MarioApi/settings.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "0e8904882c77b2cdeac1dee75216c158d2839776",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/MarioApi/urls.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/MarioApi/urls.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "7dc43064735ba8ccb5799b7ade497c28b241c658",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/MarioApi/wsgi.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/MarioApi/wsgi.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "4b62d69064d626993e1c3e3fb80bbba70059592b",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/MarioApi/manage.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//MarioApi/manage.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "213702d05448ca93112e931b3a3a6538e1d4aa44",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/Mario_GetToken.py",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//Mario_GetToken.py?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "690627b172bf10148d4679b4326811869d3150bd",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/README.md",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//README.md?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "71d9051db493be8c075c2346bf128ec68ed7cb3b",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/README_getToken.txt",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//README_getToken.txt?versionType=Branch&versionOptions=None"
        },
        {
            "objectId": "3b1591d83777ca070a6ef562810905bd239a96cd",
            "gitObjectType": "blob",
            "commitId": "b200ade364c651cedf984875bc779620f7bc8d51",
            "path": "/azure-pipelines.yml",
            "url": "https://dev.azure.com/adasupershi/SE4330-Mario/_apis/git/repositories/0fd9bae1-3a79-4731-8d1d-e6435a333bc3/items//azure-pipelines.yml?versionType=Branch&versionOptions=None"
        }
    ]
}


# returns the list of folders found within the specified repository
def get_folder_list(json_response):
    folder_list = []
    count = len(json_response['value'])
    index = 0

    while count > 0:
        if 'isFolder' in json_response['value'][index]:
            folder_list.append(os.path.basename(json_response['value'][index]['path']))
        count -= 1
        index += 1

    # print(folder_list)
    return folder_list


# returns the list of files found within the specified repository
def get_file_list(json_response):
    file_list = []
    count = len(json_response['value'])
    index = 0

    while count > 0:
        if json_response['value'][index]['gitObjectType'] == "blob":
            file_list.append(os.path.basename(json_response['value'][index]['path']))
        count -= 1
        index += 1

    # print(file_list)
    return file_list


get_folder_list(json_data)
get_file_list(json_data)







