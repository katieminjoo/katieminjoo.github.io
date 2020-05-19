---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 2. Ordinal/ Label Encoding</i>
date: 2020-02-25 14:22:00 +0800
categories: [Statistics, Encoding]
tags: [Ordinal Encoding, Label Encoding]
toc: true
comments: true
seo:
  date_modified: 2020-03-04 18:47:37 +0900
---

***  
> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  
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
LabelEncoding의 결과가 앞에서 설명한 Ordinal과 유사하기 때문에 크게 쓰일 일이 없을 것 같지만, 저는 개인적으로 <b>[sklearn.preprocessing.LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)</b>를 종종 쓰는 편입니다.[^fac] 사용방법은 sklearn의 다른 인코딩 기법과 유사하기 때문에 쉽게 익힐 수 있을 뿐아니라, <b>자료의 크기가 크거나 해석할 필요가 없는 string이 많이 포함된 범주형 자료일수록 용량을 많이 줄여주기 때문</b>입니다.[^ex] 당연히 numeric한 값으로 바꿔주어도 inverse를 손쉽게 할 수 있다는 점도 중요합니다.[^usage]  

[^fac]: pandas의 내장함수 `factorize` 역시 LabelEncoder와 유사한 기능을 수행합니다. 다만 numpy 기반의 sklearn이 속도도 더 빠를 뿐아니라 사용하기도 쉬워서 LabelEncoder만 설명드리겠습니다.

[^ex]: ![ex](/assets/img/sample/[post][encoding]size.png) [IGAWorks 경진대회](https://haehwan.github.io/posts/Comp-CTR/)에서 실제로 라벨 인코딩을 통해서 데이터 크기를 줄인 사진입니다.   

[^usage]: 저는 LabelEncoding을 train 데이터셋에서 가장 먼저 해준 뒤에, 모든 전처리 과정을 시작합니다. 이후 모델에 적용하기 전에, 다시 원형태로 돌려서 OneHotIncoder 등을 사용합니다. 즉, 저는 데이터를 핸들링하기 쉬운 상태로 만들기 위한 용도로 이를 사용합니다.   

자세한 사용방법은 아래와 같습니다.[^ref] 이는 모든 데이터셋이 범주형 자료일 때 쉽게 이용할 수 있습니다.  

[^ref]: https://stackoverflow.com/questions/24458645/label-encoding-across-multiple-columns-in-scikit-learn  


```python
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
UserName = defaultdict(LabelEncoder)
```
[defaultdict](https://docs.python.org/2/library/collections.html#defaultdict-objects)는 새로운 key에 대해서 에러를 반환하는 것이 아니라, 초기에 설정한 값을 반환하는 기능이 추가된 dictionary입니다. 사용방법은 collections 모둘로부터 `defaultdict`를 import함으로써 가능합니다. 따라서 모든 칼럼에 대해서 각각의 LabelEncoder를 만들고 싶으면, `defaultdict`와 `apply` 함수를 이용해주면 됩니다. 자세한 방법은 아래와 같습니다.  
```python
UserDataFrame.apply(lambda x: UserName[x.name].fit_transform(x))
```
`name`은 Series에 적용할 수 있는 함수이며 Series의 이름을 반환합니다. 따라서 현재 UserDataFrame에 해당하는 모든 칼럼이 `UserName[칼럼이름]`으로 각각 LabelEncoding이 된 상태입니다. 궁금하다면 아래와 같은 코드로 라벨인코딩이 잘 되있음을 확인할 수 있습니다.  
```python
UseName['UserDataFrame_column'].transform(New_UserDataFrame)
```
> 단 이때의 New_UserDataFrame은 새로운 피쳐가 아니라, 기존에 인코딩된 값으로 이루어져있어야합니다.  


원래 값을 보고싶을 때에는, `fit_transform` 대신에 `inverse_transform`을 쓰면 됩니다.
```python
UserTestDataFrame.apply(lambda x: UserName[x.name].inverse_transform(x))
```

간단한 예시는 저의 <b>[깃헙](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/_posts/%5BEncoding%5D%20OHE/LabelEncoder.md)</b>을 참고해주시기 바랍니다. 또한 실제 데이터에서 활용한 사례는 저의 [IGAWorks 경진대회](https://haehwan.github.io/tabs/projects/) 참가 프로젝트에서 확인하실 수 있습니다.

***
***

# 각주 및 참고문헌

