
데이터 : https://www.kaggle.com/rodolfomendes/abalone-dataset  
참고자료 : https://machinelearningmastery.com/columntransformer-for-numerical-and-categorical-data/

columntransformer 사용법과 특징을 익히고, 실제로 이를 활용해서 모델 결과를 확인해보겠습니다.

> 모델은 [Epsilon-Support Vector Regression](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)을 사용하였습니다.

***

## columntransformer 익히기


```python
import pandas as pd
from pandas import read_csv
# load dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/abalone.csv'
dataframe = read_csv(url, header=None)
```


```python
dataframe.set_axis(["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"],  axis=1, inplace=True)
dataframe.head(3)
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
      <th>Sex</th>
      <th>Length</th>
      <th>Diameter</th>
      <th>Height</th>
      <th>Whole weight</th>
      <th>Shucked weight</th>
      <th>Viscera weight</th>
      <th>Shell weight</th>
      <th>Rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>0.455</td>
      <td>0.365</td>
      <td>0.095</td>
      <td>0.5140</td>
      <td>0.2245</td>
      <td>0.1010</td>
      <td>0.15</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M</td>
      <td>0.350</td>
      <td>0.265</td>
      <td>0.090</td>
      <td>0.2255</td>
      <td>0.0995</td>
      <td>0.0485</td>
      <td>0.07</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>0.530</td>
      <td>0.420</td>
      <td>0.135</td>
      <td>0.6770</td>
      <td>0.2565</td>
      <td>0.1415</td>
      <td>0.21</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
X, y = dataframe.drop("Rings", axis=1), dataframe["Rings"]
print(X.shape, y.shape)
```

    (4177, 8) (4177,)
    


```python
numerical_ix = X.select_dtypes(include=['int64', 'float64']).columns
categorical_ix = X.select_dtypes(include=['object', 'bool']).columns
```


```python
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
```


```python
t = [('cat', OneHotEncoder(handle_unknown = "ignore"), categorical_ix), ('num', MinMaxScaler(), numerical_ix)]
col_transform = ColumnTransformer(transformers=t)
```


```python
col_transform.fit_transform(X).shape
```




    (4177, 10)



> 처음 생각과 다르게, nunique가 3개라서 위에서 10개의 칼럼이 만들어진 것임을 확인할 수 있습니다. 이는 아래에서 확인하겠습니다.

***

#### 최종 결과


```python
pd.DataFrame(col_transform.fit_transform(X)).head(3)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.513514</td>
      <td>0.521008</td>
      <td>0.084071</td>
      <td>0.181335</td>
      <td>0.150303</td>
      <td>0.132324</td>
      <td>0.147982</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.371622</td>
      <td>0.352941</td>
      <td>0.079646</td>
      <td>0.079157</td>
      <td>0.066241</td>
      <td>0.063199</td>
      <td>0.068261</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.614865</td>
      <td>0.613445</td>
      <td>0.119469</td>
      <td>0.239065</td>
      <td>0.171822</td>
      <td>0.185648</td>
      <td>0.207773</td>
    </tr>
  </tbody>
</table>
</div>



### test 데이터셋 

새로운 피쳐를 가지고 있는 데이터셋을 만들어보겠습니다.


```python
tmp = X.head(3)
tmp
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
      <th>Sex</th>
      <th>Length</th>
      <th>Diameter</th>
      <th>Height</th>
      <th>Whole weight</th>
      <th>Shucked weight</th>
      <th>Viscera weight</th>
      <th>Shell weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>0.455</td>
      <td>0.365</td>
      <td>0.095</td>
      <td>0.5140</td>
      <td>0.2245</td>
      <td>0.1010</td>
      <td>0.15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M</td>
      <td>0.350</td>
      <td>0.265</td>
      <td>0.090</td>
      <td>0.2255</td>
      <td>0.0995</td>
      <td>0.0485</td>
      <td>0.07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>0.530</td>
      <td>0.420</td>
      <td>0.135</td>
      <td>0.6770</td>
      <td>0.2565</td>
      <td>0.1415</td>
      <td>0.21</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmp['Sex'].replace(['M'], 'ABC', inplace = True)
tmp
```

    C:\Users\13Z970-G.AR30K\Anaconda3\lib\site-packages\pandas\core\generic.py:6586: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self._update_inplace(new_data)
    




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
      <th>Sex</th>
      <th>Length</th>
      <th>Diameter</th>
      <th>Height</th>
      <th>Whole weight</th>
      <th>Shucked weight</th>
      <th>Viscera weight</th>
      <th>Shell weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ABC</td>
      <td>0.455</td>
      <td>0.365</td>
      <td>0.095</td>
      <td>0.5140</td>
      <td>0.2245</td>
      <td>0.1010</td>
      <td>0.15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>0.350</td>
      <td>0.265</td>
      <td>0.090</td>
      <td>0.2255</td>
      <td>0.0995</td>
      <td>0.0485</td>
      <td>0.07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>0.530</td>
      <td>0.420</td>
      <td>0.135</td>
      <td>0.6770</td>
      <td>0.2565</td>
      <td>0.1415</td>
      <td>0.21</td>
    </tr>
  </tbody>
</table>
</div>



전혀 다른 피쳐를 추가했습니다.


```python
pd.DataFrame(col_transform.transform(tmp))
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.513514</td>
      <td>0.521008</td>
      <td>0.084071</td>
      <td>0.181335</td>
      <td>0.150303</td>
      <td>0.132324</td>
      <td>0.147982</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.371622</td>
      <td>0.352941</td>
      <td>0.079646</td>
      <td>0.079157</td>
      <td>0.066241</td>
      <td>0.063199</td>
      <td>0.068261</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.614865</td>
      <td>0.613445</td>
      <td>0.119469</td>
      <td>0.239065</td>
      <td>0.171822</td>
      <td>0.185648</td>
      <td>0.207773</td>
    </tr>
  </tbody>
</table>
</div>



위에서 handle_unknown으로 처리해주었기 때문에, 새로운 피쳐를 마주해도 모두 0인 벡터로 반환하여 해결합니다.

***

##### 참고 


```python
X.agg(["size", "nunique"])
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
      <th>Sex</th>
      <th>Length</th>
      <th>Diameter</th>
      <th>Height</th>
      <th>Whole weight</th>
      <th>Shucked weight</th>
      <th>Viscera weight</th>
      <th>Shell weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>size</th>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
      <td>4177</td>
    </tr>
    <tr>
      <th>nunique</th>
      <td>3</td>
      <td>134</td>
      <td>111</td>
      <td>51</td>
      <td>2429</td>
      <td>1515</td>
      <td>880</td>
      <td>926</td>
    </tr>
  </tbody>
</table>
</div>




```python
X['Sex'].agg(["unique", "nunique"])
```




    unique     [M, F, I]
    nunique            3
    Name: Sex, dtype: object



실제로 Infant라는 피쳐가 Sex 카테고리에 존재함을 확인할 수 있습니다.


```python
dataframe[dataframe['Sex'].values == 'I'].shape
```




    (1342, 9)



그리고 그 수는 꽤나 많습니다.

***


```python
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
```


```python
model = SVR(kernel='rbf',gamma='scale',C=100)
pipeline = Pipeline(steps=[('prep',col_transform), ('m', model)])
```


```python
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy import absolute, mean, std
```


```python
cv = KFold(n_splits=10, shuffle=True, random_state=1)
# evaluate the pipeline using cross validation and calculate MAE
scores = cross_val_score(pipeline, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# convert MAE scores to positive values
scores = absolute(scores)
# summarize the model performance
print('MAE: %.3f (%.3f)' % (mean(scores), std(scores)))
```

    MAE: 1.467 (0.048)
    
