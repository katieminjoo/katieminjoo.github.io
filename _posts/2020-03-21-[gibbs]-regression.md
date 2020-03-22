---
layout: post
title: <i class="far fa-chart-bar"> [bayesian inference] blocked gibbs sampler</i>
date: 2020-03-21 16:13:00 +0800
output: 
  rmarkdown::html_vignette:
    fig_width: 4
    toc: true
    toc_depth: 2
vignette: >
  %\VignetteIndexEntry{Recoding addins}
  %\VignetteEngine{knitr::rmarkdown}
  %\VignetteEncoding{UTF-8}
categories: [bayesian inference, gibbs sampling]
tags: [bayesian inference]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>  

# 



# Code and result
위에서 사용한 데이터를 생성한 과정은 [이 곳](/assets/data/posts/[gibbs-sampler]-regression-data.html)에서 확인하실 수 있습니다.

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
