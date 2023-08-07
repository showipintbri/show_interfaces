from find_id_file import FindIdFile
from build_folder_structure import BuildFoldersAndFiles
import sys


# remember include the leading "." infront of the extension letters
# example: ".exe" not "exe"
file_extension = '.id'

file_path = FindIdFile.find_and_return_the_id_file_path(file_extension)              

if file_path:
    # print(file_path)
    file_text = FindIdFile.read_file(file_path)
    print(file_text)
else:
    sys.exit(0)

def build_infrastructure(file_text):
    filenames = ['summary.md', 'configuration.md', 'details.md', 'links.md']

    bfaf = BuildFoldersAndFiles()

    all_start_tags_list = bfaf.find_all_start_tags(file_text)

    just_tags_text_list = bfaf.extract_all_tag_text(all_start_tags_list)

    bfaf.make_dirs_from_tags(file_path, just_tags_text_list, filenames)
    return None

def build_inner_html(file_text):
    bfaf = BuildFoldersAndFiles()
    all_start_tags_list = bfaf.find_all_start_tags(file_text)
    just_tags_text_list = bfaf.extract_all_tag_text(all_start_tags_list)
    list_of_dicts = bfaf.get_tag_and_element(file_text, just_tags_text_list)
    # print(list_of_dicts)
    for i in list_of_dicts:
        tag = i['tag']
        element = i['element']
        old_line = f'<{tag}>{element}</{tag}>'
        new_line = f'<span class="element" id="{tag}">{element}</span>'
        file_text = file_text.replace(old_line, new_line)
    # print(file_text)
    list_o_lines = file_text.splitlines()
    text_block = ''
    for x in list_o_lines:
        old_line = x
        new_line = f'<div>{old_line}</div>\n'
        text_block =+ new_line
    return text_block

build_infrastructure(file_text)

inner_html = build_inner_html(file_text)

print(inner_html)

sys.exit(0)


