import cv2
p = cv2.imread(r'D:\big3data\down\wulian\poseanalysis\UI\pic\bk.png')
enlarge = cv2.resize(p, (800, 600), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(r'D:\big3data\down\wulian\poseanalysis\UI\pic\bkres.png',enlarge)