---
title: <i class="fas fa-database"> P, NP, and NP-Completeness</i>
date: 2020-03-14 10:46:00 +0800
categories: [Programming, P versus NP problem]
tags: [Algorithm Analysis, P versus NP problem]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

> [지난 포스팅](https://haehwan.github.io/posts/algorithm-bigO/)에서는 알고리즘 분석에 필요한 개념들을 설명했습니다. 사실 이를 배우고 싶었던 것은 오늘 다룰 <b>P, NP 등의 개념</b>을 이해하기 위함이었습니다. 이번 글은 지난 포스팅의 내용을 모두 숙지했다는 상태로 진행하겠습니다.  

***

<br>

머신러닝 논문을 읽다보면 모르던 용어들을 마주칠 때가 있습니다. 알고리즘이나 자료구조와 같은 과목을 수강해본 적이 없는 저로써는 그럴 때마다 당황스러울 때가 많습니다. 오늘은 그 중에서 NP-hard problem과 이를 이해하기 위해 필요한 개념들에 대해 간단하게 적어보고자 합니다.[^namu]

[^namu]: 비전공자의 글로써 부정확하고 애매모호할 수 있습니다. 피드백은 언제나 환영입니다. 공부해가면서 알찬 내용으로 조금씩 수정해나가겠습니다.

<br>


# NP-hard problem in Data Science
Pattern Recognition 학술지에 기재된 [Data clustering: 50 years beyond K-means](https://www.sciencedirect.com/science/article/abs/pii/S0167865509002323) 글을 읽다가 아래와 같은 문구를 발견했습니다.

```terminal
*Minimizing this objective function is known to be an **NP-hard problem** (even for K = 2).*
```

k-means 클러스터링의 local optima에 관한 내용이겠거니 하고 넘어갈 수도 있지만 사실 그렇게 어물쩍 넘어가기에는 찝찝할 수밖에 없습니다. NP-hard problem은 컴퓨터 공학에서 큰 비중을 차지할 뿐만 아니라, 그 근간이 되는 시간복잡도 등의 개념은 매우 중요하기 때문입니다.  

오늘은 이를 이해하기 위한 개념들을 차근차근 살펴보면서 감을 잡아보려합니다.

<br>

# Class P/ NP
먼저 P, NP가 무엇인지부터 확인해보겠습니다.[^wiki]  아래의 정의에 포함된 polynomial time이 궁금하신 분은 [지난 포스팅](https://haehwan.github.io/posts/algorithm-bigO/)을 참고해주시기 바랍니다. 추가적으로 decision problem이란, 어떤 문제에 대한 대답이 yes와 no로 구분되는 문제를 의미합니다. 예를 들어서 "두 숫자 x와 y가 있을 때 y는 x로 나누어떨어지는가?" 라는 문제는 예와 아니오로 답이 존재하는 전형적인 결정문제에 해당합니다.

> The general class of questions for which some algorithm can provide an answer in polynomial time is called "class P"  

> NP is the set of decision problems for which the problem instances, where the answer is "yes", have proofs verifiable in polynomial time by a deterministic Turing machine.

[^wiki]: https://en.wikipedia.org/wiki/NP_(complexity)

보다 쉽게 설명드리면, 어떤 문제에 대해서 polynomial time algorithm이 존재하면 해당 문제를 P집합의 원소로 받아들이는 것입니다. 오해하기 쉬운 부분은 알고리즘이 아니라, 해당 "문제"가 P에 속한다는 것입니다. 예를 들어서 sorting하는 문제를 생각해보겠습니다. 지난 포스팅에서도 봤지만 버블 sorting은 $$n^2$$이라는 다항식으로 표현되는 시간복잡도를 가지고 있습니다. 따라서 sorting하는 문제는 polynomial time 알고리즘을 제시할 수 있으므로 P 문제에 속하게 됩니다. 추가적으로 정확한 명칭은 "deterministic" polynomial time입니다. 즉 동일한 input에 대해서 다항시간 이내에 같은 결과로 풀리는 것이 "증명"된 혹은 확실히 말할 수 있는 문제들을 의미합니다.  

반대로 NP란, "non"deterministic polynomial time을 의미합니다. 그런데 사실 비결정적 알고리즘이란 것은 이해하기가 쉽지 않습니다. 같은 input에 대해서 다른 결과값이 나오는 알고리즘은 직관적이지가 않기 때문입니다. 다행히도 NP에 대한 또 다른 정의를 이용할 수가 있는데 이는 다음과 같습니다.  

> 문제가 주어지고, 해당 문제에 대해 어떤 <b>suggested solution</b>이 주어졌을 때, 다항시간 안에 그 solution이 맞는지 아닌지 구분할 수 있는 문제.  
>> NP에 대한 두 정의는 표면상 달라보이지만 사실 둘은 같은 의미를 가집니다. 이에 대한 설명은 계산 복잡도 이론에 대한 공부가 더 필요한 것으로 보여집니다. 이번 글에서는 두 정의가 동일함을 받아들이고 글을 이어나가겠습니다.

NP에 대한 위의 정의를 예를 들어서 설명하도록 하겠습니다. 해당 예시는 [이 곳](https://zeddios.tistory.com/92?category=682196)의 블로그에서 사용한 예제입니다.  

다리 건너에 보물이 가득한 섬이 있습니다. 보물들은 각각의 무게와 값어치가 표시되어 있으며, 여러분은 이를 가져올 수 있는 가방도 가지고 있습니다. 그런데 두 가지 제약 조건이 있습니다. 첫째 다리가 버틸 수 있는 무게가 100kg입니다. 둘째 가지고 와야할 보물의 값어치가 반드시 2억 이상이어야합니다. 만약 위의 조건을 모두 만족한 채 보물을 챙겨서 가지고 나올 수 있을까요?

이러한 문제는 역시 결과가 yes와 no로 나뉘기 때문에 결정문제에 속합니다. 만약 이를 풀 수 있는 유일한 알고리즘이 전체 N개의 보물을 조합해가면서 제약 조건을 만족하는 보물을 일일이 찾아내는 방법뿐이라고 가정을 해보도록 하겠습니다. 각각의 보물들을 가방에 넣었다가 뺐다를 반복하는 위의 알고리즘은 전체 가지수 N으로 인해 $$2^N$$의 조합 갯수를 가지게 되고, 따라서 $$O(2^N)$$의 시간복잡도를 갖습니다. 따라서 N이 조금이라도 커지게 되면 running time은 걷잡을 수 없이 오래 걸리는 알고리즘을 가지는 문제가 됩니다.  

그렇지만 이 문제는 누군가 solution을 추천해준다면 아주 빠르게 처리가 가능합니다. 예를 들어 누군가가 가방에 담을 보물이 적힌 종이(suggested solution)를 줬다고 생각해봅시다. 만약 그렇다면 우리가 할 일은 suggested solution대로 가방에 담은 뒤에 보물들의 값어치와 무게를 누적합하면 됩니다. 당연히 다항시간 안에 누적합을 할 수 있으며, 그 결과로 손쉽게 해당 조합이 문제의 정답이 되는지 아닌지를 구분할 수 있게 됩니다. 따라서 결론적으로 이 문제는 NP 집합에 분류할 수 있게 됩니다.  

## subset


따라서 NP문제들은 다음 세가지 경우의 수 중에 한 가지에 속할 것입니다.
> 1. 다항시간 안에 풀릴 수 있음.  
> 2. 다항시간 안에 풀릴 수 없음.
> 3. 증명할 수 없음.

그리고 바로 이를 전체 NP 문제들에 대해서 확장한 것이 그 유명한 P-NP 문제입니다. 이는 밀레니엄 문제(Millennium Prize Problems) 중 첫 번째 문제로, "NP의 모든 문제들을 P 집합으로 표현할 수 있느냐"에 관한 문제입니다. 만약 두 집합이 같음을 증명할 수 있다면 우리는 모든 NP 문제들을 다항식 시간 내에 풀릴 수 있는 알고리즘으로 바꿀 수 있게 됩니다. 이러한 중요도를 생각해보면 21세기 사회에 가장 크게 공헌할 수 있는 난제로 괜히 선정된게 아님을 느낄 수 있습니다.

# 

<br>  

***
***
# 각주 및 추천자료

## 추천자료 
1. 


## 각주



