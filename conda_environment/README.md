# Setting up the Conda Environment

## Installing with Windows, Linux, or Mac 
0. Open your terminal. We recommend Anaconda Prompt or Command Prompt for Windows and Terminal for Mac/Linux. 
    - NOTE: Powershell for Windows is difficult to use Anaconda with, so we do not recommend it.

1. Change to a directory where you want to save your Conda Environment. This should be from any directory of this repository, we recommend the root directory of the Github repository. This would be the directory that ends in the name of the directory. i.e. `cd C:\Users\{path_to_repo}\social_competiton_elo_rating` for Windows and `cd /home/{}/{path_to_repo}\social_competiton_elo_rating` for Mac and Linux.

2. Copy and paste the commands one line at a time from this file into your terminal(copy all the lines that don't have the `#` in front. The ones with `#` in front are comments that don't have any effect on the code): 
    - [./environment_install.sh](./environment_install.sh)
    - NOTE: If the Conda Environment creation or the  library installation stalls after 10 minutes, we recommend exiting out with `Ctrl + C` or `Ctrl + Z`.