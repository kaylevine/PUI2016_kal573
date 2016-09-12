# PUI2016 Homework 1


## Project Work Balance:

**Assignment 1:** I completed this assignment on my own, and performed the fork with Claire (xh895).

**Assignment 2:** Mona (nm2773) has a background in computer science so she helped explain Github, Terminal, and basic coding principles to Claire and I while working on this assignment. She also helped me create this README file and explained markdown styling techniques.

To set up my work environment, I followed the commands from the homework assignment file:

`ssh -X -A -t kal573@gw.cusp.nyu.edu`

`ssh -A -X compute`

Once I accessed compute, I created the new directory PUI2016_kal573:

`mkdir PUI2016_kal573`

I then created a new environmental variable, `PUI2016_kal573` in `.bash_profile` using nano, export, and source commands as shown in the screenshot. This varialbe will allow me to store this for future use.

I also created the alias `pui2016` in `.bash_profile` as shown in the screenshot. This alias will allow me to run the command `cd $PUI2016_kal573` and change into that directory in the future. The dollar sign symbol is needed to designate the following text as a variable.

To complete Assignment 2, I input the following three commands:

`pwd`

`pui2016`

`pwd`

This reveals that I properly created the environmental variable and alias for the new directory.


![Screenshot 1: directory creation](/HW1_kal573/bash_profile.png)

![Screenshot 2: command line in terminal](/HW1_kal573/commands.png)

