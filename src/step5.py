import cv2

img = cv2.imread("input/image.png")

blur_img = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("blur" ,blur_img)
cv2.imwrite("output/blur.jpg", blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()