import cv2
import mediapipe as mp
import time

mpPose=mp.solutions.pose
pose=mpPose.Pose()

mpDraw=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
tipId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
pTime=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    #print(result.pose_landmarks)
    lmList=[]
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
        for id ,lm in enumerate(result.pose_landmarks.landmark):
            h,w,_=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            lmList.append([id,cx,cy])
            
            if id==13:
                cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
       
    if len(lmList)!=0:
        vucud=[] 
    
        if lmList[tipId[12]][2]<lmList[tipId[14]][2]:
            cv2.putText(img,"Sol el ust",(80,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        else:
            if lmList[tipId[12]][2]>lmList[tipId[14]][2]:
                    cv2.putText(img," ",(80,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        
        if lmList[tipId[11]][2]<lmList[tipId[13]][2]:
            cv2.putText(img,"Sag el ust",(80,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        else:
            if lmList[tipId[11]][2]>lmList[tipId[13]][2]:
                cv2.putText(img," ",(80,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
                
      
        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,"FPS:"+str(int(fps)),(10,65),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    
    cv2.imshow("img",img)
    cv2.waitKey(25)
