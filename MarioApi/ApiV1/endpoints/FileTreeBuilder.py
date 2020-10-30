import os
import json


class FileTreeBuilder:

    # places all of the file paths from the JSON response into a list
    # helper function for build_tree_structure()
    def get_paths(self, files):
        paths = []
        count = 0
        path_len = 0

        if 'count' in files:
            path_len = len(files['value'])

        while path_len > 0:
            paths.append(files['value'][count]['path'])
            count += 1
            path_len -= 1

        return paths

    # splits the file path into an array containing each part of the path as an element within the list
    # helper function for get_link_association
    def split_path(self, path):
        all_parts = []
        while 1:
            parts = os.path.split(path)
            if parts[0] == path:  # sentinel for absolute paths
                all_parts.insert(0, parts[0])
                break
            elif parts[1] == path:  # sentinel for relative paths
                all_parts.insert(0, parts[1])
                break
            else:
                path = parts[0]
                all_parts.insert(0, parts[1])
        return all_parts

    # creates a list that contains association pairs of folders and files within the repo
    # helper function for build_tree_structure()
    def get_link_association(self, paths):
        assoc_list = []

        for path in paths:
            path_list = self.split_path(path)
            path_len = len(path_list)
            parent = ''
            child = ''
            if path_len > 1:
                parent = path_list[path_len - 2]
                child = path_list[path_len - 1]

                assoc_list.append((parent, child))

        return assoc_list

    # builds the tree structure based on the json response of the get items call
    # main function
    def build_tree_structure(self, json_info):
        links = self.get_link_association(self.get_paths(json_info))

        name_to_node = {}
        root = {'nodes': []}
        id = 1
        for parent, child in links:
            parent_node = name_to_node.get(parent)
            if not parent_node:
                name_to_node[parent] = parent_node = {'value': parent, 'id': 'root'}
                root['nodes'].append(parent_node)
            name_to_node[child] = child_node = {'value': child, 'id': "{}".format(id)}
            parent_node.setdefault('nodes', []).append(child_node)
            id += 1
        
        return root['nodes']
