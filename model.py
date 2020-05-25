import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.externals import joblib
from sklearn import linear_model
import os
import torch
import numpy as np

df = pd.read_csv('total.csv')
Y = df['64']
X = df.iloc[:, :-2]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
def logistic_regression_classifier(train_x, train_y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l2')
    model.fit(train_x, train_y)
    return model
def knn_classifier(train_x, train_y):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(train_x, train_y)
    return model
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(train_x, train_y)
    return model
def mytrain():

    # print(X_test)

    # model = logistic_regression_classifier(X_train,y_train)
    # model = knn_classifier(X_train,y_train)
    model = gradient_boosting_classifier(X_train,y_train)

    joblib.dump(model,'./model/GBDT.pkl')
    prediction = model.predict(X_test)
    recall = metrics.recall_score(y_test, prediction,average="micro")
    precision = metrics.precision_score(y_test, prediction,average="micro")
    print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))
    accuracy = metrics.accuracy_score(y_test, prediction)
    print('accuracy: %.2f%%' % (100 * accuracy))
    print('real res:')
    print(list(y_test))
    print('predict res:')
    print(prediction)
def test_model(test_data):
    modelname = 'GBDT.pkl'
    if not os.path.exists('./model/' + modelname):
        print('还未训练'+modelname)
        return
    else:
        clf = joblib.load('./model/'+modelname)
        prediction = clf.predict(test_data)
        print('预测结果为：')
        print(prediction)
if __name__=="__main__":
    mytrain()
    #用事实说话，
    # 找一个666的
    # fp = r'D:\big3data\down\wulian\poseanalysis\poseimg\digit_raw_res\left_digit_6_000000000162_keypoints.txt'
    # vectors = []
    # with open(fp,'r') as f:
    #     for l in f.readlines():
    #         vectors.extend(l.strip().split(','))
    #
    # vectors = np.array(vectors).reshape(1,-1)
    # print(vectors)
    # vectors = ss.transform(vectors)
    # print(vectors)
    # test_model(vectors)
