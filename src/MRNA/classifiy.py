import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from sklearn.model_selection import train_test_split


np.random.rand(3079)

# data processing
rawdata = np.delete(np.loadtxt('xdata.txt', dtype=str, delimiter='\t'), -1, axis=1)  # read and remove last column
colname = rawdata[0]
xdata = np.delete(np.loadtxt('xdata.txt', dtype=str, delimiter='\t', skiprows=1), -1, axis=1)
ydata = np.loadtxt('ydata.txt', dtype=str, delimiter='\t', skiprows=1)

X_train, X_test, y_train, y_test = train_test_split(xdata, ydata, test_size=0.2, random_state=42)

# X_train, y_train = xdata[:90], ydata[:90]
# X_test, y_test = xdata[90:], ydata[90:]

# preparing the model for training
# model = Sequential([
#     Dense(32, input_dim=849),
#     Activation('relu'),
#     Dense(2),
#     Activation('softmax')
# ])
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=849))
model.add(Dense(units=2, activation='softmax'))

# define optimizer
rmsprop = RMSprop(lr=0.01, rho=0.9, epsilon=1e-08, decay=0.0)

model.compile(optimizer='Adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print('Training.......')
model.fit(X_train, y_train, epochs=3, batch_size=10)

print('\nTesting.......')
loss, accuracy = model.evaluate(X_test, y_test)
print('test loss: ', loss, ' test accuracy: ', accuracy)

