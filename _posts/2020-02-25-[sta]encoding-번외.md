---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] ColumnTransformer</i>
date: 2020-02-25 14:22:00 +0800
categories: [Statistics, Encoding]
tags: [ColumnTransformer]
toc: true
comments: true
---

```
데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다.
이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다.
특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다.
그러나 인코딩은 생각만큼 단순하지 않습니다. One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등
종류도 <b>[다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)</b>할 뿐더러,
비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다.
인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.
```   

오늘은 Encoding과 관련해서 sklearn을 사용할 때에 유용한 팁을 전해드리려고 합니다. sklearn은 파이썬에서 사용할 수 있는 머신러닝 라이브러리입니다.
많은 사람들이 이용할 뿐 아니라, 제공하고 있는 함수들도 매우 유용합니다.
<b>[저번 글](https://haehwan.github.io/posts/Sta-Encoding/)</b>에서 OneHotEncoder처럼 sklearn은 array 형태를 사용합니다.
pandas를 쓰다보면 마주칠 일이 별로 없어서 생소할 수 있지만, 
<b>array는 특히 list와 비교해서 메모리 사용량과 처리 속도에 [뛰어난 강점]
(https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)</b>을 보입니다.  

따라서 연산량이 많은 머신러닝에서는 array를 사용해서 작업하는 경우가 많은데 이는 Encoding에서도 마찬가지입니다.
특히 데이터셋이 범주형과 수치형 등으로 혼합되어서 나올 경우에 범주형에만 선택적으로 지난 시간에 배운, OneHotEncoder를 사용해줄 필요가 있습니다.
다른 수치형 자료에는 normalizing을 해주어야 하고요.
이렇듯 하나의 데이터에서 array로 서로 다른 형태의 작업을 해주어야할 때 필요한 것이 <b>[ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)</b>입니다. 


# ColumnTransformer

