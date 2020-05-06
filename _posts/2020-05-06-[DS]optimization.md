---
title: <i class="far fa-chart-bar"> Optimzation</i>
date: 2020-05-06 20:45:00 +0800
categories: [Data Science, Machine Learning]
tags: [Machine Learning, Otimization]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---

<br>

# Optimization

문제를 해결하거나 관심있는 모수를 추정할 때, 통계적 분석을 크게 필요로 하지 않는 경우가 꽤 많습니다. 예를 들어 손글씨를 디지털 텍스트로 변환하는 문제는 모로 가든 "정확하게" 맞추기만 하면 되는 문제이지, 작동원리라든가 추정에 필요한 모수의 성질은 큰 관심을 가지지 않습니다. 이러한 경우 핵심은 상황에 맞는 목적함수를 세우고 이를 <b>최적화</b>하는 일에 있습니다.

대부분 목적함수는 에러/비용이거나 정확도/이윤입니다. 이 경우 최적화는 각각 maximize 혹은 minimize가 됩니다. 그리고 두 문제는 부호를 바꿔주기만 하면 완전히 같은 상황으로 볼 수 있습니다. 물론 GAN과 같이 두 개의 서로 다른 모델을 동시에 학습하는 경우, 최적화는 minimax가 됩니다. 하지만 이 경우에도 결국 Jensen-Shannon divergence를 최소화하는 문제로 치환해서 푼다는 것을 [지난 포스팅](https://haehwan.github.io/posts/DS-GAN/)에서 확인한 바있습니다.

결론적으로, 대다수 문제에서 minimize를 통한 최적화가 얼마나 빨리, 얼마나 정확히 이뤄지는가가 핵심이라고 할 수 있습니다. 오늘은 이러한 알고리즘들 중에서 몇 가지를 소개하려고 합니다.

<br>

# Gradient Descent

가장 유명한 최적화 알고리즘입니다. 좋은 설명을 여러 곳에서 쉽게 접할 수 있으므로 핵심만 언급하고 넘어가도록 하겠습니다.

![위키 GD](https://wikimedia.org/api/rest_v1/media/math/render/svg/26a319f33db70a80f8c5373f4348a198a202056c)

1. 하이퍼파라미터($$\lambda$$)를 지정해주어야합니다.
2. minimum 값에서 급격히 무뎌집니다.

1번, $$\lambda$$는 한번에 얼만큼 내려올 것인가를 정하는 step size로 생각할 수 있습니다. 만약에 임의의 점에서 기울기가 어느 방향이든지간에 가파른 상태라면, 아무리 반복을 해도 수렴하지 못하게 됩니다. 오히려 반복을 할수록 실제 local minimum에서 멀어지는 일까지 발생할 수 있습니다. (통계학적으로 말한다면, 피셔정보량이 크기 때문에 계산하기 좋은 비용함수 -optimum에서 첨도가 작은 함수- 임에도 불구하고 오히려 값을 찾지 못하는 경우라고 할 수 있겠네요.)

![](https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-24-at-11.47.09-AM.png)

2번은 꽤나 중요한 문제입니다. gradient descent는 1차 미분을 활용하기 때문에 local minimum 근처에서 미분값이 0에 가까워집니다. 따라서 그 전까지 잘 내려오다가 정작 minimum 근처에서는 매우 조심스럽게 내려오는 태도를 보인다고 할 수 있습니다. 만약 첨도가 큰 함수라면, 답을 찾아내기 위해서 많은 반복시행을 요구하게 됩니다.

두 문제 모두, 비용함수의 첨도와 관련이 되있습니다. 첨도가 큰 함수라면, minimum 근처에서 수렴하기 어렵기 때문에 step-size가 커져야할 것입니다. 반대로 작은 함수라면 큰 step-size가 발산을 일으킬 수도 있기 때문에 조심해야합니다. 물론 이러한 논의는 가능한 모든 범위 안에서의 목적함수 모양을 모두 알고 있다는 가정 하에서 적절한 step-size를 추정하는 일이 될 것입니다. 결국 하이퍼파라미터를 사용자가 정해야한다는 점에는 여전히 큰 단점을 가지고 있는 것은 분명합니다.

물론 이를 위한 해결방법이 많이 연구되었습니다. 대표적으로 line search 방법을 활용한, backtracking line search나 golden section search 방법 등이 있습니다.

<br>

# Newton's Method in optimization

미적분학에서 뉴턴법과 최적화이론에서 뉴턴법은 서로 다른 의미를 가집니다. 먼저 일반적인 뉴턴법은 테일러 급수를 활용해서 함수의 근(root)을 찾을 때 사용하는 최적화 방식입니다. 따라서 미분가능한 연속함수가 x축과 만나는 지점을 찾기 위해 반복적으로 근을 찾는 방식이라고 생각할 수 있습니다. 이 경우 여전히 일계도함수까지만 활용함을 아래 식에서 확인할 수 있습니다.

![](https://upload.wikimedia.org/wikipedia/commons/b/b9/Newtons_method_x2.png)

함수의 최솟값을 찾아야하는 최적화 이론에서는 이를 살짝 다르게 적용합니다. 어떠한 minimum 값이든 반드시 기울기가 0입니다. 만약 함수의 값이 0이 되는 x를 구하는 방정식이 아니라, 함수의 기울기가 0이 되는 x를 찾는다면, minimum 값을 찾을 수 있게되는 것입니다. 즉, 미적분학의 뉴턴법을 한번씩 더 미분해줌으로써 간단히 해결할 수 있습니다. 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/90e32b708ca17d5659fdc482fe3c9f88996361ba)

![](https://www.researchgate.net/profile/Martin_Siggel/publication/263553090/figure/fig2/AS:669437170552833@1536617667054/Illustration-of-Newtons-method-in-optimization-Figure-a-compares-the-convergence-of.png)

자세한 내용이 가장 잘 나와있는 곳은 [위키피디아](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)이지만, 핵심적인 내용만 간추려보면 아래와 같습니다.

1. 이계도함수를 활용한다.
2. 하이퍼 파라미터가 없다.
3. minimum 근처에서도 빠르게 수렴한다. 

앞선 gradient descent 방법을 모두 해결한 것처럼 보이지만, 사실 이 또한 불완전한 알고리즘입니다. 여라가지 단점이 있습니다.

1. 두 번 미분가능해야한다.
2. 변곡점 또는 이와 유사한 값이 존재해서는 안된다.
3. 극대와 극소의 구분이 어렵다.

사실 neural network와 같이 선형결합을 여러번 반복하는 많은 모델들은 거의 대다수 두 번까지 미분이 가능합니다. 중요한 점은 변곡점이나 이와 유사한 값이 존재할 때에는 분모에 들어가는 값이 0 혹은 0에 가까운 값이 되면서, 정의되지 않거나 발산하는 문제가 발생한다는 점입니다. 다변수인 경우로 확장하면, [saddle point(안장점)](https://en.wikipedia.org/wiki/Saddle_point)가 존재할 때라고 생각할 수 있습니다. 물론 gradient descent 방법은 분모 형태가 없기 때문에 이러한 문제에서 자유롭습니다. 

![](https://www.researchgate.net/profile/Razvan_Pascanu/publication/263011979/figure/fig1/AS:614085020352522@1523420686891/Behaviors-of-different-optimization-methods-near-a-saddle-point-for-a-classical-saddle.png)

3번 문제도 꽤 중요합니다. 고등학교 때 삼차함수를 미분해보면 알 수 있듯이 일계도함수의 근은 극대와 극소 모두에서 존재합니다. 이는 다시 말해, 내가 찾은 값이 엉뚱하게 local maximum이 될 수도 있다는 이야기입니다. 이 때문에 newton's method는 초기 시작점을 여러군데 사용해야합니다. 또는 이를 보완하는 다양한 방식들(trust region 방법)이 존재합니다. 아니면 애초에 목적함수가 strongly convex function임을 밝히고 사용하는 경우도 더러 논문에서 찾아볼 수 있습니다. 

# Gauss-Newton method
앞선 최적화를 위한 뉴턴법 중에서도 목적함수가 least square 꼴일 때 사용하는 최적화 방법입니다. 



<br>  

***
***
# 각주 및 추천자료

## 추천자료 
1. [Generative Adversarial Networks (Ian J. Goodfellow)](https://arxiv.org/abs/1406.2661)  
2. [Backpropagation1 (3BLUE1BROWN SERIES)](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3. [Backpropagation2 (Haehwan Lee)](https://haehwan.github.io/assets/data/posts/[DL]backpropagation.html)


## 각주


<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
