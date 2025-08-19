import cv2

img = cv2.imread("input/nature.jpg")

edges = cv2.Canny(img,50,150)

cv2.imshow("man", img)
# cv2.imshow("edges", edges)

cv2.waitKey(0)

# blur

blur_img = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("blur" ,blur_img)
cv2.imwrite("output/blur.jpg", blur_img)
cv2.waitKey(0)

# threshold


# print(img)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imwrite("output/thresh.png", thresh)
# cv2.imshow("thres", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
