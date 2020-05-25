import json
import os
import numpy as np
# mydict= {'1':8,'2':9,'3':10,'6':11,'7':12,'8':13,'25':2,'26':3,'27':4,'17':5,'18':6,'19':7,'15':0,'24':1}
mydict = {'0':0,'6':4,'7':5,'8':6,'1':1,'2':2,'3':3,'20':7,'31':8,'13':9,'15':10,'25':14,'26':15,'27':16,'17':11,'18':12,'19':13}
def readjson(name):
     with open('../data/'+name) as js:
          jsres = js.read()
          jsres = eval(jsres)

          for i in range(len(jsres)):
               # if i>0:
               #      break
               eachlist = np.array([[0]*17]*3,dtype=float)
               eachdict = jsres[str(i)]
               # print(eachdict)
               for k,v in mydict.items():

                    for l in range(3):
                         # print(eachdict[str(mydict[k])]['translate'][l])
                         #脚太靠前
                         if  l==2:
                              if k=='7' or k=='8' or k=='2'or k=='3':
                                   eachlist[l][mydict[k]] = eachdict[k]['translate'][l] -100
                              else:
                                   eachlist[l][mydict[k]] = eachdict[k]['translate'][l]

                         # 把头抬起来,头一直低着
                         elif  l==1:
                              if k == '15':
                                   eachlist[l][mydict[k]]=eachdict[k]['translate'][l]+200
                              else:
                                   eachlist[l][mydict[k]] = eachdict[k]['translate'][l]
                         else:
                              eachlist[l][mydict[k]] = eachdict[k]['translate'][l]

               with open('../data/3dres/'+str(i)+'.txt','w') as f:
                    f.write(str(eachlist).replace(',',' '))


if __name__=='__main__':
     readjson('video2_3d_data.json')
