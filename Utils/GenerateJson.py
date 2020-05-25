from config import OPENPOSE_DIR,BASE_DIR
import os
from subprocess import run
import psutil
import signal
#调用openpose 生成json
#用于生成图片和json文件
def generatefile(videodir,videoname):
    videorawname = videoname
    #如果有后缀就先去掉后缀
    if '.' in videoname:
        videoname = videoname.split('.')[0]
    imgdir = os.path.join(BASE_DIR,'data/openposeresult', videoname, 'img')
    jsdir = os.path.join(BASE_DIR,'data/openposeresult', videoname, 'json')
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)
    if not os.path.exists(jsdir):
        os.makedirs(jsdir)
    #此处调用命令行工具，先转到对应的盘符
    rootdisc = OPENPOSE_DIR.split(':')[0]+':'
    #生成openpose命令
    cmdop = rootdisc+ '&&'+'cd ' + OPENPOSE_DIR+'&&'
    cmdop += 'OpenPoseDemo.exe '+' --video '+ videodir+'/'+videorawname +' --write_json '+ jsdir +' --write_images ' + imgdir + ' --display 0 ' +' --hand '
    print(cmdop)
    os.system(cmdop)

def webcam():
    rootdisc = OPENPOSE_DIR.split(':')[0] + ':'
    cmdop = rootdisc + '&&' + 'cd ' + OPENPOSE_DIR + '&&'
    cmdop += 'OpenPoseDemo.exe --hand'
    print(cmdop)
    os.system(cmdop)
def killopenpose():

    def getAllPid():
        pid_dict = {}
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            pid_dict[pid] = p.name()
            # print("pid-%d,pname-%s" %(pid,p.name()))
        return pid_dict

    dic = getAllPid()
    def kill(pid):
        try:
            kill_pid = os.kill(pid, signal.SIGABRT)
            print('已杀死pid为%s的进程%s,　返回值是:%s' % (pid,dic[pid] ,kill_pid))
        except Exception as e:
            print('没有如此进程!!!')

    for t in dic.keys():
        if dic[t] == "OpenPoseDemo.exe":
            kill(t)
            break

if __name__=='__main__':
    generatefile(r'D:\big3data\down\wulian\mydataset\testdance', 'video.mp4')
    # pass