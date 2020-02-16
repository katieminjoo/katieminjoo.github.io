

```python
import pandas as pd
aud = pd.read_csv("data/[label] aud_wo_install&house.csv")
aud.head(3)
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
      <th>device_ifa</th>
      <th>age</th>
      <th>gender</th>
      <th>marry</th>
      <th>cate_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1648210</td>
      <td>6</td>
      <td>M</td>
      <td>M</td>
      <td>20008:5,21001:1,01003:2,14004:2,06009:2,03003:...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1885479</td>
      <td>6</td>
      <td>F</td>
      <td>M</td>
      <td>09001:1,13002:3,01003:1,16004:3,18002:1,21007:...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1289369</td>
      <td>7</td>
      <td>F</td>
      <td>M</td>
      <td>16002:5,19001:4,04011:1,p0011:1,18004:3,p0010:...</td>
    </tr>
  </tbody>
</table>
</div>




```python
def short(x):
    return x[1::2]

def long(x):
    return x[::2]
```


```python
aud["cc_list"] = aud["cate_code"].str.findall(r"[\w']+")
aud["short"] = aud["cc_list"].apply(short)
aud["long"] = aud["cc_list"].apply(long)
aud['counts'] = aud['long'].str.len() 
```


```python
aud.head(3)
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
      <th>device_ifa</th>
      <th>age</th>
      <th>gender</th>
      <th>marry</th>
      <th>cate_code</th>
      <th>cc_list</th>
      <th>short</th>
      <th>long</th>
      <th>counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1648210</td>
      <td>6</td>
      <td>M</td>
      <td>M</td>
      <td>20008:5,21001:1,01003:2,14004:2,06009:2,03003:...</td>
      <td>[20008, 5, 21001, 1, 01003, 2, 14004, 2, 06009...</td>
      <td>[5, 1, 2, 2, 2, 5, 1, 1, 2, 3, 3, 2, 2, 4, 3, ...</td>
      <td>[20008, 21001, 01003, 14004, 06009, 03003, 130...</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1885479</td>
      <td>6</td>
      <td>F</td>
      <td>M</td>
      <td>09001:1,13002:3,01003:1,16004:3,18002:1,21007:...</td>
      <td>[09001, 1, 13002, 3, 01003, 1, 16004, 3, 18002...</td>
      <td>[1, 3, 1, 3, 1, 4, 3, 5, 1, 3, 3, 2, 4, 4, 2, ...</td>
      <td>[09001, 13002, 01003, 16004, 18002, 21007, 080...</td>
      <td>56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1289369</td>
      <td>7</td>
      <td>F</td>
      <td>M</td>
      <td>16002:5,19001:4,04011:1,p0011:1,18004:3,p0010:...</td>
      <td>[16002, 5, 19001, 4, 04011, 1, p0011, 1, 18004...</td>
      <td>[5, 4, 1, 1, 3, 1, 4, 1, 1, 4, 4, 4, 3, 3, 4, ...</td>
      <td>[16002, 19001, 04011, p0011, 18004, p0010, 190...</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>




```python
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
sns.boxplot(aud.counts, ax=ax_box)
sns.distplot(aud.counts, ax=ax_hist)
 
ax_box.set(xlabel='')
```




    [Text(0.5, 0, '')]




![png](TMP_files/TMP_5_1.png)



```python
from collections import Counter
from  itertools import chain

vc = pd.Series(Counter(chain(*aud.long))).sort_index().rename_axis('value').reset_index(name='counts')
vc = vc.sort_values(by =['counts'] , ascending = False)
vc['ratio'] = vc['counts'] / len(aud)
vc.head(3)
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
      <th>value</th>
      <th>counts</th>
      <th>ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>129</th>
      <td>14004</td>
      <td>812687</td>
      <td>0.999886</td>
    </tr>
    <tr>
      <th>179</th>
      <td>20008</td>
      <td>810422</td>
      <td>0.997099</td>
    </tr>
    <tr>
      <th>133</th>
      <td>15003</td>
      <td>810370</td>
      <td>0.997035</td>
    </tr>
  </tbody>
</table>
</div>




```python
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

sns.boxplot(vc.ratio, ax=ax_box)
sns.distplot(vc.ratio, ax=ax_hist)
 
ax_box.set(xlabel='')
```




    [Text(0.5, 0, '')]




![png](TMP_files/TMP_7_1.png)



```python
criteria = []

for i in range(13) : 
    criteria.append(vc.head(i+1).value.tolist())
```
cnt = 0
pct = []     # 밑에서 그래프를 그리기 위한 percent
exc = []     # nested_list로 사용하기 위함으로, 각각의 내부 리스트는 기준에 부합하는 index를 포함하게된다.
for cri in criteria :
    cnt += 1
    tmp = []
    for i in norm.index :
        if all(elem in norm.long[i] for elem in cri) :
            tmp.append(norm.device_ifa[i])
    exc.append(tmp)
    pct.append( len(tmp) / len(norm) )
    print("상위 {}개의 공통질문 커버리지 : {}".format(cnt, len(tmp) / len(norm)))상위 1개의 공통질문 커버리지 : 0.9999051777854949
상위 2개의 공통질문 커버리지 : 0.9971245471315664
상위 3개의 공통질문 커버리지 : 0.9945471069372918
상위 4개의 공통질문 커버리지 : 0.9914844725545104
상위 5개의 공통질문 커버리지 : 0.9865155422229775
상위 6개의 공통질문 커버리지 : 0.9694475436120614
상위 7개의 공통질문 커버리지 : 0.9290791408368492
상위 8개의 공통질문 커버리지 : 0.8853439337180407
상위 9개의 공통질문 커버리지 : 0.8346017343845054
상위 10개의 공통질문 커버리지 : 0.7901276528669559
상위 11개의 공통질문 커버리지 : 0.747868963088298
상위 12개의 공통질문 커버리지 : 0.7126825327629223
상위 13개의 공통질문 커버리지 : 0.6684288821076638
> 92%의 audience들은 상위 7개의 질문을 모두 가지고 있다.  
> 96%의 audience들은 상위 6개의 질문을 모두 가지고 있다.


```python
import matplotlib.pyplot as plt

x = list(range(1,14))
y = pct
plt.plot(x, y)
plt.show()
```


![png](TMP_files/TMP_12_0.png)



```python
good = criteria[-1]
trash = list(set(vc.value) - set(criteria[-1]))

Li = []

for i in range(len(aud)) :
    tmp_dict = dict(sorted(dict(zip(aud['long'][i], aud['short'][i])).items()))
    [tmp_dict.pop(key, None) for key in trash]
    Li.append(tmp_dict)
```

> 1. 두 개의 리스트로부터 dict 도출  
> 2. 도출한 dict을 알파벳 순서로 sort  
> 3. 이를 list에 추가함으로써 저장


```python
res = pd.DataFrame.from_records(Li, index = aud.device_ifa.values)
```


```python
res.head()
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
      <th>06001</th>
      <th>06006</th>
      <th>06009</th>
      <th>14004</th>
      <th>14005</th>
      <th>15001</th>
      <th>15003</th>
      <th>15004</th>
      <th>19001</th>
      <th>19003</th>
      <th>20008</th>
      <th>21007</th>
      <th>23005</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1648210</th>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1885479</th>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1289369</th>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>NaN</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1415766</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1928794</th>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>


