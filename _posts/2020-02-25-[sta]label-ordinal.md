---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 2. Ordinal/ Label Encoding</i>
date: 2020-02-25 14:22:00 +0800
categories: [Statistics, Encoding]
tags: [ColumnTransformer]
toc: true
comments: true
seo:
  date_modified: 2020-02-25 15:57:11 +0900
---

***  
> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  

  
  
오늘은 Ordinal 인코딩과 Label 인코딩에 대해서 간략하게 소개하려고 합니다. 두 방식은 결과적으로 큰 차이가 존재하지 않습니다. 두 방식 모두 범주형 자료를 숫자형 자료로 바꿔주기 때문입니다. 그러나 둘 다 최근들어서 많이 쓰이지 않는 것이 사실입니다.  

그럼에도 불구하고 두 개념을 이해한다면, 자료를 이해하거나 데이터 용량을 줄이는데 큰 도움을 받을 수 있습니다. 특히 복잡하게 암호화되어있는 데이터를 라벨인코딩 또는 오디널인코딩을 해준다면, 적어진 용량 덕분에 메모리 사용량도 줄이고 작업속도도 한층 개선될 것입니다.  

두 방법이 매우 흡사하기 때문에 Label Encoding을 주로 다룰 예정입니다.  

# Ordinal Encoding  
저는 Ordinal한 데이터를 다룰 때, dictionary를 pandas.Series.map에 대입하여 사용합니다.  

```python
pandas.Series.map(UserDictionary)
```  
물론 sklearn.preprocessing 모듈에서도 <b>[OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)</b> method를 통해서 Ordinal한 데이터에 특화된 인코딩기법이 있습니다. 이는 ordinal한 데이터를 원핫(더미화)방식이 아닌 integer한 쌍으로 기억한다는 점만 다를 뿐, 모든 옵션과 사용 방법은 지난 시간에 포스팅했던 OneHotEncoder와 동일합니다.  

그러나 주의해야될 점은, Ordinal 데이터를 함부로 숫자화할 수 없다는 점입니다. 실제로 대다수 데이터는 상하관계 혹은 피쳐 간의 차이가 샘플마다 다른 경우가 대다수입니다. 예를 들어 A에게 상과 중의 차이가 B가 느끼는 상과 중의 차이와 다를 수 있는 것입니다. 이렇듯 ordinal encoding을 실제로 사용하는 일은 굉장히 드뭅니다. 특히 neural network와 같은 딥러닝에서는 ordinal한 피쳐들이 가지는 대소 혹은 상하 관계가 원핫인코딩을 통해서도 반영이 될 수 있으며, 웬만한 커다란 차원은 해결이 가능하기 때문에 더더욱 사용할 경우가 적어지고 있습니다.  

Ordinal 데이터로 적합한 예시를 찾아보자면, 최종학력 정도가 있을 수 있겠습니다. 한 나라 안에서 특정한 최종학력까지의 교육과정은 모든 샘플에 대해서 거의 유사합니다. 따라서 예컨대 고등학교 졸업과 대학교 졸업 간의 차이를 수량화할 수 있다면 이는 모든 샘플들에 대해서 일괄적으로 숫자형 자료로 변화시켜도 될 것입니다. 물론 단순하게 최종학력이 높을수록 순차적으로 1씩 증가하는 형태도 괜찮을 겁니다. 다만 어떤 간격의 숫자로 바꿔주었든, normalizing을 통해서 최종적으로 사용하면 됩니다.  



# sklearn.preprocessing.LabelEncoder
LabelEncoding의 결과가 앞에서 설명한 Ordinal과 유사하기 때문에 크게 쓰일 일이 없을 것 같지만, 저는 개인적으로 <b>[sklearn.preprocessing.LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)</b>를 종종 쓰는 편입니다. 사용방법은 sklearn의 다른 인코딩 기법과 유사하기 때문에 쉽게 익힐 수 있을 뿐아니라, 자료의 크기가 크거나 string이 많이 포함된 범주형 자료일수록 용량을 많이 줄여주기 때문입니다. numeric한 값으로 바꿔주어도 inverse를 손쉽게 할 수 있고, 새로운 피쳐를 마주해도 인코딩되어있던 ordering을 해치지 않는다는 큰 장점 또한 중요합니다.[^fac]  

[^fac]: pandas의 내장함수 `factorize` 역시 LabelEncoder와 유사한 기능을 수행하나, 이러한 점에서는 [지난 포스팅](https://haehwan.github.io/posts/Sta-Encoding/)의 `get_dummies`와 같이 해결을 하지 못합니다. 즉, 새로운 피쳐로 인해서 라벨링의 순서가 뒤바뀔 수 단점이 있습니다.   

자세한 사용방법은 아래와 같습니다.



