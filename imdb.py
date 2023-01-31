import os

def load_imdb():
    X_train = []
    y_train = []

    path = 'tmp/aclImdb/train/pos/'
    X_train.extend([open(path + f).read() for f in os.listdir(path) if f.endswith('.txt')])
    y_train.extend([1 for _ in range(12500)])

    path = 'tmp/aclImdb/train/neg/'
    X_train.extend([open(path + f).read() for f in os.listdir(path) if f.endswith('.txt')])
    y_train.extend([0 for _ in range(12500)])

    X_test = []
    y_test = []
    
    path = 'tmp/aclImdb/test/pos/'
    X_test.extend([open(path + f).read() for f in os.listdir(path) if f.endswith('.txt')])
    y_test.extend([1 for _ in range(12500)])

    path = 'tmp/aclImdb/test/neg/'
    X_test.extend([open(path + f).read() for f in os.listdir(path) if f.endswith('.txt')])
    y_test.extend([0 for _ in range(12500)])
    
    return (X_train, y_train), (X_test, y_test)
