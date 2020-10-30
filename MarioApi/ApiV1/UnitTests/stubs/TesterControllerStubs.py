class TesterControllerStubs:

    def TestCase1():
        return [
            {
                "path": "/TestFolder",
                "isFolder": "True",
            },
            {
                "path": "/TestFolder/TestFile.py",
            }
        ]

    def TestCase2():
        return [
            {
                "path": "/TestFolder",
                "isFolder": "True"
            },
            {
                "path": "/TestFolder/NextFolder",
                "isFolder": "True"
            },
            {
                "path": "/TestFolder/NextFolder/TestFile.py"
            }
        ]

    def TestCase3():
        return [
            {
                "path": "/TestFolder",
                "isFolder": "True"
            },
            {
                "path": "/TestFolder/AnotherTestFile.py"
            },
            {
                "path": "/TestFolder/NextFolder",
                "isFolder": "True"
            },
            {
                "path": "/TestFolder/NextFolder/TestFile.py"
            }
        ]