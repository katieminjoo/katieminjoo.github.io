---
layout: post
title: <i class="far fa-chart-bar"> [Encoding] 4. Hash encoding</i>
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
***  

Hashing 인코딩은 Hashing Trick(해싱 트릭)을 사용하여 많은 차원의 더미변수를 보다 간편하게 다루는 기법입니다. 단어에서 느껴지듯이 Hashing이라는 기술을 이해하는 것이 핵심입니다. 이번 글에서는 Hashing의 원리와 활용처를 위주로 Hashing Encoder에 대해서 소개합니다.

# Hashing Trick
사실 Hashing 자체는 컴퓨터 공학 분야를 비롯해서 많은 필드에서 활용되는 기술입니다. 제가 블록체인 산업에서 인턴으로 반년 정도 일을 했었는데, 그곳에서도 Hashing은 가장 근간이되는 기술 중 하나였습니다. 핵심은 간단합니다. 어떠한 종류의 값을 인풋으로 받아도, `반드시 어떠한 숫자로 반환`하는 것이 핵심입니다. 이 외에 다음과 같은 특징을 가집니다.  

```terminal
1. 동일한 인풋은 동일한 결과(숫자)가 나옵니다.  
2. 결과를 바탕으로 인풋을 다시 찾을 수가 없습니다.  
3. 다른 인풋을 넣어도 같은 결과가 나올 수가 있습니다. 이를 Hash Collision이라고 합니다.  
```
> 만약 3번의 특징만 없다면 random과 매우 비슷하다고 생각할 수 있습니다. 

Hash Collision이 존재는 하지만, 실제로 이를 마주치기는 매우 드물기는 합니다. 아래의 예시를 통해서 확인할 수 있습니다.  


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




# 활용분야  


# HashingEncoder


***
***
# 각주 및 참고문헌

## 참고 
1. https://contrib.scikit-learn.org/categorical-encoding/hashing.html  
2. http://www.willmcginnis.com/2016/01/16/even-further-beyond-one-hot-hashing/


## 각주

 
