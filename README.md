This is a test readme file for processing the initial installations prior installing the EVA files

Installation
#####################
STEP 1: LINUX
-------------
Linux Users: If you're already working on Linux, please skip to STEP 2

Windows Users: Linux will need to be intalled 

STEP 2: INSTALL PYTORCH
-----------------------
sudo apt update
sudo apt install python3 idle3 -> Y
# Create environment
Python -m venv .env

STEP 3: INSTALL pipX
--------------------
sudo apt install pipX -> Y

STEP 4: INSTALL OPENAI
----------------------
pip install openai
# export API
export OPENAI_API_KEY="insert your key here"

STEP 5: MISC INSTALLATIONS
--------------------------
# install PyQt5
sudo apt install python3-pyQt 5
pip install pyqt5
# install python3-tk
sudp apt install python3-tk
# alternate to create environment
sudo apt install virtualenv
mkdir ~venv && cd ~/venv
virtualenv -p python3.11.2 myenv
  # to activate
  source myenv/bin/activate
  # to deactivate
  deactivate

# To add user as a sudoer
su
# enter password
sudo visudo
# go to "root ALL=(ALL) ALL"
# add "username ALL=(ALL) ALL
CRTL + X

# other
sudo dpkg -i /PATHINGO/file_name.deb

