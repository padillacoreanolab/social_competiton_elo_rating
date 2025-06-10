# Elo Rating Processing Notebooks

## Steps to take

0. Create a folder in [../results](../results) for your analysis
    - We recommend naming the folder in this convention: `{date}_{overall experiment name}_{protocol}`
        - e.g. `20221220_pilot3_tubetest`

1. Copy the notebooks(files ending in `.ipynb`) in this directory to the folder that you created.

2. Create a `data` folder in the folder your created, and copy all your behavior spreadsheets into it.

3. Make sure that Conda Environment is activated. If it is, in your terminal there should be the environment path in `()` next to your command line. e.g. Something like `(/nancy/projects/social_competiton_elo_rating/elo_rating_env) riwata@godzilla:/nancy/projects/social_competiton_elo_rating $`
    - If not, then follow the directions here to activate it or to create one. [../conda_environment/README.md](../conda_environment/README.md)

4a. reward_competition_processing_clean and urine_marking_processing_clean are shorter versions of the ELO score scripts that can batch process multiple urine marking or reward competition excel files for multiple cohorts. urine_marking_processing_clean also will calculate ties for you and has variables for min spot and percent differences for tie thresholds. A single excel sheet is output with the first sheet having final ELO scores across all input excel files and then one sheet per excel file with the ELO score progressiosn. 

*urine_marking_processsing* does not calculate ties for you! 

4b. From the root directory [../](../) , start Jupyter Notebook with the command `jupyter notebook --allow-root` in your terminal and press `Enter`.

5b. Navigate to the folder you created with the Jupyter Notebook GUI, which should pop in your internet browser. If you start in the root directory, you will click on `results` >> `{folder_that_you_created}`. 

6b. Click on the Jupyter Notebook you copied(the `.ipynb` file)

7b. Follow the instructions in the Jupyter Notebook and change any of the default variable values to better suit your file structure and naming convention.

8b. Run the notebook:
    - 8a. All at once with `Kernel` > `Restart & Run All`
    - 8b. Or each cell(block) individually by clicking on the block. Then click `Run` button with the play button or use the run command with `Shift + Enter` 



9b. Analyze spreadsheets and plots created in `./proc` that will be created. 
