

```python
import pandas as pd
```


```python
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>normalized_losses</th>
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>num_doors</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>wheel_base</th>
      <th>...</th>
      <th>engine_size</th>
      <th>fuel_system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression_ratio</th>
      <th>horsepower</th>
      <th>peak_rpm</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111.0</td>
      <td>5000.0</td>
      <td>21</td>
      <td>27</td>
      <td>13495.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111.0</td>
      <td>5000.0</td>
      <td>21</td>
      <td>27</td>
      <td>16500.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>152</td>
      <td>mpfi</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154.0</td>
      <td>5000.0</td>
      <td>19</td>
      <td>26</td>
      <td>16500.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164.0</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102.0</td>
      <td>5500.0</td>
      <td>24</td>
      <td>30</td>
      <td>13950.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164.0</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115.0</td>
      <td>5500.0</td>
      <td>18</td>
      <td>22</td>
      <td>17450.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 26 columns</p>
</div>




```python
ag = df.agg(["size", "count", "nunique"]).T
ag.T
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>normalized_losses</th>
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>num_doors</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>wheel_base</th>
      <th>...</th>
      <th>engine_size</th>
      <th>fuel_system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression_ratio</th>
      <th>horsepower</th>
      <th>peak_rpm</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>size</th>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>...</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
    </tr>
    <tr>
      <th>count</th>
      <td>205</td>
      <td>164</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>203</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>...</td>
      <td>205</td>
      <td>205</td>
      <td>201</td>
      <td>201</td>
      <td>205</td>
      <td>203</td>
      <td>203</td>
      <td>205</td>
      <td>205</td>
      <td>201</td>
    </tr>
    <tr>
      <th>nunique</th>
      <td>6</td>
      <td>51</td>
      <td>22</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>3</td>
      <td>2</td>
      <td>53</td>
      <td>...</td>
      <td>44</td>
      <td>8</td>
      <td>38</td>
      <td>36</td>
      <td>32</td>
      <td>59</td>
      <td>23</td>
      <td>29</td>
      <td>30</td>
      <td>186</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 26 columns</p>
</div>



> 편의상 None 값이 있는 컬럼은 모두 제거해주고 시작하자.


```python
col = ag[ag['count'].values == 205].index
df = df[col]
df.shape
```




    (205, 19)




```python
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>wheel_base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb_weight</th>
      <th>engine_type</th>
      <th>num_cylinders</th>
      <th>engine_size</th>
      <th>fuel_system</th>
      <th>compression_ratio</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548</td>
      <td>dohc</td>
      <td>four</td>
      <td>130</td>
      <td>mpfi</td>
      <td>9.0</td>
      <td>21</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548</td>
      <td>dohc</td>
      <td>four</td>
      <td>130</td>
      <td>mpfi</td>
      <td>9.0</td>
      <td>21</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>171.2</td>
      <td>65.5</td>
      <td>52.4</td>
      <td>2823</td>
      <td>ohcv</td>
      <td>six</td>
      <td>152</td>
      <td>mpfi</td>
      <td>9.0</td>
      <td>19</td>
      <td>26</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.agg(['nunique'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>wheel_base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb_weight</th>
      <th>engine_type</th>
      <th>num_cylinders</th>
      <th>engine_size</th>
      <th>fuel_system</th>
      <th>compression_ratio</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>nunique</th>
      <td>6</td>
      <td>22</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>3</td>
      <td>2</td>
      <td>53</td>
      <td>75</td>
      <td>44</td>
      <td>49</td>
      <td>171</td>
      <td>7</td>
      <td>7</td>
      <td>44</td>
      <td>8</td>
      <td>32</td>
      <td>29</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



예제를 들어 살펴보기 간편한 임의의 칼럼들을 골랐습니다.


```python
data = df[['curb_weight', 'make', 'body_style', 'drive_wheels']]
data.shape
```




    (205, 4)



`make`와 `body_style`은 22개, 5개의 피쳐를 가지므로 2진법으로 표현해줄 것입니다. : 22 -> 5자리, 5 -> 3자리 : 총 8자리로 축소

`drive_wheels`는 OneHotEncoding을 사용할 것입니다.

`curb_weight` 변수는 MinMaxScaler를 해줄겁니다.


```python
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from category_encoders import *
```


```python
preprocess = make_column_transformer(
    (MinMaxScaler(), ['curb_weight']),
    (BinaryEncoder(drop_invariant=True), ['make', 'body_style']),
    (OneHotEncoder(), ['drive_wheels']),
    verbose = True, remainder='drop')
```


```python
res = preprocess.fit_transform(data)
res = pd.DataFrame(res)
res.shape
```

    [ColumnTransformer] .. (1 of 3) Processing minmaxscaler, total=   0.0s
    [ColumnTransformer] . (2 of 3) Processing binaryencoder, total=   0.1s
    [ColumnTransformer] . (3 of 3) Processing onehotencoder, total=   0.0s
    




    (205, 12)




```python
res.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.411171</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.411171</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.517843</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



예상대로 12자리 숫자가 나왔음을 확인할 수 있습니다.
