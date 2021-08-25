---
title: <i class="far fa-chart-bar"> Variational Inference </i>
date: 2020-05-24 16:09:00 +0800
categories: [Statistics, Bayesian]
tags: [Variational Inference]
toc: true
comments: true
sitemap:
  changefreq: daily
  priority: 1.0
---

Variational Inference는 Approximate Inference를 수행하기 위한 방법론입니다. 이번 포스팅에서는 Variational Inference와 관련된 주요 내용들을 알아보겠습니다.

# Bayesian Statistics

베이즈 통계학은 Approximate inference를 가장 깊이 연구하는 학문 중 하나입니다. 실제로 Variational Inference 또한 베이즈 통계학에 뿌리를 두고 있다고 말할 수 있습니다. 그래서 간단히 베이즈 통계학에 대한 이야기부터 시작하려고 합니다.

통계학에서는 <b>모수를 추정하는 방식</b>에 따라 두 가지 학파가 있습니다. 빈도주의 통계학에서는 모수를 상수로 취급합니다. 반면, 베이지안은 이를 확률변수로 다룹니다. 사소해 보이지만 어떠한 관점을 취하냐에 따라서 상당히 큰 차이가 만들어집니다. 예를 들어, 누군가 주사위에서 숫자 1이 나올 확률을 물어본다고 가정하겠습니다. 우리가 가지고 있는 데이터는 동일한 주사위를 6번 던져서 1이 2번 나왔다는 사실만을 알고 있습니다.

만약 이 확률을 상수로 취급한다면, 우리가 대답할 수 있는 모수에 대한 추정은, MLE(Maximum likelihood estimator)가 가장 대표적입니다. MLE는 모수에 대한 추정값으로, 지금 가지고 있는 데이터가 나타났을 확률을 가장 크게 만들어주는 $$\theta$$를 선택합니다. 간결히 말하면, $$P(X \mid \theta)$$를 최대화해주는 $$\hat{\theta}_{mle}$$를 찾아내는 것이 핵심이라고 할 수 있습니다. 만약 위의 문제 속 확률변수(주사위를 던졌을 때, 1이 나오는 사건)가 binomial distribution을 따른다면, 빈도주의자들은 1/3을 정답으로 생각합니다.

반면에 베이지안은 모수를 확률변수라고 생각하기 때문에, 똑같은 질문에 대한 답을 "분포"로 생각합니다. 위의 문제 같은 경우에는, 확률이 모수이므로 0과 1 사이의 범위에서 정의된 분포로 대답을 할 것입니다. 예를 들어서, 모수(주사위 1이 나올 확률)가 1/3일 확률이 0.5, 2/3이 0.25, 1/6이 0.25라고 대답하는 식입니다. 그리고 이 대답은 같은 베이지안이라고 할지라도 연구자에 따라 다양하게 나타납니다. 예를 들어, 누군가는 1/3에서 굉장히 높은 값을 가지는 분포로, 다른 누구는 데이터와 상관없이 0과 1 사이에서 평평한 uniform 분포로 답변할 수 있습니다. 단 이 때에, 내가 제시한 답안이 오직 <b>Bayes' Rule(Bayes' theorem)</b>을 만족만 하고 있으면, 어떠한 대답도 정답이 될 수 있습니다. 요약하면 이들은 <b>$$P(\theta \mid X)$$</b>를 찾아낸다고 말할 수 있습니다. 그리고 이를 가리켜, posterior 분포라고 이야기합니다.

다양한 대답이 나오는 이유는, 베이지안의 큰 장점 중 하나인 직관성과 관련이 깊습니다. 이를 위해서는 posterior 분포를 prior distribution, likelihood 그리고 normalizing constant에 대한 식으로 재구성할 필요가 있습니다. 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/87c061fe1c7430a5201eef3fa50f9d00eac78810)

위의 식을 통해서 우리는 베이지안들이 사실은, 빈도주의자들이 구했던 likelihood에 더해서, prior 분포와 정규화 상수를 계산한다는 것을 알 수 있습니다. 앞에서 베이지안의 정답이 여러 개가 가능한 이유가 사실 바로 이 prior 분포 때문입니다. prior 분포란, 주어진 데이터와 무관하게 연구자가 모수에 대해서 가지는 확률분포라고 이야기할 수 있습니다. 예를 들어, 주어진 정보를 많이 신뢰하는 사람이 있을 수도 있지만, 반대로 이전에 본인이 알고 있던 지식에 더 큰 비중을 두는 사람이 있을 수도 있습니다. 전자의 경우가 주사위 예시에서 1/3에서 뾰족한 분포를 정답으로 생각하게 되고, 만약 후자의 사람이 주사위가 매우 공정하다는 믿음이 있다면 0과 1의 모든 값에서 평평한 확률 분포를 도출해낼 것입니다. 이처럼 베이지안은 연구자의 믿음이나 지식에 따라서 다양한 분포가 나온다고 할 수 있습니다.

어느 관점이 더 합리적이고 유용한가는 연구자에 따라 다르겠지만, 베이지안은 빈도주의자에 비해 직관적이고, 설명력을 가지며, 정보의 업데이트가 편리하다는 큰 장점을 가지고 있음을 알 수 있습니다. 조금 더 자세하고 친절한 내용은 [이 곳](https://www.youtube.com/watch?v=OZJoBK2slOA)에 잘 나와있습니다. 

# Approximate Inference

이러한 뛰어난 장점에도 불구하고, 베이즈 정리에서 알 수 있듯이, 베이즈 통계학에는 빈도주의자보다 필요로 하는 계산식이 더 많습니다. 특히 그 중에서 문제가 되는 것은, normalizing constant입니다. conjugate prior를 사용하는 몇몇의 경우를 제외하고 대다수 문제에서 <b>normalizing constant를 구하는 것이 불가능</b>합니다. 사실 normalizing constant, $$P(X)$$는 $$$\int_{\mathcal{theta}} \mathbb{P}(\theta, X) d\theta$$입니다. 즉, X와 $$\theta$$의 joint 분포에서 $$\theta$$를 marginal out한 값인데, 이 $$\theta$$가 사실은 미지의 분포이기 때문에 이를 구하는 과정이 어려워지게 되는 것입니다. 그리고 이 때문에 특히 posterior 분포를 바탕으로 조건부 평균이라든가 분산 혹은 확률과 같은 특정 '값'들을 의논하는 것도 더욱 큰 난관에 봉착하게 됩니다. 조금 더 자세히 살펴보겠습니다.

우선 베이지안은 posterior 분포에 관심을 갖기 때문에, 평균과 분산과 같이 특정 '값'에 대해서 말할 때에도, 주어진 데이터를 조건으로 하는 값들에 대해서 관심을 갖습니다. 그리고 이들은 아래와 같은 과정으로 요약해서 구할 수가 있습니다. 

$$\mathbb{E}[h(theta \mid X)] = \int_{\mathcal{theta}} X \mathbb{P}(\theta \mid X) d\theta$$

여기서 만약 h 함수가 identity 함수라면, 이는 평균값을 의미합니다. 또는 $$\theta-\mu_{theta}$$라면 분산이, 혹은 $$I(\theta > a)$$와 같은 indicator 함수라면 확률로도 이해할 수 있습니다.

당연히 이 적분은 가능한 모든 $$\theta$$의 공간인 '$$\mathcal{\theta}$$'에서 수행되어야합니다. 하지만 위에서와 같은 이유로 이 적분은 무척 어렵습니다. 이 때문에 결국 분포를 계산하는 일도, 분포의 평균과 분산을 구하는 일도 어려움에 도달하게 됩니다. 이렇듯 posterior 분포를 정확히 계산하기가 어렵기 때문에 근사적인 방식으로 이를 해결해야합니다. 그리고 이러한 과정을 가리켜서 <b>approximate inference</b>라고 부릅니다. 다행히도 이를 해결하는 시뮬레이션이나 최적화 방법들이 컴퓨터 성능의 발달로 구현이 가능해지면서, 최근에 비약적인 성과를 보이고 있습니다.

## Markov Chain Monte Carlo

가장 대표적인 해결방법이 샘플링 혹은 stochastic 방식입니다. 그리고 그 유명한 Markov Chain Monte Carlo(MCMC)가 바로 이 범주에 속하는 샘플링 기법입니다. 오늘은 VAE에 대한 내용을 다루기 때문에 핵심적인 내용만 살펴보겠습니다. 먼저, 출발점은 우리가 Law of Large numbers(대수의 법칙)을 활용하여 위의 식을 아래처럼 바꿀 수 있다는 사실에 있습니다.

$$\int_{\mathcal{X}} X \mathbb{P}(X|Y) dX \sim \frac{1}{N} \sum_{i=1}^N X_i$$

이러한 방법을 가리켜서 Monte Carlo라고 부릅니다. 단순히 샘플을 구하고 그것의 평균으로 계산하는 일은 매우 강력한 해결방법입니다. 하지만 한 가지 조건이 있습니다. 이를 위해서는 반드시 <b>posterior분포로부터 구해진 iid 샘플</b>, $$X_i$$들이 필요하다는 점입니다. 그런데 사실 [샘플링은 그리 쉬운 일이 아닙니다.](http://www.secmem.org/blog/2019/01/11/mcmc/) 실제로 우리가 샘플링할 수 있는 분포도 몇 개 없을 뿐더러, 위에서 말했듯이 posterior 분포 자체가 복잡하기 때문에 이로부터 샘플을, 그것도 '독립적'으로 뽑아내기 위해서는 또 다른 해결책이 필요합니다.

이를 해결하는 방법이 MCMC 알고리즘입니다. 조금 더 쉽게 이야기하면, Markov Chain을 활용한 샘플링이라고 할 수 있습니다. 당연히 Markov Chain을 이해하는 것이 중요합니다. 이 부분은 [이 곳](https://www.youtube.com/watch?v=pAWc8BCUHlo)의 영상으로 대체하겠습니다. 요약하면, 우리가 정확한 posterior 분포를 모른다고 할지라도, transition probability를 잘 정의해줌으로써 stationary distribution로부터 posterior 분포를 구할 수 있다는 점입니다. 여기서 stationary distribution은 posterior와 비례관계에 있는, prior와 likelihood의 곱으로 이루어진 분포입니다. transition probability를 정의하는 방법은 대표적으로 <b>Metropolitan-Hasting Algorithm</b>이 있습니다. 워낙 중요하기도 하고, 활용분야도 많다보니, 다음 기회에 더 자세히 다루도록 하겠습니다.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Metropolis_algorithm_convergence_example.png/420px-Metropolis_algorithm_convergence_example.png)

## Variational Inference

그리고 또 다른 대표적인 방법이 Variational Inference입니다. 앞에서 잠깐 언급했던, MCMC가 독립적인 샘플링을 할 때에, 마치 순열값들을 쓰듯이, 확률 과정(stochastic process)을 통해서 posterior 분포로 수렴했다면, VI는 deterministic 방법이라고 말할 수 있습니다. 이를 이해하기 위해서는 MCMC와 비교를 통해서 감을 빨리 잡을 수 있습니다.

앞에서 MCMC는 결국에는 posterior 분포로 완벽히 수렴해갈 수 있음이 증명되어있습니다. 물론 몇 가지 가정을 만족해야하지만, starting point를 여러개 잡기만 한다면, 이러한 가정은 쉽게 대체될 수 있습니다. 정확한 값을 추론할 수 있지만 당연히 단점은, 많은 계산량을 수반한다는 점입니다. 자연히 비교적 작은 크기의 문제를 해결하는데 초점이 맞춰지게 됩니다.

반면에 VI는 처음부터 posterior 분포를 근사적으로 구하고자 합니다. 애초에 정확한 값을 추론하는 것이 아니라, 내가 잘 다룰 수 있는 어떠한 분포로 대체해서 표현하는 것이기 때문에 계산량과 속도측면에서 훨씬 우월합니다. 따라서 차원이 높고 연산이 많이 필요한 문제에서 응용 가능합니다.

또 한 가지 장점은 VI는 문제 유형을 바꿔준다는 점이 있습니다. 앞에서 말했듯, VI는 내가 잘 아는 여러 분포들 중에 실제 posterior 분포와 가장 근사한 분포를 찾아서 이를 대신해서 사용합니다. 대체해서 쓰는 분포가 실제 분포와 유사해야하기 때문에 이 때에는 divergence를 활용해서 분포 간의 차이를 나타내게 됩니다. divergence란, distance와 유사한 개념으로 생각하면 됩니다. 일종의 차이를 표현하는 수단입니다. 중요한 점은 이렇게 divergence로 분포와 분포 사이의 차이를 나타낸 뒤에, 이를 최소화하는 분포를 찾는다는 것입니다. 결국, 위 문제는 최적화 알고리즘 문제로 바뀝니다. 이 때문에 VI가 속도 측면에서 훨씬 강점이 있다고 할 수 있습니다.

![](https://charlesmartin14.files.wordpress.com/2017/09/kl-div.png?w=600&h=358)

그렇다면 보다 구체적으로 Variational Inference는 어떻게 작동하는지 차근차근히 살펴보겠습니다.

# Variational Transform

non-linear한 복잡한 함수를 조금 더 단순한 함수로 바꿔주는 것을 의미합니다. 대표적으로 

<br>  

***
***
# 각주 및 추천자료

## 추천자료 / 참고자료
1. [Variational Inference](https://calculatedcontent.com/2017/09/06/free-energies-and-variational-inference/)

2. [카이스트 문일철 교수 기계학습 강좌영상](https://www.youtube.com/watch?v=4w1lidx6mV4&list=PLbhbGI_ppZIRPeAjprW9u9A46IJlGFdLn)

## 각주


<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
