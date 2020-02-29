
### 사용할 데이터


```python
import pandas as pd

tr = pd.read_csv("train.csv.gz", compression = "gzip")
tr.shape
```




    (5500000, 25)




```python
pd.set_option("display.max_columns", None)
tr.head(3)
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
      <th>click</th>
      <th>event_datetime</th>
      <th>bid_id</th>
      <th>ssp_id</th>
      <th>campaign_id</th>
      <th>adset_id</th>
      <th>placement_type</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>media_bundle</th>
      <th>media_domain</th>
      <th>publisher_id</th>
      <th>publisher_name</th>
      <th>device_ifa</th>
      <th>device_os</th>
      <th>device_os_version</th>
      <th>device_model</th>
      <th>device_carrier</th>
      <th>device_make</th>
      <th>device_connection_type</th>
      <th>device_language</th>
      <th>device_country</th>
      <th>device_region</th>
      <th>device_city</th>
      <th>advertisement_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2019-10-01 00:00:04.878</td>
      <td>1b1Yz4S9wG</td>
      <td>A6E0SZLhXP</td>
      <td>taRA9jVfVL</td>
      <td>GdBSlETcLy</td>
      <td>1pcQ3RJgQt</td>
      <td>IyDyyhXBnW</td>
      <td>dAWR8DOmzo</td>
      <td>V8yCzbCKcB</td>
      <td>pjBT3sDGbH</td>
      <td>YOSTF4U4h4</td>
      <td>tXBXkBEsgT</td>
      <td>McFB9FyHPk</td>
      <td>TG14pLUXCY</td>
      <td>V7LhUlY53m</td>
      <td>AsY5LC0NLu</td>
      <td>wrzW2uRaKh</td>
      <td>HiGuczmB3W</td>
      <td>Hx7e3tE5mu</td>
      <td>8GSkINt29e</td>
      <td>PCCn9Q1m20</td>
      <td>EdsKnCCtPO</td>
      <td>e7JXTJQ5Qw</td>
      <td>TbkcVoisoR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>2019-10-01 00:00:04.940</td>
      <td>eCYeFjnExb</td>
      <td>CD3hRiI3bN</td>
      <td>jWRKzxzhyX</td>
      <td>GlheP2trvZ</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>o9tQ73S7C8</td>
      <td>pjBT3sDGbH</td>
      <td>FpOvhbPDXd</td>
      <td>BnqjbSLXhH</td>
      <td>zY0iVzLcSA</td>
      <td>TG14pLUXCY</td>
      <td>aU9KSuwh6B</td>
      <td>nz5kFLSj4p</td>
      <td>wrzW2uRaKh</td>
      <td>rp6gWKT7zk</td>
      <td>WCK2G73H3A</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>aI9W3Httpm</td>
      <td>uuYScbMuRa</td>
      <td>Hy6SSlFrrj</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>2019-10-01 00:00:04.963</td>
      <td>QHcMnYqF3h</td>
      <td>SrN77Arvqh</td>
      <td>DW5C3As8ij</td>
      <td>WGJnvetv2a</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>p75piF74nC</td>
      <td>pjBT3sDGbH</td>
      <td>FpOvhbPDXd</td>
      <td>BnqjbSLXhH</td>
      <td>u5Mkw7fBRk</td>
      <td>TG14pLUXCY</td>
      <td>aU9KSuwh6B</td>
      <td>nz5kFLSj4p</td>
      <td>wrzW2uRaKh</td>
      <td>rp6gWKT7zk</td>
      <td>Hx7e3tE5mu</td>
      <td>8GSkINt29e</td>
      <td>PCCn9Q1m20</td>
      <td>EdsKnCCtPO</td>
      <td>e7JXTJQ5Qw</td>
      <td>7dyzy9aZoJ</td>
    </tr>
  </tbody>
</table>
</div>



***

## LabelEncoder

#### 인코딩이 불필요한 변수 탐색


```python
nuni = tr.agg(["nunique"])
nuni
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
      <th>click</th>
      <th>event_datetime</th>
      <th>bid_id</th>
      <th>ssp_id</th>
      <th>campaign_id</th>
      <th>adset_id</th>
      <th>placement_type</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>media_bundle</th>
      <th>media_domain</th>
      <th>publisher_id</th>
      <th>publisher_name</th>
      <th>device_ifa</th>
      <th>device_os</th>
      <th>device_os_version</th>
      <th>device_model</th>
      <th>device_carrier</th>
      <th>device_make</th>
      <th>device_connection_type</th>
      <th>device_language</th>
      <th>device_country</th>
      <th>device_region</th>
      <th>device_city</th>
      <th>advertisement_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>nunique</th>
      <td>2</td>
      <td>5478966</td>
      <td>5500000</td>
      <td>17</td>
      <td>186</td>
      <td>872</td>
      <td>4</td>
      <td>5815</td>
      <td>6810</td>
      <td>6286</td>
      <td>162</td>
      <td>3939</td>
      <td>1222</td>
      <td>1869137</td>
      <td>2</td>
      <td>125</td>
      <td>1664</td>
      <td>536</td>
      <td>299</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>148</td>
      <td>1326</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



> 1. label 인코딩을 해줄 필요 없는 변수 : `event_datetime`, `bid_id`  
> 2. click과 관계를 봐줄 필요가 없는 변수 : `device_ifa`


```python
tr.drop(["event_datetime", "bid_id", "device_ifa"], axis = 1, inplace = True)
tr.shape
```




    (5500000, 22)



#### 라벨인코딩


```python
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
d = defaultdict(LabelEncoder)
df = tr.apply(lambda x: d[x.name].fit_transform(x))
df.head()
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
      <th>click</th>
      <th>ssp_id</th>
      <th>campaign_id</th>
      <th>adset_id</th>
      <th>placement_type</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>media_bundle</th>
      <th>media_domain</th>
      <th>publisher_id</th>
      <th>publisher_name</th>
      <th>device_os</th>
      <th>device_os_version</th>
      <th>device_model</th>
      <th>device_carrier</th>
      <th>device_make</th>
      <th>device_connection_type</th>
      <th>device_language</th>
      <th>device_country</th>
      <th>device_region</th>
      <th>device_city</th>
      <th>advertisement_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>166</td>
      <td>233</td>
      <td>0</td>
      <td>1773</td>
      <td>4333</td>
      <td>3130</td>
      <td>133</td>
      <td>2247</td>
      <td>1095</td>
      <td>0</td>
      <td>61</td>
      <td>289</td>
      <td>509</td>
      <td>92</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>39</td>
      <td>852</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>4</td>
      <td>138</td>
      <td>239</td>
      <td>0</td>
      <td>4082</td>
      <td>3699</td>
      <td>5088</td>
      <td>133</td>
      <td>1021</td>
      <td>247</td>
      <td>0</td>
      <td>74</td>
      <td>1345</td>
      <td>509</td>
      <td>266</td>
      <td>5</td>
      <td>11</td>
      <td>0</td>
      <td>92</td>
      <td>1209</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>7</td>
      <td>40</td>
      <td>466</td>
      <td>0</td>
      <td>4082</td>
      <td>3699</td>
      <td>5198</td>
      <td>133</td>
      <td>1021</td>
      <td>247</td>
      <td>0</td>
      <td>74</td>
      <td>1345</td>
      <td>509</td>
      <td>266</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>39</td>
      <td>852</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>13</td>
      <td>156</td>
      <td>218</td>
      <td>2</td>
      <td>4222</td>
      <td>3380</td>
      <td>1440</td>
      <td>133</td>
      <td>3574</td>
      <td>1150</td>
      <td>0</td>
      <td>61</td>
      <td>535</td>
      <td>220</td>
      <td>224</td>
      <td>5</td>
      <td>11</td>
      <td>0</td>
      <td>39</td>
      <td>852</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>7</td>
      <td>9</td>
      <td>430</td>
      <td>0</td>
      <td>4082</td>
      <td>3699</td>
      <td>795</td>
      <td>133</td>
      <td>1021</td>
      <td>247</td>
      <td>0</td>
      <td>74</td>
      <td>1345</td>
      <td>509</td>
      <td>266</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>39</td>
      <td>852</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>



### 각 피쳐별 클릭과의 관계성 파악하기


```python
import matplotlib.pyplot as plt
```


```python
dic = {}
cnt = 0
for i in df.columns[1:] :
    tmp = df[[i, 'click']].groupby([i]).agg(['sum', 'count'])
    tmp = pd.DataFrame(tmp.to_records())
    tmp.set_axis(["id", "click", "total"], axis=1, inplace=True)
    
    tmp['CTR per features'] = tmp['click'] / tmp['total']
    tmp['frequency ratio'] = tmp['total'] / tmp.total.sum()
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)
    
    tmp['cum_perc'] = 100*tmp['frequency ratio'].cumsum()
    tmp.index = range(len(tmp))
    dic[i] = tmp[tmp.cum_perc.values >= 90].index[0] / len(tmp)
    
    
    tmp[['frequency ratio']].plot(kind = 'bar',  figsize = (45, 20), fontsize = 50)
    tmp['CTR per features'].plot(secondary_y=True, fontsize = 50, color='red', lw= 10, legend = True, mark_right = False)
    plt.rc('legend', fontsize=40)
    
    ax = plt.gca()
    plt.xlim([-0.4, len(tmp)])
    ax.set_xticklabels(tuple(tmp.id))
    
    cnt += 1
    fn = '[' + str(cnt) + ']'+ i
    plt.suptitle(fn + ': ' + str(nuni[i][0]), fontsize=55)
    
    plt.savefig(fn + ".png")
    print(fn + '\t\t\t\t저장이 완료되었습니다.======================{}/{}'.format(cnt, len(df.columns[1:])))
    plt.close('all')
```

    [1]ssp_id				저장이 완료되었습니다.======================1/21
    [2]campaign_id				저장이 완료되었습니다.======================2/21
    [3]adset_id				저장이 완료되었습니다.======================3/21
    [4]placement_type				저장이 완료되었습니다.======================4/21
    [5]media_id				저장이 완료되었습니다.======================5/21
    [6]media_name				저장이 완료되었습니다.======================6/21
    [7]media_bundle				저장이 완료되었습니다.======================7/21
    [8]media_domain				저장이 완료되었습니다.======================8/21
    [9]publisher_id				저장이 완료되었습니다.======================9/21
    [10]publisher_name				저장이 완료되었습니다.======================10/21
    [11]device_os				저장이 완료되었습니다.======================11/21
    [12]device_os_version				저장이 완료되었습니다.======================12/21
    [13]device_model				저장이 완료되었습니다.======================13/21
    [14]device_carrier				저장이 완료되었습니다.======================14/21
    [15]device_make				저장이 완료되었습니다.======================15/21
    [16]device_connection_type				저장이 완료되었습니다.======================16/21
    [17]device_language				저장이 완료되었습니다.======================17/21
    

    C:\Users\13Z970-G.AR30K\Anaconda3\lib\site-packages\pandas\plotting\_core.py:1001: UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
      ax.set_xlim(left, right)
    

    [18]device_country				저장이 완료되었습니다.======================18/21
    [19]device_region				저장이 완료되었습니다.======================19/21
    [20]device_city				저장이 완료되었습니다.======================20/21
    [21]advertisement_id				저장이 완료되었습니다.======================21/21
    

***


```python
Inequ = pd.DataFrame(dic.items(), columns=['col', 'per'])
Inequ.head(3)
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
      <th>col</th>
      <th>per</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ssp_id</td>
      <td>0.411765</td>
    </tr>
    <tr>
      <th>1</th>
      <td>campaign_id</td>
      <td>0.456989</td>
    </tr>
    <tr>
      <th>2</th>
      <td>adset_id</td>
      <td>0.321101</td>
    </tr>
  </tbody>
</table>
</div>




```python
Inequ.T
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
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col</th>
      <td>ssp_id</td>
      <td>campaign_id</td>
      <td>adset_id</td>
      <td>placement_type</td>
      <td>media_id</td>
      <td>media_name</td>
      <td>media_bundle</td>
      <td>media_domain</td>
      <td>publisher_id</td>
      <td>publisher_name</td>
      <td>device_os</td>
      <td>device_os_version</td>
      <td>device_model</td>
      <td>device_carrier</td>
      <td>device_make</td>
      <td>device_connection_type</td>
      <td>device_language</td>
      <td>device_country</td>
      <td>device_region</td>
      <td>device_city</td>
      <td>advertisement_id</td>
    </tr>
    <tr>
      <th>per</th>
      <td>0.411765</td>
      <td>0.456989</td>
      <td>0.321101</td>
      <td>0.25</td>
      <td>0.0235598</td>
      <td>0.015859</td>
      <td>0.0159084</td>
      <td>0</td>
      <td>0.0104087</td>
      <td>0.0278232</td>
      <td>0</td>
      <td>0.04</td>
      <td>0.0276442</td>
      <td>0.011194</td>
      <td>0.00334448</td>
      <td>0.25</td>
      <td>0.030303</td>
      <td>0</td>
      <td>0.0405405</td>
      <td>0.0188537</td>
      <td>0.433333</td>
    </tr>
  </tbody>
</table>
</div>



> 0.03보다 작으면 불평등 지수가 심각한 것으로 판단하자 :  피쳐를 합치고 다시 봐줄 것


```python
out = Inequ[Inequ.per.values <= 0.03]
nor = Inequ[Inequ.per.values >= 0.03]
out.shape, nor.shape
```




    ((12, 2), (9, 2))




```python
out.T
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
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>17</th>
      <th>19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col</th>
      <td>media_id</td>
      <td>media_name</td>
      <td>media_bundle</td>
      <td>media_domain</td>
      <td>publisher_id</td>
      <td>publisher_name</td>
      <td>device_os</td>
      <td>device_model</td>
      <td>device_carrier</td>
      <td>device_make</td>
      <td>device_country</td>
      <td>device_city</td>
    </tr>
    <tr>
      <th>per</th>
      <td>0.0235598</td>
      <td>0.015859</td>
      <td>0.0159084</td>
      <td>0</td>
      <td>0.0104087</td>
      <td>0.0278232</td>
      <td>0</td>
      <td>0.0276442</td>
      <td>0.011194</td>
      <td>0.00334448</td>
      <td>0</td>
      <td>0.0188537</td>
    </tr>
  </tbody>
</table>
</div>



***

#### 새로운 라벨인코딩으로 만들어주기


```python
cnt = 0
Total = tr.shape[0]
for i in out['col'] : 
    tmp = df.groupby([i]).agg(["count"])['click']
    tmp = pd.DataFrame(tmp.to_records())
    tmp['frequency ratio'] = tmp['count'] / Total
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)
    
    tmp['cum_perc'] = 100*tmp['frequency ratio'].cumsum()
    trash = tmp[tmp.cum_perc.values >= 80].index.tolist()
    df[i].replace(trash, trash[0], inplace = True)
    
    cnt += 1
    print("[{}]{}: {} ... {} 제거======================{}/{}".format(cnt, i, len(tmp), len(trash), cnt, len(out)))
```

    media_id: 5815 ... 5771 제거......1/12
    media_name: 6810 ... 6779 제거......2/12
    media_bundle: 6286 ... 6241 제거......3/12
    media_domain: 162 ... 162 제거......4/12
    publisher_id: 3939 ... 3926 제거......5/12
    publisher_name: 1222 ... 1210 제거......6/12
    device_os: 2 ... 2 제거......7/12
    device_model: 1664 ... 1644 제거......8/12
    device_carrier: 536 ... 533 제거......9/12
    device_make: 299 ... 298 제거......10/12
    device_country: 1 ... 1 제거......11/12
    device_city: 1326 ... 1322 제거......12/12
    

#### 결과확인


```python
bef = nuni.T
bef.drop(["event_datetime", "bid_id", "device_ifa"], axis = 0, inplace = True)
bef.rename(columns = {bef.columns[0]: 'before'}, inplace = True)
bef.head(3)
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
      <th>before</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>click</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ssp_id</th>
      <td>17</td>
    </tr>
    <tr>
      <th>campaign_id</th>
      <td>186</td>
    </tr>
  </tbody>
</table>
</div>




```python
aft = df.agg(["nunique"]).T

Con = pd.concat([bef, aft], axis = 1)
Con.rename(columns = {'nunique' : 'clean1'}, inplace = True)

Con.head(3)
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
      <th>before</th>
      <th>clean1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>click</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>ssp_id</th>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>campaign_id</th>
      <td>186</td>
      <td>186</td>
    </tr>
  </tbody>
</table>
</div>




```python
Con.before.sum(), Con.clean1.sum()
```




    (29487, 1610)



***

#### 나중에 쓸 수 있으니깐 정리해보기


```python
df.to_csv("[1][label]train.csv", index = False)
```


```python
data = df.apply(lambda x: d[x.name].inverse_transform(x))
data.to_csv("[1][ori]train.csv", index = False)
```

***

### 라벨인코딩한 것에다가 원핫인코딩 입히기


```python
numerical_ix = data.select_dtypes(include=['int64', 'float64']).columns
categorical_ix = data.select_dtypes(include=['object', 'bool']).columns
len(numerical_ix), len(categorical_ix)
```




    (1, 21)




```python
numerical_ix
```




    Index(['click'], dtype='object')




```python
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
```


```python
preprocess = make_column_transformer(
    (OneHotEncoder(handle_unknown = "ignore", sparse = False), categorical_ix), verbose = True, remainder = 'drop')
```


```python
del tr
```

#### 1) 라벨링


```python
res = preprocess.fit_transform(df)
res.shape
```


    ---------------------------------------------------------------------------

    MemoryError                               Traceback (most recent call last)

    <ipython-input-23-a2c1aa646201> in <module>
    ----> 1 res = preprocess.fit_transform(df)
          2 res.shape
    

    ~\Anaconda3\lib\site-packages\sklearn\compose\_column_transformer.py in fit_transform(self, X, y)
        466         self._validate_remainder(X)
        467 
    --> 468         result = self._fit_transform(X, y, _fit_transform_one)
        469 
        470         if not result:
    

    ~\Anaconda3\lib\site-packages\sklearn\compose\_column_transformer.py in _fit_transform(self, X, y, func, fitted)
        410                     message=self._log_message(name, idx, len(transformers)))
        411                 for idx, (name, trans, column, weight) in enumerate(
    --> 412                         self._iter(fitted=fitted, replace_strings=True), 1))
        413         except ValueError as e:
        414             if "Expected 2D array, got 1D array instead" in str(e):
    

    ~\Anaconda3\lib\site-packages\joblib\parallel.py in __call__(self, iterable)
        919             # remaining jobs.
        920             self._iterating = False
    --> 921             if self.dispatch_one_batch(iterator):
        922                 self._iterating = self._original_iterator is not None
        923 
    

    ~\Anaconda3\lib\site-packages\joblib\parallel.py in dispatch_one_batch(self, iterator)
        757                 return False
        758             else:
    --> 759                 self._dispatch(tasks)
        760                 return True
        761 
    

    ~\Anaconda3\lib\site-packages\joblib\parallel.py in _dispatch(self, batch)
        714         with self._lock:
        715             job_idx = len(self._jobs)
    --> 716             job = self._backend.apply_async(batch, callback=cb)
        717             # A job can complete so quickly than its callback is
        718             # called before we get here, causing self._jobs to
    

    ~\Anaconda3\lib\site-packages\joblib\_parallel_backends.py in apply_async(self, func, callback)
        180     def apply_async(self, func, callback=None):
        181         """Schedule a func to be run"""
    --> 182         result = ImmediateResult(func)
        183         if callback:
        184             callback(result)
    

    ~\Anaconda3\lib\site-packages\joblib\_parallel_backends.py in __init__(self, batch)
        547         # Don't delay the application, to avoid keeping the input
        548         # arguments in memory
    --> 549         self.results = batch()
        550 
        551     def get(self):
    

    ~\Anaconda3\lib\site-packages\joblib\parallel.py in __call__(self)
        223         with parallel_backend(self._backend, n_jobs=self._n_jobs):
        224             return [func(*args, **kwargs)
    --> 225                     for func, args, kwargs in self.items]
        226 
        227     def __len__(self):
    

    ~\Anaconda3\lib\site-packages\joblib\parallel.py in <listcomp>(.0)
        223         with parallel_backend(self._backend, n_jobs=self._n_jobs):
        224             return [func(*args, **kwargs)
    --> 225                     for func, args, kwargs in self.items]
        226 
        227     def __len__(self):
    

    ~\Anaconda3\lib\site-packages\sklearn\pipeline.py in _fit_transform_one(transformer, X, y, weight, message_clsname, message, **fit_params)
        714     with _print_elapsed_time(message_clsname, message):
        715         if hasattr(transformer, 'fit_transform'):
    --> 716             res = transformer.fit_transform(X, y, **fit_params)
        717         else:
        718             res = transformer.fit(X, y, **fit_params).transform(X)
    

    ~\Anaconda3\lib\site-packages\sklearn\preprocessing\_encoders.py in fit_transform(self, X, y)
        629                 self._categorical_features, copy=True)
        630         else:
    --> 631             return self.fit(X).transform(X)
        632 
        633     def _legacy_transform(self, X):
    

    ~\Anaconda3\lib\site-packages\sklearn\preprocessing\_encoders.py in transform(self, X)
        730                                        copy=True)
        731         else:
    --> 732             return self._transform_new(X)
        733 
        734     def inverse_transform(self, X):
    

    ~\Anaconda3\lib\site-packages\sklearn\preprocessing\_encoders.py in _transform_new(self, X)
        707                                 dtype=self.dtype)
        708         if not self.sparse:
    --> 709             return out.toarray()
        710         else:
        711             return out
    

    ~\Anaconda3\lib\site-packages\scipy\sparse\compressed.py in toarray(self, order, out)
        960         if out is None and order is None:
        961             order = self._swap('cf')[0]
    --> 962         out = self._process_toarray_args(order, out)
        963         if not (out.flags.c_contiguous or out.flags.f_contiguous):
        964             raise ValueError('Output array must be C or F contiguous')
    

    ~\Anaconda3\lib\site-packages\scipy\sparse\base.py in _process_toarray_args(self, order, out)
       1185             return out
       1186         else:
    -> 1187             return np.zeros(self.shape, dtype=self.dtype, order=order)
       1188 
       1189 
    

    MemoryError: 


# 실패

***

## 추가로, 변수 정리하기


```python
cnt = 0
Total = df.shape[0]
for i in nor['col'] : 
    tmp = df.groupby([i]).agg(["count"])['click']
    tmp = pd.DataFrame(tmp.to_records())
    tmp['frequency ratio'] = tmp['count'] / Total
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)

    trash = tmp[tmp['frequency ratio'].values <= 0.005].index.tolist()
    cnt += 1
    if len(trash) > 0 :
        df[i].replace(trash, trash[0], inplace = True)
        print("[{}]{}: {} ... {} 제거======================{}/{}".format(cnt, i, len(tmp), len(trash), cnt, len(out)))
        
    else :
        print("{}\t\t\t: 그대로 사용가능합니다.".format(i))
```

    [1]ssp_id: 17 ... 3 제거======================1/12
    [2]campaign_id: 186 ... 118 제거======================2/12
    [3]adset_id: 872 ... 820 제거======================3/12
    placement_type			: 그대로 사용가능합니다.
    [5]device_os_version: 125 ... 114 제거======================5/12
    [6]device_connection_type: 8 ... 3 제거======================6/12
    [7]device_language: 33 ... 31 제거======================7/12
    [8]device_region: 148 ... 133 제거======================8/12
    [9]advertisement_id: 30 ... 7 제거======================9/12
    

#### 결과확인


```python
aft = df.agg(["nunique"]).T

Con = pd.concat([Con, aft], axis = 1)
Con.rename(columns = {'nunique' : 'clean2'}, inplace = True)

Con.head(3)
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
      <th>before</th>
      <th>clean1</th>
      <th>clean2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>click</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>ssp_id</th>
      <td>17</td>
      <td>17</td>
      <td>15</td>
    </tr>
    <tr>
      <th>campaign_id</th>
      <td>186</td>
      <td>186</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>




```python
Con.before.sum(), Con.clean1.sum(), Con.clean2.sum()
```




    (29487, 1610, 389)




```python
Con.T
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
      <th>click</th>
      <th>ssp_id</th>
      <th>campaign_id</th>
      <th>adset_id</th>
      <th>placement_type</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>media_bundle</th>
      <th>media_domain</th>
      <th>publisher_id</th>
      <th>publisher_name</th>
      <th>device_os</th>
      <th>device_os_version</th>
      <th>device_model</th>
      <th>device_carrier</th>
      <th>device_make</th>
      <th>device_connection_type</th>
      <th>device_language</th>
      <th>device_country</th>
      <th>device_region</th>
      <th>device_city</th>
      <th>advertisement_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>before</th>
      <td>2</td>
      <td>17</td>
      <td>186</td>
      <td>872</td>
      <td>4</td>
      <td>5815</td>
      <td>6810</td>
      <td>6286</td>
      <td>162</td>
      <td>3939</td>
      <td>1222</td>
      <td>2</td>
      <td>125</td>
      <td>1664</td>
      <td>536</td>
      <td>299</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>148</td>
      <td>1326</td>
      <td>30</td>
    </tr>
    <tr>
      <th>clean1</th>
      <td>2</td>
      <td>17</td>
      <td>186</td>
      <td>872</td>
      <td>4</td>
      <td>45</td>
      <td>32</td>
      <td>46</td>
      <td>1</td>
      <td>14</td>
      <td>13</td>
      <td>1</td>
      <td>125</td>
      <td>21</td>
      <td>4</td>
      <td>2</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>148</td>
      <td>5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>clean2</th>
      <td>2</td>
      <td>15</td>
      <td>69</td>
      <td>53</td>
      <td>4</td>
      <td>45</td>
      <td>32</td>
      <td>46</td>
      <td>1</td>
      <td>14</td>
      <td>13</td>
      <td>1</td>
      <td>12</td>
      <td>21</td>
      <td>4</td>
      <td>2</td>
      <td>6</td>
      <td>3</td>
      <td>1</td>
      <td>16</td>
      <td>5</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>



***

#### 나중에 쓸 수 있으니깐 정리해보기


```python
df.to_csv("[2][label]train.csv", index = False)
```


```python
data = df.apply(lambda x: d[x.name].inverse_transform(x))
data.to_csv("[2][ori]train.csv", index = False)
```

***


```python
dic = {}
cnt = 0
for i in df.columns[1:] :
    tmp = df[[i, 'click']].groupby([i]).agg(['sum', 'count'])
    tmp = pd.DataFrame(tmp.to_records())
    tmp.set_axis(["id", "click", "total"], axis=1, inplace=True)
    
    tmp['CTR per features'] = tmp['click'] / tmp['total']
    tmp['frequency ratio'] = tmp['total'] / tmp.total.sum()
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)
    
    tmp['cum_perc'] = 100*tmp['frequency ratio'].cumsum()
    tmp.index = range(len(tmp))
    dic[i] = tmp[tmp.cum_perc.values >= 90].index[0] / len(tmp)
    
    
    tmp[['frequency ratio']].plot(kind = 'bar',  figsize = (45, 20), fontsize = 50)
    tmp['CTR per features'].plot(secondary_y=True, fontsize = 50, color='red', lw= 10, legend = True, mark_right = False)
    plt.rc('legend', fontsize=40)
    
    ax = plt.gca()
    plt.xlim([-0.4, len(tmp)])
    ax.set_xticklabels(tuple(tmp.id))
    
    cnt += 1
    fn = '[' + str(cnt) + ']'+ i
    plt.suptitle(fn + ': ' + str(nuni[i][0]), fontsize=55)
    
    plt.savefig(fn + ".png")
    print(fn + '\t\t\t\t\t저장이 완료되었습니다.======================{}/{}'.format(cnt, len(df.columns[1:])))
    plt.close('all')
```

    [1]ssp_id					저장이 완료되었습니다.======================1/21
    [2]campaign_id					저장이 완료되었습니다.======================2/21
    [3]adset_id					저장이 완료되었습니다.======================3/21
    [4]placement_type					저장이 완료되었습니다.======================4/21
    [5]media_id					저장이 완료되었습니다.======================5/21
    [6]media_name					저장이 완료되었습니다.======================6/21
    [7]media_bundle					저장이 완료되었습니다.======================7/21
    

    C:\Users\13Z970-G.AR30K\Anaconda3\lib\site-packages\pandas\plotting\_core.py:1001: UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
      ax.set_xlim(left, right)
    

    [8]media_domain					저장이 완료되었습니다.======================8/21
    [9]publisher_id					저장이 완료되었습니다.======================9/21
    [10]publisher_name					저장이 완료되었습니다.======================10/21
    

    C:\Users\13Z970-G.AR30K\Anaconda3\lib\site-packages\pandas\plotting\_core.py:1001: UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
      ax.set_xlim(left, right)
    

    [11]device_os					저장이 완료되었습니다.======================11/21
    [12]device_os_version					저장이 완료되었습니다.======================12/21
    [13]device_model					저장이 완료되었습니다.======================13/21
    [14]device_carrier					저장이 완료되었습니다.======================14/21
    [15]device_make					저장이 완료되었습니다.======================15/21
    [16]device_connection_type					저장이 완료되었습니다.======================16/21
    [17]device_language					저장이 완료되었습니다.======================17/21
    

    C:\Users\13Z970-G.AR30K\Anaconda3\lib\site-packages\pandas\plotting\_core.py:1001: UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
      ax.set_xlim(left, right)
    

    [18]device_country					저장이 완료되었습니다.======================18/21
    [19]device_region					저장이 완료되었습니다.======================19/21
    [20]device_city					저장이 완료되었습니다.======================20/21
    [21]advertisement_id					저장이 완료되었습니다.======================21/21
    

***

## 추가로, 변수 정리하기(2)


```python
cnt = 0
for i in df.columns[1:] :
    tmp = df[[i, 'click']].groupby([i]).agg(['sum', 'count'])
    tmp = pd.DataFrame(tmp.to_records())
    tmp.set_axis(["id", "click", "total"], axis=1, inplace=True)
    
    tmp['CTR per features'] = tmp['click'] / tmp['total']
    tmp['frequency ratio'] = tmp['total'] / tmp.total.sum()
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)

    trash = tmp[(tmp['frequency ratio'].values <= 0.025) & (tmp['CTR per features'].values <= 0.02)].index.tolist()
    cnt += 1
    if len(trash) > 0 :
        df[i].replace(trash, trash[0], inplace = True)
        print("[{}]{}: {} ... {} 제거======================{}/{}".format(cnt, i, len(tmp), len(trash), cnt, len(out)))
        
    else :
        print("{}\t\t\t: 그대로 사용가능합니다.".format(i))
```

    [1]ssp_id: 15 ... 4 제거======================1/12
    [2]campaign_id: 69 ... 7 제거======================2/12
    [3]adset_id: 53 ... 14 제거======================3/12
    placement_type			: 그대로 사용가능합니다.
    [5]media_id: 45 ... 14 제거======================5/12
    [6]media_name: 32 ... 9 제거======================6/12
    [7]media_bundle: 46 ... 17 제거======================7/12
    media_domain			: 그대로 사용가능합니다.
    [9]publisher_id: 14 ... 3 제거======================9/12
    [10]publisher_name: 13 ... 2 제거======================10/12
    device_os			: 그대로 사용가능합니다.
    device_os_version			: 그대로 사용가능합니다.
    device_model			: 그대로 사용가능합니다.
    device_carrier			: 그대로 사용가능합니다.
    device_make			: 그대로 사용가능합니다.
    device_connection_type			: 그대로 사용가능합니다.
    device_language			: 그대로 사용가능합니다.
    device_country			: 그대로 사용가능합니다.
    [19]device_region: 16 ... 1 제거======================19/12
    device_city			: 그대로 사용가능합니다.
    [21]advertisement_id: 24 ... 1 제거======================21/12
    

#### 결과확인


```python
aft = df.agg(["nunique"]).T

Con = pd.concat([Con, aft], axis = 1)
Con.rename(columns = {'nunique' : 'clean3'}, inplace = True)

Con.head(3)
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
      <th>before</th>
      <th>clean1</th>
      <th>clean2</th>
      <th>clean3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>click</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>ssp_id</th>
      <td>17</td>
      <td>17</td>
      <td>15</td>
      <td>12</td>
    </tr>
    <tr>
      <th>campaign_id</th>
      <td>186</td>
      <td>186</td>
      <td>69</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
Con.before.sum(), Con.clean1.sum(), Con.clean2.sum(), Con.clean3.sum()
```




    (29487, 1610, 389, 384)




```python
Con.T
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
      <th>click</th>
      <th>ssp_id</th>
      <th>campaign_id</th>
      <th>adset_id</th>
      <th>placement_type</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>media_bundle</th>
      <th>media_domain</th>
      <th>publisher_id</th>
      <th>publisher_name</th>
      <th>device_os</th>
      <th>device_os_version</th>
      <th>device_model</th>
      <th>device_carrier</th>
      <th>device_make</th>
      <th>device_connection_type</th>
      <th>device_language</th>
      <th>device_country</th>
      <th>device_region</th>
      <th>device_city</th>
      <th>advertisement_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>before</th>
      <td>2</td>
      <td>17</td>
      <td>186</td>
      <td>872</td>
      <td>4</td>
      <td>5815</td>
      <td>6810</td>
      <td>6286</td>
      <td>162</td>
      <td>3939</td>
      <td>1222</td>
      <td>2</td>
      <td>125</td>
      <td>1664</td>
      <td>536</td>
      <td>299</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>148</td>
      <td>1326</td>
      <td>30</td>
    </tr>
    <tr>
      <th>clean1</th>
      <td>2</td>
      <td>17</td>
      <td>186</td>
      <td>872</td>
      <td>4</td>
      <td>45</td>
      <td>32</td>
      <td>46</td>
      <td>1</td>
      <td>14</td>
      <td>13</td>
      <td>1</td>
      <td>125</td>
      <td>21</td>
      <td>4</td>
      <td>2</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>148</td>
      <td>5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>clean2</th>
      <td>2</td>
      <td>15</td>
      <td>69</td>
      <td>53</td>
      <td>4</td>
      <td>45</td>
      <td>32</td>
      <td>46</td>
      <td>1</td>
      <td>14</td>
      <td>13</td>
      <td>1</td>
      <td>12</td>
      <td>21</td>
      <td>4</td>
      <td>2</td>
      <td>6</td>
      <td>3</td>
      <td>1</td>
      <td>16</td>
      <td>5</td>
      <td>24</td>
    </tr>
    <tr>
      <th>clean3</th>
      <td>2</td>
      <td>12</td>
      <td>67</td>
      <td>53</td>
      <td>4</td>
      <td>45</td>
      <td>32</td>
      <td>46</td>
      <td>1</td>
      <td>14</td>
      <td>13</td>
      <td>1</td>
      <td>12</td>
      <td>21</td>
      <td>4</td>
      <td>2</td>
      <td>6</td>
      <td>3</td>
      <td>1</td>
      <td>16</td>
      <td>5</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>



***

#### 여기서부터는 GCP를 통해서 해결이 가능합니다.


```python
res = preprocess.fit_transform(data)
```


```python
res_ori = pd.DataFrame(res)
res_ori.shape
```
