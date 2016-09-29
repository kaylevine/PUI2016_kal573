# PUI Homework 4

## Project Work Balance:
### Assignment 1:

For this assignment, I received guidance from Mona to refresh my memory about using github to fork repositories. Otherwise, I worked alone.

### Assignment 2:

For this assignment, I worked with Claire and Mona. More specifically, I found the first article (T-test) on Plos One and helped determine the variables and hypothesis. Claire found the second article (Correlation).

### Assignment 3:

For this assignment, I worked with Claire, Mona, and Alexey to reproduce the analysis of the Hard to Employ program. Specifically, I worked alone to create my initial code, and then received help from Mona and Alexey to debug my code for the chi-squared analysis section. 

### Assignment 4:

For this assignment, I worked with Claire, Mona, and Alexey to manipulate the CitiBike data and perform the analyses. Mona helped determine which code to use to subset, sort, and change the size of the data.


# Assignment 1:

For this assignment, I began by forking lx565's PUI2016 repository on GitHub. Then, I analyzed his Homework 3, Assignment 2 file according to the directions. I then determined that lx565 should use the *blank* test to finish the CitiBike analysis.

# Assignment 2:

For this assignment, my group (Claire and Mona) and I investigated research articles that utlized T-tests and Correlations between variables. The results of this search and analysis are described in the table below:

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
T-test	| 1, Types of Viruses | categorical | 1, % of light reflected | continuous | 1, healthy leaves | categorical | 	Do viruses affect the percentage polarization of light reflected from leaves.| Reflected light % before virus = Reflected light % after virus | 0.05; 0.001 | [The Effects of Plant Virus Infection on Polarization Reflection from Leaves](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0152836) |
Correlation	| 2, olfactory abilities, executive brain functioning abilities | continuous | 1, correlation | continuous | 1, sub-clinical psychopathologies | categorical | 	How strongly correlated and in what direction are the olfactory abilities and executive brain functioning abilities. | Olfactory abilities are weakly correlated to executive brain functioning abilities. | 0.01 | [Olfactory Impairment Is Correlated with Confabulation in Alcoholism](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0023190) |
||||||||

# Assignment 3:

For this assignment, I first followed along with the professor's sample python notebook about the Hard to Employ program in NY. Starting at the To Do section, I described the Null Hypothesis in words and symbols, and then stated my significance level. I then performed a Z-test, which demonstrated that the p-value was smaller than the critical value, and therefore the Null Hypothesis could not be rejected. I then performed a chi-squared analysis on the data, and again the Null Hypothesis could not be rejected. Lastly, I placed my calculated values into a contigency table.

# Assignment 4: 

For this assignment, I began by importing the CitiBike data from June 2016. Then, I crated male and female age columns for future use, and coded the gender column into binary numbers (1,2). Next, I plotted histograms of the data as well as normalized cumulative distributions. I then performed a KS test on the data, comparing the male and female age samples. To perform the next two tests, Pearson and Spearman, I then had to subset the data and sort the data. After that was completed, I performed the other two tests. I described in the notebook how these tests relate to the null hypothesis.




