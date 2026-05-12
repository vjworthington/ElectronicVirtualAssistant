<h1 align="center">EVA: Electronic Virtual Assistant</h1>
<div align="center">

<a href="https://github.com/vjworthington/ElectronicVirtualAssistant"><img src="https://img.shields.io/badge/github-repo-blue?logo=github" alt="GitHub Badge"/></a>
<a href="https://github.com/vjworthington/ElectronicVirtualAssistant"><img src="https://img.shields.io/badge/version-1.0.2-blue" alt="Version Badge"/></a>
<a href="https://github.com/vjworthington/ElectronicVirtualAssistant"><img src="https://img.shields.io/badge/artificial_intelligence-yes-green" alt="AI Badge"/></a>
<a href="https://github.com/vjworthington/ElectronicVirtualAssistant"><img src="https://img.shields.io/badge/build_status-passing-green" alt="Build Badge"/></a>
<a href="https://github.com/vjworthington/ElectronicVirtualAssistant"><img src="https://img.shields.io/badge/pull_requests-0_open-yellow" alt="Pull Badge"/></a>
<a href="https://github.com/vjworthington/ElectronicVirtualAssistant/issues"><img src="https://img.shields.io/badge/issues-0_open-yellow" alt="Issues Badge"/></a> <!-- <FIX THIS> -->

<!-- Include a visual here -->

</div>

---

## Overview
Electronic Virtual Assistant, EVA for short, is an interactive AI assistant that integrates GPT-based conversational responses with emotion-driven visual feedback. The project dynamically categorizes conversational tone and displays corresponding emotional states through a graphical slime character to create a more immersive user experience.

### Features
-	GPT-powered conversational responses 
-	Emotion classification using keyword analysis 
-	Dynamic graphical emotion display 
-	Modular assistant architecture 
-	Linux-based Python environment 

### Technology Used
-	Python 
-	OpenAI API 
-	PyQt5 
-	Virtual Environments (venv) 
-	Linux

---

### Installation
<!-- Write NEW installation up -->

### STEP 1: LINUX
Linux Users: If you're already working on Linux, please skip to STEP 2

Windows Users: Linux will need to be installed 

### STEP 2: INSTALL PYTORCH
```bash
sudo apt update
sudo apt install python3 idle3 -> Y
# Create environment
python3 -m venv .env
```

### STEP 3: INSTALL pipX
```bash
sudo apt install pipX -> Y
```

### STEP 4: INSTALL OPENAI
```bash
pip install openai
# export API
export OPENAI_API_KEY="insert your key here"
```

### STEP 5: MISC INSTALLATIONS
```bash
# install PyQt5
sudo apt install python3-pyqt5
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
```
```bash
# To add user as a sudoer
su
# enter password
sudo visudo
# go to "root ALL=(ALL) ALL"
# add "username ALL=(ALL) ALL
CRTL + X
```
```bash
# other
sudo dpkg -i /PATHINGO/file_name.deb
```



