import cv2
img = cv2.imread("Solar.jpg")
cv2.putText(
    img,
    "Sun",
    (100,100),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=2,
    color=(0,0,255)
    )
cv2.putText(
    img,
    "Mercury",
    (100,170),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Venus",
    (180,260),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Earth",
    (270,150),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Mars",
    (380,270),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Jupiter",
    (500,100),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1.5,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Saturn",
    (780,300),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Uranus",
    (950,125),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.putText(
    img,
    "Neptune",
    (1100,300),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
    )
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("SolarWithName.jpg",img)
