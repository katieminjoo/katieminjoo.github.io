---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 4. Hash encoding</i>
date: 2020-03-02 01:56:00 +0800
categories: [Statistics, Encoding]
tags: [Hash Encoding]
toc: true
comments: true
seo:
  date_modified: 2020-02-25 15:57:11 +0900
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

***  
> <b>데이터를 처리하다보면 범주형 자료를 수치형 자료로 바꾸어야할 필요성이 많습니다. 이러한 변환을 인코딩이라고 하는데, 다양한 목적과 자료의 특징에 맞추어 올바르게 인코딩한 범주형 자료는 모델의 퍼포먼스와 효율에 상당한 영향을 끼칩니다. 특히 최근 각광받는 머신러닝과 딥러닝에서 범주형 자료에 대한 인코딩은 필수적입니다. 그러나 인코딩은 생각만큼 단순하지 않습니다. *[One-Hot-Encoding/ Ordinal-Encoding/ Label Encoding/ Target Encoding... 등 종류도 다양](http://contrib.scikit-learn.org/categorical-encoding/index.html)*할 뿐더러, 비슷한 인코딩도 library에 따라 크고작은 차이가 있습니다. 인코딩 특집 글에서는 여러 인코딩 기법 중 자주 쓰이고, 중요한 방식들에 대해서 포스팅하겠습니다.</b>   


***  
***  

Hashing 인코딩은 Hashing Trick(해싱 트릭)을 사용하여 많은 차원의 더미변수를 보다 간편하게 다루는 기법입니다. 단어에서 느껴지듯이 Hashing이라는 기술을 이해하는 것이 핵심입니다. 이번 글에서는 Hashing의 원리와 활용처를 위주로 Hashing Encoder에 대해서 소개합니다.

# Hashing Trick
사실 Hashing 자체는 컴퓨터 공학 분야를 비롯해서 많은 필드에서 활용되는 기술입니다. 간단하게 핵심을 설명하자면, 어떠한 종류의 값을 인풋으로 받아도, `반드시 어떠한 숫자로 반환`하는 것이 핵심입니다. 중요한 점은 `반드시`입니다. 즉, 어떤 기대도 하지 않았던 값을 집어넣어도 반드시 결과는 우리가 읽을 수 있는 숫자가 나온다는 점입니다. 이는 많은 머신러닝에서 Hashing이 각광받는 이유가 됩니다. 이 외에 다음과 같은 중요한 특징을 갖습니다.  

```terminal
1. 동일한 인풋은 동일한 결과(숫자)가 나옵니다.  
2. 결과를 바탕으로 인풋을 다시 찾을 수가 없습니다.  
3. 다른 인풋을 넣어도 같은 결과가 나올 수가 있습니다. 이를 Hash Collision이라고 합니다.  
```
> 만약 3번의 특징만 없다면 random과 매우 비슷하다고 생각할 수 있습니다. 

Hash Collision이 존재하기는 하지만, 실제로 이를 마주치기는 매우 드문 편입니다. 아래의 예시를 통해서 쉽게 Hash 함수를 이해할 수 있습니다.  


```python
hash('abc'), hash('ab')
```
    (4359651368998010986, 8189326971213839819)   

> 살짝만 달라져도 다른 값을 도출합니다.

```python
H_abc = hash('abc')
H_abc, hash(H_abc)
```
    (4359651368998010986, 2053808359784317035)   

> 같은 값을 넣으면 동일한 값을 되풀이하지만, 원래 값을 확인할 수는 없습니다.  

이러한 Hashing의 특징은 여러 분야에서 쓰이지만 대표적으로 암호화를 필요로하는 많은 필드들이 주된 사용처입니다. 제가 블록체인 산업에서 인턴으로 반년 정도 일을 했었는데, 그곳에서도 Hashing은 이런 이유로 인해서 가장 근간이되는 기술 중 하나였습니다.  


# Classification in Machine Learning with Hashing  
독특하게도 Hash가 중요하게 활용되는 부분이 머신러닝에서 Classification 문제를 해결할 때입니다. 직관적으로 와닿지는 않지만, 조금만 자세히 들여다보면 금방 이해가 가는 부분입니다. 가장 고전적인 스팸메일 분류방식을 예시로 알아보겠습니다.  

## Basic Method

스팸 메일과 정상 메일을 구별하는 가장 대표적인 방법은 사용된 어휘를 바탕으로 모델을 학습시키는 것입니다. 실제로 스팸 메일을 받아보신 분이라면, 대다수 메일들이 정상적이지 않은 단어들로 이뤄진 것을 아실 겁니다. 이에 기초해서 만들어진 초창기 메일 분류방식은 아래와 같습니다.  

```terminal
1. 스팸메일과 정상메일에 쓰여진 단어를 모두 모읍니다.
   편의상 전체 메일은 모두 N개의 단어로 이루어져있다고 가정하겠습니다.  
   해당 단어에 라벨인코딩을 해줍니다.  
   이렇게 되면 사용된 모든 단어가 0부터 N-1까지의 숫자를 부여받게 됩니다.  
   
2. 더불어 모아진 단어의 갯수(N)만큼의 차원을 가지는 벡터를 메일의 갯수만큼 준비합니다.  
   앞에서 라벨인코딩으로 부여받은 숫자는 해당 벡터에서 각 단어가 가지는 위치를 의미합니다.  
   
3. 각각의 메일이 가지고 있는 단어에 해당하는 벡터의 자릿수를 1로 바꿔줍니다.  
   결과적으로 모든 트레이닝 데이터가 N차원의 벡터를 가집니다.
   그리고 그 안에는 해당 메일이 어떤 단어를 담고 있는지에 관한 뜻을 담고 있습니다.  
   
4. 마지막으로 input을 N차원의 벡터를 받는 머신러닝 모델에 집어넣어 줍니다.
```

이는 굉장히 직관적이면서, 실제로 훈련시킨 데이터셋 안에서 예측력은 굉장히 높습니다. 그러나 한가지 문제점이 있습니다. 만약 새로운 이메일에 새로운 단어가 나타난다면, 이러한 훌륭한 모델이 아무런 쓸모가 없어진다는 사실입니다. 만약 해커가 스팸메일의 단어를 새롭게 바꾸고 정상적인 단어를 몇 개 덫붙인다고 가정해봅시다. 이렇게 되면 새로운 단어는 기존에 가지고 있는 N개의 단어장에 없기 때문에, 벡터의 어느 자릿수에도 표현되지 못합니다. 따라서 우리의 모델은 해당메일을 반드시 정상메일로 분류하게 됩니다. 즉, 새로운 단어가 기존의 N차원 벡터에 영향을 주지 못해서 어떠한 학습도 할 수 없게 되는 것입니다. 위 모델을 계속 발전시키기 위해서는 따라서 새로운 단어가 나타날 때마다 매번 단어장을 새로 수정하고, 모델을 다시 학습시켜야합니다. 당연히 이러한 방식으로는 classification 문제를 현실적으로 해결할 수 없을 것입니다.    

위 문제점은 결국 <b>새로운 데이터가 가지고 있는 정보가 기존의 정보량과 달라서 이를 포함하고자할 때, 차원이 달라져야하는 상황</b> 때문에 발생합니다. 따라서 input 데이터 갯수와 무관하게 차원을 유지할 수 있는 방법이 필요하게 됩니다.  


## Hash
앞에서 파이썬의 `hash()` 함수는 `반드시` 임의의 숫자로 결과를 반환함을 확인했습니다. 이 점이 바로 input과 무관하게 동일한 차원이 나와야하는 현재 문제를 풀 수 있는 열쇠가 됩니다. 만약 우리가 충분히 큰 수로 값이 나오게끔 해쉬함수를 설정해서 어떠한 값을 input으로 넣어도 input 값마다 고유의 라벨링이 가능하다면, 우리는 위의 문제를 해결할 수 있습니다. 조금 더 자세한 방법은 아래와 같습니다.  

```terminal
1. 예를 들어 2^20과 같이 큰 수에 해당하는 0 벡터를 만들어줍니다.  
2. hash 함수값의 범위를 2^20 보다 작은 값이 나오도록 설정해줍니다.  
3. 메일의 모든 단어를 input으로 hash 함수에 집어넣습니다.  
4. 결과값으로 나오는 숫자를 자릿수로 인식하여 1로 바꾸어줍니다.  
```

이렇게 하면 결과적으로 어떠한 input을 집어넣어도 고정된 차원($$2^{20}$$) 안에서 모두 표현이 가능하게 됩니다. 따라서 해커들이 새로운 단어로 스팸메일 발송에 성공하여도, 사용자가 이를 스팸메일로 분류하여 라벨링을 해주는 순간 해커의 노력은 모델을 위한 학습자료로 활용이 됩니다. 결국 아무리 새로운 단어를 마주해도 실시간 학습이 이루어지게 됩니다. 2^20이 충분히 큰 수이기 때문에 새로운 단어들이 계속해서 추가되어도 단어마다의 고유한 라벨링이 깨질 위험도 굉장히 작습니다.  

뿐만 아니라 gradient descent 알고리즘을 활용하는 대다수 머신러닝에서 0은 어차피 어떤 수를 곱해도 바뀌지 않기 때문에, 특정 단어를 포함하느냐의 여부에 따라 오직 0과 1로만 가지고 있는 현재의 데이터는 그다지 큰 연산량을 필요로 하지는 않습니다. 실제로는 sparse 메트릭스의 차원을 축소해주는 과정도 사용되고, 효율적인 자원사용을 위해 최적의 차원 갯수를 결정하는 연산과정도 들어가기 때문에 이 방식은 꽤나 성공적으로 스팸과 정상메일을 분류해줄 수 있게 됩니다. 물론 2^20 같이 큰 수가 아니라 작은 수를 차원의 갯수로 정해도 위의 알고리즘은 계속해서 실시간 학습을 이어나갈 수 있습니다. 그러나 이 경우에는 hashing collision이 발생하기 때문에 정확도가 떨어질 것입니다. 서로 다른 단어가 같은 결과값으로 반환되기 때문입니다.      

이처럼 Hashing은 input이 제한되어있지 않은 언어를 원하는 차원의 갯수로 한정시키는데에 탁월함을 알 수 있습니다. 실제로 많은 자연어 처리기반의 알고리즘에서 이를 활용하는 까닭입니다.  

<br>  
<br>  

# Hashing Encoding
`HashingEncoder`도 결국 위와 같은 Hash 함수의 성질을 이용한 인코딩기법입니다. 따라서 아무리 많은 피쳐의 범주형 자료들을 마주하더라도, 원하는 차원의 갯수로 표현이 가능합니다. 당연히 차원의 갯수가 커질수록 정확도는 높아지고, 연산량도 증가합니다. 따라서 최적의 차원을 정하기 위한 하이퍼파라미터 튜닝과정이 필요하기는 합니다. 그럼에도 불구하고 이전에 소개한 여러 인코딩 기법들과 달리 장점이 있습니다.  

## online learning
이전에 인코딩 기법들은 새로운 피쳐를 마주하면, 하나의 동일한 피쳐로 바꾸었습니다. 대표적으로 OneHotEncoder와 BinaryEncoder가 있을 것입니다. 이들은 차원을 유지하기위해서 새로운 모든 값들을 0 벡터로 반환했습니다. 이렇게하면 어떠한 데이터셋을 마주해도 계속해서 완성해놓은 모델에 적용할 수 있게됩니다. 그러나 만약 <b>테스트 데이터의 실제 결과값을 확인할 수 있어서 이를 다시금 모델에 반영하고자 한다면</b> 문제가 생깁니다. 분명히 다른 값들임에도 불구하고 자동적으로 같은 값으로 인식이 되기 때문에 정확도가 떨어질 수 밖에 없습니다. 예를 들어서 고객이 새로운 메일을 스팸으로 분류하여 정보를 전달해주어도 이를 활용할 수가 없게 되는 것입니다.  

그러나 HashingEncoder는 새로운 피쳐에 대해서도 고유한 값을 도출할 수 있습니다. 따라서 테스트 데이터의 결과를 확인할 수 있다면, 이를 피드백으로 모델에 적용해도 문제가 없습니다. 따라서 모델을 갱신할 필요없이, 같은 모델의 예측력을 계속해서 발전시켜나가게 됩니다. 이를 가리켜 <b>online learning</b>이라고 합니다. 이러한 특징 때문에 실제 산업분야에서 해쉬함수는 애용됩니다. 물론 이는 피쳐 갯수가 차원 수보다 엄청나게 커져서, hashing collision을 발생시키지 않는다는 가정을 하고 있습니다. 이와 관련한 간단한 예시를 저의 <b>[깃헙]()</b>에서 확인하실 수 있습니다.  


## category_encoders.hashing.HashingEncoder
hash 함수를 통해서 인코딩하는 가장 쉬운 방법은 sklearn의 `HashingEncoder`입니다. 마찬가지로 다른 `category_encoders method`와 동일한 사용법을 가집니다. 차이점은 다른 인코딩 방법이 가지고 있는 `inverse_transform`이 없다는 점입니다. Hashing의 특징을 생각해보면 사실 당연한 결과입니다. 이외에도 아래와 같은 특징이 있습니다.  

```
HashingEncoder(n_components = UserNumber, cols=["User Columns"], hash_method='md5', max_process = 1)
```  
HashingEncoder에 기본적으로 필요한 옵션들입니다. 다른 인코딩과 구별되는 가장 큰 특징은 `n_components`입니다. 바로 이 부분이 사용자가 원하는 차원을 결정하는 부분입니다. default 값으로는 8로 설정이 되어있습니다.  

두 번째로 중요한 부분은 `hash_method`입니다. 실제로 hash 함수는 여러개 존재하는데, 파이썬도 역시 대다수 <b>[hash 함수](https://docs.python.org/3/library/hashlib.html)</b>를 제공합니다. 각 함수들은 사용하고 있는 random 방법과 range에 따라 약간씩 차이가 있지만, 대다수 경우에는 default로 제공하고 있는 `md5`로도 충분할 것입니다.  

세 번째로 구별되는 특징은 `max_process`입니다. 해당 인코딩 기법은 컴퓨터의 CPU와 프로세스에 따라 결과값이 달라지게 됩니다. 각자 컴퓨터 사양에 맞추어 절반의 프로세스를 default로 사용하게끔 되어있습니다. 저는 개인적으로 최소한의 프로세스를 사용하기 위해서 이 값을 1로 설정하는 편입니다.   


## 직접 구현해보기
hash를 활용해서 인코딩하는 함수를 직접 구현할 수도 있습니다. 사용자가 입력한 임의의 숫자만큼 차원을 만들고, `hash()` 함수를 통해서 생성된 숫자를 각 벡터에 고유하게 배당하는 방법으로 만들어 볼 수 있습니다.  



```python
import pandas as pd

X = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart']})
```


```python
N = 10
cols = ['col_%d' % d for d in range(N)]
```


```python
def hash_fn(x):
    tmp = [0 for _ in range(N)]
    for val in x.values:
        tmp[hash(val) % N] += 1  
        print("{}: \t{} \t{}".format(val, hash(val), hash(val) % N))
    
    print("{}\n".format(tmp))
        
    return pd.Series(tmp, index=cols)
```


```python
X
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>store</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cleaning</td>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cleaning</td>
      <td>Dia</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Entertainment</td>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Entertainment</td>
      <td>Fnac</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tech</td>
      <td>Dia</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tech</td>
      <td>Walmart</td>
    </tr>
  </tbody>
</table>
</div>




```python
res = X.apply(hash_fn, axis = 1)
```

    Cleaning: 	2757853755239877974 	4
    Walmart: 	954132345483583663 	3
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    
    Cleaning: 	2757853755239877974 	4
    Walmart: 	954132345483583663 	3
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    
    Cleaning: 	2757853755239877974 	4
    Dia: 	-6914920821674701215 	5
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    
    Entertainment: 	-8470121183086974585 	5
    Walmart: 	954132345483583663 	3
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    
    Entertainment: 	-8470121183086974585 	5
    Fnac: 	-1687995386747530867 	3
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    
    Tech: 	3426699838082966844 	4
    Dia: 	-6914920821674701215 	5
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    
    Tech: 	3426699838082966844 	4
    Walmart: 	954132345483583663 	3
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    
    


```python
res
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_0</th>
      <th>col_1</th>
      <th>col_2</th>
      <th>col_3</th>
      <th>col_4</th>
      <th>col_5</th>
      <th>col_6</th>
      <th>col_7</th>
      <th>col_8</th>
      <th>col_9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>  

  
   
   
위에서 구현한 방식의 특징은 범주형 자료마다 인코딩 기법이 들어가는 것이 아니라 각기 다른 범주형 자료를 모두 한꺼번에 인코딩해줄 수 있다는 장점이 있음을 확인할 수 있습니다. 이를 위한 참고자료는 하단에 첨부하였습니다.  

***
***
# 각주 및 참고문헌

## 참고 
1. https://contrib.scikit-learn.org/categorical-encoding/hashing.html  
2. http://www.willmcginnis.com/2016/01/16/even-further-beyond-one-hot-hashing/
3. https://medium.com/value-stream-design/introducing-one-of-the-best-hacks-in-machine-learning-the-hashing-trick-bf6a9c8af18f
 
