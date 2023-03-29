import cv2 as cv2


cam = cv2.VideoCapture(0)

while True:
     
    result, img = cam.read()

    
    # img = cv2.imread('input.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray,50,255,0)
    contours,_ = cv2.findContours(threshold, 1, 2)
    
    i = 0
    for contour in contours:
    
    
        if i == 0:
            i = 1
            continue
    
    
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)
        
        
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
    
    
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
    

        # if len(approx) == 3:
        #     cv2.putText(img, 'Triangle', (x, y),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        # elif len(approx) == 4:
        #     cv2.putText(img, 'Quadrilateral', (x, y),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        # elif len(approx) == 5:
        #     cv2.putText(img, 'Pentagon', (x, y),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        # elif len(approx) == 6:
        #     cv2.putText(img, 'Hexagon', (x, y),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        # else:
        #     cv2.putText(img, 'Circle', (x, y),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    

    cv2.imshow('input.png', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()




