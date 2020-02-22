---
layout: post
title: <i class="far fa-chart-bar"> [Encoding 특집] 1. One Hot Encoding</i>
date: 2020-02-22 22:28:00 +0800
categories: [Statistics, Encoding]
tags: [label encoding]
toc: true
comments: true
---

데이터를 처리하다보면 범주형 자료와 자주 마주칩니다. 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 그러나 인코딩이 생각만큼 단순한 일이 아닙니다. get_dummies/ One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target-Encoding... 등 정말 [다양한](http://contrib.scikit-learn.org/categorical-encoding/index.html) 인코딩 방법이 존재합니다. 앞으로 인코딩 특집 글에서는 여러 인코딩 기법 중에 가장 자주 쓰이고, 중요한 인코딩 방식들에 대해서 포스팅하겠습니다.  

+ 위에서 범주형 자료(categorical data)란 용어로 편하게 언급하였으나, 사실 데이터의 종류는 범주형과 수치형 데이터로만 나누어져있지 않습니다. 인코딩을 더욱 잘 이해하기 위해서는 데이터의 특징에 따라 정확한 분류가 선행되어야합니다. 이 부분은 [읽을 거리](https://towardsdatascience.com/7-data-types-a-better-way-to-think-about-data-types-for-machine-learning-939fae99a689)로 대체합니다.

## One Hot Encoding
One Hot Encoding(OHE)은 인코딩 기법 중에 가장 간단하면서도 특히 머신러닝에서 가장 많이 쓰입니다. (그러나 가장 좋은 방법이 아닐 때가 더러 있습니다. 이는 마지막에 설명드리겠습니다.) OHE는 각각의 범주에다가 1의 값을 주기 때문에 자료 간의 위계관계가 전혀 없는 순수한 범주형 데이터에 적합합니다. 



