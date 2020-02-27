```python
import pandas as pd
```


```python
rankings = {'co': ['India', 'South Africa', 'England', 'New Zealand', 'Australia'], 
            'wealth': ['low', 'middle', 'high', 'high', 'middle'],
            'num': [100, 60, 120, 120, 130],
            'ppl': [60000, None, 1, 19, 96],
            'liv': ['apt', 'condo', 'apt', 'motel', 'hotel']} 

df = pd.DataFrame(rankings)
```


```python
df
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
      <th>co</th>
      <th>wealth</th>
      <th>num</th>
      <th>ppl</th>
      <th>liv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>India</td>
      <td>low</td>
      <td>100</td>
      <td>60000.0</td>
      <td>apt</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Africa</td>
      <td>middle</td>
      <td>60</td>
      <td>NaN</td>
      <td>condo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>England</td>
      <td>high</td>
      <td>120</td>
      <td>1.0</td>
      <td>apt</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New Zealand</td>
      <td>high</td>
      <td>120</td>
      <td>19.0</td>
      <td>motel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Australia</td>
      <td>middle</td>
      <td>130</td>
      <td>96.0</td>
      <td>hotel</td>
    </tr>
  </tbody>
</table>
</div>



다음의 작업을 통해서 make_column_transformer의 사용법을 소개합니다.

> 1. OneHotEncoder : 'co', 'wealth', 'liv'  
> 2. MinMaxScaling : 'num'  
> 3. 사용하지 않을 변수 : "ppl"

select_dtypes를 활용하면 원하는 전처리를 각각의 칼럼에 쉽게 적용할 수 있습니다.


```python
numerical_ix = df.select_dtypes(include=['int64', 'float64']).columns
categorical_ix = df.select_dtypes(include=['object', 'bool']).columns
```


```python
categorical_ix
```




    Index(['co', 'wealth', 'liv'], dtype='object')




```python
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import make_column_transformer
```


```python
preprocess = make_column_transformer(
    (MinMaxScaler(), ["num"]), 
    (OneHotEncoder(handle_unknown = "ignore"), categorical_ix), verbose = True)
```

1. preprocess라는 인수로 저장을 하였습니다.

2. 만약 튜플에서 언급하지 않은 변수를 그대로 두길 원했다면, "remainder='passthrough"를 사용해주면 됩니다.


```python
res = preprocess.fit_transform(df)
```

    [ColumnTransformer] .. (1 of 2) Processing minmaxscaler, total=   0.0s
    [ColumnTransformer] . (2 of 2) Processing onehotencoder, total=   0.0s
    

verbose를 true로 해주었기 때문에 걸린 시간이 잘 표현이 됩니다.


```python
pd.DataFrame(res)
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
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.571429</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.857143</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.857143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



> 컬럼 이름을 지정해주지 않았지만, 각 변수의 카테고리 피쳐 갯수의 합만큼 컬럼의 갯수가 늘어났음을 확인할 수 있습니다.

#### 새로운 test 데이터셋을 마주하면 어떻게 바뀌는지 확인해보겠습니다.


```python
rankings = {'co': ['Kor', 'NoKo', 'England', 'New Zealand', 'Australia'], 
            'wealth': ['Super A', 'high', 'low', 'middle', 'middle'],
            'ppl': [60000, None, 1, 19, 96],
            'num': [100, 60, 120, 120, 130],
            'liv': ['Super Condo', 'condo', 'apt', 'motel', 'hotel']} 

test = pd.DataFrame(rankings)
test
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
      <th>co</th>
      <th>wealth</th>
      <th>ppl</th>
      <th>num</th>
      <th>liv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kor</td>
      <td>Super A</td>
      <td>60000.0</td>
      <td>100</td>
      <td>Super Condo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NoKo</td>
      <td>high</td>
      <td>NaN</td>
      <td>60</td>
      <td>condo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>England</td>
      <td>low</td>
      <td>1.0</td>
      <td>120</td>
      <td>apt</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New Zealand</td>
      <td>middle</td>
      <td>19.0</td>
      <td>120</td>
      <td>motel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Australia</td>
      <td>middle</td>
      <td>96.0</td>
      <td>130</td>
      <td>hotel</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmp = preprocess.transform(test)
```


```python
pd.DataFrame(tmp)
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
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.571429</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.857143</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.857143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



> 0번째 index에 해당하는 값들은 모두 새로운 피쳐를 사용했습니다.  

>새로운 피쳐를 마주해도 "ignore"하도록 세팅했기 때문에 여전히 같은 차원을 유지하고 있음을 알 수 있습니다.

> 이는 "handle_unknown = "ignore""를 해주었기 때문입니다.  

***

추가 자료 : https://jorisvandenbossche.github.io/blog/2018/05/28/scikit-learn-columntransformer/
