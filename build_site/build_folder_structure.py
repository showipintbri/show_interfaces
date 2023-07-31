# This file can build the template folder structure and placeholder *.md files based on a single 'tagged'/'annotated'  show interfaces output
# Simply execute this script and supply the filename of the annotated file: 
# "build_folder_structure.py show_interfaces.id"
import re
import os

class BuildFoldersAndFiles:

    def __init__(self, cmd_output: str, filenames: list):
        self.cmd_output = cmd_output
        self.filenames = filenames
        pass

    def find_all_tags(self) -> list:
        cmd_output = self.cmd_output
        # re.findall(pattern, string, flags=0)
        list = re.findall('</*\w+>', cmd_output)
        self.all_tags = list
        return self.all_tags

    # all_tags = find_all_tags(id)

    # print(all_tags)

    def find_all_start_tags(self) -> list:
        cmd_output = self.cmd_output
        list = re.findall('<\w+>', cmd_output)
        start_tags = [tag for tag in list if tag[1] != '/'] #This may not be needed anymore
        self.start_tags = start_tags
        return self.start_tags

    # start_tags = find_all_start_tags(id)

    # print(start_tags)

    def extract_tag_text(self, tag) -> str:
        remove_first_char = tag[1:]
        remove_last_char = remove_first_char[:-1]
        return remove_last_char

    def extract_all_tag_text(self, list) -> list:
        new_list = []
        for i in list:
            just_text = self.extract_tag_text(i)
            new_list.append(just_text)
        self.all_tag_text = new_list
        return self.all_tag_text

    # just_tag_text = extract_all_tag_text(start_tags)

    # print(just_tag_text)
            

    def get_tag_and_element(string: str, all_raw_tag_text: list) -> list:
        list_of_dicts = []
        for tag in all_raw_tag_text:
            w = re.search(f'<{tag}>(?P<element>.+)</{tag}>', string)
            elem = w.group('element')
            d = {'tag': tag, 'element': elem}
            list_of_dicts.append(d)
        return list_of_dicts
            
            
    # list_of_dicts = get_tag_and_element(id, just_tag_text)

    # print(list_of_dicts)

    # List of empty filenames to create:



    def create_placeholder_files(dir: str, filenames: list) -> None:
        for file in filenames:
            try:
                open(f'{dir}/{file}', 'a').close()
            except OSError:
                print(f'ERROR: Failed creating the file: "{dir}/{file}"')   
            else:
                print(f'File "{dir}/{file}" successfully created or already exists.')
        return None

    def make_dirs_from_tags(path: str, list_of_tags: list, list_of_filenames: list) -> None:
        file_path = os.path.splitext(path)
        file_path_head = file_path[0]
        if not os.path.exists(file_path_head):
            os.makedirs(file_path_head)
        for tag in list_of_tags:
            path_with_tag = f'{file_path_head}/{tag}'
            if not os.path.exists(path_with_tag):
                try:
                    os.makedirs(path_with_tag)
                except:
                    print(f'ERROR: Couldn\'t make folder: "{path_with_tag}"')
                else:
                    print(f'Folder "{path_with_tag}" created.')
                    create_placeholder_files(path_with_tag, list_of_filenames)
            else:
                print(f'Folder "{path_with_tag}" already exists.')
                create_placeholder_files(path_with_tag, list_of_filenames)
        return None

    # make_dirs_from_tags(just_tag_text)

