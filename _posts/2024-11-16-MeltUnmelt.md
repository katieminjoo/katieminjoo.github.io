---
title: Melt and Unmelt(Pivot) in Pandas, Python
date: 2024-11-16 10:30:00 +0900
categories: [Pandas]
tags: [python]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
Reshaping data from long to wide or wide to long is a common task in data manipulation, and pandas provides several powerful methods to achieve this.

# Converting Long to Wide
Long data is where multiple rows represent the same overservation across different conditions or categories.

## Methods for Long -> Wide

## 1.pivot()
Reshapes data by turning unique values from a column into new column, It is commonly used when converting time-series data where rows represent repeated measurements into a wide format.
```
df.pivot(index = 'identifier', columns = 'category', values = 'value')
```
* param : {'index' : what you want the index to be, 'columns' : what you want the column to be, 'value' : what you want the value to be}

## 2. pivot_table()
Similar to pivot(), but it allows for aggregation in case of duplicate entries. so this can aggregate and reshape simultaneously when you have duplicates.
```
df.pivot_table(index = 'identifier', columns = 'category', values = 'value', aggfunc = 'mean')
```

## 3. unstack()

moves an index level to columns, converting hierarchical rows into columns. it works well with MultiIndex Dataframes.
```
df_wide = df.set_index(['identifier', 'category]).unstack()
```

# Converting Wide to Long
wide data is where each column represents a variable, condition, or category.

## Methods for Wide to Long

## 1. melt()
`column to value`  
Transforms wide data into a long format by combining multiple columns into two : one for the variable names and one for values.
```
df.melt(id_vars = '', var_name = '', value_name = '')
```
-> returns `DataFrame`

## 2. wide_to_long()
Reshapes column names with a pattern into a long format.
```
pd.wide_to_long(df, stubnames = 'measure', i = '', j = '')
```
in this case, there should be columns named 'measure_1', 'measure_2', ... since we give 'measure' as `stubnames`.  
`i` is the new column name that will identify each rows.  
`j` is the new column that will contain the values.  

ex) if there was this row with the column name 'measure_pink' and if the value was 7, then we give stubnames as stubnames, color as i, since it seems like letters after '_' refers color palettes. and then let's say 7 is the count number that we got from somewhere, then j should be 'count'.

## 3. stack()
`column to index`
it moves column into rows.
```
df.set_index('').stack().reset_index()
```
-> returns `Series`

| **Method**             | **Converts From** | **Converts To**       | **Best Use Case**                                      |
|------------------------|-------------------|-----------------------|-------------------------------------------------------|
| **`pivot()`**          | Long             | Wide                  | Unique index-column combinations                     |
| **`pivot_table()`**    | Long             | Wide                  | Aggregating and reshaping simultaneously             |
| **`melt()`**           | Wide             | Long                  | Tidy format where one column holds variable names    |
| **`wide_to_long()`**   | Wide             | Long                  | Panel data or repeated measurement reshaping         |
| **`stack()`**          | Wide             | Long                  | Wide format with MultiIndex conversion               |
| **`unstack()`**        | Long             | Wide                  | Moving index levels into columns                     |

### Key Considerations
* pivot_table() instead of pivot() if you expect duplicates.
* for stack() and unstack(), make sure your DataFrame is properly indexed.
* for custom patterns, consider wide_to_long() or write custom reshaping logic using grobupy() and agg() or etc.