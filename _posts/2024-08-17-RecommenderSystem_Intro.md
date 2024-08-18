---
title: <i class="far fa-chart-bar"> Recommender System (1) Intro </i>
date: 2024-08-17 00:00:00 +0900
categories: [MachineLearning, RecommenderSystem]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
# What is Recommender System?

A recommendation system is a machine learning algorithm, often associated with artificial intelligence, that leverages large datasets to provide personalized suggestions to users. By analyzing past behaviors, preferences, and patterns—such as purchase history, search activity, and demographic information—these systems predict consumer interests with a high degree of accuracy. Recommender systems are widely used across various online platforms, including e-commerce, social media, and entertainment, to enhance user engagement, satisfaction, and retention. They play a critical role in helping users navigate the overwhelming amount of available content, driving both user satisfaction and revenue for businesses.

In recommender systems, data used to generate recommendations can be categorized into two main types: **implicit data** and **explicit data**. Understanding the difference between these two types of data is crucial for designing effective recommendation algorithms.

![](/assets/img/post/RecommenderSystem(1)Intro/image.png)

## Implicit Data

**Implicit data** refers to information that is inferred from a user’s behavior without requiring any direct input from the user. It is collected passively as users interact with a platform, without them consciously providing feedback. Examples of implicit data include:

- **Click-through rates**: The items a user clicks on while browsing a website.
- **Browsing history**: The pages or products a user views.
- **Purchase history**: Items that a user has bought previously.
- **Time spent on content**: How long a user spends watching a video, reading an article, or listening to a song.
- **Search queries**: The keywords or phrases a user searches for.

Implicit data is valuable because it doesn’t require users to take any additional action; it is automatically collected as they interact with the system. However, because it is inferred, it may not always accurately reflect a user's true preferences. For example, a user might click on an item out of curiosity but not actually be interested in it.

## Explicit Data

**Explicit data** is the information that users actively provide to the system, usually in the form of direct feedback. This type of data is collected when users intentionally express their preferences. Examples of explicit data include:

- **Ratings**: When a user rates a product, movie, or song on a scale (e.g., 1 to 5 stars).
- **Reviews**: Written feedback where users describe their experience with a product or service.
- **Likes/Dislikes**: When a user clicks a "like" or "dislike" button.
- **Favorites**: Items that a user adds to a favorites list or a wish list.

Explicit data is generally more accurate than implicit data because it reflects a user’s direct input about their preferences. However, gathering explicit data can be challenging because it requires users to take additional steps, which they may not always be willing to do.

## Combining Implicit and Explicit Data

Most modern recommender systems use a combination of both implicit and explicit data to generate more accurate and comprehensive recommendations. Implicit data provides a wealth of passive information that can help to fill in the gaps when explicit feedback is limited. Meanwhile, explicit data adds a layer of accuracy and reliability to the recommendations.

For example, a streaming service might use your viewing history (implicit data) to recommend movies you might enjoy while also considering the ratings you’ve given to similar movies (explicit data) to fine-tune those recommendations.

By leveraging both types of data, recommender systems can create a more holistic view of a user’s preferences, leading to more personalized and relevant suggestions.





Once we have collected all the implicit and explicit data, we can make user-item matrix!

A **user-item matrix** (also known as a **user-item interaction matrix** or **utility matrix**) is a fundamental concept in recommender systems, representing the relationship between users and items. It is a two-dimensional matrix where:

- **Rows** correspond to users.
- **Columns** correspond to items (such as products, movies, books, etc.).

Each cell in the matrix captures the interaction between a specific user and a specific item, indicating how the user has interacted with the item. The type of interaction captured in the matrix can vary depending on the context and the data available.

In cases where users provide explicit ratings (e.g., giving a movie 4 out of 5 stars), the matrix entries will be the numerical ratings given by the users to the items.

When explicit ratings are not available, the matrix might reflect implicit feedback, such as whether a user has interacted with an item. The entries could be binary (e.g., 1 for interacted, 0 for no interaction) or could represent the strength of the interaction (e.g., the number of times a user has clicked on or viewed an item).

![image.png](/assets/img/post/RecommenderSystem(1)Intro/image1.png)

we are going to talk about how we can utilize this user-item matrix in the next post!!

---
## References

[https://towardsdatascience.com/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748](https://towardsdatascience.com/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748)

[https://www.nvidia.com/en-us/glossary/recommendation-system/#:~:text=A recommendation system](https://www.nvidia.com/en-us/glossary/recommendation-system/#:~:text=A%20recommendation%20system%20) (or%20recommender,exponentially%20growing%20number%20of%20options.