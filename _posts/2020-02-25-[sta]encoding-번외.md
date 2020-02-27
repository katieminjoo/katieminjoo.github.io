---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] ColumnTransformer</i>
date: 2020-02-25 14:22:00 +0800
categories: [Statistics, Encoding]
tags: [ColumnTransformer]
toc: true
comments: true
seo:
  date_modified: 2020-02-25 15:57:11 +0900
---

> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  
  

오늘은 Encoding과 관련해서 sklearn을 사용할 때에 유용한 팁을 전해드리려고 합니다. sklearn은 파이썬에서 사용할 수 있는 머신러닝 라이브러리입니다.
많은 사람들이 이용할 뿐 아니라, 제공하고 있는 함수들도 매우 유용합니다.
<b>[저번 글](https://haehwan.github.io/posts/Sta-Encoding/)</b>에서 OneHotEncoder처럼 sklearn은 array 형태를 사용합니다.
pandas를 쓰다보면 마주칠 일이 별로 없어서 생소할 수 있지만, 
<b>array는 특히 list와 비교해서 메모리 사용량과 처리 속도에</b> <b>[뛰어난 강점](https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)</b>을 보입니다.  

따라서 연산량이 많은 머신러닝에서는 array를 사용해서 작업하는 경우가 많은데 이는 Encoding에서도 마찬가지입니다.
특히 데이터셋이 범주형과 수치형 등으로 혼합되어서 나올 경우에 범주형에만 선택적으로 지난 시간에 배운, OneHotEncoder를 사용해줄 필요가 있습니다.
다른 수치형 자료에는 normalizing을 해주어야 하고요.[^stand]
이렇듯 하나의 데이터에서 array로 서로 다른 형태의 작업을 해주어야할 때 필요한 것이 <b>[ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)</b>입니다. 

  
[^stand]: 이론적으로는 수치형 데이터를 표준화해줄 필요는 없습니다만, 실제로는 표준화작업을 거치면 더욱 빠르게 수렴하기 때문에 좋은 모델이 됩니다.
   

# ColumnTransformer
기본적인 사용법은 아래와 같습니다. 

```
transformer = ColumnTransformer(transformers=[('Name', OneHotEncoder(), ["col1", "col2"])])
```  

transformer라는 변수 안에, `이름/ 작업할 함수/ 선택할 컬럼` 이렇게 3개를 연달아 집어넣습니다.  

만약 선택한 변수가 수치형 자료라면 아래와 같을 것입니다.

```
transformer = ColumnTransformer(transformers=[('Name','num', MinMaxScaler(), ["col3", "col4"])])
```  

주의해야할 점은, transformer 변수 자체가 list of tuples의 형태로 입력받는다는 것입니다.
따라서 각기 다른 변환을 원하는 columns들에 대해서 위의 3가지를 입력해준 뒤에 튜플을 씌어준다면 여러 변환을 하나의 리스트 안에 담을 수 있습니다.
예시는 아래와 같습니다.  

```
t1 = ('Name', OneHotEncoder(), ["col1", "col2"])
t2 = ('Name', MinMaxScaler(), ["col3", "col4"])
t3 = ('Name', SimpleImputer(strategy='median'), ["col5", "col6"])
t = [t1, t2, t3]
transformer = ColumnTransformer(transformers=t)
```  
>  `SimpleImputer()`는 Sklearn에서 결측치를 해결해주는 함수입니다.  

***  

참고로 마지막에 넣어주어야하는 column은 리스트 형태 안에 string 혹은 위치에 따른 integer을 넣어줘도 모두 가능합니다.  


보다 자세한 예시[^참고]는 [깃헙](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/_posts/%5BEncoding%5D%20OHE/%EC%8B%AC%ED%99%94%EA%B3%BC%EC%A0%95/ColumnTransformer.ipynb)에 올려놨습니다.  

  
[^참고]: https://machinelearningmastery.com/columntransformer-for-numerical-and-categorical-data/



***
***

# 각주 및 참고자료
