---
title: <i class="far fa-chart-bar"> Recommender System (3) Types </i>
date: 2024-08-24 15:00:00 +0900
categories: [MachineLearning, RecommenderSystem]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

# (Model based) Latent factor Collaborative Filtering

So far, we’ve just used similarity based recommendation system but from now on, we use machine-learning based model!

The reason why it is also called a latent factor collaborative filtering is because the model captures the latent factor(taste) of each users.

This model based collaborative filtering is all about **MATRIX COMPLETION** which goes from Sparse Matrix to Dense Matrix!

The good thing about using model based system is

1. The size of model gets way small with a compressed version of rating matrix which has a enormous size of matrix and computing speed.
2. Learns data with a diversity so there’s a possibility of recommend sth new! 
In contrast to NN based Collaboritve Filtering System only can focus on item which is rated, Model based one fills the empty space of sparse matrix (matrix compression), that’s why it has a better availability of learning whole data set so that makes easy to resolve cold-start issue.

So what do we have in Model-based Collaborative Filtering?

- Association Rule Mining
- Matrix Factorization (Mostly used)
    - SVD(Singular Value Decomposition) - for optimization Stochastic Gradient Descent(SGD), Alternating Least Squares(ALS)
- Probabilistic Models
    - Clustering, Bayes Rules
- SVM, Regression Methods(Logistic Regression), Deep Learning

[Ch 06-3. Latent Factor Model, Matrix Factorization](https://velog.io/@hyxxnii/Ch-06-3.-Latent-Factor-Model-Matrix-Factorization)

# Hybrid Filtering