---
title: <i class="far fa-chart-bar"> Difference between Sequential Models and Functional Models in Tensorflow </i>
date: 2024-09-21 16:00:00 +0900
categories: [DeepLearning]
tags: [deeplearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
# Sequential API
stacked layer-by-layer

### PROS
* Basic, Simple, very easy to create
* Good for beginners

### CONS
* It does not allows you to create models that share layers
* does not allows you to have multiple inputs / outputs
-> Not flexible for network that need Merge Layers, Concatenate Layers, Add Layers.

### Example
**Simple Linear Regression Code with Sequntial API**
```
from tensorflow.keras import Sequential
from tensorflow.keras import layers

# we just need to start with Sequential()
LR_model_seq = Sequential()

# and just add whatever layers you need
LR_model_seq.add(layers.Dense(1, activation='linear')) 
```


# Functional API (Ultimate way to be an expert)

Input layer with a shape of input needs to be defined first.

### PROS
* provides more flexibility as you can connect layers to any other layers -> allows you to create complex network such as Residual Network

### CONS



### Example
**Simple Linear Regression Code with Functional API**
```
from tensorflow.keras import Model, Input

# we get whatever layer we need from tf.keras.layers
from tensorflow.keras import layers

# We need to specify how the input look like
inputs = Input(shape=(1,))

# Then we forward inputs into another layer, in this example, since it's a simple LR, we just directly go ahead into the output layer.
output = layers.Dense(1, activation='linear')(inputs) 

LR_model_func = Model(inputs, output)
```

# Model Subclassing
subclassing the `Model` Class
Define your layers in `__init__` and implement the model’s forward pass in `call`.

# Code examples designed for image classification tasks demonstrating three ways to build a CNN using Tensorflow

### 1. Sequential API
```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout

# Define the Sequential model
model_sequential = Sequential()
model_sequential.add(Con2D(32, (3,3), activation = 'relu', input_shape = (64, 64, 3)))
model_sequential.add(BatchNormalization())
model_sequential.add(MaxPooling2D(pool_size = (2,2)))
model_sequential.add(Conv2D(64, (3,3), activation = 'relu'))
model_sequential.add(BatchNormalization())
model_sequential.add(MaxPooling2D(pool_size = (2,2)))
model_sequential.add(Flatten())
model_sequential.add(Dense(128, activation = 'relu'))
model_sequential.add(Dropout(0.5))
model_sequential.add(Dense(10, activation = 'softmax'))

# Compile the model
model_sequential.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model_sequential.summary()
```

### 2. Functional API
```
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout

# Define input layer
inputs = Input(shape=(64, 64, 3))

# Add layers
x = Conv2D(32, (3, 3), activation='relu')(inputs)
x = BatchNormalization()(x)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = BatchNormalization()(x)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)

# Define output layer
outputs = Dense(10, activation='softmax')(x)

# Define the model
model_functional = Model(inputs=inputs, outputs=outputs)

# Compile the model
model_functional.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model_functional.summary()
```

### 3. Subclassing API
```
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout

# Define a custom model class
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(32, (3, 3), activation='relu')
        self.bn1 = BatchNormalization()
        self.pool1 = MaxPooling2D(pool_size=(2, 2))
        self.conv2 = Conv2D(64, (3, 3), activation='relu')
        self.bn2 = BatchNormalization()
        self.pool2 = MaxPooling2D(pool_size=(2, 2))
        self.flatten = Flatten()
        self.fc1 = Dense(128, activation='relu')
        self.dropout = Dropout(0.5)
        self.fc2 = Dense(10, activation='softmax')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.bn1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.dropout(x)
        return self.fc2(x)

# Instantiate and compile the model
model_subclass = MyModel()
model_subclass.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model_subclass.build((None, 64, 64, 3))
model_subclass.summary()
```


---
#### REFERENCE   
[https://medium.com/analytics-vidhya/keras-model-sequential-api-vs-functional-api-fc1439a6fb10](https://medium.com/analytics-vidhya/keras-model-sequential-api-vs-functional-api-fc1439a6fb10)   
[https://wikidocs.net/38861](https://wikidocs.net/38861)
