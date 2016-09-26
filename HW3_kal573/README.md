# PUI2016 Homework 3

## Project Work Balance:

I completed assignment's 1 and 2 of this homework with Mona (nm2773) and Claire (xh895). 

In Assignment 1, I used the sample code provided by the Professor to analyze the various distributions. Mona and Claire helped me to debug my code. They also advised me to chose Standard Cauchy as my fifth distribution.

In Assignment 2, I helped our group define the hypothesis in words. I also advised the group to use distance between start/end stations rather than trip duration due to the lack of information about the path of the bike trips. Mona helped create a lot of the code, and Claire helped create the statistical formula for our hypothesis. I explained to the group that the data provided for start/end stations was in decimal degrees, and could be manipulated to calculate distance. Mona researched geopy and our group decided to use this package for our calculation of distance.

In Assignment 3, I worked alone and used sample code provided by the Professor to perform the z test and analysis.

## Assignment 1:

The methodology for each of the distributions was identical.

I first created an empty dictionary for that distribution, used numpy to create a random sample distribution, plotted that distribution, and found the mean and standard deviation.

Next, I used linspace to create 100 samples of different sizes N (N>10 & N<2000) from each of my 5 different distributions (500 samples in total), all with the same population mean.

I then plotted a scatterplot the means of the 100 sample distributions, along with a line of best fit, and then a histogram of the means in bins.

## Assignment 2:

The markdown for this assignment is located directly in the python notebook HW3_Assignment2.

## Assignment 3:

The markdown for this assignment is located directly in the python notebook PUI_HW3_Assignment3.



