
import cv2
import os
from moviepy.editor import VideoFileClip
import xlwt

curdir = os.path.dirname(os.path.dirname(__file__))
videodir = os.path.join(curdir,'poseimg/bixin')
class videocheck():

    def __init__(self):
        self.file_dir = videodir

    def get_filesize(self, filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    def get_file_times(self, filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time

    def sizeConvert(self, size):  # 单位换算
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(size / G) + 'G Bytes'
        elif size >= M:
            return str(size / M) + 'M Bytes'
        elif size >= K:
            return str(size / K) + 'K Bytes'
        else:
            return str(size) + 'Bytes'

    def timeConvert(self, size):  # 单位换算
        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒'
        if size < H:
            return u'%s分钟%s秒' % (int(size / M), int(size % M))
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt

    def get_all_file(self):
        u"""
        获取视频下所有的文件
        """
        for root, dirs, files in os.walk(videodir):
            return files  # 当前路径下所有非目录子文件



if __name__=='__main__':

    video = cv2.VideoCapture(videodir+'/02.flv') #读入视频文件
    videocheker = videocheck()
    last_time = videocheker.get_file_times(videodir+'/02.flv')
    print(last_time)
    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))


    c=0
    rval=video.isOpened()
    #timeF = 1  #视频帧计数间隔频率
    while rval:   #循环读取视频帧
        c = c + 1
        rval, frame = video.read()
    #    if(c%timeF == 0): #每隔timeF帧进行存储操作
    #        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
        if rval :
            if c>210 and c<300:
            #img为当前目录下新建的文件夹
                cv2.imwrite(videodir+'/'+'02_'+str(c) + '.jpg', frame) #存储为图像
            # cv2.waitKey(1):
            if c>300:
                break
    video.release();
