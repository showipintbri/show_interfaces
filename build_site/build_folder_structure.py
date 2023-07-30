# This file can build the template folder structure and placeholder *.md files based on a single 'tagged'/'annotated'  show interfaces output
# Simply execute this script and supply the filename of the annotated file: 
# "build_folder_structure.py show_interfaces.id"
import re
import os

class BuildFoldersAndFiles:

    def __init__(self, id):
        self.id = ''
        self.filenames = []

    def find_all_tags(self, string) -> list:
        # re.findall(pattern, string, flags=0)
        list = re.findall('</*\w+>', string)
        return list

    # all_tags = find_all_tags(id)

    # print(all_tags)

    def find_all_start_tags(self, string) -> list:
        import re
        # re.findall(pattern, string, flags=0)
        list = re.findall('<\w+>', string)
        start_tags = [tag for tag in list if tag[1] != '/']
        return start_tags

    # start_tags = find_all_start_tags(id)

    # print(start_tags)

    def extract_tag_text(self, tag) -> str:
        remove_first_char = tag[1:]
        remove_last_char = remove_first_char[:-1]
        return remove_last_char

    def extract_all_tag_text(self, list) -> list:
        new_list = []
        for i in list:
            just_text = extract_tag_text(i)
            new_list.append(just_text)
        return new_list

    # just_tag_text = extract_all_tag_text(start_tags)

    # print(just_tag_text)
            

    def get_tag_and_element(self, string: str, all_raw_tag_text: list) -> list:
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



    def create_placeholder_files(self, dir: str, filenames: list) -> None:
        for file in filenames:
            try:
                open(f'{dir}/{file}', 'a').close()
            except OSError:
                print(f'ERROR: Failed creating the file: "{dir}/{file}"')   
            else:
                print(f'File "{dir}/{file}" successfully created or already exists.')
        return None

    def make_dirs_from_tags(self, list_of_tags: list) -> None:
        for tag in list_of_tags:
            if not os.path.exists(tag):
                try:
                    os.makedirs(tag)
                except:
                    print(f'ERROR: Couldn\'t make folder: "{tag}"')
                else:
                    print(f'Folder "{tag}" created.')
                    create_placeholder_files(tag, filenames)
            else:
                print(f'Folder "{tag}" already exists.')
                create_placeholder_files(tag, filenames)
        return None

    # make_dirs_from_tags(just_tag_text)

