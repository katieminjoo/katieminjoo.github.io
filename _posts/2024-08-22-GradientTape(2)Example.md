---
title: <i class="far fa-chart-bar"> Gradient Tape(2) Example </i>
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

Here is an example of how you might use model.fit to train a model:
```
# Define the model
model = MyModel()

# Compile the model with a loss function and an optimizer
model.compile(loss=tf.losses.mean_squared_error, optimizer=tf.optimizers.SGD(learning_rate=0.001))

# Generate some synthetic data
x = np.random.rand(64, 10)
y = np.random.rand(64, 1)

# Use the model.fit method to train the model
model.fit(x, y, epochs=10, batch_size=32)
```

And Let’s deep dive into how we can customize the training loop, with a reference to [Tensorflow documentation](https://www.tensorflow.org/tutorials/quickstart/advanced). 

Basic code goes like this.

## First of all, import all the libraries we need

```
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras import Model
import numpy as np
```

## Data Load

In this code, we are going to use MNIST(https://yann.lecun.com/exdb/mnist/) dataset for the experiment.

It’s easy to load sample datasets from the module, tf.keras.datasets !

In this module, we have 8 accessible dataset modules which combines

### **Modules**

[boston_housing](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing) module: DO NOT EDIT.

[california_housing](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing) module: DO NOT EDIT.

[cifar10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10) module: DO NOT EDIT.

[cifar100](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100) module: DO NOT EDIT.

[fashion_mnist](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist) module: DO NOT EDIT.

[imdb](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb) module: DO NOT EDIT.

[mnist](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist) module: DO NOT EDIT.

[reuters](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters) module: DO NOT EDIT.

We can easily obtain splitted x,y, train, test data through load_data() function.

```
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#make image data value from 0 to 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Add a channels dimension
x_train = x_train[..., tf.newaxis].astype("float32")
x_test = x_test[..., tf.newaxis].astype("float32")
```


## Now Let’s slice the data into certain batches.

```
train_ds = tf.data.Dataset.from_tensor_slices(

(x_train, y_train)).shuffle(10000).batch(32)

test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)
```

The dataset for train and test is ready!

## Define the model

We are going to make a simple multi layer model.
```
inputs = tf.keras.layers.Input(shape=(28,28,1))

#build your own model
x = Conv2D(32,3,activation = 'relu')(inputs)
x = MaxPooling2D((2,2))(x)
x = Conv2D(64,3,activation = 'relu')(x)
x = MaxPooling2D((2,2))(x)
x = Conv2D(64,3,activation = 'relu')(x)
x = Flatten()(x)
x = Dense(64, activation= 'relu')(x)

outputs = Dense(10)(x)

model = tf.keras.models.Model(inputs, outputs)

model.summary()
```

![](/assets/img/post/GradientTape(2)Example/image00.png)



## Choose an optimizer and loss function for training

```
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

optimizer = tf.keras.optimizers.Adam()
```

## Choose metrics to evaluate the model's loss and accuracy. These metrics will aggregate the values over the epochs and display the final results.

```
train_loss = tf.keras.metrics.Mean(name='train_loss')

train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

test_loss = tf.keras.metrics.Mean(name='test_loss')

test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')
```

## Finally, let's define the training and testing functions, and then proceed to train the model on the dataset!

**GradientTape**

TensorFlow provides the `tf.GradientTape` API for automatic differentiation, which involves computing the gradients of operations with respect to input variables.

`tf.GradientTape` "records" all operations executed within its context on a "tape."

TensorFlow then uses reverse mode differentiation to compute the gradients of the operations "recorded" on the tape.

```
def train_step(images, labels):

    # apply GradientTape for differentiation
    with tf.GradientTape() as tape:

        # 1. Prediction
        predictions = model(images)

        # 2. Calculate loss (between truth ground and prediction)
        loss = loss_object(labels, predictions)

# 3. Calculate Gradients
gradients = tape.gradient(loss, model.trainable_variables)

# 4. Update weights through Backpropagation
optimizer.apply_gradients(zip(gradients, model.trainable_variables))

# Update loss and accuracy
train_loss(loss)
train_accuracy(labels, predictions)
```

```
def test_step(images, labels):

    # 1. Prediction
    predictions = model(images)

    # 2. Calculate loss
    loss = loss_object(labels, predictions)

    # 3. No gradients caluculation and backpropagation in test step.
    # 4. Update Loss and Accuracy

    test_loss(loss)
    test_accuracy(labels, predictions)
```

```
epochs = 5

for epoch in range(epochs):

    # Reset the metrics at the start of the next epoch
    train_loss.reset_state()
    train_accuracy.reset_state()
    test_loss.reset_state()
    test_accuracy.reset_state()

    for images, labels in train_ds:
        train_step(images, labels)

    for test_images, test_labels in test_ds:
        test_step(images, labels)

    print(
    f’Epoch {epoch + 1}, '
    f'Loss: {train_loss.result():0.2f}, '
    f'Accuracy: {train_accuracy.result() * 100:0.2f}, '
    f'Test Loss: {test_loss.result():0.2f}, '
    f'Test Accuracy: {test_accuracy.result() * 100:0.2f}'
    )

```

![image.png](/assets/img/post/GradientTape(2)Example/image01.png)

---
## reference

[https://teddylee777.github.io/tensorflow/gradient-tape/](https://teddylee777.github.io/tensorflow/gradient-tape/)

[https://www.tensorflow.org/tutorials/quickstart/advanced](https://www.tensorflow.org/tutorials/quickstart/advanced)