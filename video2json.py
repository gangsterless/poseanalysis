import os
from moviepy.editor import *
def writejson():
    fatherpath = r'D:\big3data\down\wulian\mydataset'
    eachperson = os.listdir(fatherpath)
    # print(eachperson)
    with open('generatejson.bat','w') as f:
        for each in eachperson:
            if each=='output':
                continue
            if not os.path.exists(os.path.join(fatherpath, 'output', each)):
                os.mkdir(os.path.join(fatherpath, 'output', each))
            eachmovementlist = [each.split('.')[0] for each in os.listdir(os.path.join(fatherpath,each))]
            for movment in eachmovementlist:
                if not os.path.exists(os.path.join(fatherpath, 'output', each,movment)):
                    os.mkdir(os.path.join(fatherpath, 'output', each,movment))
                nowjsondir = os.path.join(fatherpath, 'output', each, movment)
                videodir = os.path.join(fatherpath,each,movment+'.mp4')
                order = r'D:\big3data\down\wulian\openpose\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\openpose\bin\OpenPoseDemo.exe --video '+ videodir + ' --write_json '+ nowjsondir +' --hand '+ ' --face '+'\n'
                f.write(order)
                print(order)
def rotate90():
    rawfile = r'D:\big3data\down\wulian\mydataset\me-fa\six-both.mp4'
    res = 'res.mp4'
    video = VideoFileClip(rawfile)
    video = video.rotate(90)
    video.write_videofile(res)

if __name__=='__main__':
    # writejson()
    rotate90()