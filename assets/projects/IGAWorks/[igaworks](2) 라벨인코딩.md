
### 사용할 데이터


```python
import pandas as pd

tr = pd.read_csv("train.csv.gz", compression = "gzip")
tr.shape
```




    (5500000, 25)




```python
tr.drop(["event_datetime", "bid_id", "device_ifa"], axis = 1, inplace = True)
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



#### 라벨인코딩


```python
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
d = defaultdict(LabelEncoder)
df = tr.apply(lambda x: d[x.name].fit_transform(x))
df.shape
```




    (5500000, 22)




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
  </tbody>
</table>
</div>



***


```python
cnt = 0
load = len(df.columns[1:])

for i in df.columns[1:] :
    tmp = df[[i, 'click']].groupby([i]).agg(['sum', 'count'])
    tmp = pd.DataFrame(tmp.to_records())
    tmp.set_axis(["id", "click", "total"], axis=1, inplace=True)
    
    tmp['CTR per features'] = tmp['click'] / tmp['total']
    tmp['frequency ratio'] = tmp['total'] / tmp.total.sum()
    tmp.sort_values(by = ['frequency ratio'], ascending = False, inplace = True)

    trash = tmp[(tmp['frequency ratio'].values <= 0.05) | (tmp['CTR per features'].values <= 0.02)].index.tolist()
    cnt += 1
    if len(trash) > 0 :
        df[i].replace(trash, trash[0], inplace = True)
        print("[{}]{}: {} ... {} 제거======================{}/{}".format(cnt, i, len(tmp), len(trash), cnt, load))
        
    else :
        print("[{}]{}\t\t\t: 그대로 사용가능합니다.".format(cnt, i))
```

    [1]ssp_id: 17 ... 13 제거======================1/21
    [2]campaign_id: 186 ... 186 제거======================2/21
    [3]adset_id: 872 ... 872 제거======================3/21
    [4]placement_type: 4 ... 2 제거======================4/21
    [5]media_id: 5815 ... 5813 제거======================5/21
    [6]media_name: 6810 ... 6808 제거======================6/21
    [7]media_bundle: 6286 ... 6282 제거======================7/21
    [8]media_domain: 162 ... 161 제거======================8/21
    [9]publisher_id: 3939 ... 3936 제거======================9/21
    [10]publisher_name: 1222 ... 1219 제거======================10/21
    [11]device_os: 2 ... 1 제거======================11/21
    [12]device_os_version: 125 ... 121 제거======================12/21
    [13]device_model: 1664 ... 1660 제거======================13/21
    [14]device_carrier: 536 ... 532 제거======================14/21
    [15]device_make: 299 ... 297 제거======================15/21
    [16]device_connection_type: 8 ... 4 제거======================16/21
    [17]device_language: 33 ... 31 제거======================17/21
    [18]device_country			: 그대로 사용가능합니다.
    [19]device_region: 148 ... 145 제거======================19/21
    [20]device_city: 1326 ... 1324 제거======================20/21
    [21]advertisement_id: 30 ... 26 제거======================21/21
    

***


```python
nuni = tr.agg(["nunique"])
bef = nuni.T
bef.rename(columns = {bef.columns[0]: 'before'}, inplace = True)

aft = df.agg(["nunique"]).T
Con = pd.concat([bef, aft], axis = 1)
Con.rename(columns = {'nunique' : 'after'}, inplace = True)

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
      <th>after</th>
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
      <td>5</td>
    </tr>
    <tr>
      <th>campaign_id</th>
      <td>186</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Con.before.sum(), Con.after.sum()
```




    (29487, 74)



***


```python
ori = df.apply(lambda x: d[x.name].inverse_transform(x))
```


```python
ori.agg(["nunique"])
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
      <th>nunique</th>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



***


```python
del tr
```


```python
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import make_column_transformer
```


```python
numerical_ix = ori.select_dtypes(include=['int64', 'float64']).columns
categorical_ix = ori.select_dtypes(include=['object', 'bool']).columns
```


```python
len(numerical_ix), len(categorical_ix)
```




    (1, 21)




```python
preprocess = make_column_transformer(
    (OneHotEncoder(handle_unknown = "ignore", sparse = False), categorical_ix), verbose = True, remainder = 'drop')
```


```python
del df
```


```python
res = preprocess.fit_transform(ori)
res.shape
```

    [ColumnTransformer] . (1 of 1) Processing onehotencoder, total= 1.1min
    




    (5500000, 72)




```python
res_label = pd.DataFrame(res)
res_label.head()
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
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
      <th>26</th>
      <th>27</th>
      <th>28</th>
      <th>29</th>
      <th>30</th>
      <th>31</th>
      <th>32</th>
      <th>33</th>
      <th>34</th>
      <th>35</th>
      <th>36</th>
      <th>37</th>
      <th>38</th>
      <th>39</th>
      <th>40</th>
      <th>41</th>
      <th>42</th>
      <th>43</th>
      <th>44</th>
      <th>45</th>
      <th>46</th>
      <th>47</th>
      <th>48</th>
      <th>49</th>
      <th>50</th>
      <th>51</th>
      <th>52</th>
      <th>53</th>
      <th>54</th>
      <th>55</th>
      <th>56</th>
      <th>57</th>
      <th>58</th>
      <th>59</th>
      <th>60</th>
      <th>61</th>
      <th>62</th>
      <th>63</th>
      <th>64</th>
      <th>65</th>
      <th>66</th>
      <th>67</th>
      <th>68</th>
      <th>69</th>
      <th>70</th>
      <th>71</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
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
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
res_label.iloc[14:17,:5]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
ori[ori.ssp_id.values == ori['ssp_id'].agg(["unique"])['unique'].tolist()[-1]].head(3)
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
      <th>15</th>
      <td>0</td>
      <td>Uox85xVMSC</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>n0p3m00ieQ</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>dShknap9uf</td>
      <td>N8djnVWnYo</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>fiJqINpRUy</td>
      <td>kvNzH5Iavg</td>
      <td>javoIwtGqV</td>
      <td>2xglifxY3C</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>aI9W3Httpm</td>
      <td>uuYScbMuRa</td>
      <td>tmj7wCMWB5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0</td>
      <td>Uox85xVMSC</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>WnrXFsYXNs</td>
      <td>hkFCnTpDpn</td>
      <td>n0p3m00ieQ</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>dShknap9uf</td>
      <td>N8djnVWnYo</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>fiJqINpRUy</td>
      <td>bJ0VstP9sA</td>
      <td>javoIwtGqV</td>
      <td>aEmZFzgDfq</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>0uNJFn0odR</td>
      <td>vMA8Bkm3Bm</td>
      <td>tmj7wCMWB5</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0</td>
      <td>Uox85xVMSC</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>kIeE1J0KCa</td>
      <td>hkFCnTpDpn</td>
      <td>n0p3m00ieQ</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>dShknap9uf</td>
      <td>N8djnVWnYo</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>DQpMqyILvb</td>
      <td>bJ0VstP9sA</td>
      <td>javoIwtGqV</td>
      <td>aEmZFzgDfq</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>0uNJFn0odR</td>
      <td>vMA8Bkm3Bm</td>
      <td>tmj7wCMWB5</td>
    </tr>
  </tbody>
</table>
</div>




```python
ori.head()
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
      <td>SrN77Arvqh</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>n0p3m00ieQ</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>dShknap9uf</td>
      <td>N8djnVWnYo</td>
      <td>TG14pLUXCY</td>
      <td>V7LhUlY53m</td>
      <td>fiJqINpRUy</td>
      <td>wrzW2uRaKh</td>
      <td>HiGuczmB3W</td>
      <td>Hx7e3tE5mu</td>
      <td>8GSkINt29e</td>
      <td>PCCn9Q1m20</td>
      <td>EdsKnCCtPO</td>
      <td>e7JXTJQ5Qw</td>
      <td>tmj7wCMWB5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>SrN77Arvqh</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>FpOvhbPDXd</td>
      <td>BnqjbSLXhH</td>
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
      <td>SrN77Arvqh</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>FpOvhbPDXd</td>
      <td>BnqjbSLXhH</td>
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
    <tr>
      <th>3</th>
      <td>1</td>
      <td>nwf1A3O5cO</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>kIeE1J0KCa</td>
      <td>j7H2fWftrL</td>
      <td>Uk5MGt9vxz</td>
      <td>DldwurRI4R</td>
      <td>pjBT3sDGbH</td>
      <td>u8sVI0rp7b</td>
      <td>w0Hd4CHeHj</td>
      <td>TG14pLUXCY</td>
      <td>V7LhUlY53m</td>
      <td>KBowLApKOt</td>
      <td>PH0EDk0nOb</td>
      <td>javoIwtGqV</td>
      <td>WCK2G73H3A</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>EdsKnCCtPO</td>
      <td>e7JXTJQ5Qw</td>
      <td>7dyzy9aZoJ</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>SrN77Arvqh</td>
      <td>NcQyEjtPlS</td>
      <td>pLG2mhPQ2A</td>
      <td>1pcQ3RJgQt</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>7jwRHIrTWJ</td>
      <td>pjBT3sDGbH</td>
      <td>FpOvhbPDXd</td>
      <td>BnqjbSLXhH</td>
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
      <td>tmj7wCMWB5</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>after</th>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
test = pd.read_csv("test.csv.gz", compression = "gzip")
test.drop(["event_datetime", "bid_id", "device_ifa"], axis = 1, inplace = True)
```


```python
test.shape
```




    (550000, 21)




```python
tmp = preprocess.transform(test)
```


```python
te = pd.DataFrame(tmp)
te.head()
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
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
      <th>26</th>
      <th>27</th>
      <th>28</th>
      <th>29</th>
      <th>30</th>
      <th>31</th>
      <th>32</th>
      <th>33</th>
      <th>34</th>
      <th>35</th>
      <th>36</th>
      <th>37</th>
      <th>38</th>
      <th>39</th>
      <th>40</th>
      <th>41</th>
      <th>42</th>
      <th>43</th>
      <th>44</th>
      <th>45</th>
      <th>46</th>
      <th>47</th>
      <th>48</th>
      <th>49</th>
      <th>50</th>
      <th>51</th>
      <th>52</th>
      <th>53</th>
      <th>54</th>
      <th>55</th>
      <th>56</th>
      <th>57</th>
      <th>58</th>
      <th>59</th>
      <th>60</th>
      <th>61</th>
      <th>62</th>
      <th>63</th>
      <th>64</th>
      <th>65</th>
      <th>66</th>
      <th>67</th>
      <th>68</th>
      <th>69</th>
      <th>70</th>
      <th>71</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
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
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
test.head()
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
      <td>nwf1A3O5cO</td>
      <td>7Noz5InNj5</td>
      <td>yH0QQDoPNl</td>
      <td>kIeE1J0KCa</td>
      <td>j7H2fWftrL</td>
      <td>Uk5MGt9vxz</td>
      <td>DldwurRI4R</td>
      <td>pjBT3sDGbH</td>
      <td>u8sVI0rp7b</td>
      <td>w0Hd4CHeHj</td>
      <td>TG14pLUXCY</td>
      <td>V7LhUlY53m</td>
      <td>trndviTQNX</td>
      <td>bJ0VstP9sA</td>
      <td>javoIwtGqV</td>
      <td>WCK2G73H3A</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>EdsKnCCtPO</td>
      <td>e7JXTJQ5Qw</td>
      <td>7dyzy9aZoJ</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Uox85xVMSC</td>
      <td>NxzS8oTLt4</td>
      <td>ytPy92XPEV</td>
      <td>kIeE1J0KCa</td>
      <td>9bC9qJ87qL</td>
      <td>YJ1AErf0W7</td>
      <td>eQc8dY09AQ</td>
      <td>pjBT3sDGbH</td>
      <td>MEuwbNJKkM</td>
      <td>166T4jJO38</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>DQpMqyILvb</td>
      <td>PH0EDk0nOb</td>
      <td>javoIwtGqV</td>
      <td>2xglifxY3C</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>Fbps8yvFv1</td>
      <td>XHWzpweJP2</td>
      <td>K6ZwviDgnR</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Uox85xVMSC</td>
      <td>NxzS8oTLt4</td>
      <td>ytPy92XPEV</td>
      <td>kIeE1J0KCa</td>
      <td>9bC9qJ87qL</td>
      <td>YJ1AErf0W7</td>
      <td>eQc8dY09AQ</td>
      <td>pjBT3sDGbH</td>
      <td>MEuwbNJKkM</td>
      <td>166T4jJO38</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>DQpMqyILvb</td>
      <td>bJ0VstP9sA</td>
      <td>javoIwtGqV</td>
      <td>aEmZFzgDfq</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>Ik4H8OeSjh</td>
      <td>xIMfctayjY</td>
      <td>K6ZwviDgnR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M6QaRvdZ8h</td>
      <td>ctd4ThNAdz</td>
      <td>2TWeHHdrJ8</td>
      <td>kIeE1J0KCa</td>
      <td>ZrCGAwgu28</td>
      <td>02mP803Z7Z</td>
      <td>eQc8dY09AQ</td>
      <td>pjBT3sDGbH</td>
      <td>vjSjiBHBO7</td>
      <td>ZsKb5SwceB</td>
      <td>TG14pLUXCY</td>
      <td>V7LhUlY53m</td>
      <td>z29gOe4wqw</td>
      <td>8v5w1w9FEX</td>
      <td>rp6gWKT7zk</td>
      <td>WCK2G73H3A</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>aI9W3Httpm</td>
      <td>uuYScbMuRa</td>
      <td>VMHkGmzhR9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uox85xVMSC</td>
      <td>A2FWaDfu78</td>
      <td>AX8mFBH96H</td>
      <td>kIeE1J0KCa</td>
      <td>9bC9qJ87qL</td>
      <td>YJ1AErf0W7</td>
      <td>eQc8dY09AQ</td>
      <td>pjBT3sDGbH</td>
      <td>MEuwbNJKkM</td>
      <td>166T4jJO38</td>
      <td>TG14pLUXCY</td>
      <td>D9UYEWCoxO</td>
      <td>9F9EA8EvOT</td>
      <td>PH0EDk0nOb</td>
      <td>javoIwtGqV</td>
      <td>2xglifxY3C</td>
      <td>LXYiFbLmMp</td>
      <td>PCCn9Q1m20</td>
      <td>aI9W3Httpm</td>
      <td>uuYScbMuRa</td>
      <td>K6ZwviDgnR</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
