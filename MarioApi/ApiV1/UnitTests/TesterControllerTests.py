from django.test import TestCase
from .stubs.TesterControllerStubs import TesterControllerStubs
from endpoints import TesterController

class TesterControllerTests(TestCase):

    def testParseFileNamesTestCase1(self):
        print("Parsing file names: Test case 1...")
        expectedFiles = ["TestFile.py"]
        expectedCount = len(expectedFiles)
        result = TesterController.ParseFileNames(TesterControllerStubs.TestCase1())
        self.assertEqual(len(result), expectedCount)
        self.assertEqual(result, expectedFiles)

    def testParseFileNamesTestCase2(self):
        print("Parsing file names: Test case 2...")
        expectedFiles = ["TestFile.py"]
        expectedCount = len(expectedFiles)
        result = TesterController.ParseFileNames(TesterControllerStubs.TestCase2())
        self.assertEqual(len(result), expectedCount)
        self.assertEqual(result, expectedFiles)

    def testParseFileNamesTestCase3(self):
        print("Parsing file names: Test case 3...")
        expectedFiles = ["AnotherTestFile.py", "TestFile.py"]
        expectedCount = len(expectedFiles)
        result = TesterController.ParseFileNames(TesterControllerStubs.TestCase3())
        self.assertEqual(len(result), expectedCount)
        self.assertEqual(result, expectedFiles)
