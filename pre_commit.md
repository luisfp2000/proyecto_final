## Precommit instalation and use

## Pre-commits
Pre-commits are automated checks that run on your code before you commit changes, helping ensure code quality and consistency. In this guide, we'll use the `pre-commit` tool to set up pre-commits for Python projects in Visual Studio Code (VSC).

### Prerequisites

1. Python is installed on your system.
2. Visual Studio Code (VSC) is installed on your system.
3. `pip` is installed on your system.

### Step 1: Install `pre-commit`

First, you need to install the `pre-commit` tool on your system. Open your terminal or command prompt and run the following command:

pip install pre-commit

### Step 2: Create a Pre-Commit Configuration File
Create a file named `.pre-commit-config.yaml` in the root of your Python project. This file will define the pre-commit hooks to be executed.

### Step 3: Configure Pre-Commit Hooks
In the `.pre-commit-config.yaml` file, define the pre-commit hooks you want to run. Each hook represents a specific check on your code. There are many pre-configured hooks available, and you can also create custom hooks if needed.

### Step 4: Initialize Pre-Commit for Your Project
After creating the `.pre-commit-config.yaml` file, initialize pre-commit for your project. Open your terminal or command prompt, navigate to the root directory of your project, and run the following command:

pre-commit install

### Step 5: Commit Your Changes
With the pre-commit hooks installed, you can now make changes to your Python code. When you're ready to commit your changes, run the following command to trigger the pre-commit checks:

git commit -m FILE_NAME.py
