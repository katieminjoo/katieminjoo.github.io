---
title: <i class="far fa-chart-bar"> Gradient Tape VS Model.fit </i>
date: 2024-08-19 22:00:00 +0900
categories: [DeepLearning]
tags: [deeplearning, tensorflow]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

 When we build a deep-learning based architecture, `model.compile()` and `model.fit()`, which are the Built-in Solution, are mostly used.

we can find `model.fit()` in [Beginners Guide](https://www.tensorflow.org/tutorials/quickstart/beginner) of Tensorflow!

The Optimizer and Loss function is set through the process of `model.compile()` and the training process is repeated in the loop with the batches of training data through `model.fit()`.

In tensorflow, training can be done with `model.compile()` and `model.fit()` methods but  it is also available to customize the training process.
And you can find the information on the [Experts Guide](https://www.tensorflow.org/tutorials/quickstart/advanced) of Tensorflow.


![IMG_0009.PNG](/assets/img/post/GradientTape/IMG_0009.png)

There are multiple things which have to be taken care of when we customize the training loop.

 In terms of data, batching, shuffling and validation needs to be managed.
In contrast to using `model.fit()`, when using a custom training loop, you have to implement the code of how to divide the data into batches and how to iterate over these batches. Not only about dividing, but also whether to shuffle, how to shuffle and how to split your data into training and validation sets and how to evaluate the model on the validation set. ( Loss has to be calculated through the process, Weight needs to be updated.)

Plus, when we customize the training loop, we can’t use either `tf.keras.callbacks.Earlystopping` callback or `tf.keras.callbacks.ModelCheckpoint` callback to check the progress conveniently. We also need to implement the code to see if the performance is not improving.

So there are quite some things that you need to consider when you use a custom training loop.

The overall architecture goes like this.

1. Define the model (network)
2. Define Optimizer, Loss function, Metrics
3. Build Training Loop
    
    Define function for updating the parameters, training loop for every epoch and validation
    
4. Train the model
5. Validate the model with the test set
6. Evaluate the model

In the next post, we are going to deal with the code example!


---

References

[https://stackoverflow.com/questions/53953099/what-is-the-purpose-of-the-tensorflow-gradient-tape](https://stackoverflow.com/questions/53953099/what-is-the-purpose-of-the-tensorflow-gradient-tape)

[https://teddylee777.github.io/tensorflow/gradient-tape/](https://teddylee777.github.io/tensorflow/gradient-tape/)

[https://medium.com/@stefanhebuaa/should-i-use-model-fit-or-tf-gradienttape-in-tensorflow-ec8664067a3](https://medium.com/@stefanhebuaa/should-i-use-model-fit-or-tf-gradienttape-in-tensorflow-ec8664067a3)

[https://junstar92.tistory.com/147](https://junstar92.tistory.com/147)
