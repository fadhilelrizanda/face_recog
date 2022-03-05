import cv2
import datetime


video = cv2.VideoCapture(0)

# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2
shoot = 0

while 1:
    date_name = datetime.datetime.now().strftime("%Y%m%d%I%M%S")
    file_name = "./data_output/"+date_name+".jpg"
    ret, frame = video.read()
    frame = cv2.putText(frame, f"Shoot [ {shoot} ]", org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Absensi", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(file_name, frame)
        break
    if cv2.waitKey(1) & 0xFF == ord('z'):
        cv2.imwrite(file_name, frame)
        shoot += 1


video.release()
cv2.destroyAllWindows()
