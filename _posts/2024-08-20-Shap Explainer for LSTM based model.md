---
title: <i class="far fa-chart-bar"> Shap Explainer for LSTM based model </i>
date: 2024-08-20 00:00:00 +0900
categories: [DeepLearning]
tags: [deeplearning, tensorflow]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
## WHAT is SHAP?
SHAP(SHapley Additive exPlanations) values are used to explain the output of any machine learning model. They are based on concepts from cooperative game theory, specifically the Shapley value, which fairly distributes the “payout” (in this case, the prediction) among the “players” (features) based on their contributions.

## WHY use SHAP?
Because of Model Interpretability!  
 SHAP provides a unified measure of feature importance, showing how each feature contributes to the model's prediction for a given instance. This is crucial for understanding models like deep neural networks, gradient boosting machines, or any other complex models that are often seen as "black boxes."

[SHAP Official Documentation](https://shap.readthedocs.io/en/latest/)

There are several explainers we can use.  
1. TreeExplainer  
    This is optimized for tree-based models like decision trees, random forests, and gradient boosting machines(XGBoost, LightGBM, CatBoost)
2. KernelExplainer  
    It is a model-agnostic explainer, which means it can be used with any ml model, regardless of its type.
3. DeepExplainer
    Designed for deeplearning models created with Tensorflow or Pytorch
4. LinearExplainer  
    Made for linear models, such as logistic regression or ordinary least squares regression. This is ideal for interpreting models where the relationships between features and predictions are straightforward and additive.
5. PartionExplainer  
    An extension version of TreeExplainer! (When dealing with extremely large decision trees)
6. GradientExplainer  
    Similar to DeepExplainer, but specifically optimized for models that use gradient boosting, such as XGBoost or LightGBM.  
  
![img](/assets/img/post/shap/IMG_0010.png)  

 It is said that most deep learning based models are worked with DeepExplainer.  
But when we deep dive into it, DeepExplainer is primarily designed for feedforward neural networks and CNNs, which have a more straightforward, static input-output relationship. LSTMs, with their recurrent nature, complex internal states, and dependence on the entire sequence of inputs, pose significant challenges for DeepExplainer. 
 And therefore, Long Short-Term Memory (LSTM) networks, which are a type of recurrent neural network (RNN), present specific challenges when it comes to using SHAP's DeepExplainer.  
Those are the possible scenarios why LSTM struggles with DeepExplainer.  

**1. LSTMs Have Recurrence**: LSTM networks process data sequentially, maintaining a hidden state that is updated at each step in the sequence. This recurrence means that the output at each time step depends not only on the current input but also on the entire sequence of previous inputs.  

**2. Complex Internal States**: LSTM networks have complex internal states (cell state and hidden state) that are updated using gating mechanisms (input gate, forget gate, output gate). These operations are not straightforward to interpret using methods designed for feedforward networks like DeepExplainer.

 
In my experience, and in my case of modeling, All I can say is  
## Try **GradientExplainer**

Below is the code that i used to get the shapvalues and visualize the feature importance after building a model.

```
import shap

explainer = shap.GradientExplainer(model, input_x)

#calculate shap values
shap_values = explainer.shap_values(input_x)

#Calculate mean absolute SHAP values for each input set
#in this case, I used two different input sets
mean_shap_1 = np.abs(shap_values[0][0]).mean(axis = 0).reshape(-1)
mean_shap_2 = np.abs(shap_values[0][1]).mean(axis = 0).reshape(-1)
all_mean_shap = np.concatenate([mean_shap_1, mean_shap_2])

#setup feature names
feature_names_1 = list(x_train.iloc[:,:n].columns)
feature_names_2 =list(x_train.iloc[:,:n].columns)
all_feature_names = feature_names_1 + feature_names_2


#Create a bar plot for feature importance
plt.figure(figsize = (8,4))
plt.bar(all_feature_names, all_mean_shap)
plt.xlabel(‘features’)
plt.ylabel(‘Mean of Shap Value (Feature Importance))
plt.title(‘Overall Feature Importance’)
plt.xticks(rotation = 45)
plt.show()
```
---

References

https://shap.readthedocs.io/en/latest/