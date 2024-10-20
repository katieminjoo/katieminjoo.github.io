---
title: <i class="far fa-chart-bar">What is Bagging and Boosting?</i>
date: 2024-10-20 17:30:00 +0900
categories: [MachineLearning]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
Bagging and Boosting are two popular ensemble learning techniques used in MachineLearning to improve the performance of models by combining multiple weaker models (often called weak learners) to create a stronger, more accurate model.

# 1. Bagging (Bootstrap Aggregating)
Bagging is a technique where multiple models are trained independently and in parallel.  
Each model is trained on a different random subset of the training data(created by bootstrapping, which means sampling with replacement). The idea is to reduce variance by averaging the predictions from multiple models.

* Multiple datasets are created by randomly sampling from the original dataset with replacement (복원추출)
* So each model is trained on a different bootstrapped dataset.
* The final prediction is made by averaging the predictions(for regression task) or using a majority vote (for classification task) from all models.

### Popular Algorithms : Random Forests
An ensemble of decision trees, where each tree is trained on a different random subset of data and features.

### Advantage
: Bagging **reduces overfitting** by combining multiple models, leading to **better generalization**.  
*(Poor Generalization -> cause Overfitting : Boosting )*

### Disadvantage
: Since models are trained independently, bagging might not always perform well with models that rely on sequential learning.

# 2. Boosting
: Boosting is a technique where multiple models are trained sequentially. Each new model tries to correct the errors made by the previous models. The idea is to **boost** the performance of the overall model by focusing on the mistakes of earlier models.
: The samples that are incorrectly predicted in one iteration will have higher weight in the next one. Thus, isolated and mislabelled points tend to strongly force the classifier to create complicated hypothesis to fit them, which we will call overfitting. 

* At first, all data points are given equal weights.
* The first model is trained, and the erros are stored.
* The next model is then trained, but it **gives more weight** to the data points that were misclassified by the previous model. This process continues **sequentially**.
* The final model combines all the individual models, with more weight given to models that performed well.

### Popular Algorithms
* **AdaBoost** : Adjusts weights on misclassified samples so the next model can more focus on them.  
* **GBM** : Corrects the residual errors from the previous model using gradient descent.  
* **XGBoost, LightGBM, CatBoost** : Optimized versions of Gradient Boosting designed for speend and efficiency.

### Advantage
: Boosting **reduces bias** by focusing on difficult-to-predict cases, leading to **higher accuracy**.

### Disadvantage
: Boosting can be **prone to overfitting**, especially if not carefully managed.

---
# Key Differences between Bagging and Boosting
| Feature  |      Bagging    |  Boosting |
|:----------:|:----------------:|:----------:|
| Training | Models are trained independently and in **parallel** | Models are trained **sequentially**, each trying to correct errors of the previous one |
| Goal | Reduce **Variance** (to prevent Overfitting) | Reduce **bias** (to improve accuracy) |
| Data Sampling method | **Bootstrapping** (random sampling with replacement) | Adjusts **weights** on each sample, focusing on difficult cases |
| Combining Models | Averaging (for regression), voting (classification) | Weighted combination of all models |
| Algorithms | Random Forests | AdaBoost, Gradient Boosting, XGBoost |


> ### Bagging focuses on **stability** by reducing overfitting.
> ### Boosting focuses on **accuracy** by correcting errors sequentially.