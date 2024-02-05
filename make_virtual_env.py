import os
import getpass
import sys

MyUserName = getpass.getuser()
Here = os.getcwd()

dirname = input("directory name of environmnet: ")

env = os.path.join(Here,dirname)

default_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

in_version = input("enter desired python version or press enter use system default of " + str(default_version) + ": ")

if in_version == "":
	version = default_version
elif "3." in in_version:
	version = in_version
else:
	version = default_version

os.system("mkdir " + env)
os.system("python" + version +" -m venv " + env)

# os.system("source " + env + "/bin/activate")

print("run the command below to start the new virtual environment...")

print("source " + env + "/bin/activate")