---
title: Precision and Recall in Classification Tasks (KOR)
date: 2024-11-06 17:30:00 +0900
categories: [Machine Learning]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

In classification tasks, several evaluation metrics are commonly used, including *Accuracy, Precision, Recall, and F1 Score*. These metrics are based on the **Confusion Matrix**, which forms the foundation for calculating them.

> (In a confusion matrix, the first part—True (T) or False (F)—indicates whether the model's prediction is correct. The second part—Positive (P) or Negative (N)—represents the actual prediction value.) T로 시작하는 것이 맞게 예측한부분 (T/F 는 맞게 예측했는지, 틀리게 예측했는지), Positive/Negative 는 예측한 클래스이다.

|  | Predicted Positive | Predicted Negative |
|---|---------------------|---------------------|
| **Actual Positive** | TP (True Positive) | FN (False Negative) |
| **Actual Negative** | FP (False Positive) | TN (True Negative) |

- **TP (True Positive)**: positive를 positive로 제대로 예측
- **FP (False Positive)**: Positive 로 예측했지만 틀렸다는 것. (실제 답 : Negative)
- **FN (False Negative)**: Negative 로 예측했지만 틀렸다는 것. (실제 답 : Positive)
- **TN (True Negative)**: Negative 를 Negative 로 제대로 예측

---

## 1. Accuracy
**Formula**: (TP + TN) / (TP + FP + FN + TN)  
Accuracy measures the proportion of correct predictions out of the total cases. However, accuracy can be heavily influenced by the class balance in the dataset. For example, if 99% of cases are negative, a model that always predicts "negative" would still achieve 99% accuracy, even though it lacks predictive power.  
모든 TP + FP + FN + TN 중 정확하게 분류한 data sample 의 개수를 분자로 두는 지표이다. 하지만 이 accuracy는 class별 data sample 비율에 영향을 많이 받는다.
가령 Negative가 99%로 이루어져있을 경우, 모두 negative 로 분류하더라도 99%의 놀라운 정확도를 보일 수 있다. 즉, accuracy는 불균형 데이터의 영향을 많이 받는다.

## 2. Precision & Recall
To address class imbalance, **Precision** and **Recall** provide a more nuanced view. These metrics have a trade-off relationship, and it’s essential to decide whether to focus on precision or recall, adjusting thresholds accordingly to emphasize one over the other.  
두 평가지표 Precision, Recall 모두 positive 로 예측한 샘플에 대한 평가지표

### Precision
**Formula**: TP / (TP + FP)  
Precision measures the proportion of true positive predictions out of all positive predictions. This metric emphasizes reducing FP, which are instances incorrectly classified as positive.  
1로 예측한 샘플 중 1로 맞게 예측한 비율. 즉, FP (1로 잘못 예측한 건)을 줄이는데 초점을 둔다.

### Recall
**Formula**: TP / (TP + FN)  
Recall measures the proportion of true positive predictions out of all actual positive cases. This metric emphasizes reducing FN, which are positive cases missed by the model.  
실제 1 중 1로 맞게 예측된 샘플의 비율로 FN (0으로 잘못 예측한 건)을 줄이는데 초점을 둔다.

---

## Trade-offs and Use Cases

### Case 1: High Precision, Low Recall
- Useful when it’s crucial to accept only highly qualified cases and avoid unqualified ones.
- Ideal for conservative, risk-averse approaches, where minimizing false positives is essential.
- High precision ensures that when the model predicts an applicant as successful, it is likely accurate.
- **Business Implication**: If unqualified applicants cause significant financial loss, prioritizing precision reduces the risk of approving applicants likely to default.
- 무조건 적합한 자만 받고 싶을 때, 부적합한 케이스까지 끌어왔다가는 오히려 비용이 많이 들거나 문제가 생길 때. 몇개 놓치는게 큰 문제가 아닐때. 알짜배기를 놓칠 수도 있지만 부적합한 건은 최대한 걸러낼 수 있음. 놓치는 것보다 부적합 건을 거르는 것이 더 중요할 때. (귀찮음을 감수하더라도 놓치지 않겠다.)

### Case 2: High Recall, Low Precision
- Useful when it’s essential to capture as many potential positives as possible, even at the risk of including unqualified cases.
- This approach minimizes false negatives and is beneficial in cases where missing positive cases is more detrimental.
- High recall means the model captures most qualified applicants, which can increase revenue or improve customer satisfaction.
- **Business Implication**: If the cost of missing qualified applicants is high, prioritizing recall ensures that most eligible applicants are approved, even if some unqualified ones slip through.
- 일단은 가능한 모든 case 를 받고싶을 때. 일말의 가능성이 보이는 케이스까지 전부 끌어모아서 직접 확인해야할 때. 하나라도 놓쳤다가는 큰일날때. 놓치느니 부적합 건이 함께 들어오는게 낫다.

---

## Practical Examples of Usage
- **Spam Detection**: It’s more acceptable for a few spam emails to land in the inbox than for important emails to go to spam, so prioritizing precision is key here.
- **Cancer Detection**: Prioritizing recall is crucial to avoid missing any potential positive cases, as the consequences of false negatives are significant.

## 3. F1 Score
When class imbalance is present, **F1 Score** provides a balanced metric, considering both precision and recall. F1 Score is commonly used in real-world problems to account for both false positives and false negatives.

## 4. PR-AUC
### When to Use?
- **Imbalanced Datasets**: PR-AUC is particularly helpful when the dataset has a rare positive class (e.g., fraud detection).
- **Significance of False Positives**: If false positives are costly (e.g., spam detection), PR-AUC focuses on the positive class and is more informative than ROC-AUC.

### Why PR-AUC?
1. **Focus on the Positive Class**: PR-AUC emphasizes precision and recall for the positive class, highlighting the model’s accuracy in capturing positive cases (e.g., loan approvals).
2. **Reduced Negative Class Influence**: Unlike ROC-AUC, which includes both positive and negative classes, PR-AUC provides a clearer view of performance for the positive class, especially in imbalanced data.

### How to Interpret PR-AUC Score?
A PR-AUC closer to the top right corner (high precision and recall) indicates strong performance. A score close to 1 suggests the model maintains high precision and recall, effectively identifying positives with minimal false positives.

### Using PR-AUC for Threshold Tuning
While precision may be prioritized, PR-AUC score and PR curve remain valuable tools for assessing model performance in imbalanced datasets. By examining the PR curve, we can identify threshold points where precision is maximized while recall remains at an acceptable level, allowing for fine-tuning to achieve the best trade-off based on priorities.

---

# Example: Imbalanced Datasets and Loan Approval Case

When class imbalance is present, it’s more effective to look at precision, recall, and F1-score rather than accuracy alone. For example, in a **Loan Approval/Rejection** task:

## Precision
- Prioritize precision if the goal is risk minimization (avoiding defaults and reducing financial loss).
- High precision ensures that only highly likely successful applicants are approved, aligning with a conservative approach.
- 완벽히 깔끔한 신용등급 사람들만 허용, 신용등급 애매한 사람들을 받음으로써 오는 피해가 더 클 경우


## Recall
- Prioritize recall if capturing as many qualified applicants as possible is crucial to maximize profitability and retain customers.
- High recall ensures that most eligible applicants are approved, reducing the chance of missing potentially successful applications.
- 회원을 잃는 것이 더 손해일 때, 조금 더 여유롭게 수용

In many cases, a balanced approach with F1-score can be useful to capture both precision and recall, especially when both false positives and false negatives are costly but not equally impactful.