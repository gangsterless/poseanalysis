#把跳舞的数据集建立出来，把符合要求的图片对应的json弄出来
import os
import numpy as np
from shutil import copyfile
f_dir = r'D:\big3data\down\wulian\mydataset'
handpose = ('1','2','3','6','good','ok','2handheart')
handpose = ('1','2','3','6','good','ok')
bodypose = ('1handup','2handflat','2handtoge','2handup')
HAND_POINT_COUNT =21
def copydata():
    for i in range(1,3):
        src_js_dir = r'D:\big3data\down\wulian\mydataset\testdance'+'\json'+str(i)
        if not os.path.exists(os.path.join(f_dir,'dancejsres','video'+str(i))):
            os.mkdir(os.path.join(f_dir,'dancejsres','video'+str(i)))

        each = os.path.join(f_dir,'dancejsres','video'+str(i))
        for name in handpose+bodypose:
            thisdir = os.path.join(each,name)
            if not os.path.exists(thisdir):
                os.mkdir(thisdir)
            thistarjsnamels = os.listdir(os.path.join(f_dir,'poseimgs','video'+str(i),name))
            thistarjsnamels = [each.split('_')[0]+'_'+each.split('_')[1]+'_'+'keypoints.json' for each in thistarjsnamels]
            for sub in thistarjsnamels:
                copyfile(os.path.join(src_js_dir,sub), os.path.join(thisdir,sub))

#一些无意义动作


#保证鲁棒性，对任何输入情况都要可以处理
def init():

    def info_extractor(myjson, imgname, bodysign,handsign,thre=0.3):
        # 手部有21个
        #跟腿部没关系所以不检测腿部
        seven_parts_list = []
        l_reslist = []
        r_reslist = []
        infodict = {'frame':imgname,'lhand':[],'rhand':[],'7parts':[]}
        try:
            lhand = myjson['people'][0]['hand_left_keypoints_2d']
            rhand = myjson['people'][0]['hand_right_keypoints_2d']
        except:
            print('没找到手部信息' + imgname)

        for i in range(HAND_POINT_COUNT):
            l_reslist.append((lhand[i * 3], lhand[i * 3 + 1], lhand[i * 3 + 2]))
            r_reslist.append((rhand[i * 3], rhand[i * 3 + 1], rhand[i * 3 + 2]))
        l_ave_score = np.mean([each[-1] for each in l_reslist])
        r_ave_score = np.mean([each[-1] for each in r_reslist])
        tardir = os.path.join(f_dir,'danceTXT','video'+str(i))
        #说明没有检测到
        if l_ave_score==0:

            # print('没左手')
            pass
        elif l_ave_score>thre:
           infodict['lhand'] = l_reslist+[handsign]
        if r_ave_score==0:
            # print('没右手')
            pass
        elif r_ave_score>thre:
            infodict['rhand'] = r_reslist+[handsign]
        try:
            keyparts = myjson['people'][0]['pose_keypoints_2d'][1 * 3:8 * 3] + [bodysign]
            score = 0
            for k in range(7):
                score += keyparts[k * 3 + 2]
            score /= 7
            if score > thre:
                seven_parts_list = keyparts
                infodict['7parts'] = seven_parts_list

        except:
            print('没找到上身的7部分')
        return infodict
    #手部动作的reslist
    handreslist = []
    #胳膊的reslist
    armreslist = []
    for i in range(1, 6):

        if not os.path.exists(os.path.join(f_dir,'danceTXT','video'+str(i))):
            os.mkdir(os.path.join(f_dir,'danceTXT','video'+str(i)))
        else:
           subdir = os.path.join(f_dir,'danceTXT','video'+str(i))
           for sub in handpose:

                handsign = sub
                bodysign = 'NULL'
                eachposesrcdir = os.path.join(f_dir,'dancejsres','video'+str(i),sub)
                jslist = os.listdir(eachposesrcdir)
                for s in jslist:
                    thisjson = open(eachposesrcdir+'/'+s)
                    res =info_extractor(eval(thisjson.read()),s,bodysign,handsign)
                    handreslist.append(res)

           for sub in bodypose:
                handsign = 'NULL'
                bodysign = sub
                eachposesrcdir = os.path.join(f_dir, 'dancejsres', 'video' + str(i), sub)
                jslist = os.listdir(eachposesrcdir)
                for s in jslist:
                    thisjson = open(eachposesrcdir+'/'+s)
                    res =info_extractor(eval(thisjson.read()),s,bodysign,handsign)
                    armreslist.append(res)

    with open('handres.csv','w') as f:

        for each in handreslist:
            subs1 = [each['frame']]
            subs2 = [each['frame']]
            if  each['lhand'] and each['lhand'][-1]!='NULL':
                for ix in range(len(each['lhand'])):
                    if ix !=len(each['lhand'])-1:
                        for subsub in each['lhand'][ix]:
                            subs1.append(subsub)
                    else:
                        subs1.append(each['lhand'][ix])
                f.write(str(subs1)[1:-1]+'\n')

            if each['rhand'] and each['rhand'][-1]!='NULL':
                for ix in range(len(each['rhand'])):
                    if ix !=len(each['rhand'])-1:
                        for subsub in each['rhand'][ix]:
                            subs2.append(subsub)
                    else:
                        subs2.append(each['rhand'][ix])
                f.write(str(subs2)[1:-1]+'\n')
    with open('armres.csv','w') as f:
        for each in armreslist:

            if each['7parts'] and each['7parts'][-1]!='NULL':
                f.write(each['frame']+','+str(each['7parts'])[1:-1]+'\n')


if __name__=='__main__':
    #copydata()
    init()

    pass

