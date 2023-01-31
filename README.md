Pygame Zero Test Project
========================
This is a test project used to get familiar with getting your environment set up and using git commands.

It contains instructions to:
* Set up your local environment.
* Get familiar with common git commands such as:
  * Clone a Github project
  * Creating a new branch
  * Commit a new file
  * Create a pull request
  * Merge a pull request

Note: This tutorial is based on Mac or Linux based environments. The Windows commands may slightly differ.

Setting up Your Local Environment
------------------------
### Installing Conda and Creating Your Environment
[#todo: Write instructions for Windows computers.]
First, open up your terminal or command line.
Navigate to your directory you want to save the project files to.
For example:
```
cd ~
mkdir PythonProjects
cd PythonProjects
```

I highly recommend installing [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), which will help you create a programming environment for Python projects.
Once installed, you can run the following commands from the directory you created:
```
conda create --name pygamezero
conda install -n pygamezero pip
conda activate pygamezero
```
### Installing Git and GitHub CLI
Install GitHub CLI with Conda and login to your GitHub account.
```
conda install git
conda install gh --channel conda-forge
gh auth login -w
```

### Cloning the Project
```
gh repo clone guamcoderz/project1
cd project1
pip install -r requirements.txt
```

### Setting Up Your IDE
Next, comes the discussion of which Python IDE to use. I personally use [PyCharm](https://www.jetbrains.com/pycharm/download/) in developing Python projects, but whatever IDE you end up choosing, be sure that it contains git functionality to make it easier to add files to commit and make pull requests.

Open up your project in your IDE of choice by selecting the directory you just cloned.
You will need to make sure that the correct Python Interpreter is set to the conda environment you created in the earlier step.

Run the main.py file to make sure that your local environment was set up correctly. You should see a window pop up with a bird flapping its wings moving to the right in an endless cycle. Click on the bird to see what it does.

Getting Familiar with Git
------------------------
### Creating a Dev Branch
Now that your local environment is set up, you will need to create a new branch for your development. Do not make any changes to the code until you do this! In your terminal or in your IDE, create a new branch called `dev-[github_username]`:
```
git branch dev-aznleng
git checkout dev-aznleng
```
### Editing a File and Commit
Now, open the `team.csv` file and add a new line with your name, email address, and GitHub username.
If using the command line, you can enter the following to open up the file and make edits:
```
nano team.csv
```
Press CTRL+X to save and close the file. Once the change has been made, in your command line, you are going to add and commit the changes to your dev branch. Be sure to change `dev-aznleng` to the name of your branch.
```
git add team.csv
git commit -m "Add my info to team file."
git push --set-upstream origin dev-aznleng
```
### Creating a Pull Request and Merging
On GitHub in the web browser, go to the [Pull Request](https://github.com/guamcoderz/project1/pulls) page. Click on the button for New Pull Request. Select `main` as the base and your dev branch as compare. Next, click on the button to Create Pull Request. Finally, you will merge the pull request by click on the Merge Pull Request button.

