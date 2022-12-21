# Behavioral Dataframe Processing

## Overview 

- This project helps calculate the ELO score for different social competition assays. The data collected for these assays are Excel sheets that are used during the recording. The assays includes tube test, urine marking, home cage observation, and reward competition. ELO scores keep track of the overall performance for a given subject, which can be compared to other subjects within the same cage to approximate the "ranking". Because the assays have multiple recordings for each subject, the ELO scores will be calculated after each interaction.

## Repository Organization
- [./jupyter_notebooks](./jupyter_notebooks)
    - Directory that has the Jupyter Notebooks to extract/process the MED-PC and the accompanying dataframes/plots that are created from it.
- [./results](./results)
    - Directory that has a record of previous iterations of the Jupyter Notebooks 
- [./src](./src)
    - Directory that has the Python source code used in the Jupyter Notebooks. All the original functions used in the notebooks will be imported from this.
`TODO`: Add sections on `conda environments`

## Steps To Take

### Step 0: Learn how to use the Command Line
- The Command-line interface is where we type in commands to make a computer do various tasks. This interface is presented by programs that are usually called the "terminal." 
    - For  more information: https://en.wikipedia.org/wiki/Command-line_interface

https://code.visualstudio.com/Download
1. Before starting, you must pick a program for your Command-line interface.
    - For Mac, we recommend the Terminal application.
        - Instructions on how to use the Terminal: https://macpaw.com/how-to/use-terminal-on-mac
        - Video Tutorial: https://www.youtube.com/watch?v=MBBWVgE0ewk
    - For Windows, we recommend using the Command Prompt 
        - Instructions on how to use the Command Prompt: https://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html
        - Video Tutorial: https://www.youtube.com/watch?v=aKRYQsKR46I

1.1 When editing and reading code, it is helpful to use a code editor that has features specific to programing. We recommend downloading Visual Studio Code. 
    - Download Link: https://code.visualstudio.com/Download

### Step 1. Clone this repository 
1. Check if you have the Git program on your computer. Open up Command-line interface program. We recommend Command Prompt for Windows, and Terminal for Mac. 

https://desktop.github.com/

1.1 In the terminal, type `git` then enter. 
    - Documentation of Git should be displayed if it is properly installed on your computer. If it says that command is not recognized or that the program doesn't exist, then install it with one of the following instructions: 
        - Windows: https://garnet-rotate-01f.notion.site/Git-Installation-with-Windows-09e4f9f13c9f47c48c8d02a1f7647704
        - Mac: https://garnet-rotate-01f.notion.site/Git-Installation-with-Mac-b5e51901e97b4c65a114bb25bc9f2dfa

2. Once you have Git, download the repository in a folder that you want to save it in. To move to the desired folder, type the following command into your Command-line interface program: `cd {/path/to/folder}`
    - Replace `{/path/to/folder}` with the absolute or relative path to the folder that you want to save the Github repository in. We recommend creating a folder for programming related projects.
    - More information on what an absolute or relative path is:
        - Mac: https://www.josharcher.uk/code/find-path-to-folder-on-mac/
        - Windows: https://www.computerhope.com/issues/ch001708.htm

2.1 Download the Github repository with the command: `git clone https://github.com/padillacoreanolab/behavioral_dataframe_processing`
    - NOTE: Every time you use this repo after cloning it, check for updates with: 
        - `cd {./path/to}/behavioral_dataframe_processing`
        - `git pull origin main`

### Step 2. Create Conda Environment to Install Necessary Python libraries
1. Check if you have Anaconda:
    - Type `python` in your terminal, and then press `Enter`. If you have Anaconda, then it will say "Anaconda" somewhere in the output.
    - If you don't have Anaconda, follow the installation instructions:
        - Mac: https://garnet-rotate-01f.notion.site/Anaconda-Installation-Mac-487707ed7b5749bc92a168be8717b9be
        - Windows: https://garnet-rotate-01f.notion.site/Anaconda-Installation-Windows-a90983afbed448d29ab6f4fade6730d5 

2. Create the Conda environment by following the instructions in: [./conda_environment/README.md](./conda_environment/README.md)
    - NOTE: This step only needs to be done once. Every subsquent time you want to run the analysis, you'll turn on the Conda environment with:
        - `conda deactivate`
        - `conda activate {./path/to}/elo_rating_env`

### Step 3. Run each Data Processing/Analysis Jupyter Notebooks
1. Follow the instructions to run the Jupyter Notebooks at [./jupyter_notebooks/README.MD](./jupyter_notebooks/README.MD)
    - NOTE: The dataframes and the plots should be saved in the subdirectories in the folder you created: Similar to[./jupyter_notebooks/proc](./jupyter_notebooks/proc)

## Resources

### ELO Score
- https://www.omnicalculator.com/sports/elo