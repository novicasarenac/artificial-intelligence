from sklearn.datasets import fetch_mldata
import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD

def to_categorical(labels, n):
    retVal = np.zeros((len(labels), n), dtype='int')
    ll = np.array(list(enumerate(labels)))
    retVal[ll[:,0],ll[:,1]] = 1
    return retVal

#import MNIST set
mnist = fetch_mldata('MNIST original')
data = mnist.data / 255.0
labels = mnist.target.astype('int')

train_rank = 70000
test_rank = 2000
#MNIST subset
train_subset = np.random.choice(data.shape[0], train_rank)
test_subset = np.random.choice(data.shape[0], test_rank)

#train dataset
train_data = data[train_subset]
train_labels = labels[train_subset]

#test dataset
test_data = data[test_subset]
test_labels = labels[test_subset]

#train and test to categorical
train_out = to_categorical(labels, 10)
test_out = to_categorical(test_labels, 10)

#prepare model
model = Sequential()
#input in input layer:784, output:784
model.add(Dense(784, input_dim=784))
model.add(Activation('relu'))
#input in output layer: 784, output:10
model.add(Dense(10))
model.add(Activation('softmax'))

#compile model with optimizer
sgd = SGD(lr=0.1, decay=0.001, momentum=0.7)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#training
training = model.fit(data, train_out, nb_epoch=20, batch_size=200, verbose=0)
print training.history['loss'][-1]

#evaluate on test data
scores = model.evaluate(test_data, test_out, verbose=1)
print 'test', scores

#evaluate on train data
scores_train = model.evaluate(train_data, train_out, verbose=1)
print 'train', scores_train

model.save('nn15000test5.h5')
