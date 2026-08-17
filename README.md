<h1 align="center">EVA: Electronic Virtual Assistant</h1>

<div align="center">

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/vjworthington/ElectronicVirtualAssistant?label=release&color=blue)](https://github.com/vjworthington/ElectronicVirtualAssistant/releases/latest)
![CI](https://github.com/vjworthington/ElectronicVirtualAssistant/actions/workflows/ci.yml/badge.svg)
[![Issues](https://img.shields.io/github/issues/vjworthington/ElectronicVirtualAssistant)](https://github.com/vjworthington/ElectronicVirtualAssistant/issues)
[![Docker](https://img.shields.io/badge/docker-ghcr.io%2Fvjworthington%2Felectronic--virtual--assistant-blue?logo=docker)](https://ghcr.io/vjworthington/electronic-virtual-assistant)
[![Coverage](https://codecov.io/gh/vjworthington/ElectronicVirtualAssistant/branch/main/graph/badge.svg)](https://codecov.io/gh/vjworthington/ElectronicVirtualAssistant)



[![Stars](https://img.shields.io/github/stars/vjworthington/ElectronicVirtualAssistant?style=social)](https://github.com/vjworthington/ElectronicVirtualAssistant/stargazers)
[![Watchers](https://img.shields.io/github/watchers/vjworthington/ElectronicVirtualAssistant?style=social)](https://github.com/vjworthington/ElectronicVirtualAssistant/watchers)
[![Forks](https://img.shields.io/github/forks/vjworthington/ElectronicVirtualAssistant?style=social)](https://github.com/vjworthington/ElectronicVirtualAssistant/network/members)

</div>

<div align="center">
<img src="assets/EVAscreenshot.png" width="500" align="center" alt="Screenshot">
</div>


---

## Overview
Electronic Virtual Assistant, EVA for short, is an interactive AI assistant that integrates GPT-based conversational responses with emotion-driven visual feedback. The project dynamically categorizes conversational tone and displays corresponding emotional states through a graphical slime character to create a more immersive user experience.

### Features
-	AI-powered conversational interface 
-	Emotion classification using keyword analysis 
-	Dynamic emotion-based avatar rendering 
-	Modular assistant architecture 
-	Linux-based Python environment 

### Technology Used
-	Python 
-	OpenAI / OpenRouter API 
-	PyQt5 
-	Virtual Environments (venv) 
-	Windows
-	VTube Studio (Avatar)
-	Testing

### Testing

- **pytest / pytest-cov** – Unit and integration testing with code coverage
- **Ruff** – Code quality and linting
- **mypy** – Static type checking
- **GitHub Actions** – Automated CI testing
- **Codecov** – Test coverage reporting

Additional testing and security analysis will be documented as the project develops.

### Documentation

The project documentation will be developed in the following order:

- **Software Requirements Specification (SRS)** – Defines EVA's functional and non-functional requirements, system capabilities, constraints, and project scope.
- **Software Design Document (SDD)** – Describes EVA's architecture, major components, interfaces, design decisions, and implementation structure.
- **Coding and Testing Document (CT)** – Documents the testing process, test results, code quality analysis, security testing, issues discovered, resolutions, and final assessment.

The documentation follows a structured progression from **requirements → design → implementation and testing**.

---

### Installation (Windows)

### 1. Install Python
Download Python 3.11+ from:
https://www.python.org/downloads/

### 2. Clone the Repository
```bash
git clone https://github.com/vjworthington/ElectronicVirtualAssistant.git
cd ElectronicVirtualAssistant
```

### 3. Add API Key
- Open 'config.txt'
- Paste your OpenAI or OpenRouter API key in API_KEY=
- Paste OpenAI or OpenRouter model name in MODEL=


### 4. Run the Program
```bat
start.bat
```
---

### Application Sequence Diagram
<div align="center">
<img src="assets/sequence_diagram.png" width="500" align="center" alt="Sequence Diagram">
</div>

## Asset Credits

The animated slime avatar used in EVA was purchased from the Etsy creator below:

- Creator: MelonMinty
- Etsy Shop: https://www.etsy.com/shop/MelonMinty

All rights to the artwork remain with the original creator.
