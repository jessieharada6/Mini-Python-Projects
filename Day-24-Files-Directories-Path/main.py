
# # open file
# file = open("my_file.txt")
# # read file
# contents = file.read()
# print(contents)
# # once finish, clear the resource that opens and reads the file
# file.close()

# "with" remembers closes the file, mode by default is "r"
# /Users/jewang/Desktop/my_file.txt --- absolute file path, the first / shows it is a root directory
# / represents the root path, e.g. same as MacintoshHD/ for mac or C:/ for windows
# ../../../my_file.txt --- relative path, go up three levels from the current working directory
with open("../../../my_file.txt") as file:
    contents = file.read()
    print(contents)

# overwrite everything
with open("my_file.txt", mode = "w") as file:
    file.write("New text")

# append
with open("my_file.txt", mode = "a") as file:
    file.write("\nNew text")

# mode is "w" and file does not exist, it will create a brand new file
# only work if mode is "w"
with open("new_file.txt", mode = "w") as file:
    file.write("New text oh yeah")

# absolute file path: from root to the current file - related to the root
# relative path: relative to the current working directory
#   working directory (the directory we are working on) -
#   then based on the current working directory
#   1. go downwards (current work directory is above the file we want to get): ./folder/file
#   2.  if the same hierachical level, can remove ./, call "my_file.txt" just as above
#        Although you can also write this as "./my_file.txt", the "./" is optional.
#   3. go upwards (current work directory is below the file we want to get): ../file
#           two dots: go up

# mac : /
# window: \
# in python, use /

# all_files
# ------ my_files
# --------- quiz_files
#  ------------ quiz.txt
# ------ my_project
# ---------job_application_bot.py
# If you are writing code inside job_application_bot.py,
# what is the relative file path to open quiz.txt?

# ../my_file/quiz_files/quiz.txt
# The .. goes up one folder, same level as my_files, then go down
