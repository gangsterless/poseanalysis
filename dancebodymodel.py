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
import json
import cv2
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
def trainbody():

    # print(X_test)

    # model = logistic_regression_classifier(X_train,y_train)
    # model = knn_classifier(X_train,y_train)
    model = gradient_boosting_classifier(X_train,y_train)

    joblib.dump(model,'./model/danceGBDT.pkl')

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
    return model
# def test_model(test_data):
#     modelname = 'GBDT.pkl'
#     if not os.path.exists('./model/' + modelname):
#         print('还未训练'+modelname)
#         return
#     else:
#         clf = joblib.load('./model/'+modelname)
#         prediction = clf.predict(test_data)
#         print('预测结果为：')
#         print(prediction)
def predictframe(model):
    tagdict = {}
    total = 0
    right = 0
    for index, row in df.iterrows():
        #就用第二个吧
        framename = row[0].split('_')[0]
        if framename=='video':
            total+=1
            print('frame',row[0])
            vector =  np.array(row[1:-2]).reshape(1, -1)
            vector =  ss.transform(vector)
            preres = model.predict(vector)
            tagdict[row[0].split('_')[0]+'_'+row[0].split('_')[1]] = preres[0][2:-1]
            print('predict: ', preres,' real: ',row[-1])
            if preres==row[-1]:
                right +=1
    print(right/total)
    jsObj = json.dumps(tagdict)

    fileObject = open(r'video1dict.json', 'w')

    fileObject.write(jsObj)

    fileObject.close()
    return tagdict
#给图片打标签
def brandtag():
    jsdict = open("video1dict.json", encoding='utf-8')
    mydict = dict(json.load(jsdict))
    imgdir = r'D:\big3data\down\wulian\mydataset\testdance\video1res\videoimages'
    keyframeforvideo = set(mydict.keys())
    print('keys:')
    print(keyframeforvideo)
    print(len(keyframeforvideo))
    imgnames = os.listdir(imgdir)
    for each in imgnames:
        tag = each.split('_')[0]+'_'+each.split('_')[1]
        if tag in keyframeforvideo:
            bk_img = cv2.imread(imgdir+'/'+each)
            bk_img = cv2.resize(bk_img, (432 ,768), interpolation=cv2.INTER_CUBIC)
            bk_img = cv2.putText(bk_img, mydict[tag], (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('haha.jpg',bk_img)
            cv2.waitKey(0)
if __name__=="__main__":
    df = pd.read_csv('./data/dancedata/armres.csv')
    print(df.info())
    Y = df.iloc[:,22]
    print(Y)
    X = df.iloc[:, 1:-2]
    keyframeset = set(df.iloc[:,0])
    print(keyframeset)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)
    X_test = ss.transform(X_test)
    M = trainbody()
    tagdict = predictframe(M)
    # brandtag()

