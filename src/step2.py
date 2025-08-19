import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input/nature.jpg")

half = cv2.resize(img,(300,300))

# half_rgb = cv2.cvtColor(half, cv2.COLOR_BGR2RGB)

# # Show with matplotlib
# plt.imshow(half_rgb)
# plt.axis("off")
# plt.show()
cv2.imshow("imag",half)
cv2.waitKey(0)
cv2.destroyAllWindows()