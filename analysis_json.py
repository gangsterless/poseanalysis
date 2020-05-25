####分析手部节点json并建立一个数据集
#把raw_data的路径改成自己的就可以运行了

import json
import os
import numpy as np
import pandas as pd
HAND_POINT_COUNT=21
curdir = os.path.dirname(__file__)
jsonpdir = curdir + r'/poseimg/digit/raw_data'


def img_filter(myjson,imgname,thre=0.5):
    #手部有21个
    try:
        lhand = myjson['people'][0]['hand_left_keypoints_2d']
        rhand = myjson['people'][0]['hand_right_keypoints_2d']
    except:
        print('没找到'+imgname)
        return

    l_reslist = []
    r_reslist = []

    for i in range(HAND_POINT_COUNT):
        l_reslist.append((lhand[i*3],lhand[i*3+1],lhand[i*3+2]))
        r_reslist.append((rhand[i*3],rhand[i*3+1],rhand[i*3+2]))
    l_ave_score = np.mean([each[-1] for each in l_reslist])
    r_ave_score = np.mean([each[-1] for each in r_reslist])

    if l_ave_score >0.3:
        with open(curdir+'/poseimg/digit_raw_res/left_'+imgname+'.txt','w') as f:
            for sub in l_reslist:
                f.write(str(sub[0])+','+str(sub[1])+','+str(sub[2])+'\n')

    if r_ave_score >0.3:
        with open(curdir+'/poseimg/digit_raw_res/right_'+imgname+'.txt','w') as f:
            for sub in r_reslist:
                f.write(str(sub[0])+','+str(sub[1])+','+str(sub[2])+'\n')

    print(r_ave_score)
    print(l_ave_score)
def builddataset():
    jsondir = curdir + r'/poseimg/digit_raw_res'
    twenty_one_points_list = [[] for _ in range(HAND_POINT_COUNT)]
    print(twenty_one_points_list)
    txtfiles = os.listdir(jsondir)
    for each in txtfiles:
        sign = each.split('_')[2]
        directsign = 'left' if 'left' in each else 'right'
        with open(jsondir+'/'+each,'r') as f:
            for i,v  in enumerate(f.readlines()):
                twenty_one_points_list[i].append(v.strip()+','+directsign+','+sign)
    linec = len(twenty_one_points_list[0])
    with open('signres.csv', 'w') as ff:
        for l in range(linec):
            thisign = twenty_one_points_list[0][l].split(',')[-1]
            thisdirectsign =  twenty_one_points_list[0][l].split(',')[-2]
            for r in range(HAND_POINT_COUNT):
                eachsign =  twenty_one_points_list[r][l].split(',')[-1]
                eachdirectsign = twenty_one_points_list[0][l].split(',')[-2]
                assert eachsign==thisign
                assert thisdirectsign == eachdirectsign
                ff.write(','.join(twenty_one_points_list[r][l].split(',')[:-2]))
                #如果是最后一项
                if r==HAND_POINT_COUNT-1:
                    ff.write(','+thisdirectsign+','+thisign+'\n')
                else:
                    ff.write(',')
    #
    #     for each in twenty_one_points_list:
    #         ff.write(each+'\n')

    print(twenty_one_points_list)
def flip_and_save():
    df = pd.read_csv('signres.csv',header=None)
    #先把第一列，第二列搞出来
    flip_res = 720-df.iloc[:,0]
    flip_res = pd.concat((flip_res,df.iloc[:,1:3]),axis=1)
    # print(flip_res)
    for i in range(1,HAND_POINT_COUNT):
        colx = 720-df.iloc[:,i*3]
        coly = df.iloc[:, i * 3 + 1:i * 3 + 3]
        tmpres = pd.concat((colx,coly),axis=1)
        flip_res =  pd.concat((flip_res,tmpres),axis=1)
    flip_res =  pd.concat((flip_res,df.iloc[:,-2:]),axis=1)
    totalres = pd.concat((df,flip_res),axis=0)
    totalres.to_csv('total.csv',index=False)
    print(totalres)
    # print(df.describe())

if __name__=='__main__':
    #10个数字
    for i in range(10):
        jsondir = jsonpdir+'/'+str(i)+'/'
        jsonfiles = [each for each in os.listdir(jsondir) if each.split('.')[-1] == 'json']
        for each in jsonfiles:
            print('-' * 5 + each + '-' * 5)
            with open(jsondir + '/' + each, 'r') as f:
                jstest = f.read()
            jstest = eval(jstest)
            img_filter(jstest,imgname=each.split('.')[0])

    builddataset()
    flip_and_save()

