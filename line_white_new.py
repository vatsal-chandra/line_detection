import cv2
import numpy as np

video = cv2.VideoCapture("black_white_road.mp4")

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("black_white_road.mp4")
        continue

    #hsv
    new_frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv= cv2.cvtColor(new_frame, cv2.COLOR_BGR2HSV)

    #canny
    lower_white = np.array([0, 0, 212])
    upper_white = np.array([131, 255, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    edges = cv2.Canny(mask, 75, 150)

    ###ROI  (not suitable for the video i have used)
    #height = edges.shape[0]    
    #polygon = np.array([
    #    [(0,400) ,(1600,height),(200,0 ),(1600,0)]
    #   ])
    #mask2 = np.zeros_like(edges)
    #cv2.fillPoly(mask2, polygon, 255)
    #masked = cv2.bitwise_and(mask2, edges)
    #lines = cv2.HoughLinesP(masked, 1, np.pi/180, 50, maxLineGap=50)

    #houghlines  (if using roi, then comment this section as the code already exists in roi)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

        
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(new_frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            cv2.imshow("frame", new_frame)
    #cv2.imshow("edges", edges)
    if cv2.waitKey(1) & 0xFF == ord(' '):     #end video with spacebar
        break
    
video.release()
cv2.destroyAllWindows()
