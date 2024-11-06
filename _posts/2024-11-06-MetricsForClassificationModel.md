---
title: <i class="far fa-chart-bar">Precision and Recall in Classification task</i>
date: 2024-11-06 17:30:00 +0900
categories: [MachineLearning]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

There are several classification evaluation metrics including *Accuracy, Precision, Recall and F1 Score*.

And **Confusion Matrix** is the basis of all those metrics.

(so the first part which is T or F is whether the model's prediction is right or not. If it predicts right, then it's True, othersie, it's False.
And the second part which is P or N indicates the prediction value.)
(maybe image later)
TP FP
FN TN

* TP means the model predicts positive in a true way. (Got the answer)
* FP means the model predicts positive in a false way. (So the real value is Negative)
* FN means the model predicts negative in a false way. (So the real value here is Positive)
* TN means the model predicts negative in a true way. (Got the answer)

## Accuracy (image)
Accuracy is a metric of (TP + TN) / (TP + FP + FN + TN). it means from the whole case, we want to see how correctly the model predicts.
But this metric often get influenced by the ratio of classes of data sample. Especially imbalanced dataset.
For example, let's say 99% of data is consisted of negative value. Then if the model predicts everything as negative, we still get 99% of Accuracy even though the model can't really classify negative and positive value.

## Precision & Recall
That's why we have to look at Precision and Recall, and there's a lot in it. Because they are the trade-offs relationship.
and we have to decide where to focus on between precision and recall. once we decide it, we can adjust the threshold to make precision bigger and recall smaller or vice versa.

## Precision
TP / (TP + FP)
= (the actual positive sample from the samples that model predicts as positive) / the sample that model predicts as positive
So this focuses on lessen FP which is the model predicts the actual false as positive. (1로 잘못 예측한 건)


## Recall
TP / (TP + FN)
= ( the actual positive sample from the samples that model predicts as positive) / ACTUAL POSITIVE SAMPLES
This metric focuses on lessen FN which is the model predicts the actual true as negative. (0으로 잘못 예측한 건)

## Trade-off and Example

### Case 1 : High precision and Low Recall
- 무조건 적합한 자만 받고 싶을 때, 부적합한 케이스까지 끌어왔다가는 오히려 비용이 많이 들거나 문제가 생길 때. 몇개 놓치는게 큰 문제가 아닐때. 알짜배기를 놓칠 수도 있지만 부적합한 건은 최대한 걸러낼 수 있음. 놓치는 것보다 부적합 건을 거르는 것이 더 중요할 때.
- very conservative
- picky
- to minimize false positives
- High precision means that when the model predicts an application as successful (approved), it is likely to be correct.
- Business Implication: If approving unqualified applicants leads to significant financial risk or losses, then precision is more important. High precision would reduce the risk of approving applicants who are likely to default.



### Case 2 : High Recall and Low Precision
- 일단은 가능한 모든 case 를 받고싶을 때. 일말의 가능성이 보이는 케이스까지 전부 끌어모아서 직접 확인해야할 때. 하나라도 놓쳤다가는 큰일날때. 놓치느니 부적합 건이 함께 들어오는게 낫다.
- to minimize false negative
- careful
- High recall means that most successful applicants are identified by the model, so very few truly qualified applicants are rejected.
- If the cost of rejecting potentially successful applicants is high (e.g., loss of business opportunities or valuable customers), then recall becomes more important. High recall ensures that most eligible applicants get approved, potentially increasing revenue or customer satisfaction.


## Usage
- Spam mail detection
: it's probably more desirable to avoid important emails being moved into the spam folder than to have the occasional actual spam emails going into the inbox. in this case, we have to prioritize precision. (귀찮음을 감수하더라도 놓치지 않겠다.)

- Cancer detection


## F1 score
when the class of dataset is imbalanced, f1 score is more suitable than accuracy. (Mostly used in real world problem.)

## PR-AUC
### When to use?
- Imbalanced Datasets: When the positive class is rare, and the dataset is heavily imbalanced, the PR curve is more informative than the ROC curve. Examples include fraud detection and disease diagnosis.
- Costly False Positives: If false positives are more costly or significant than false negatives, such as in spam email detection, the PR curve is more suitable as it focuses on precision.

### Why PR-AUC?
1. Focus on the positive class  
PR-AUC is based on precision and recall, so it specifically evaluateds how well the model identifies the positive class (loan approvals). This is important because it highlights the model's accuracy in predicting loan approvals, which is the minority class.  
2. Reduced Influence from the Negative class  
ROC-AUC includs both the positive and negative classes, so in highly imbalanced data, it may give optimistic results due to the high proportion of the negative class. PR-AUC, on the other hand, assess the trade-off between precision and recall, so it is less influenced by the high number of negative cases and provides a clearer picture of the model's performance of the positive class.

### How to interpret the score?
PR-AUC curve closer to the top right corner(high precision, high recall) indicates better performance.
A score close to 1 indicates storng model performance.
High PR-AUC means the model maintains high precision and high recall simultaneously, effectively identifying positive cases without making too many incorrect positive predictions.

Again, PR-AUC is especially useful in imbalanced datasets, where it provides insight into the model's availability to capture the positive class accurately without being skewed by the high prevalence of the negative class.

while we're gonna prioritizing precision, it's still valuable to look at the PR-AUC score and the PR curve.

# Step-by-Step

1. First, find a model which has better pr-auc score. when comparing multiple models, PR-AUC can still serve as a useful summary metric to identify the most promising model.
2. Set Threshold : The PR curve shows how precision and recall changes at different threshold levels. we can identify threshold points where precision is maximized while recall remains at an acceptable level. This allows us to fine-tune the threshold to achieve the best trade-off according to our priority for precision/recall.

----
## Example
when one of the case dominate the dataset. when imbalanced.
we better look at precision, recall and f1 rather than accuracy.
 
Loan Approval / Rejection case.

### Precision
- If avoiding bad loans is a top priority(to reduce financial risk)
- when approving unqualified applicants cost a lot we'd not want to accept unqualified applicants.
- 완벽히 깔끔한 신용등급 사람들만 허용
- 신용등급 애매한 사람들을 받음으로써 오는 피해가 더 클 경우

### Recall
- If maximizing approval of qualified applicants is more important
- if it's crucial to catch as many positive cases as possible, even if it means allowing some not sure applicants. in other words, if missing qualified applicants is more harmful, then recall will be more important. 
- 회원을 잃는 것이 더 손해일 때
- 조금 더 여유롭게 수용

Often, a balanced approach with F1-score can be useful to capture both precision and recall, especially if both outcomes (false positives and false negatives) are costly but not equally impactful.