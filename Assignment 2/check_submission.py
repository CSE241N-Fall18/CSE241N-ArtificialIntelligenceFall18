import utils
import models

import numpy as np
import json
import random

# set the random seed
np.random.seed(0)
random.seed(0)

# load the saved parameters
filename = 'hyper_param.json'

try:
    with open(filename, 'r') as fp:
        dict_hyper = json.load(fp)
except:
    # end the program
    print("error")

#----------------------------------------------------------------------
# Linear
#----------------------------------------------------------------------

# load the linear paramaters
feat_type = dict_hyper['linear']['feat_type']
param = dict_hyper['linear']['param']
lr = dict_hyper['linear']['lr']
weight_init = dict_hyper['linear']['weight_init']

# generate artificial data
(x_train, y_train, x_val, y_val, x_test, y_test, left_limit, right_limit) = utils.data_generator(utils.linear)

# convert all the splits into numpy arrays
x_train, y_train = np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1)
x_val, y_val = np.array(x_val).reshape(-1,1), np.array(y_val).reshape(-1,1)
x_test, y_test = np.array(x_test).reshape(-1,1), np.array(y_test).reshape(-1,1)

# create a model object from the linear_model class
W_size = models.calc_features(np.array([[0]]), choice=feat_type, param=param).shape[1]
learning_model = models.linear_model(W_size=W_size, lr=lr, init=weight_init) 

no_epochs = 200

# train the model
feat_train = models.calc_features(x_train, choice=feat_type, param=param)
for epoch in range(no_epochs):
    
    # forward pass: calculate the model's prediction on training data
    y_pred_train = learning_model.forward(feat_train)

    # backward pass: train the linear regression model, using gradient descent
    learning_model.backward(y_train, y_pred_train, feat_train)

# compute loss on test data
feat_test = models.calc_features(x_test, choice=feat_type, param=param)
y_pred_test = learning_model.forward(feat_test)
loss_test_linear = utils.loss(y_test, y_pred_test)  



#----------------------------------------------------------------------
# Polynomial
#----------------------------------------------------------------------

# load the polynomial paramaters
feat_type = dict_hyper['poly']['feat_type']
param = dict_hyper['poly']['param']
lr = dict_hyper['poly']['lr']
weight_init = dict_hyper['poly']['weight_init']

# generate artificial data
(x_train, y_train, x_val, y_val, x_test, y_test, left_limit, right_limit) = utils.data_generator(utils.poly)

# convert all the splits into numpy arrays
x_train, y_train = np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1)
x_val, y_val = np.array(x_val).reshape(-1,1), np.array(y_val).reshape(-1,1)
x_test, y_test = np.array(x_test).reshape(-1,1), np.array(y_test).reshape(-1,1)

# create a model object from the linear_model class
W_size = models.calc_features(np.array([[0]]), choice=feat_type, param=param).shape[1]
learning_model = models.linear_model(W_size=W_size, lr=lr, init=weight_init) 

no_epochs = 200

# train the model
feat_train = models.calc_features(x_train, choice=feat_type, param=param)
for epoch in range(no_epochs):
    
    # forward pass: calculate the model's prediction on training data
    y_pred_train = learning_model.forward(feat_train)

    # backward pass: train the linear regression model, using gradient descent
    learning_model.backward(y_train, y_pred_train, feat_train)

# compute loss on test data
feat_test = models.calc_features(x_test, choice=feat_type, param=param)
y_pred_test = learning_model.forward(feat_test)
loss_test_poly = utils.loss(y_test, y_pred_test)  


#----------------------------------------------------------------------
# Periodic
#----------------------------------------------------------------------

# load the periodic paramaters
feat_type = dict_hyper['periodic']['feat_type']
param = dict_hyper['periodic']['param']
lr = dict_hyper['periodic']['lr']
weight_init = dict_hyper['periodic']['weight_init']

# generate artificial data
(x_train, y_train, x_val, y_val, x_test, y_test, left_limit, right_limit) = utils.data_generator(
    utils.sawtooth, 
    train_left=-10, train_right=10, train_size=256,
    val_left=11, val_right=15, val_size=64,
    test_left=12, test_right=14, test_size=64)

# convert all the splits into numpy arrays
x_train, y_train = np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1)
x_val, y_val = np.array(x_val).reshape(-1,1), np.array(y_val).reshape(-1,1)
x_test, y_test = np.array(x_test).reshape(-1,1), np.array(y_test).reshape(-1,1)

# create a model object from the linear_model class
W_size = models.calc_features(np.array([[0]]), choice=feat_type, param=param).shape[1]
learning_model = models.linear_model(W_size=W_size, lr=lr, init=weight_init) 

no_epochs = 200

# train the model
feat_train = models.calc_features(x_train, choice=feat_type, param=param)
for epoch in range(no_epochs):
    
    # forward pass: calculate the model's prediction on training data
    y_pred_train = learning_model.forward(feat_train)

    # backward pass: train the linear regression model, using gradient descent
    learning_model.backward(y_train, y_pred_train, feat_train)

# compute loss on test data
feat_test = models.calc_features(x_test, choice=feat_type, param=param)
y_pred_test = learning_model.forward(feat_test)
loss_test_periodic = utils.loss(y_test, y_pred_test)  



#----------------------------------------------------------------------
# Unknown
#----------------------------------------------------------------------

# load the periodic paramaters
feat_type = dict_hyper['unknown']['feat_type']
param = dict_hyper['unknown']['param']
lr = dict_hyper['unknown']['lr']
weight_init = dict_hyper['unknown']['weight_init']

# load the data
(x_train, y_train, x_val, y_val) = np.load('linear_reg_data.npy')
try:
    (x_test, y_test) = np.load('linear_reg_data_test.npy')
except:
    (x_test, y_test) = (x_val, y_val)

# convert all the splits into numpy arrays
x_train, y_train = np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1)
x_val, y_val = np.array(x_val).reshape(-1,1), np.array(y_val).reshape(-1,1)
x_test, y_test = np.array(x_test).reshape(-1,1), np.array(y_test).reshape(-1,1)

# create a model object from the linear_model class
W_size = models.calc_features(np.array([[0]]), choice=feat_type, param=param).shape[1]
learning_model = models.linear_model(W_size=W_size, lr=lr, init=weight_init) 

no_epochs = 200

# train the model
feat_train = models.calc_features(x_train, choice=feat_type, param=param)
for epoch in range(no_epochs):
    
    # forward pass: calculate the model's prediction on training data
    y_pred_train = learning_model.forward(feat_train)

    # backward pass: train the linear regression model, using gradient descent
    learning_model.backward(y_train, y_pred_train, feat_train)

# compute loss on test data
feat_test = models.calc_features(x_test, choice=feat_type, param=param)
y_pred_test = learning_model.forward(feat_test)
loss_test_unknown = utils.loss(y_test, y_pred_test)  



print('linear: ', loss_test_linear)
print('poly: ', loss_test_poly)
print('periodic: ', loss_test_periodic)
print('unknown: ', loss_test_unknown)
