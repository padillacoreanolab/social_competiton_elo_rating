# Elo Rating Processing Notebooks

## Steps to take

0. Create a folder in [../results](../results) for your analysis
    - We recommend naming the folder in this convention: `{date}_{overall experiment name}_{protocol}`
        - e.g. `20221220_pilot3_tubetest`

1. Copy the notebooks(files ending in `.ipynb`) in this directory to the folder that you created.

2. Create a `data` folder in the folder your created, and copy all your behavior spreadsheets into it.

3. Make sure that Conda Environment is activated. If it is, in your terminal there should be the environment path in `()` next to your command line. e.g. Something like `(/nancy/projects/social_competiton_elo_rating/elo_rating_env) riwata@godzilla:/nancy/projects/social_competiton_elo_rating $`
    - If not, then follow the directions here to activate it or to create one. [../conda_environment/README.md](../conda_environment/README.md)

4. From the root directory [../](../) , start Jupyter Notebook with the command `jupyter notebook --allow-root` in your terminal and press `Enter`.

5. Navigate to the folder you created with the Jupyter Notebook GUI, which should pop in your internet browser. If you start in the root directory, you will click on `results` >> `{folder_that_you_created}`. 

6. Click on the Jupyter Notebook you copied(the `.ipynb` file), and then run with `Kernel` > `Restart & Run All`

7. Follow the instructions in the Jupyter Notebook and change any of the default variable values to better suit your file structure and naming convention.

8. Analyze spreadsheets and plots created in `./proc` that will be created. 
