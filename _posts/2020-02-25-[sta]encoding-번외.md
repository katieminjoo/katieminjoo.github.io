---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] make_column_transformer</i>
date: 2020-02-25 14:22:00 +0800
categories: [Statistics, Encoding]
tags: [ColumnTransformer]
toc: true
comments: true
seo:
  date_modified: 2020-02-25 15:57:11 +0900
---

***  
> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  
  

<b>[저번 글](https://haehwan.github.io/posts/Sta-Encoding/)</b>에서 OneHotEncoder를 소개하면서 깃헙에서 보여드렸던 모든 예시들은 오직 범주형 자료만을 가지고 있는 상황이였습니다. 그러나 대부분 데이터셋은 범주형과 수치형 등을 모두 가지고 있습니다. 이러한 상황에서는 어떻게 가장 효율적으로 코드를 구현할 수 있을지 이번 시간에 sklearn의 함수들을 바탕으로 소개하려고 합니다.

## make_column_transformer
데이터를 마주해도 각 데이터의 변수마다 적합한 전처리를 해줘야 합니다. 예를 들어 범주형 자료에는 지난 시간에 배운대로 더미화를 해주어야하고, 수치형 자료는 normalizing을 해주어야 합니다.[^stand] 그리고 normalizing의 방법조차 변수마다 다르게 적용해야할 필요가 있습니다. 심지어 때로는 전혀 사용하지 않을 변수도 존재합니다. 이렇듯 변수가 많을수록 전처리의 방법은 다양해지고, 이를 작업하기 위해서 raw 데이터셋을 자르거나 합치거나 등의 작업을 여러 cell에서 수행을 하는 것은 꽤나 까다롭습니다.  

[^stand]: neural network에서 이론적으로는 수치형 데이터를 표준화해줄 필요는 없습니다만, 실제로는 표준화작업을 거치면 더욱 빠르게 수렴하기 때문에 좋은 모델이 됩니다.


이때 정말 유용하게 쓸 수 있는 함수가 <b>[sklearn.compose.make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)</b>입니다.  

```
from sklearn.compose import make_column_transformer
```

사용방법은 간단합니다. 아래와 같이 여러개의 튜플을 인수로 받으며, 각 튜플마다 다양한 인코딩 혹은 normalizing의 방법을 적용하고 싶은 column들과 같이 써주면 됩니다. 

```
preprocess = make_column_transformer(
    (MinMaxScaler(), ["numeric"]), 
    (OneHotEncoder(handle_unknown = "ignore"), ["categoric"]))
```
> OneHotEncoder 안에 지난 시간에 배운대로 새로운 범주형 피쳐를 만났을 때 모두 0으로 이루어진 벡터로 반환하도록 명령했습니다.

옵션 또한 굉장히 직관적이고 다양해서 유용합니다. 제가 자주 쓰는 몇 가지를 소개하겠습니다.

```
verbose = True
```
작업을 할 때 걸리는 시간을 알려줍니다. 

```
remainder='passthrough'
```
튜플에서 정의하지 않은 변수들은 그대로 살려서 남겨놓습니다. 

자세한 예시는 저의 <b>[깃헙](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/_posts/%5BEncoding%5D%20OHE/%EC%8B%AC%ED%99%94%EA%B3%BC%EC%A0%95/make_column_transformer.md)</b>을 참고해주시길 바랍니다.  

***  

# ColumnTransformer
<b>[ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)</b>는 `make_column_transformer`과 거의 동일하게 같은 기능을 제공합니다. 똑같이 array로 작동하며, 인스턴스에 변수들을 저장하기 때문에 새로운 데이터셋을 마주해도 똑같은 차원으로 가공을 할 수 있습니다. 따라서 두 방법 중 익숙한 방법을 선택하시면 될 겁니다.  

기본적인 사용법은 아래와 같습니다. 

```
transformer = ColumnTransformer(transformers=[('Name', OneHotEncoder(), ["col1", "col2"])])
```  

transformer라는 변수 안에, `이름/ 작업할 함수/ 선택할 컬럼` 이렇게 3개를 연달아 집어넣습니다. 유일한 차이점은 이름을 추가해준다는 것 정도임을 알 수 있습니다.  

만약 선택한 변수가 수치형 자료라면 아래와 같을 것입니다.

```
transformer = ColumnTransformer(transformers=[('Name', MinMaxScaler(), ["col3", "col4"])])
```  

또 다른 차이점은 transformer 변수 자체가 list of tuples의 형태로 입력받는다는 것입니다. 이는 `make_column_transformer`은 따로 리스트 안에 처리할 컬럼과 적용방식을 담지 않았던 것과 차이를 보입니다.  

각기 다른 변환을 원하는 columns들에 대해서 위의 3가지를 입력해준 뒤에 튜플을 씌어준다면 여러 변환을 하나의 리스트 안에 일목요연하게 담을 수 있습니다. 예시는 아래와 같습니다.  

```
t1 = ('Name', OneHotEncoder(), ["col1", "col2"])
t2 = ('Name', MinMaxScaler(), ["col3", "col4"])
t3 = ('Name', SimpleImputer(strategy='median'), ["col5", "col6"])
t = [t1, t2, t3]
transformer = ColumnTransformer(transformers=t)
```  
>  `SimpleImputer()`는 Sklearn에서 결측치를 해결해주는 함수입니다.  

***  


보다 자세한 예시는 [깃헙](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/_posts/%5BEncoding%5D%20OHE/%EC%8B%AC%ED%99%94%EA%B3%BC%EC%A0%95/ColumnTransformer.md)에 올려놨습니다.  



***
***

# 각주 및 참고자료
1. https://machinelearningmastery.com/columntransformer-for-numerical-and-categorical-data/
