# rock-paper-scissors-exercise

## Repo Setup

Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub online interface, add a "README.md" file and a Python-flavored ".gitignore" file during the repo creation process.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```
cd ~/Desktop/rock-paper-scissors-exercise'
```

## Environment Setup

Create and activate a new project-specific Anaconda virtual environment:

``` 
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```
        
## ENV Setup

After activating the virtual environment, install package dependencies (see the "requirements.txt" file):

```
pip install -r requirements.txt
```

NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial cd step above)

## Setup

In in the root directory of your local repository, (if it does not already exist) create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

```
USER_NAME="Jon Snow"
```

## Run the game

Now you're all set to play rock, paper, scissors! Run the game by executing the command

```
python game.py
```