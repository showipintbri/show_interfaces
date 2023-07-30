from find_id_file import FindIdFile
from build_folder_structure import BuildFoldersAndFiles
import sys
import os
import re

# remember include the leading "." infront of the extension letters
# example: ".exe" not "exe"
file_extension = '.id'

file_path = FindIdFile.find_and_return_the_id_file_path(file_extension)              

if file_path:
    print(file_path)
    file_text = FindIdFile.read_file(file_path)
    print(file_text)
else:
    sys.exit(0)


filenames = ['summary.md', 'configuration.md', 'details.md', 'links.md']