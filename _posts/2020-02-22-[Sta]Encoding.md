---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 1. One Hot Encoding</i>
date: 2020-02-22 22:28:00 +0800
categories: [Statistics, Encoding]
tags: [label encoding]
toc: true
comments: true
---

데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받고 있는 머신러닝과 딥러닝에서는 대다수 경우 범주형 자료에 대한 인코딩이 필수적입니다. 

그러나 이는 생각만큼 단순한 일이 아닙니다. One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target-Encoding... 등 종류도 <b>[다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)</b>할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.  
  
  
## One Hot Encoding
One Hot Encoding은 범주형 자료를 0과 1로 이루어진 벡터로 바꾸는  가장 기본적이고 널리 쓰이는 방식입니다. <b>scikit-learn</b>에서는 이를 위해 `sklearn.preprocessing.OneHotEncoder`를 제공합니다. 유사한 기능을 python의 내장함수, `get_dummies()`도 제공하기 때문에 `더미화`라고도 많이 부릅니다. 두 방식은 매우 흡사하지만 쓰임에 따라 장단점이 명확합니다. 오늘 글에서는 범주형 자료를 수치형으로 변환하는 두 방식의 차이와 더불어, 실제 자료에 이를 적용해보는 것으로 이번 글을 마치겠습니다.  
  

## nominal VS ordinal
들어가기에 앞서, 저는 앞에서 범주형 자료(categorical data)에 대한 구체적인 정의를 하지 않았습니다. 그러나 데이터는 범주형과 수치형으로만 구분하지 않습니다. 여러 기준이 존재하며 각 성질에 따라 적용해야하는 인코딩 기법 또한 달라지게 됩니다. 특히 오늘 다룰 one hot encoding은 전적으로 nominal data에 관한 인코딩 기법입니다. 따라서 같은 범주형 자료일지라도 <b>순서가 존재하는 ordinal 데이터</b>와 구분할 수 있어야 합니다. 가장 대표적인 예시가 사회학에서 응답자의 상태를 하나의 축 위의 4개 또는 5개 점으로 찍어서 표현하는 리커트 척도(Likert scale)가 있습니다. 실제로 scikit-learn에서는 이러한 ordinal data를 위해서 `sklearn.preprocessing.OrdinalEncoder`를 제공합니다. 그러나 모든 ordinal data가 OrdinalEncoder를 쓰기 적절한 것은 아닙니다.  

조금 더 구체적으로 살펴보겠습니다. 같은 ordinal data라도 아래와 같은 두 가지 경우가 있습니다. 

> 1. 범주 간 간격이 '비교적' 일정하다.  
> 2. 그렇지 못한 경우.  

만약 ordianl data의 범주 사이 간격이 일정하거나 그 차이를 어느 정도 알 수 있다면, 우리는 `sklearn.preprocessing.OrdinalEncoder`을 사용할 수 있습니다. 다음 포스팅에 더 자세히 다루겠지만, 그 상하 순서를 살려서 숫자로 변환하는 것을 의미합니다. 그러나 <b>그 간격을 알지 못하거나 확신할 수 없는 경우</b>가 많습니다. 예를 들어 low/ middle/ high는 0, 1, 2도 해당하지만, 0, 1, 100도 해당합니다. 만약 실제 응답자의 middle과 high 간격이 매우 컸다면, `OrdinalEncoder`을 사용한 모델의 성능은 좋지 않을 수 밖에 없습니다. 이 때에는 아무리 순서 상의 상하 관계가 존재한다고 하여도 단순한 nominal한 범주형 자료로 봐주고 `OneHotEncoder`나 `get_dummies` 인코딩을 하는 편이 안전합니다. 물론 이렇게 하면 데이터가 담고 있는 관계성을 잃어버릴지라도 말입니다.   

나머지 데이터의 종류에 관해서는 <b>[읽을 거리](https://towardsdatascience.com/7-data-types-a-better-way-to-think-about-data-types-for-machine-learning-939fae99a689)</b>로 대체하겠습니다. interval, ratio 등의 분류는 매우 중요하니 꼭 읽어보실 것을 추천드립니다.    

***  
  
## 1. get_dummies()
`get_dummies()`는 pandas의 내장함수이니만큼 pandas의 Series나 DataFrame 등에서 사용하기 편리합니다. 특히 `OneHotEncoder`가 instance라는 개념을 사용하기 때문에 처음 사용하기 어려운 반면, `get_dummies()`는 즉각적으로 값을 변환하여 주기 때문에 직관적으로 다가옵니다.

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
      <th>Wealth</th>
      <th>bld</th>
      <th>Qual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jai</th>
      <td>27</td>
      <td>A</td>
      <td>Msc</td>
    </tr>
    <tr>
      <th>Princi</th>
      <td>27</td>
      <td>B</td>
      <td>MA</td>
    </tr>
    <tr>
      <th>Salah</th>
      <td>22</td>
      <td>A</td>
      <td>MA</td>
    </tr>
    <tr>
      <th>Anuj</th>
      <td>32</td>
      <td>O</td>
      <td>Msc</td>
    </tr>
  </tbody>
</table>
</div>  
  

방법은 매우 간단합니다. `pandas.get_dummies()` 함수 안에 본인이 변환하고자 dataframe을 넣어주면 됩니다.  

```python
dummy = pd.get_dummies(data)
dummy
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
      <th>Wealth</th>
      <th>bld_A</th>
      <th>bld_B</th>
      <th>bld_O</th>
      <th>Qual_MA</th>
      <th>Qual_Msc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jai</th>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Princi</th>
      <td>27</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Salah</th>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Anuj</th>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>  
  
  
보다시피, Wealth라는 수치형 변수는 그대로 나오지만 범주형 변수에 해당하는 다른 column들은 모두 범주 갯수에 해당하는 자릿수만큼 추가적인 column이 생기고, 각 해당되는 값에 1이 찍힘을 알 수 있습니다. 주의해야할 것은 이는 pandas가 신출귀몰한 재주로 주어진 자료에서 범주형 데이터를 골라낼 수 있기 때문이 아니라 `isinstance()`라는 함수를 활용해서 <b>string일 때에 모두 더미화</b>를 시키기 때문입니다.[^isinstance] 따라서 주어진 수치형 자료가 string 형태로 들어가있지 않도록 주의해야합니다. 더불어 missing_value가 있거나, None 값이 존재하는 경우에도 `get_dummies()`는 문제가 생길 수 있습니다. 자세한 내용은 <b>[깃헙]()<>/b에 올려놨습니다.

## 2. sklearn.preprocessing.OneHotEncoder
sklearn에서 제공하는 `OneHotEncoder`는 위에서 설명한 `get_dummies()`에 비해 매우 복잡하게 느껴지는 것은 사실입니다. 특히 익숙한 dataframe에 즉각적으로 표현이 잘 되지 않기 때문에 더욱 그렇습니다. 그러나 방법이 완전히 없는 것은 아닙니다. `fit_transform`과 array를 `reshape`하면 sklearn의 `OneHotEncoder`를 사용해서도 dataframe에 바로 표현이 가능합니다. 자세한 내용은 제 <b>[깃헙](https://github.com/HaeHwan/HaeHwan.github.io/blob/master/_posts/%5BEncoding%5D%20OHE/1.%20OneHotEncoder%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C%20pandas%20dataframe%EC%9D%84%20%EB%B0%94%EA%BF%94%EB%B3%B4%EA%B8%B0.ipynb)</b>에 올려놨습니다.  

그럼에도 불구하고 OneHotEncoder는 get_dummies()가 갖지 못한 커다란 장점이 있습니다. 바로 새로운 데이터에도 적용할 수 있다는 사실입니다. 예시를 위해 아래와 같은 두 가지 데이터셋을 준비했습니다.  

  
  
***
***  

## 각주 및 참고문헌

