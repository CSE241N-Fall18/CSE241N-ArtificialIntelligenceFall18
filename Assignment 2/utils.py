import numpy as np
import matplotlib.pyplot as plt
import random
import time
import json

def data_generator(generator_fn,
                   train_left=-1, train_right=1, train_size=256,
                   val_left=1.5, val_right=3.5, val_size=64,
                   test_left=2, test_right=3, test_size=64):
    '''
    Used for generating artificially synthesized data corresponding to the generator_fn()
    '''

    x_train = list(np.arange(train_left, train_right, (train_right-train_left)/(10*train_size)))
    x_train = random.sample(x_train, train_size)

    x_val = list(np.arange(val_left, val_right, (val_right-val_left)/(10*val_size)))
    x_val = random.sample(x_val, val_size)

    x_test = list(np.arange(test_left, test_right, (test_right-test_left)/(10*test_size)))
    x_test = random.sample(x_test, test_size)

    y_train = generator_fn(x_train)
    y_val = generator_fn(x_val)
    y_test = generator_fn(x_test)

    left_limit = min(train_left, train_right, val_left, val_right, test_left, test_right)
    right_limit = max(train_left, train_right, val_left, val_right, test_left, test_right)

    return (x_train, y_train, x_val, y_val, x_test, y_test, left_limit, right_limit) 

def sawtooth(X):
    Y = []
    for x in X:
        if int(x) % 2 == 0:
            Y.append(0 + 2*np.random.random())
        else:
            Y.append(10 + 2*np.random.random())
    return Y

def linear(X, W=0.3, b=2):
    Y = [W*x+b + 0.2*np.random.random() for x in X]
    return Y

def poly(X):
    Y = [3*x**3-2*x**2+4 + 20*np.random.random() for x in X]
    return Y


def plot(TRAIN_LOSS, VAL_LOSS, W_LIST,
               x_train, y_train, x_val, y_val,
               x_test, y_test, x_pred, y_pred):
    '''
    Plots graphs for learning curves, convergence of weights and a visualization of the model fit.

    INPUT:
    -----
    TRAIN_LOSS: Training loss after each epoch
    VAL_LOSS: Validation loss after each epoch
    W_LIST: collection of weight vector after epoch
    x_train, y_train: training data
    x_val, y_val: validation data
    x_test, y_test: test data
    x_pred, y_pred: predictions made by the model
    '''
    
    plt.figure()
    ax1 = plt.subplot(1,2,1)
    plt.plot(TRAIN_LOSS, label='training curve')
    plt.plot(VAL_LOSS, label='validation curve')
    ax1.set_title('Learning Curves')
    plt.xlabel('epochs')
    plt.ylabel('Error')
    ax1.legend()


    ax2 = plt.subplot(1,2,2)
    plt.plot(W_LIST)
    ax2.set_title('Convergence of Weight Vector')
    plt.xlabel('epochs')
    plt.ylabel('magnitude of weight vector components')


    plt.figure()
    plt.plot(x_pred, y_pred, color='r', label='model fit')
    plt.scatter(x_val, y_val, s=10, label='validation data') 
    plt.scatter(x_test, y_test, s=10, label='test data') 
    plt.scatter(x_train, y_train, s=10, label='training data') 
    plt.title('Visualization of the Model Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


# # compute loss on test data
# feat_test = utils.calc_features(x_test, choice=feat_type, param=param)
# y_pred_test = model.forward(feat_test)
# loss_test = model.loss(y_test, y_pred_test)  

def save_hyper(prob_name, feat_type, param, lr, weight_init):
    '''
    Saves the parameters tuned for different sub-problems of the assignment into a file.
    This file is later used for evaluation purposes.
    '''
    
    prob_dict = dict()
    prob_dict['feat_type'] = feat_type
    prob_dict['param'] = param
    prob_dict['lr'] = lr
    prob_dict['weight_init'] = weight_init

    filename = 'hyper_param.json'
    
    try:
        with open(filename, 'r') as fp:
            dict_hyper = json.load(fp)
    except:
        dict_hyper = dict()

    dict_hyper[prob_name] = prob_dict
    with open(filename, 'w') as fp:
        json.dump(dict_hyper, fp)


def loss(y_actl, y_pred):
    ''' 
    Calculation of loss while evaluating the assignment submissions.
    '''
    tmp = y_pred - y_actl
    l = np.dot(tmp.T, tmp)/(2*y_actl.shape[0])

    return l[0][0]
