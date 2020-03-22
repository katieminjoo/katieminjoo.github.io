---
layout: post
title: <i class="far fa-chart-bar"> [bayesian inference] blocked gibbs sampler</i>
date: 2020-03-21 16:13:00 +0800
categories: [bayesian inference, gibbs sampling]
tags: [bayesian inference]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

1.  
\documentclass{article}
\usepackage{amsmath}
\begin{document}
\begin{align*}
2x^2 + 3(x-1)(x-2) & = 2x^2 + 3(x^2-3x+2)\\&= 2x^2 + 3x^2 - 9x + 6\\&= 5x^2 - 9x + 6
\end{align*}
\end{document} 

2.  
\begin{align*}
2x^2 + 3(x-1)(x-2) & = 2x^2 + 3(x^2-3x+2)\\&= 2x^2 + 3x^2 - 9x + 6\\&= 5x^2 - 9x + 6
\end{align*}



<b>주어진 [데이터](/assets/data/posts/[gibbs-sampler]-regression-data.html)를 활용하여 다음 모형의 계수를 추정하시오.</b>  

<p align="center">$$y_i = X_i\beta+\epsilon_i$$</p>  
where $$i = {1, 2, ... N},\;\;\beta \sim {1, 2, ... P},\;\;\beta \sim N(0,\tau I)\;\;$$ and $$,\;\;\epsilon \sim N(0,\kappa I)$$
  
이때 prior distribution은 다음과 같이 설정해준다.  
<p align="center">$$\tau \sim IG(a,b)\; and \;\kappa \sim IG(c,d)$$</p>  

<br>

## Step 1. Find a proportionality
<p align="center">$$p(\beta,\tau,\kappa|Y) \propto p(Y|\beta,\kappa)\;p(\beta | \tau)\;p(\tau)\;p(\kappa)$$</p>   

<br>

## Step 2. Find each full conditional distribution
### 1. $$p(Y|\beta,\kappa)$$ 
<p align="center">$$= \prod_{i=1}^{N} \frac{1}{\sqrt{2\pi\kappa}} exp(-\frac{1}{2\kappa}(y_i-X_i\beta)^2)$$

$$= {(2\pi\kappa)}^{(-N/2)} exp(-\frac{1}{2\kappa}(Y-X\beta)^T(Y-X\beta))$$</p>    

where $$\;Y\;$$ is a set of $$\;y_i\;$$ and $$\;X\;$$ is a set of $$\;X_i$$.  

### 2. $$p(\beta | \tau)$$[^multi]
[^multi]: ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c66e6f6abd66698181e114a4b00da97446efd3c4)

<p align="center">$$= \frac{1}{\sqrt{(2\pi)^P |\tau I|}} exp(-\frac{1}{2}\beta^T(\tau I)^{-1}\beta)$$  


### 3. $$p(\tau)$$

### 4. $$p(\kappa)$$

<br>
## Step 3. Iteratively update and draw new samples with the probability in R
```r
#install.packages("invgamma")
library(invgamma)
library(MASS)

rm(list = ls())

data <- read.csv("regression_data.csv")
Y <- data$Y
X <- as.matrix(data[,2:4])
N <- dim(X)[1]
p <- dim(X)[2]

num_iters <- 10000

tau_samples <- c()
beta_samples <- list()
kappa_samples <- c()

# ======= Hyperparameters ======= #
a <- 1 ; b <- 1 
c <- 1 ; d <- 1

# ======= initial values ======= # 
beta <- rep(0,p)

for(i in 1:num_iters){
  # ======= update kappa ======= #
  kappa <- rinvgamma(1, c+N/2, t(Y - X%*%beta) %*% (Y - X%*%beta)/2 + d)
  
  # ======= update tau ======= #
  tau <- rinvgamma(1, a+p/2, t(beta)%*%beta/2+b)
  
  # ======= beta ====== #
  cov_beta <- solve(t(X)%*%X/kappa + diag(p)/tau)
  mu_beta <- cov_beta %*% t(X) %*% Y/kappa
  beta <- mvrnorm(1, mu=mu_beta, Sigma=cov_beta)
  
  # ======= collect samples ======= #
  kappa_samples[i] <- kappa
  tau_samples[i] <- tau
  beta_samples[[i]] <- beta
}
```

## results
```r
out_of_burn <- 5001:10000

hist(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[1])))
acf(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[1])))
hist(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[2])))
acf(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[2])))
hist(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[3])))
acf(as.numeric(lapply(beta_samples[out_of_burn], function(x) x[3])))
hist(tau_samples[out_of_burn])
acf(tau_samples[out_of_burn])
hist(kappa_samples[out_of_burn])
acf(kappa_samples[out_of_burn])
```


<br>  

***
***
# 각주 및 추천자료

## 추천자료 
1. https://jinwonsohn.github.io/lecture/2020/01/10/Bayesian-Inference.html
2. [손진원 선배님 PDF](https://jinwonsohn.github.io/pdfs/BI_L4.pdf) 

## 각주