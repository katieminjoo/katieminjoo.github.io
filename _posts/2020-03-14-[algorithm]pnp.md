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

[^namu]: 비전공자의 글로써 부정확하고 애매모호할 수 있습니다. 공부할 때마다 알찬 내용으로 수정해갈 예정입니다. 피드백은 언제나 환영이니 연락주시면 감사합니다.

<br>


# NP-hard problem
Pattern Recognition 학술지에 기재된 [Data clustering: 50 years beyond K-means](https://www.sciencedirect.com/science/article/abs/pii/S0167865509002323) 글을 읽다가 아래와 같은 문구를 발견했습니다.

> *Minimizing this objective function is known to be an **NP-hard problem** (even for K = 2).*

k-means 클러스터링의 local optima에 관한 내용이겠거니 하고 넘어갈 수도 있지만 사실 그렇게 어물쩍 넘어가기에는 찝찝할 수밖에 없습니다. NP-hard problem은 컴퓨터 공학에서 큰 비중을 차지할 뿐만 아니라, 그 근간이 되는 시간복잡도 등의 개념은 매우 중요하기 때문입니다.  

오늘은 이를 이해하기 위한 개념들을 차근차근 살펴보면서 감을 잡아보려합니다.

<br>

# Big-O notation
빅O 표기법은 컴퓨터 공학의 알고리즘 수업뿐만 아니라 수학 과목에서도 자주 등장하는 개념입니다. 각 학과에서 이를 정의하는 뉘앙스가 조금씩 다를 수는 있지만, 결국 그 맥락은 유사합니다. 먼저 수학 과목에서 자주 사용하는 예제를 통해 살펴보도록 하겠습니다.  
