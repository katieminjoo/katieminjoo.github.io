---
title: <i class="far fa-chart-bar"> Recommender System (2) Types </i>
date: 2024-08-18 21:00:00 +0900
categories: [MachineLearning, RecommenderSystem]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

# Recommender System (2) Types

So we have talked about the introduction of Recommender Systems. We are going to deal with types of recommender(recommendation) systems and how we are going to handle some chanllenges and what to consider more about the recommender system!

# **Types of Recommendation Systems**

There are mainly 3 types of recommendation systems, each using different approaches to generate suggestions.

![IMG_0005.PNG](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/IMG_0005.png)

## (0. Demographic Filtering)

Shortly, It stereotypes every person into specific category according to each user’s information(age, sex, occupation, hobby, etc.)

Actually, this method is not much used compared to other methods that we’ll be dealing with!

The biggest reason why it isn’t often used is it’s hard to collect user’s demographic information these days and the fact that every user has to be classified in a specific group causes widely personalized recommendation result which is comparable to other very personalized methods.

We can classify ever user into more diverse groups so that every group can have their own traits but if we did this, Low computing cost, which is one of the advantages of using demographic filtering, vanishes. 

So these days, we prefer those two methods in the below!

## 1. Content-based Filtering

![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image.png)

This method focuses on the attributes of **the items themselves**. ( Don’t need any other user information) If you like a particular type of music, a content-based system will recommend similar songs or artists based on the characteristics of the music you've enjoyed in the past.

This method is all about the similarity of item themselves. so methods to get similarity is used in this filtering method, including Cosine Similarity, Euclidean Distance and Manhattan Distance.

To train a Machine Learning model with this approach we can use a [**k-NN model](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).** For instance, if we know that user *u* bought an item *i*, we can recommend to *u* the available items with features most similar to *i*.

The **advantage** of this approach is that items metadata are known in advance, so we can also apply it to [Cold-Start scenarios](/assets/img/post/https://en.wikipedia.org/wiki/Cold_start_(recommender_systems)) where a new item or user is added to the platform and we don’t have user-item interactions to train our model.

The **disadvantages** are that we don’t use the full set of known user-item interactions (each user is treated independently), and that we need to know metadata information for each item and user. no diversity ! always get the similar taste of what user’s been explored.

## 2. Collaborative Filtering

![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image%201.png)

This approach makes recommendations based on the preferences of **users who have similar tastes**.

For instance, if you and another user have both enjoyed the same movies in the past, a collaborative filtering system might recommend a movie to you that the other user liked but you haven't seen yet.

## 2-1. (Memory-based) Nearest Neighbor based Collaborative Filtering

It’s very simple, All we have to do is calculating similarity either between user-user or between item-item in user-item matrix !

![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image%202.png)

This can be divided into 2 ways again.

The user-based one and the item-based one.

![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image%203.png)

## 2-1-1. User-based Collaborative Filtering

User-based method needs matrix with users on the rows and items on the columns.

Two users give similar ratings on the same products, so they are similar!

If you look at the left image, users(B,D) who have similar tastes chose A,B,C items. so another similar user can be interested in A,B,C items.

So It’s about sharing their taste of item between two close friends who has same taste.

This will be a great method for systems where users occupy a large portion of the platform such as SNS.

## 2-1-2. Item-based Collaborative Filtering

On the other hand, Item-based method needs matrix with items on the rows and the users on the columns.

ItemA and ItemB has a similar rating distribution, so they might be similar item.

If you look at the right image, A,C,D Users chose item#4 choose item#2 this time. so without knowing user’s taste, another user who chose item#2 earlier can be interested in item#4 this time!

~~Users are not friends, they don’t know each other, but you got recommendation from your favorite fashion brand staff ! so there is high likelihood that you might like what she likes! because you guys are connected through items. (not sure about this example)~~

*different between content-based and item-based : content based goes with just only the features of item itself, but item-based is attached with many users’.

### [ User-based and Item-based Collaborative Filtering ]

- when there’s more users than items, go with the user-based method and vice-versa.
    
    #user < #item : User-based
    
    #user > #item : Item-based
    
    Focus on sth smaller!
    
- It’s broadly said that item-based collaborative filtering is more precise and likely used than user-based one since having similar taste doesn’t exactly mean that you like similar things.
- Item-based method can be explained with the similarity of other items but the user-based one can’t be precisely explained

### There are some challenges in using memory-based collaborative Filtering tho!

1. **Sparsity**: In most real-world scenarios, the user-item matrix is highly sparse because users typically interact with only a small subset of all available items. This sparsity makes it challenging to generate accurate recommendations.
→ To fill in missing values and uncover significant patterns from a small number of user-product interactions, dealing with data sparsity necessitates the use of sophisticated methods like matrix factorizing and data imputation.
2. **Cold Start Problem**: When new users or items are introduced, they have little to no interaction data, making it difficult to recommend items for these new users or to recommend the new items to existing users.
    
    → To address the cold start issue, hybrid methods that combine collaborative filtering with content-based filtering or knowledge-based recommendations can be effective. Gathering more data on new users or items over time is essential for improving recommendations.
    
3. **Diversity and serendipity (Long-Tail Economy)**
    
    ![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image%204.png)
    
    In order to provide consumers with a wide selection of items and to avoid suggestion bias, it is essential to ensure a wide range of offers. Collective filtering often favors known products over less known or specialized products.
    → Incorporating diversity-aware recommendation techniques, such as variation-aware collaborative filtering or hybrid methods, can help broaden the range of recommendations and introduce unpredictability into the system.
    

## 2-2. (Model based) Latent factor Collaborative Filtering

![image.png](/assets/img/post/Recommender%20System%20(2)%20Types%2032dd76d684124531bcff74603f6100a3/image%205.png)

It is all about the Matrix Completion task! (From Sparse Matrix → Dense Matrix)

based on matrix factorization (MF).

It divides user-item matrix into user-latent, item-latent vectors. (we don’t know what exactly this latent factor represents tho)

The biggest advantage of using this method is it helps to reduce the computing power and the resource of computer.

Matrix Factorization
- SVD(Singular Value Decomposition), ALS(Alterning Least Square)

## 3. Hybrid Filtering (Collaborative Filtering + Content-based)

maybe we should do another post about this model based method and the hybrid method later since it gets too long,,,🤔

### CODE
  
---

References

[https://www.tensorflow.org/resources/recommendation-systems](https://www.tensorflow.org/resources/recommendation-systems)

[https://utsavdesai26.medium.com/recommendation-systems-explained-understanding-the-basic-to-advance-43a5fce77c47](https://utsavdesai26.medium.com/recommendation-systems-explained-understanding-the-basic-to-advance-43a5fce77c47)

[https://lsjsj92.tistory.com/564](https://lsjsj92.tistory.com/564)

[https://medium.com/@nidhishukla2023/challenges-of-the-recommendation-system-f2406b3f2232](https://medium.com/@nidhishukla2023/challenges-of-the-recommendation-system-f2406b3f2232)

[https://velog.io/@hyxxnii/Ch-05-1.-이웃기반-협업필터링](https://velog.io/@hyxxnii/Ch-05-1.-%EC%9D%B4%EC%9B%83%EA%B8%B0%EB%B0%98-%ED%98%91%EC%97%85%ED%95%84%ED%84%B0%EB%A7%81)

[https://medium.com/@kyasar.mail/recommender-systems-what-long-tail-tells-91680f10a5b2](https://medium.com/@kyasar.mail/recommender-systems-what-long-tail-tells-91680f10a5b2)

[https://www.sciencedirect.com/science/article/abs/pii/S1567422321000612#:~:text=Traditional recommendation algorithms tend to,significant loss to the business](https://www.sciencedirect.com/science/article/abs/pii/S1567422321000612#:~:text=Traditional%20recommendation%20algorithms%20tend%20to,significant%20loss%20to%20the%20business).

[https://data-science-hi.tistory.com/169](https://data-science-hi.tistory.com/169)

[https://medium.com/eunjios-dev-blog/collaborative-filtering-mbcf-model-based-collaborative-filtering-b33ac3a5c705](https://medium.com/eunjios-dev-blog/collaborative-filtering-mbcf-model-based-collaborative-filtering-b33ac3a5c705)