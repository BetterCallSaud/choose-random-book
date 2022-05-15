from time import sleep
from os import listdir
from os.path import isfile, join
from random import randint

onlyfiles = [f for f in listdir("D:\Books") if isfile(join("D:\Books", f))]

randfile = onlyfiles[randint(0, len(onlyfiles))]

print(randfile)
sleep(5);
