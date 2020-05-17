---
title: <i class="far fa-chart-bar"> [Paper review] NIPS 2016 Tutorial:Generative Adversarial Networks</i>
date: 2020-04-11 10:21:00 +0800
categories: [Data Science, Machine Learning]
tags: [Machine Learning, GAN]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---

<b>NIPS</b>(Neural Information Processing Systems)는 AI 연구자들에게 가장 각광받는 행사로, 그 해의 의미가 큰 논문을 발표하고 의견을 나누는 행사입니다. 2016년에는 이안 굿펠로우가 자신이 처음 소개한 GAN에 관하여 발표를 진행했었습니다. 이 글에서는 arXiv에 제출된 <b>[NIPS 2016 Tutorial:Generative Adversarial Networks](https://arxiv.org/pdf/1701.00160.pdf)</b> 글을 리뷰합니다. generative modeling부터 GAN의 자세한 메커니즘까지 이해하고 공부해보겠습니다.

# Generative models

일반적으로 Generative model은 주어진 샘플들이 따르고 있는 미지의 분포($P_{data}$)를 표현하기 위해 사용합니다. 이를 표현하는 방법은 크게 두 가지가 있습니다. 직접적으로(explicitly) $P_{data}$를 구하는 것도 방법이지만, $P_{data}$를 따르는 샘플들을 계속해서 만들어냄으로써 이를 표현하기도 합니다. 예를 들어 대한민국 남성 키에 대한 일부 자료가 있다고 생각해보겠습니다. 이 데이터를 가지고 정규분포 식을 만들었다면 이는 explicit하게 $P_{data}$를 표현한 것입니다. 하지만 그렇게 하지않고, $P_{data}$ 분포를 따르는 새로운 변수들을 계속해서 뽑아낸다면, 이 역시도 분포를 표현하는 하나의 방법이 될 수 있습니다.

* <b>Generative models:</b> any model that takes a training set, consisting of samples drawn from a distribution $p_{data}$, and learns to represent an estimate of that distribution somehow.


# Why generative modeling is worth studying.

물론 $P_{data}$를 표현할 때에는 explicit하게 나타내는 것이 좋습니다. 만약 우리가 대한민국 남성들의 키를 정규분포로 추정했다면, 단 두 가지 모수(평균과 분산)로 키에 대한 모든 정보를 대체할 수 있기 때문입니다. 

그러나 데이터를 generate하는 것만 가능할지라도, 이는 다음과 같은 이유로 매우 중요합니다.

1. high-dimensional probability distribution
high-dimensional probability distribution은 많은 응용수학과 공학에서 매우 중요한 주제입니다. generative model을 학습시키고 샘플링하는 일이 이런 고차원 확률분포에 대한 검정을 해줄 수 있습니다.

2. reinforcement learining
generative model은 특히 모델 기반의 강화학습에 큰 도움을 줄 수 있습니다. 예를 들어, 시계열 데이터에 대한 generative model은 가능한 결과값들을 시뮬레이션함으로써 조건부 기대분포를 구하는데 활용될 수 있습니다.

3. semi-supervised learning
최근 딥러닝 알고리즘이 잘 작동하기 위해서는 기본적으로 라벨링이 되어 있는 트레이닝셋이 존재해야합니다. 이 때문에 실질적으로 적용가능한 경우는 많지 않을 수 있습니다. 하지만 generative model은 결측치가 있는 데이터로 학습이 가능하기 때문에, 만약 input 데이터가 결측치를 가지고 있더라도 예측을 해낼 수가 있습니다. 이 때문에 generative model을 잘 활용하면, semi-supervised learning이 가능해집니다.

4. multi-modal outputs
전통적인 머신러닝에서는 하나의 인풋에 대해서 하나의 결과값이 나오게끔 학습합니다. 하지만 하나의 인풋에 대한 정답이 반드시 하나만 존재하지 않는 경우도 많습니다. 대표적으로 동영상에서 다음 장면을 예측하는 일은 여러 개의 복수 정답이 존재하는 문제입니다. 이처럼 multi-modal한 결과값을 다루기에 generative model, 특히 GAN이 잘 작동합니다.

![](/assets/img/post/[DS]Generative/video frame.png)

5. realitic generation of samples
마지막으로 실제로 어떤 분포로부터 샘플을 만들어내는 일이 필요한 경우가 굉장히 많습니다. 대표적으로 single image super-resolution이 있습니다.<br>  

***
***
# 각주 및 추천자료

## 추천자료 


## 각주


<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
