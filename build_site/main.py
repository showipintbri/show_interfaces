from find_id_file import FindIdFile
from build_folder_structure import BuildFoldersAndFiles


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

filenames = ['summary.md', 'configuration.md', 'details.md', 'links.md']

bfaf = BuildFoldersAndFiles()

all_start_tags_list = bfaf.find_all_start_tags(file_text)

just_tags_text_list = bfaf.extract_all_tag_text(all_start_tags_list)

bfaf.make_dirs_from_tags(file_path, just_tags_text_list, filenames)

