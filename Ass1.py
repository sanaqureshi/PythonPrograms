# 1. Write a python script for creating directory,displaying its contents. 

import os,sys
os.mkdir("SanaDir")
os.chdir("SanaDir")
os.system("touch file5")
os.system("ls")
os.system("cat file5")
