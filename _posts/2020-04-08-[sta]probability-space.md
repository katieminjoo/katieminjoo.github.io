---
title: <i class="far fa-chart-bar"> Probability Space </i>
date: 2020-04-08 02:59:00 +0800
categories: [Statistics, Probability Space]
tags: [Probability Space]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Probability Space
확률공간(Probability Space)이란, 확률(Probability)을 다루기 위해서 가장 기본적으로 선행되어야할 일종의 조건과 가깝습니다. 이 부분은 저의 사설이지만, 수학에서 Space가 의미하는 바를 이해한다면 조금 더 체화해서 이해할 수 있을 것 같습니다.

대수학에 수많은 Space가 있겠지만, metric space 예시를 들어볼까 합니다.[^space] 보통 우리가 metric space $$M$$이라고 이야기하는 것은, 특정 집합 $$M$$과 distance function $$d$$를 가리킵니다. 여기서 distance function이란, distance의 4가지 성질을 만족하는 어떠한 함수여도 무방합니다. 이러한 space가 정의되어 있어야만 비로소 우리는 $$d$$를 가리켜 $$M$$에 대한 metric(a metric on $$d$$)이라고 부르며 이를 통해서 거리를 이야기하게 됩니다. Euclidean Space에서 배우는 Open, Interior, Closed 등등의 모든 기초개념들도 바로 이를 바탕으로 세워진 개념들입니다.

[^space]: space란 표현은 수학적으로 딱히 정의를 하지 않고 쓰는 표현입니다. 많은 종류의 ~~ space 같은 표현을 사용하지만 정작 space가 뭔지에 대해서는 얘기를 안 하는데, 이는 마치 integral number(=integer), rational number, complex number 등등 number에 대한 이야기는 많이 하지만 정작 number가 뭔지에 대해서는 크게 고민하지 않고 쓰는 것과 비슷합니다. 다만, 보편적으로 space는 어떤 set에 structure가 주어진 경우를 일컫는데, 이때 structure란 point 사이의 관계에 대한 이야기로, point란 space를 구성하는 mathematical object 정도로 생각하면 됩니다.

마찬가지로 확률을 이야기하고, 이를 기반으로 sensible한 model을 만들기 위해서는 확률공간이 잘 정의되어있어야합니다. 임종호 교수님 말씀처럼 각각의 개념들에 대해 self-explanation을 할 수 있을 정도로 숙달할 필요가 있어야한다는 말이 조금은 이해가 됩니다. 다행히 확률공간은 3가지 개념들로 이루어져있으니 그리 어렵지는 않습니다.

<br>

## $$\Omega$$, sample space
<b>set of all outcomes of random experiments</b>  

여기에서 random experiments란, 확률적으로 어떤 결과가 나올지 모르는 실험으로써 아래와 같은 성질을 만족해야합니다.

1. A collection of every possible outcome of an experiment can be described prior to its performance.
2. The experiment can be repeated under the same conditions.

어떤 결과가 나올지 예상조차 할 수 없는 실험(1)이나, 동일한 조건에서 반복되어질 수 없는 실험(2)은 random experiments라고 하지 않습니다. 예를 들어 동전 던지기를 한다면 우리는 결과값이 앞면 또는 뒷면만이 나오며, 동전을 던질 때마다 마모가 일어나서 동전이 가지는 고유한 성질이 바뀌지 않아야합니다.

또 다른 예시로 "주사위 던지기"를 생각해본다면, sample space는 가능한 모든 결과들의 집합이므로, {1, 2, 3, 4, 5, 6}에 해당합니다. (더 엄밀히 말한다면, 보통 주사위는 pip dice이니깐 {점의 갯수가 1개, 점의 갯수가 2개, ..., 점의 갯수가 6개}라고 해야할 것입니다. sample space를 이처럼 숫자값의 집합이 아니라 추상적인 결과들의 집합으로 이해하는 것이 확률공간을 이해하는 데에 더 용이합니다.)

<br> 

## $$\mathcal {F}$$,  σ-algebra (on a sample space, $$\Omega$$)
<b>collection of subsets of sample space =  
collection of events</b>

사실 위의 정의는 엄밀한 의미의 σ-algebra가 아니라, 단순히 event space라고 부르는 것이 맞습니다. σ-algebra로 불리기 위해서는 이에 더해 몇 가지 조건을 만족해야합니다. (σ-algebra는 algebra보다 조금 더 강한 조건들을 만족해야하는 subset으로 생각하면 됩니다.) 간단하게 이를 살펴보면 다음과 같습니다.

1. $$\Omega$$를 포함해야합니다.
2. 여집합에 대해서 닫혀있어야 합니다.
3. countable union에 대해서 닫혀있어야 합니다.

각각의 성질은 긴밀하게 연관되어 있어서 더 많은 성질을 함축적으로 표현하고 있습니다. 예를 들어 2번 성질로 인해서 σ-algebra는 반드시 공집합을 포함하고 있어야하며, 1과 2번 성질을 이용하여 countable intersection에 대해서도 닫혀있어야함을 보일 수가 있습니다. 종합하면 공집합과 전체집합을 가지고 있되, 교집합, 합집합, 여집합에 대해서 닫혀있는 집합을 σ-algebra라고 합니다.[^complement] 

[^complement]: 사실 원서로 공부하다보면 한자어로 이뤄진 한국어가 더 어려울 때가 많습니다. 여집합은 complement, 즉 전체집합에 대한 차집합입니다. 간혹 차집합이랑 헷갈릴 때가 있으므로, 처음부터 $$\Omega \setminus A$$로 익혀두는 것이 훨씬 좋습니다.

가장 대표적인 σ-algebra가 바로 파워집합입니다. 가장 직관적이고 계산도 편리하기 때문에 매우 유용하게 사용됩니다. 반대로 가장 작은 σ-algebra도 생각해볼 수 있습니다. 이 경우, σ-algebra는 공집합과 X만을 포함하는 집합이 됩니다. 이 외에도 어떤 집합 X에 대한 σ-algebra는 여러개 존재하게 됩니다. 

### Reasoning
$$P$$에 대해서 이야기를 나누기 전에, 굳이 이렇게 어렵게 σ-algebra를 정의해가면서 확률을 이야기하는 까닭을 생각해볼 필요가 있습니다. 

쑥쓰럽지만 제가 개인적으로 확률공간을 공부하면서 가장 아름답다고 생각한 부분이기도 한데, 이 부분을 되새김질하다 보면, 우리가 상식적으로 이해하는 관념들을 간결한 언어로 표현하는 것이 얼마나 어려운 일인가를 체감하게 되기 때문인 것 같습니다.

* why the complement should be elements 

만약 우리가 어떤 사건이 발생할 확률을 알고 있다고 가정해보겠습니다. 자연스럽게 우리는 이를 어떤 사건이 발생하지 않을 확률도 알고 있는 상황과 동일하다는 것을 받아들입니다. 이를 set theory에서 가장 간결하게 표현할 수 있는 방법이 바로, complement를 활용하는 것입니다.

* why the empty set should be elements

예를 들어 일반적인 주사위를 던진다고 했을 때, 우리는 눈의 수가 7이나 0 따위의 값이 나올 확률이 없다는 것을 알고 있습니다. 마찬가지로 주사위를 던지면 무슨 값이 나올지는 모를 수 있어도, 그 값이 반드시 {1, 2, ..., 6} 사이에서 나타날 것이라는 것도 알고 있습니다. 이러한 상식을 표현하기 위해서 공집합의 여집합인 전체 sample space도 원소로 가지고 있어야합니다. 그리고 σ-algebra는 자신의 첫 번째 성질로 이를 만족하고 있습니다.

* why the union and the intersection should be elements

한 가지 사고 실험을 해보겠습니다. 어떤 random experiment의 가능한 모든 결과가 {1, 2, 3} 3가지 경우의 수 중 하나라고 하고 그 중에서 우리가 {1, 3}과 {2, 3}이 발생할 확률이 각각 $$\frac{3}{4}$$임을 알고 있다고 하겠습니다. {1, 3}이 일어날 확률이 $$\frac{3}{4}$$이라는 사실은 우리가 {2}가 일어날 확률이 $$\frac{1}{4}$$임을 알고 있다는 사실이고, 따라서 어렵지 않게 {3}이 발생할 확률이 $$\frac{1}{2}$$임을 이해할 수 있습니다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Probability-measure.svg/450px-Probability-measure.svg.png)

이처럼 sample space의 여러 원소들의 발생확률을 알고 있다면 우리는 그 교집합에 해당하는 원소가 발생할 확률을 당연히 이해하고 있는 상황입니다. (이는 union도 마찬가지가 됩니다.) 이처럼 우리가 당연히 알고 있는 결과를 σ-algebra라는 집합의 성질을 이용하면 간단하게 표현할 수 있게 됩니다. 

* incomplete information
대부분의 확률공간에서 정의되는 σ-algebra는 우리가 각각의 sample space의 값들이 무슨 확률로 일어날지를 알고 있는 상황에 맞추어져 있습니다. 예를 들어, 우리는 fair한 주사위에서는 1부터 6까지의 값들이 모두 $$\frac{1}{6}$$이라고 알고 있습니다. 이처럼 가능한 모든 정보를 이미 알고 있는 상황을 complete information이라고 정의하는데, 이때에는 해당 확률공간의 σ-algebra가 가장 큰 형태인 power set꼴에 해당합니다.

그러나 모든 상황이 그런 것은 아닙니다. 예를 들어 동전을 3번 던지는 random experiment를 생각해보겠습니다. 만약에 fair한 동전이었다면, 앞면이 나올 확률은 $$\frac{1}{2}$$ 일테니깐 우리는 총 $$2^8$$가지의 가능한 결과값들의 확률을 모두 구할 수 있었을 것입니다. 그러나 이 동전이 약간의 굴곡이 있어서 fair하지 않다고 가정해보겠습니다. 그렇게 되면 우리가 알고 있는 사실은 단 두가지 뿐입니다. 첫째, 그 결과값이 어찌되었건 {HHH, HHT, ... , TTT} 중에 하나일 것입니다. 둘째, {동전이 선다}와 같이 불가능한 사건은 결코 발생하지 않는다는 사실입니다. 이처럼 어떠한 것도 모르는 상태를 표현할 수 있는 σ-algebra가 집합 X와 공집합만을 포함하는 가장 작은 크기의 σ-algebra가 되는 것이였습니다.

그런데 마치 신의 계시라도 받은 듯, 우리가 3번 던진 동전 중에 나온 앞면의 갯수를 알고 있다고 가정해보겠습니다. 그렇게 되면 우리가 알고 있는 sample space를 다음처럼 disjoint한 union으로 새롭게 표현할 수 있습니다.

 <div align="center"> $$\Omega = B0 ⊔ B1 ⊔ B2 ⊔ B3 =$$ {HHH} ⊔ {HHT, HTH, THH} ⊔ {TTH, THT, HTT} ⊔ {TTT} </div>

이를 가리켜서 parition $$\Omega$$라고 하는데, 이 경우 σ-algebra는 $$2^4$$개의 events를 포함하는 집합이 됩니다. 즉, 적어도 B0, B1, B2, B3를 조합해서 나올 수 있는 모든 경우의 수들에 대해서는 어떠한 확률값으로 결과를 말해줄 수 있기 때문입니다.

이처럼 특정한 상황의 확률만을 알고 있을 때에도 σ-algebra를 통해서 우리는 아주 손쉽게 수리적으로 직관적인 상황들을 표현할 수 있게 됩니다. σ-algebra가 고정되지 않고 유동적으로 정의될 수 있어야하는 까닭이기도 합니다.

<br>

## $${P}$$, probability measure
<b>A function that, to every set $A \in \mathcal {F}$, assigns a number in [0, 1], called the probability of $A$ and written P(A) and having all two of the following properties.

* P($\Omega$) = 1
* countable additivity</b>  

probability measure $$P$$를 완벽히 이해하기 위해서 조금 더 그 기저의 수학적 내용을 다뤄보도록 하겠습니다.

### measurable space

실해석학에서는 (X, σ-algebra on X)를 가리켜서 measurable space라고 정의합니다. 자연히 확률공간의 ($$\Omega$$, $$\mathcal {F}$$) 역시 이에 해당합니다. 어떤 공간이 measurable space라는 점은 꽤나 중요합니다. <b>이 공간에서 우리는 σ-algebra의 (추상적인) 원소들에 real-numbered values를 부여할 수 있는 function을 정의</b>할 수 있기 때문입니다. 이러한 function을 가리켜서 set function 혹은 real-valued function이라고 부릅니다.

여기서 추상적이라고 표현했던 이유는 현재 집합 σ-algebra가 가지고 있는 원소들이 특정한 숫자값들이 아닐 수 있기 때문입니다. 예컨데, 집합 X가 sample space인 확률공간을 생각해본다면, σ-algebra의 원소들은 {동전의 앞면이 나온다, 동전의 뒷면이 나온다} 또는 {점의 갯수가 1개이다} 따위에 해당합니다. 이러한 abstract elements들에 실수값들을 부여할 수 있는 함수가 정의된다는 것을 큰 장점이 될 수 밖에 없습니다.


### measure space

이와 같은 여러 function들 중에서 아래와 같은 성질을 만족하는 function을 가리켜 특별히, <b>measure</b>라고 부릅니다. 

* Let (X, Σ) be a measurable space. A set function μ defined on Σ is called a measure iff it has the following properties.
1. 0 ≤ μ(A) ≤ ∞ for any A ∈ Σ.
2. μ(Φ) = 0.
3. σ-additivity is satisfied.

그렇게 되면, 비로소 measurable space와 measure를 합쳐서 우리는 <b>measure space</b>라고 부를 수 있게 됩니다. 마치 metric space가 정의되어 있어야지만 원소 간의 거리를 이야기할 수 있듯이 이 measure space가 정의되어 있어야 우리는 "크기(volume)"에 관해 논의할 수 있게 됩니다. 앞에서 우리가 힘들게 σ-algebra를 정의한 것이 확률에 대해서 우리가 가지고 있는 당연한 생각을 간결하게 표현하기 위였음이라고 밝혔습니다. 마찬가지로 "어떠한 것의 크기라고 하는 것이 항상 0 이상의 값을 가지며", "존재하지 않는 것의 크기는 0이다" 따위의 상식을 간결하게 표현하기 위해서는 부분집합의 집합인 σ-algebra가 필요했던 것입니다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Measure_illustration_%28Vector%29.svg/330px-Measure_illustration_%28Vector%29.svg.png)

### Probability measure
다시 돌아와서 Probability measure에 대해서 이야기해보겠습니다.  

Probability measure는 결국 measurable space로부터 만들어졌고, 일정 조건들을 만족하고 있는 set function이라고 이해할 수 있습니다. 이렇게 Probability measure까지 정의되고 나서 우리는 3가지 구성요소를 일컬어, 확률공간이라고 정의하게 됩니다.

<br>
마지막으로 첨언을 하자면, 이번 글에서는 주로 σ-algebra에 대해서 다루었습니다. σ-algebra는 단지 measure space나 probability space를 정의하기 위해서만 사용되는 개념은 아닙니다. 확률과정에서 배우는, 마팅게일(Martingales)이라는 개념과도 관련이 있고 이는 또 금융공학에서 자주 등장합니다. 이처럼 σ-algebra의 정의와 목적은 확률을 이론적으로 공부하기 위해서 뿐만 아니라 기초지식으로 반드시 이해하고 있어야할 것입니다.


<br>  

***
***
# 각주 및 추천자료

## 추천자료 
1. measure 관련 : https://www.bauer.uh.edu/rsusmel/phd/sR-0.pdf
2. Probability Space 관련 : https://en.wikipedia.org/wiki/Probability_space



## 각주


