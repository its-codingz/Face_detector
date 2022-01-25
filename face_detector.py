import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')
image_ = input("Enter photo file name(with extension): ")
img = cv2.imread(image_)

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img , (x,y) , (x+w , y+h), (255,255,255), 2 )

cv2.imwrite("output.png",img)
print('Successfully saved')
