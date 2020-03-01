---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] Binary/ BaseN encoding</i>
date: 2020-03-01 13:42:00 +0800
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
 
<b>[OneHotEncoding](https://haehwan.github.io/posts/Sta-Encoding/)</b>은 매우 직관적이고 모든 범주형 자료에서 활용가능합니다. 하지만 차원이 피쳐의 갯수만큼 증가한다는 커다란 단점이 있습니다. 이는 로우의 갯수가 많고, 컬럼들의 피쳐가 많아질수록 필요한 연산량이 기하급수적으로 증가함을 의미합니다. 원핫인코딩 때문에 GCP를 사용한다면 여간 불편할 일일 뿐 아니라, GCP를 사용해도 데이터의 크기가 너무 크기 때문에 불편합니다.  

이때 좋은 해결방법이 바로 N진법으로 표현하는 방법입니다. 이를 가리켜 BaseN Encoding이라고 하며, 주로 2진법을 많이 사용하기 때문에 그 중에서 N=2인 Binary Encoding이 가장 대표적입니다. 두 방법 모두 sklearn에서 범주형 자료에 대한 인코딩을 전문적으로 다루는 <b>[Categorical Encoding Methods](http://contrib.scikit-learn.org/categorical-encoding/)</b>의 일종입니다. 따라서 이를 위해서는 아래와 같이 라이브러리를 설치해주어야합니다.[^ce]    

[^ce]: 물론 category_encoders에서도 OneHot과 Label 인코딩을 제공합니다만, 저 같은 경우는 두 인코딩 기법은 sklearn에 내장되어있는 함수가 더 익숙한 편입니다. (물론 `category_encoders`의 방식이 좀 더 [다양한 옵션](http://contrib.scikit-learn.org/categorical-encoding/onehot.html)들을 제공하기는 합니다.)  

```python 
pip install category_encoders
import category_encoders as ce
```

# BinaryEncoder
먼저 2진법으로 표현하는 것의 장점을 간략하게 말씀드리려고 합니다. 평소에 원핫으로 인코딩을 한다는 것은, 완전히 맞는 말은 아니지만 1진법으로 표현하는 것과 유사합니다. 1진법이란, 흔히 개표를 할 때 바를 정(正)자를 써서 득표수를 쓰는 것을 의미합니다. 이 경우, 득표수만큼 획순을 더해가게 되는데, 원핫인코딩도 사실 같은 논리입니다. 다만 <b>피쳐의 갯수만큼 벡터의 길이가 늘어납니다.</b>  

반면 2진법은 각 자릿수마다 0과 1의 두가지 숫자로 표현하게됩니다. 예를 들어, `100`은 `1100100`이 됩니다. 만약 100가지의 피쳐를 가지는 범주형 변수를 원핫인코딩을 한다거나, 이를 1진법으로 표현하기 위해서는 100차원의 벡터 혹은 100번의 획순이 필요한 것과 비교하면 단 7자리로 표현이 가능하니 엄청난 차원축소라고 할 수 있습니다. 따라서 원핫인코딩으로 [메모리 부족](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/assets/projects/IGAWorks/%5Bigaworks%5D(1)%20EDA.md)[^ex]이 생기던 문제도 말끔히 해결할 수 있게 됩니다.  

[^ex]: 계속해서 피쳐들을 정리해가면서 원핫인코딩을 적용을 하려고 해도, 로컬컴퓨터와 Colab에서는 메모리 부족의 에러가 발생하는 ipynb 파일입니다.  

구체적인 사용법은 아래와 같습니다.  


# BaseN

***
***
# 각주 및 참고문헌

참고 : https://towardsdatascience.com/smarter-ways-to-encode-categorical-data-for-machine-learning-part-1-of-3-6dca2f71b159
