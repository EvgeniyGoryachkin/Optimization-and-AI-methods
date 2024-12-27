# Artificial intelligence methods
A solution was developed for the following tasks, which were set by the teacher Platov Alexander Yurievich

## Minimization of the Rasstrigin function
1. Solve the problem of minimization of the Rastrigin function on the segment (-6,6) using the golden ratio
Rastrigin's function F=20+x^2+y^2-10 cos〖2πx-10〗 cos2πy
Accept y=x.
2. Solve the same problem using minimize_scalar function from SciPy package.
3. Solve the problem with Rastrigin function in the region x in -[5,5] and y in [-5,5] using Monte Carlo method.

## Annealing method
1.	Solve the Rasstrigin problem using the annealing method. 
2.	Solve the TSP problem using the annealing method.
3.	Solve the AAP problem using the annealing method.
   
## The genetic algorithm
1.	Solve the problem with the Rastrigin function in the region x at -5.5 and y at -5.5 using the genetic algorithm
2.	Solve with the help of genetic algorithm the problem of building a program for calculating the expression x*x + y + 3, x^3 + y^2 - 2, x+y+z

# Data analysis
Solution for the tasks that were set by the teacher Prokopenko Natalia Yurievna

## Mathematical modeling and sensitivity analysis
In accordance with the objectives, the following programs were written

## Implementation of the KDD methodology
For the data taken from Kaggle “Consumption of alcoholic beverages in Russia 2017-2023”
using Python libraries to implement KDD methodology. The scenario and the report should contain all stages: audit, transformation, models (several with different settings), perform calculations on new data for the best model, analyze the results. 

On the basis of the data obtained, it is necessary to conduct a data study:
1. Analyze the distributions of the data: 
- Calculate the number of unique values, zero and empty values + share in % of the total number of values; 
- Mean, median, standard deviation, minimum, maximum, data type for each indicator in the data provided; 
- Examine the distribution of data for each characteristic;
- Do a check for:
- Missing and null values in fields; 
- Presence of duplicates and contradictions;
- Presence of incorrect characters;
2.	Perform the binning procedure (if necessary, create a dataset with the output field beforehand). Analyze the bins in terms of logic and interpretation. List the significant signs. Which variables should be eliminated from further consideration and why?
3.	Prepare a final dataset, if necessary: 
- Correct data - correct errors (clean up problems identified in the data during the audit process)
- Convert categorical indicators to integer indicators;
4.	Build a correlation matrix. This matrix will allow us to trace the degree of correlation between variables to see if we can remove them or not.
Write out the significant and insignificant indicators.
5.	Describe all explanations of the data study and all transformations of the data
6.	The result of performing the audit is cleaned data.
7.	Produce hypotheses that we will test in the modeling phase.
8.	Divide the data into training and test sample
9.	Ensemble of models (several with different settings), for the best model perform calculations on test data, analyze the results. 
10.	Compare the errors of the models.
