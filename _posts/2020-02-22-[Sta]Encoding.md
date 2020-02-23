---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 1. One Hot Encoding</i>
date: 2020-02-22 22:28:00 +0800
categories: [Statistics, Encoding]
tags: [label encoding]
toc: true
comments: true
---

데이터를 처리하다보면 범주형 자료와 자주 마주칩니다. 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 그러나 인코딩이 생각만큼 단순한 일이 아닙니다. get_dummies/ One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target-Encoding... 등 정말 [다양한](http://contrib.scikit-learn.org/categorical-encoding/index.html) 인코딩 방법이 존재합니다. 앞으로 인코딩 특집 글에서는 여러 인코딩 기법 중에 가장 자주 쓰이고, 중요한 인코딩 방식들에 대해서 포스팅하겠습니다. 

들어가기에 앞서, 저는 앞에서 인코딩을 범주형 자료(categorical data)와 연관지어 편하게 언급하였습니다. 그러나 사실 데이터의 종류는 범주형과 수치형 데이터로만 나누어져있지 않습니다. 인코딩을 더욱 잘 이해하기 위해서는 데이터의 특징에 따라 정확한 분류가 선행되어야합니다. 이 부분은 <b>[읽을 거리](https://towardsdatascience.com/7-data-types-a-better-way-to-think-about-data-types-for-machine-learning-939fae99a689)</b>로 대체합니다.

## One Hot Encoding
One Hot Encoding(OHE)은 인코딩 기법 중에 가장 간단하면서도 특히 머신러닝에서 쉽게 쓰이기 때문에 유명합니다. (그러나 가장 좋은 방법이 아닐 때가 더러 있습니다. 이는 차차 설명드리겠습니다.) OHE는 각각의 범주에다가 1의 값을 주기 때문에 자료 간의 위계관계가 전혀 없는 순수한 범주형 데이터에 적합합니다. 설명의 편의를 위해 아래 예제 데이터[^ex]를 활용하겠습니다.  
[^ex]: [IGAWorks 클릭수 경진대회](https://haehwan.github.io/posts/Comp-CTR/) 자료를 일부 가공하였습니다.  

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
      <th>bid_id</th>
      <th>adset_id</th>
      <th>campaign_id</th>
      <th>media_bundle</th>
      <th>media_id</th>
      <th>media_name</th>
      <th>device_model</th>
      <th>device_os</th>
      <th>device_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1b1Yz4S9wG</td>
      <td>GdBSlETcLy</td>
      <td>taRA9jVfVL</td>
      <td>V8yCzbCKcB</td>
      <td>IyDyyhXBnW</td>
      <td>dAWR8DOmzo</td>
      <td>AsY5LC0NLu</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>eCYeFjnExb</td>
      <td>GlheP2trvZ</td>
      <td>jWRKzxzhyX</td>
      <td>o9tQ73S7C8</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>nz5kFLSj4p</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>QHcMnYqF3h</td>
      <td>WGJnvetv2a</td>
      <td>DW5C3As8ij</td>
      <td>p75piF74nC</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>nz5kFLSj4p</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>p5v9KCdjS6</td>
      <td>FiSRHSfVaf</td>
      <td>qR4Xa60DLl</td>
      <td>DldwurRI4R</td>
      <td>j7H2fWftrL</td>
      <td>Uk5MGt9vxz</td>
      <td>KBowLApKOt</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>aAEDD9AeIv</td>
      <td>UASfSkWw7S</td>
      <td>2T5sOm2MoW</td>
      <td>7jwRHIrTWJ</td>
      <td>hkFCnTpDpn</td>
      <td>Xbdchs5uK3</td>
      <td>nz5kFLSj4p</td>
      <td>TG14pLUXCY</td>
      <td>PCCn9Q1m20</td>
    </tr>
  </tbody>
</table>
</div>

위의 자료는 암호화되어서 자료의 해석을 불가능하지만, 범주형 자료임을 이해할 수 있습니다. 조금 더 자세히 분류하자면, 

***  

## 각주 및 참고문헌

