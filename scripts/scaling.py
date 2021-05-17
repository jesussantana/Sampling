# Variable Scaling

from sklearn.preprocessing import StandardScaler

def transform(X_train, X_test):

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    
    return X_train, X_test