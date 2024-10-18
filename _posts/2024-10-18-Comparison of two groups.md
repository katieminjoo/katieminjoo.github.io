---
title: <i class="far fa-chart-bar"> A Comprehensive Approach to Comparing Two Independent Groups Statistically_When to Use t-Tests and Mann-Whitney U Tests</i>
date: 2024-10-18 16:00:00 +0900
categories: [MachineLearning]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
### When you want to see if there’s a significant difference between 2 datasets, we use statistics.

1. First, check if your data follows a normal distribution.
For this part, you can perform a Shapiro-Wilk test to check the normality of each group.  
you can use shapiro from scipy.stats just like the below code example.
```
from scipy.stats import shapiro

# Normality test
stat1, p1 = shapiro(group1)
stat2, p2 = shapiro(group2)
print(f'Group 1 p-value: {p1}, Group 2 p-value: {p2}')
```

>if **p-value > 0.05**, you can assume that the data *follows a normal distribution*.  
elif **p-value <= 0.05**, your data *does not follow a normal distribution*.  


2-1. If both groups pass the normality test, you can proceed with an Independent t-test to compare the means of the two groups. (code example below.)
```
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-statistic: {t_stat}, p-value: {p_value}")
```
>**t-statistic**: This is the value of the t-test statistic that indicates the size of the difference between the group means relative to the variance in the data.  
**p-value**: This tells you whether the difference is statistically significant. If the **p-value ≤ 0.05**, the difference is considered statistically significant, and the means are likely different.

and there’s a part that we haven’t dealt with yet. **Non-Normal Data**.

2-2. if the normality test fails *(p-vales ≤ 0.05)*, the t-test is not appropriate, and it’d be better to use a non-parametic test such as the Mann-Whitney U Test, which doesn’t assume normality.  
This test compares the ranks of the two groups instead of their means and is suitable when the normality assumption is violated.  

the example code goes like this.

```
from scipy.stats import mannwhitneyu

# Mann-Whitney U Test
stat, p_value = mannwhitneyu(group1, group2)
print(f'Mann-Whitney U: Statistics={stat}, p-value={p_value}')
```
>and we can interpret this test with   
If the p-value ≤ 0.05, you can reject the null hypothesis and conclude that the two groups are statistically different.  
If the p-value > 0.05, there is no statistically significant difference between the two groups. The difference could be due to random variation rather than a true underlying difference between the groups.  

---
* Mean VS Median for group comparison
Mean is used when the data follows a normal distribution and there are no outliers. The mean gives a good representation of the central tendency in normally distributed data.  
Median is used when the data does not follow a normal distribution or when there are outliers. The median is less sensitive to extreme values and gives a better representation of the central tendency for non-normally distributed data.
