Pygame Zero Test Project
------------------------
This is a test project used to get familiar with getting your environment set up and using git commands.

It contains instructions to:
* Clone a Github project.
* Set up your local environment.
* Get familiar with common git commands such as:
  * Creating a new branch
  * Commit a new file
  * Create a pull request
  * Merge a pull request

Note: This tutorial is based on Mac or Linux based environments. The Windows commands may slightly differ.

Cloning the Project
------------------------
First, open up your terminal or command line.
Navigate to your directory you want to save the project files to.
For example:
```
cd Document/PythonProjects
```
Next, clone the file into that directory.
```
git clone https://github.com/guamcoderz/project1.git
cd project1
```

Setting up Your Local Environment
----------------
I highly recommend installing [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), which will help you create a programming environment for Python projects.
Once installed, you can run the following commands from the root directory of the repository:
```
conda create --name pygamezero
conda install -n pygamezero pip
conda activate pygamezero
pip install -r requirements.txt
```
Next, comes the discussion of which Python IDE to use. I personally use [PyCharm](https://www.jetbrains.com/pycharm/download/) in developing Python projects, but whatever IDE you end up choosing, be sure that it contains git functionality to make it easier to add files to commit and make pull requests.

Open up your project in your IDE of choice by selecting the directory you just cloned.
You will need to make sure that the correct Python Interpreter is set to the conda environment you created in the earlier step.

Run the main.py file to make sure that your local environment was set up correctly. You should see a window pop up with a bird flapping its wings moving to the right in an endless cycle. Click on the bird to see what it does.

Getting Familiar with Git
========================
Now that your local environment is set up, you will need to create a new branch for your development. Do not make any changes to the code until you do this!
```
git branch dev
git checkout dev
```