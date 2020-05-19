---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 5. Target Encoding</i>
date: 2020-03-04 18:15:00 +0800
categories: [Statistics, Encoding]
tags: [Target Encoding]
toc: true
comments: true
seo:
  date_modified: 2020-03-05 12:37:37 +0900
---

***  
> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  
***  

target 인코딩은 범주형 자료의 값들을 트레이닝 데이터에서 "타겟"에 해당하는 변수로 바꿔주는 방식입니다. 이 때 대부분 타겟 변수의 평균으로 변환해줍니다. 뚜렷한 장점만큼 뚜렷한 단점도 존재하기 때문에 단점을 상쇄하기 위한 훌륭한 기법들도 잘 마련되어 있는 인코딩 기법입니다. 오늘은 바로 이 타겟인코딩에 대해서 소개합니다.  


# Target Encoding



# Over-fitting
target 인코딩은 여러가지 유의점이 있습니다. 예를 들어 평균값으로 범주를 대체하기 때문에 데이터가 적으면 적을수록 좋은 방법이 되지 못합니다. 따라서 기본적으로 데이터 관측치가 많아야하는 조건이 따릅니다. 이외에도 여러 유의점이 있겠으나 가장 중요한 점은 <b>오버피팅</b> 문제입니다. 


# Leave One Out

***
***
# 각주 및 참고문헌

## 참고 
1. https://contrib.scikit-learn.org/categorical-encoding/targetencoder.html

## 각주

 
