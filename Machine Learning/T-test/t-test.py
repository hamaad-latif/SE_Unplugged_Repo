import numpy as np
from scipy import stats
import pandas

## Define 2 random distributions
#Sample Size
N = 360
#Gaussian distributed data with mean = 2 and var = 1
dataset = pandas.read_csv("../unplugged.csv")
dataset.sample(frac=1)
dataset = dataset[0:360]
del dataset['Comments']


gender = {'M': 1, 'F': 2}
dataset.Gender = [gender[item] for item in dataset.Gender]

before = {'F': 0, 'P': 1}
dataset.Results_Before = [before[item] for item in dataset.Results_Before]

after = {'F': 0, 'P': 1}
dataset.Results_After = [after[item] for item in dataset.Results_After]

positive = {'F': 0, 'T': 1}
dataset['Positive Outcomes'] = [positive[item] for item in dataset['Positive Outcomes']]

positiveOutcome = dataset[['Positive Outcomes']]
resultsAfter = dataset[['Results_After']]

## Calculate the Standard Deviation
#Calculate the variance to get the standard deviation

#For unbiased max likelihood estimate we have to divide the var by N-1, and therefore the parameter ddof = 1
var_a = positiveOutcome.var(ddof=1)
var_b = resultsAfter.var(ddof=1)
# print('var_a is ', var_a['Positive Outcomes'])
# print('var_b is ', var_b['Results_After'])
#std deviation
sum_a = var_a['Positive Outcomes'] + var_b['Results_After']
# print ('sum_a is ',sum_a)
s = np.sqrt((sum_a)/2)

# Calculate the t-statistics
t = (positiveOutcome.mean()['Positive Outcomes'] - resultsAfter.mean()['Results_After'])/(s*np.sqrt(2/N))

# print ('positive_outcome',positiveOutcome.mean())

# Compare with the critical t-value
# Degrees of freedom
df = 2*N - 2

#p-value after comparison with the t
p = 1 - stats.t.cdf(t,df=df)


print("t = " + str(t))
print("p = " + str(2*p))
### You can see that after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.


## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(positiveOutcome,resultsAfter)
print("t = " + str(t2))
print("p = " + str(p2))
