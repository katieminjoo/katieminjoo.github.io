
# sklearn.preprocessing.LabelEncoder


```python
import pandas as pd

tr = pd.read_csv("train.csv", index_col = 0)
tr.shape
```




    (100, 6)




```python
tr.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>click</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1b1Yz4S9wG</th>
      <td>0</td>
      <td>GdBSlETcLy</td>
      <td>taRA9jVfVL</td>
      <td>AsY5LC0NLu</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>eCYeFjnExb</th>
      <td>0</td>
      <td>GlheP2trvZ</td>
      <td>jWRKzxzhyX</td>
      <td>nz5kFLSj4p</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>QHcMnYqF3h</th>
      <td>0</td>
      <td>WGJnvetv2a</td>
      <td>DW5C3As8ij</td>
      <td>nz5kFLSj4p</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
  </tbody>
</table>
</div>

데이터는 철저히 암호화되어 있으며 완전히 범주형 자료로 해석해도 무방함을 알 수 있다. 따라서 이 경우에 단순한 LabelEncoding을 해주다면 메모리 용량을 줄이는 한편, 처리 속도를 높일 수 있을 것이다.


```python
tr.agg(["nunique"])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>click</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>nunique</th>
      <td>2</td>
      <td>57</td>
      <td>40</td>
      <td>26</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



***

## 한 번에 모든 데이터를 LabelEncoding하기


```python
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
d = defaultdict(LabelEncoder)
```


```python
d
```




    defaultdict(sklearn.preprocessing.label.LabelEncoder, {})




```python
# Encoding the variable
fit = tr.apply(lambda x: d[x.name].fit_transform(x))
```


```python
fit.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>click</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1b1Yz4S9wG</th>
      <td>0</td>
      <td>9</td>
      <td>35</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>eCYeFjnExb</th>
      <td>0</td>
      <td>12</td>
      <td>27</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>QHcMnYqF3h</th>
      <td>0</td>
      <td>26</td>
      <td>8</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>p5v9KCdjS6</th>
      <td>1</td>
      <td>8</td>
      <td>32</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>aAEDD9AeIv</th>
      <td>0</td>
      <td>22</td>
      <td>1</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
d
```




    defaultdict(sklearn.preprocessing.label.LabelEncoder,
                {'click': LabelEncoder(),
                 'adset_id': LabelEncoder(),
                 'campaign_id': LabelEncoder(),
                 'device_model': LabelEncoder(),
                 'device_os': LabelEncoder(),
                 'device_country': LabelEncoder()})



***

## 임의의 일부분을 원래 데이터로 다시 살펴보기 위해서


```python
test = fit.iloc[50,:]
test = pd.DataFrame(test).T
test
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>click</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MhUDSdQoqp</th>
      <td>0</td>
      <td>9</td>
      <td>35</td>
      <td>19</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
test.apply(lambda x: d[x.name].inverse_transform(x))
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>click</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MhUDSdQoqp</th>
      <td>0</td>
      <td>GdBSlETcLy</td>
      <td>taRA9jVfVL</td>
      <td>fiJqINpRUy</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
  </tbody>
</table>
</div>


