---
layout: post
title: <i class="fab fa-medapps"> Bokeh Pie chart</i>
date: 2020-02-20 20:12:00 +0800
categories: [Python, Visualization]
tags: [Bohek]
toc: true
comments: true
---

훌륭한 시각화는 자신의 분석내용을 다른 사람에게 전달하는 가장 효과적인 방법 중 하나입니다.  
이번 글에서는 Python 라이브러리 중 하나로, 인터렉티브한 시각화 제작에 유리한 Bokeh를 소개하려 합니다.

## pie chart
```python
from math import pi
import pandas as pd

from bokeh.plotting import figure
from bokeh.palettes import Category20c, Blues8
from bokeh.transform import cumsum

from bokeh.io import output_notebook, show
output_notebook()
```

```html
    <div class="bk-root">
        <a href="https://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="1001">Loading BokehJS ...</span>
    </div>
```




```python
x = { 'United States': 157, 'United Kingdom': 93, 'Japan': 89, 'China': 63,
      'Germany': 44, 'India': 42, 'Italy': 40, 'Australia': 35, 'Brazil': 32,
      'France': 31, 'Taiwan': 31, 'Spain': 29 }

data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['color'] = Category20c[len(x)]
#data['color'] = Blues8[len(x)]

# represent each value as an angle = value / total * 2pi
data['angle'] = data['value']/data['value'].sum() * 2*pi

data
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
      <th>country</th>
      <th>value</th>
      <th>color</th>
      <th>angle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>United States</td>
      <td>157</td>
      <td>#3182bd</td>
      <td>1.437988</td>
    </tr>
    <tr>
      <th>1</th>
      <td>United Kingdom</td>
      <td>93</td>
      <td>#6baed6</td>
      <td>0.851802</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Japan</td>
      <td>89</td>
      <td>#9ecae1</td>
      <td>0.815165</td>
    </tr>
    <tr>
      <th>3</th>
      <td>China</td>
      <td>63</td>
      <td>#c6dbef</td>
      <td>0.577027</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>44</td>
      <td>#e6550d</td>
      <td>0.403003</td>
    </tr>
    <tr>
      <th>5</th>
      <td>India</td>
      <td>42</td>
      <td>#fd8d3c</td>
      <td>0.384685</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Italy</td>
      <td>40</td>
      <td>#fdae6b</td>
      <td>0.366366</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Australia</td>
      <td>35</td>
      <td>#fdd0a2</td>
      <td>0.320571</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Brazil</td>
      <td>32</td>
      <td>#31a354</td>
      <td>0.293093</td>
    </tr>
    <tr>
      <th>9</th>
      <td>France</td>
      <td>31</td>
      <td>#74c476</td>
      <td>0.283934</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Taiwan</td>
      <td>31</td>
      <td>#a1d99b</td>
      <td>0.283934</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Spain</td>
      <td>29</td>
      <td>#c7e9c0</td>
      <td>0.265616</td>
    </tr>
  </tbody>
</table>
</div>




```python
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value")

p.wedge(x=0, y=1, radius=0.4, 
        
        # use cumsum to cumulatively sum the values for start and end angles
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
```








  <div class="bk-root" id="4ee452bd-0564-47ac-b54a-7907e15dfc05" data-root-id="1002"></div>





