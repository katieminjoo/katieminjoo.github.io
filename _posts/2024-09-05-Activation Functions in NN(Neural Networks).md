---
title: <i class="far fa-chart-bar"> Activation Functions in NN(Neural Networks) </i>
date: 2024-09-05 20:00:00 +0900
categories: [DeepLearning]
tags: [deeplearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
## What is activation Function?

Basically it converts all the sum of inputs into output. It’s like a convert machine which helps to describe data with nonlinearity

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdv81N9o3hzl9pmGlGViNmr7a2uEbxxf_Mxv7qroZbjYkhqO-2DdeqX8ExG98tEKuYPijiX_InlA5QGWwzlN4oObjoYk2VxLeIARqAicqoAo931yOnuICZL-sjtYC3VVn8V1RuLPX6k5A78y1iz6meRFgnB?key=HXuWbznUo3eoIGhGB3eU2A](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdv81N9o3hzl9pmGlGViNmr7a2uEbxxf_Mxv7qroZbjYkhqO-2DdeqX8ExG98tEKuYPijiX_InlA5QGWwzlN4oObjoYk2VxLeIARqAicqoAo931yOnuICZL-sjtYC3VVn8V1RuLPX6k5A78y1iz6meRFgnB?key=HXuWbznUo3eoIGhGB3eU2A)

## Why do we use it?

It is used to determine the output of neural network like yes or no. It maps the resulting values in between 0 to 1 or -1 to 1 depending upon the function you select to use.

The Nonlinear Activation functions are the most used activation functions that makes easy for the model to generalize or adapt with variety of data and to differentiate between the output.

- without Activation func : Linear & Simple Prediction
    
    Linear Activation function : Impossible to execute backpropagation
    
    - when the function is defined as c(x), even though we put bunch of hidden layers on top of each layers, the output will be always c`(x)
- With Activation func : nonlinear & complex prediction available

And there are 6 mostly used Activation Function from sigmoid to Relu. Let’s dig in!

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzJTkuTbmc-HyuvoxGx2UUT7XOkvg3k-LWVbHrymuw1sD1h69zEr00ftyU_faeffvHPKKuxk6Om-oJYzy9wpcgvoXx773YQEF64PTLV2J0sbro2wugBeWM3Bcg7Xhpnk8bz_UuxEIXH4OWrbIZ8IR9NXiv?key=HXuWbznUo3eoIGhGB3eU2A](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzJTkuTbmc-HyuvoxGx2UUT7XOkvg3k-LWVbHrymuw1sD1h69zEr00ftyU_faeffvHPKKuxk6Om-oJYzy9wpcgvoXx773YQEF64PTLV2J0sbro2wugBeWM3Bcg7Xhpnk8bz_UuxEIXH4OWrbIZ8IR9NXiv?key=HXuWbznUo3eoIGhGB3eU2A)

## 1. Sigmoid Function

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFNRl2RVU_uKmSUNknipYd3-MKvIRqUbanJzj-v82LxdD6jX0wpMCPqZpIWzUTYffL07leFgrBvzwWUGoxIWcxDCOzxFBuB67VmuX2jPZoe0-lW2NPRYWML0EZEg42nWWfwzFI-aTvJf_C8CZdKcvfbUNB?key=HXuWbznUo3eoIGhGB3eU2A](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFNRl2RVU_uKmSUNknipYd3-MKvIRqUbanJzj-v82LxdD6jX0wpMCPqZpIWzUTYffL07leFgrBvzwWUGoxIWcxDCOzxFBuB67VmuX2jPZoe0-lW2NPRYWML0EZEg42nWWfwzFI-aTvJf_C8CZdKcvfbUNB?key=HXuWbznUo3eoIGhGB3eU2A)

Is it especially used for models where we have to predict the probability as an output. (Because probability of anything exists only between the range of 0 and 1!)

(The shape itself is same with the Logistic Function but it ranges between 0 and 1)

Softmax Function is a more generalized logistic activation function which is used for multiclass classification while sigmoid is used for binary classification tasks.

🔀 0 ~1

👍

👎 But they have several problems.

1. Saturated neurons kill the gradients
2. Sigmoid outputs are not zero-centered.
3. exp() is a bit compute-wise expensive.

## 2. Tanh / Hyperbolic Tangent Activation Function

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYy2GTmxp9hGuJQwa36b1nzgBUWtpKMW-LG1zZBbHaRNaeYvwDSoWryf7b1_PFZzxjnOK9_fPr4U4ZM0dXOVUon1UPPTmNd60jrmaBnCFtFdvLQ93ikZS8uJ-5V0Us4TwfdgFTldTZrpOojsNRziS--HY?key=HXuWbznUo3eoIGhGB3eU2A](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYy2GTmxp9hGuJQwa36b1nzgBUWtpKMW-LG1zZBbHaRNaeYvwDSoWryf7b1_PFZzxjnOK9_fPr4U4ZM0dXOVUon1UPPTmNd60jrmaBnCFtFdvLQ93ikZS8uJ-5V0Us4TwfdgFTldTZrpOojsNRziS--HY?key=HXuWbznUo3eoIGhGB3eU2A)

Tanh is also like logistic sigmoid but the range of it is different.

This is also mainly used to classify between two classes.

🔀 -1 ~ 1

👍the negative inputs will be mapped strongly negative and the zero will be mapped near zero ( zero-centered?)

👎 But it still kills gradients when saturated.

## 3. ReLU (Rectified Linear Unit) Activation Function

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdm02fwz-0sQ6UqFZSbr0DtJxhjHX7XnTvNolJ8-wyxTkpBARx3HXDqtG6NgZBVADIE3b-jJ_4yqNPtwwsBE0ef10Ap2WmS9A9u_g1v8FsAi7dmwQ3nF_kroLQH06xeVFH_0x3hUXb_e1c7IB6u-mQnB4Q?key=HXuWbznUo3eoIGhGB3eU2A](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdm02fwz-0sQ6UqFZSbr0DtJxhjHX7XnTvNolJ8-wyxTkpBARx3HXDqtG6NgZBVADIE3b-jJ_4yqNPtwwsBE0ef10Ap2WmS9A9u_g1v8FsAi7dmwQ3nF_kroLQH06xeVFH_0x3hUXb_e1c7IB6u-mQnB4Q?key=HXuWbznUo3eoIGhGB3eU2A)

It is the most used activation function in the world right now!

🔀 0 ~ Infinity

👍

👎 Gradient vanishes when x<0 -> will never activate = never update

## 4. Leaky ReLU

## 5. LU Family

## 6. MaxOut



[ㄹㅇ 쉬운 딥러닝 4강 : 활성함수가 없으면 뉴럴네트워크가 아님 (Activation Function)](https://www.youtube.com/watch?v=rpHuwa-dbbI)

[https://deepinsight.tistory.com/95](https://deepinsight.tistory.com/95)

[https://deepinsight.tistory.com/113](https://deepinsight.tistory.com/113)

[https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)

https://towardsdatascience.com/sigmoid-and-softmax-functions-in-5-minutes-f516c80ea1f9