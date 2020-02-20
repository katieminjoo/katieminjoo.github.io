---
layout: post
title: <i class="fab fa-medapps"> Bokeh Pie chart</i>
date: 2020-02-20 20:12:00 +0800
categories: [Python, Visualization]
tags: [Bohek]
toc: true
comments: true
---

훌륭한 시각화는 자신의 분석내용을 전달하기 위한 가장 효과적인 방법 중 하나입니다.  
Bokeh는 Python 라이브러리 중 하나로, 인터렉티브한 시각화 제작에 탁월합니다.  
Bokeh의 기본 기능을 소개하는 한편, 앞으로 Bokeh를 바탕으로 제작한 프로젝트를 소개하고자 합니다.  
이번 글에서는 그 중 가장 기본적인 pie chart 그리는 법을 소개합니다.  

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

<div class="bk-root">
    <a href="https://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
    <span id="1001">Loading BokehJS ...</span>
</div>

***  
  

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

***  
  

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

<html lang="en">
  
  <head>
    
      <meta charset="utf-8">
      <title>Bokeh Plot</title>
      
      
        
          
        <link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.2.0.min.css" type="text/css" />
        
        
          
        <script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.2.0.min.js"></script>
        <script type="text/javascript">
            Bokeh.set_log_level("info");
        </script>
        
      
      
    
  </head>
  
  
  <body>
    
      
        
          
          
            
              <div class="bk-root" id="bdaeccdb-b408-4af3-beee-806414a0fb38" data-root-id="1001"></div>
            
          
        
      
      
        <script type="application/json" id="1160">
          {"c6240eb6-86d9-4c96-b579-2d9ed8198c73":{"roots":{"references":[{"attributes":{"items":[{"id":"1039","type":"LegendItem"}]},"id":"1038","type":"Legend"},{"attributes":{"axis_label":null,"formatter":{"id":"1036","type":"BasicTickFormatter"},"ticker":{"id":"1018","type":"BasicTicker"},"visible":false},"id":"1017","type":"LinearAxis"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{"label":{"field":"country"},"renderers":[{"id":"1031","type":"GlyphRenderer"}]},"id":"1039","type":"LegendItem"},{"attributes":{},"id":"1018","type":"BasicTicker"},{"attributes":{"dimension":1,"grid_line_color":null,"ticker":{"id":"1018","type":"BasicTicker"}},"id":"1021","type":"Grid"},{"attributes":{"callback":null,"data":{"angle":{"__ndarray__":"eQLEMwAC9z+3V8R09kHrP+QcmNXVFeo/hZ74ygF34j8vDs2tzcrZP1vToA6tntg/iJh0b4xy1z93BYbhOoTUPzmtw/IJwtI/0I8to/kr0j/Qjy2j+SvSP/xUAQTZ/9A/","dtype":"float64","shape":[12]},"color":["#3182bd","#6baed6","#9ecae1","#c6dbef","#e6550d","#fd8d3c","#fdae6b","#fdd0a2","#31a354","#74c476","#a1d99b","#c7e9c0"],"country":["United States","United Kingdom","Japan","China","Germany","India","Italy","Australia","Brazil","France","Taiwan","Spain"],"index":[0,1,2,3,4,5,6,7,8,9,10,11],"value":[157,93,89,63,44,42,40,35,32,31,31,29]},"selected":{"id":"1046","type":"Selection"},"selection_policy":{"id":"1045","type":"UnionRenderers"}},"id":"1027","type":"ColumnDataSource"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"callback":null,"tooltips":"@country: @value"},"id":"1022","type":"HoverTool"},{"attributes":{"axis_label":null,"formatter":{"id":"1034","type":"BasicTickFormatter"},"ticker":{"id":"1013","type":"BasicTicker"},"visible":false},"id":"1012","type":"LinearAxis"},{"attributes":{"end_angle":{"expr":{"id":"1026","type":"CumSum"},"units":"rad"},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"radius":{"units":"data","value":0.4},"start_angle":{"expr":{"id":"1025","type":"CumSum"},"units":"rad"},"x":{"value":0},"y":{"value":1}},"id":"1030","type":"Wedge"},{"attributes":{"source":{"id":"1027","type":"ColumnDataSource"}},"id":"1032","type":"CDSView"},{"attributes":{},"id":"1045","type":"UnionRenderers"},{"attributes":{"callback":null},"id":"1006","type":"DataRange1d"},{"attributes":{},"id":"1046","type":"Selection"},{"attributes":{"data_source":{"id":"1027","type":"ColumnDataSource"},"glyph":{"id":"1029","type":"Wedge"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1030","type":"Wedge"},"selection_glyph":null,"view":{"id":"1032","type":"CDSView"}},"id":"1031","type":"GlyphRenderer"},{"attributes":{"text":"Pie Chart"},"id":"1002","type":"Title"},{"attributes":{"end_angle":{"expr":{"id":"1026","type":"CumSum"},"units":"rad"},"fill_color":{"field":"color"},"line_color":{"value":"white"},"radius":{"units":"data","value":0.4},"start_angle":{"expr":{"id":"1025","type":"CumSum"},"units":"rad"},"x":{"value":0},"y":{"value":1}},"id":"1029","type":"Wedge"},{"attributes":{"field":"angle","include_zero":true},"id":"1025","type":"CumSum"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1022","type":"HoverTool"}]},"id":"1023","type":"Toolbar"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{},"id":"1034","type":"BasicTickFormatter"},{"attributes":{"callback":null},"id":"1004","type":"DataRange1d"},{"attributes":{"below":[{"id":"1012","type":"LinearAxis"}],"center":[{"id":"1016","type":"Grid"},{"id":"1021","type":"Grid"},{"id":"1038","type":"Legend"}],"left":[{"id":"1017","type":"LinearAxis"}],"plot_height":350,"renderers":[{"id":"1031","type":"GlyphRenderer"}],"title":{"id":"1002","type":"Title"},"toolbar":{"id":"1023","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1004","type":"DataRange1d"},"x_scale":{"id":"1008","type":"LinearScale"},"y_range":{"id":"1006","type":"DataRange1d"},"y_scale":{"id":"1010","type":"LinearScale"}},"id":"1001","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1036","type":"BasicTickFormatter"},{"attributes":{"grid_line_color":null,"ticker":{"id":"1013","type":"BasicTicker"}},"id":"1016","type":"Grid"},{"attributes":{"field":"angle"},"id":"1026","type":"CumSum"}],"root_ids":["1001"]},"title":"Bokeh Application","version":"1.2.0"}}
        </script>
        <script type="text/javascript">
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json = document.getElementById('1160').textContent;
                  var render_items = [{"docid":"c6240eb6-86d9-4c96-b579-2d9ed8198c73","roots":{"1001":"bdaeccdb-b408-4af3-beee-806414a0fb38"}}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    var attempts = 0;
                    var timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        embed_document(root);
                        clearInterval(timer);
                      }
                      attempts++;
                      if (attempts > 100) {
                        console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                        clearInterval(timer);
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        </script>
    
  </body>
  
</html>

