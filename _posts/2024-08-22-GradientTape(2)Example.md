---
title: <i class="far fa-chart-bar"> Gradient Tape(2) Example </i>
date: 2024-08-23 00:00:00 +0900
categories: [DeepLearning]
tags: [deeplearning, tensorflow]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
This is the combination version of 
[TensorFlow 2 quickstart for experts](https://www.tensorflow.org/tutorials/quickstart/advanced) & 
[Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping) from the official document from Tensorflow!  
(These two codes work well individually, but if you try to combine them and run them as one, it might be a bit confusing. They are fundamentally similar, but there are slight differences in how the loss is updated and in the variable names. I’ve combined these two codes so that they can run together seamlessly.)


## Here is an example of how you might use model.fit to train a model, very simple and clear!
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

And Let’s deep dive into how we can customize the training loop! 

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

(This is the part where I've made some changes to the code. The first implementation used the mean metric, while the second used SparseCategoricalCrossentropy directly as the metric. I've included a brief explanation of these metrics below, just in case you're having trouble finding information on the official website!)
* tf.keras.metrics.Mean  
: Averages any numeric values passed to it, often used to compute the average loss across batches.

* tf.keras.metrics.SparseCategoricalCrossentropy  
: Specifically computes the sparse categorical cross-entropy loss, suitable for classification tasks with integer labels.

```
train_loss_metric = tf.keras.metrics.SparseCategoricalCrossentropy()
train_acc_metric = tf.keras.metrics.SparseCategoricalAccuracy()

val_loss_metric = tf.keras.metrics.SparseCategoricalCrossentropy()
val_acc_metric = tf.keras.metrics.SparseCategoricalAccuracy()
```

## Finally, let's define the training and testing functions, and then proceed to train the model on the dataset!

**GradientTape**

TensorFlow provides the `tf.GradientTape` API for automatic differentiation, which involves computing the gradients of operations with respect to input variables.

`tf.GradientTape` "records" all operations executed within its context on a "tape."

TensorFlow then uses reverse mode differentiation to compute the gradients of the operations "recorded" on the tape.

```
@tf.function
def train_step(x, y):
  # apply GradientTape for differentiation
  with tf.GradientTape() as tape:

      # 1. Prediction
      logits = model(x, training=True)

      # 2. Calculate loss (between truth ground and prediction)
      loss_value = loss_object(y, logits)

  # 3. Calculate Gradients
  grads = tape.gradient(loss_value, model.trainable_weights)

  # 4. Update weights through Backpropagation
  optimizer.apply_gradients(zip(grads, model.trainable_weights))
  
  # Update loss and accuracy
  train_acc_metric.update_state(y, logits)
  train_loss_metric.update_state(y, logits)
  
  # the reason why we return the loss_value
  # is to check if the loss gets smaller after every batches, epochs
  return loss_value

@tf.function
def test_step(x, y):

  # 1. Prediction
  logits = model(x, training=False)

  # 2. No gradients caluculation and backpropagation in test step.

  # 3. Update Loss and Accuracy
  val_acc_metric.update_state(y, logits)
  val_loss_metric.update_state(y, logits)
```

## ver 01. Just Train
```
EPOCHS = 5

for epoch in range(EPOCHS):
  # Reset the metrics at the start of the next epoch
  train_loss_metric.reset_state()
  train_acc_metric.reset_state()
  val_loss_metric.reset_state()
  val_acc_metric.reset_state()

  for images, labels in train_ds:
    train_step(images, labels)


  for test_images, test_labels in test_ds:
    test_step(test_images, test_labels)

  print(
    f'Epoch {epoch + 1}, '
    f'Loss: {train_loss_metric.result():0.2f}, '
    f'Accuracy: {train_acc_metric.result() * 100:0.2f}, '
    f'Test Loss: {val_loss_metric.result():0.2f}, '
    f'Test Accuracy: {val_acc_metric.result() * 100:0.2f}'
  )

```
![image.png](/assets/img/post/GradientTape(2)Example/image01.png)

## ver 02. Add EarlyStopping
**CAUTION !! make sure use the method `reset_state()`, not `reset_states()`.**  
I used the code from an official document example from tensorflow.
But you'll encounter the AttributeError when you follow the instruction from the tensorflow document.
The correct method to reset the state of a metric in TensorFlow is reset_state(), not reset_states(). By changing the method name, the code should now execute without the AttributeError!!
```
#new ver
import time

epochs = 100
patience = 5
wait = 0
best = float('inf')

for epoch in range(epochs):
    print("\nStart of epoch %d" % (epoch,))
    start_time = time.time()

    for step, (x_batch_train, y_batch_train) in enumerate(train_ds):
      # calculate loss_value every batch
      loss_value = train_step(x_batch_train, y_batch_train)
      if step % 200 == 0:
        print("Training loss at step %d: %.4f" % (step, loss_value.numpy()))
        print("Seen so far: %s samples" % ((step + 1) * 128))
    # Report acc, loss per epoch
    train_acc = train_acc_metric.result()
    train_loss = train_loss_metric.result()
    train_acc_metric.reset_state()
    train_loss_metric.reset_state()
    print("Training acc over epoch: %.4f" % (train_acc.numpy()))

    for x_batch_val, y_batch_val in test_ds:
      # calculate loss_value every batch
      test_step(x_batch_val, y_batch_val)
    # Report acc, loss per epoch
    val_acc = val_acc_metric.result()
    val_loss = val_loss_metric.result()
    val_acc_metric.reset_state()
    val_loss_metric.reset_state()
    print("Validation acc: %.4f" % (float(val_acc),))
    print("Time taken: %.2fs" % (time.time() - start_time))

    # The early stopping strategy: stop the training if `val_loss` does not
    # decrease over a certain number of epochs.
    wait += 1
    if val_loss < best:
      best = val_loss
      wait = 0
    if wait >= patience:
      break
```



---
## reference

[https://teddylee777.github.io/tensorflow/gradient-tape/](https://teddylee777.github.io/tensorflow/gradient-tape/)

[https://www.tensorflow.org/tutorials/quickstart/advanced](https://www.tensorflow.org/tutorials/quickstart/advanced)

[https://www.tensorflow.org/guide/migrate/early_stopping](https://www.tensorflow.org/guide/migrate/early_stopping)
