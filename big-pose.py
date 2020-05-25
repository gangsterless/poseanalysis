import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.externals import joblib
from sklearn import linear_model
from model import gradient_boosting_classifier
import pickle
HAND_POINT_COUNT=21

#big pose 有 大型比心，strong,双掌合十
#经过检查 利用的是body_25,有25个节点
#大型比心 至少有1,2,3,4,5,6,7 strong，双掌合十都差不多，那我们暂时就先弄这7个
fatherdir = r'D:\big3data\down\wulian\mydataset\altitude-dataset'
def regularit(df):
    newDataFrame = pd.DataFrame(index=df.index)
    columns = df.columns.tolist()
    for c in columns:
        d = df[c]
        MAX = d.max()
        MIN = d.min()
        newDataFrame[c] = ((d - MIN) / (MAX - MIN)).tolist()
    return newDataFrame

def json_filter(people):
    ###大型动作
    big_pose = {'big-heart','clapping','strong-both','jump'}
    seven_parts_list = []
    for each in big_pose:
        this_big_pose_list = os.listdir(os.path.join(fatherdir,people,each))

    # print(big_heart_json_list)
        for ix,v in enumerate(this_big_pose_list):
            # if ix>0:
            #     break
            with open(os.path.join(fatherdir,people,each,v)) as js:
                js = js.read()
            jsres = eval(js)

            try:
                keyparts = jsres['people'][0]['pose_keypoints_2d'][1*3:8*3]+[each]
                score = 0
                for k in range(7):
                    score+=keyparts[k*3+2]
                score/=7
                if score>0.3:
                    seven_parts_list.append(keyparts)
            except:
                print('没找到,' + v)

    seven_parts_df = pd.DataFrame(seven_parts_list)
    # print(seven_parts_df)
    seven_parts_df_data = seven_parts_df.iloc[:,0:-1]
    seven_parts_df_flag = seven_parts_df.iloc[:,-1]
    seven_parts_df_normal = regularit(seven_parts_df_data)
    seven_parts_df_normal = pd.concat((seven_parts_df_normal,seven_parts_df_flag),axis=1)
    return  seven_parts_df_normal
def test_model():
    test_data = json_filter('gmz-bf')
    model = joblib.load('./model/bigpose-GBDT.pkl')
    prediction = model.predict(test_data.iloc[:,0:-1])
    print(prediction)
    precision = metrics.precision_score(test_data.iloc[:,-1], prediction, average="micro")
    print('precision: %.2f%%' % (100 * precision))
def big_pose_model():
    seven_parts_df_normal = json_filter('gmz-bf')
    seven_parts_df_normal = pd.concat((seven_parts_df_normal,json_filter('lbq-bf-mom')))

    Y = seven_parts_df_normal.iloc[:,-1]
    X = seven_parts_df_normal.iloc[:, 0:-1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    model = gradient_boosting_classifier(X_train, y_train)
    # if not os.path.exists('./model/bigpose-GBDT.pkl'):
    #     joblib.dump(model, './model/bigpose-GBDT.pkl')
    joblib.dump(model, './model/bigpose-GBDT.pkl')
    prediction = model.predict(X_test)
    print(prediction)
    recall = metrics.recall_score(y_test, prediction, average="micro")
    precision = metrics.precision_score(y_test, prediction, average="micro")

    print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))
    accuracy = metrics.accuracy_score(y_test, prediction)
    # print('accuracy: %.2f%%' % (100 * accuracy))
    # print('real res:')
    # print(list(y_test))
    # print('predict res:')
    # # print(prediction)
if __name__=='__main__':
    # json_filter()
    big_pose_model()
    test_model()