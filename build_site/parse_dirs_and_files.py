# file to walk-through all the directories and files, reading data and outputing a python dictionary.
# The dictionary is to be processed by the next script to build all the javascript objects.

import os

# remember include the leading "." infront of the extension letters
# example: ".exe" not "exe"
file_extension = '.id'

def find_and_return_the_id_file_path(file_ext):
    current_dir = os.getcwd()

    # parent_dir = os.path.dirname(current_dir)

    list_dir = os.listdir(current_dir)

    # print(list_dir)

    for i in list_dir:
        path = f'{current_dir}/{i}'
        if os.path.isdir(path):
            list_of_files = os.listdir(path)
            for file in list_of_files:
                if os.path.isfile(f'{path}/{file}'):
                    split_ext = os.path.splitext(f'{path}/{file}')
                    if split_ext[1] == file_ext:
                        print(f'FOUND: "{path}/{file}"')
                        return f'{path}/{file}'
    print(f'INFO: No *{file_ext} file found.')
    return False

file_path = find_and_return_the_id_file_path(file_extension)              

if file_path:
    print(file_path)
else:
    print('returned FALSE')