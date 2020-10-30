from django.test import TestCase
from .stubs.FileTreeBuilderTestStub import FileTreeBuilderTestStub
from endpoints.FileTreeBuilder import FileTreeBuilder

testStub = FileTreeBuilderTestStub()
builder = FileTreeBuilder()


class MyTestCase(TestCase):

    def test_avg_file_tree(self):
        print("Testing Avg File Tree")
        actual = builder.build_tree_structure(testStub.get_json_avg())
        expected = testStub.get_json_avg_expected()
        self.assertEqual(actual, expected)

    def test_empty_file_tree(self):
        print("Testing Empty File Tree")
        actual = builder.build_tree_structure(testStub.get_json_empty())
        expected = testStub.get_json_empty_expected()
        self.assertEqual(actual, expected)

    def test_no_folder_file_tree(self):
        print("Testing No Folder File Tree")
        actual = builder.build_tree_structure(testStub.get_json_no_folder())
        expected = testStub.get_json_no_folder_expected()
        self.assertEqual(actual, expected)

    def test_single_folder_file_tree(self):
        print("Testing Single Folder File Tree")
        actual = builder.build_tree_structure(testStub.get_json_single_folder())
        expected = testStub.get_json_single_folder_expected()
        self.assertEqual(actual, expected)

    def test_small_file_tree(self):
        print("Testing Small File Tree")
        actual = builder.build_tree_structure(testStub.get_json_small())
        expected = testStub.get_json_small_expected()
        self.assertEqual(actual, expected)

    def test_split_path_small(self):
        print("Testing Small Path Split")
        actual = builder.split_path(testStub.get_path_small())
        expected = testStub.get_path_small_expected()
        self.assertEqual(actual, expected)
