from sklearn.model_selection import train_test_split

def train_test_split_func(df, testsize):

    X = df.drop(columns= df[-1])
    y = df[-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize)
    return X_train, X_test, y_train, y_test
