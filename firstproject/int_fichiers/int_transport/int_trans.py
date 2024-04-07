
import os
import shutil

with open("firstproject\int_fichiers\int_transport\hello.cqa", "w+") as startfile:
    startfile.write("Hello world ! \n : )")
    startfile.close

source = "firstproject\int_fichiers\int_transport\hello.cqa"
target = "firstproject\int_fichiers\int_transport\dest\hello.cqa"

shutil.copy(source, target)
os.remove(source)