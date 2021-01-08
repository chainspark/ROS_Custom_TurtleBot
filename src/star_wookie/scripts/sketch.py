#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("rgbd_camera/rgb/image_my_opencv",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("rgbd_camera/rgb/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

		
    cv2.imshow('Sketch Window', cartoonize(cv_image, ksize=5,sketch_mode=True))
    cv2.imshow('Cartoonized Window', cartoonize(cv_image, ksize=5,sketch_mode=False))
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def cartoonize(img,ksize=5,sketch_mode=False):

	repetitions,sigma_color,sigma_space,ds_factor=10,5,7,4
	img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	img_gray=cv2.medianBlur(img_gray,11)

	edges =cv2.Laplacian(img_gray,cv2.CV_8U,ksize=ksize)
		
	#Sketch mask
	ret, mask =cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
	kernel = np.ones((3,3), np.uint8)
	mask_eroded = cv2.erode(mask, kernel, iterations=1)
	
	
	if sketch_mode:
		img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
		kernel = np.ones((3,3), np.uint8)
		img_eroded = cv2.erode(img_sketch, kernel, iterations=1)
		return cv2.medianBlur(img_eroded, ksize=5)
		

	for i in range(repetitions):
		img =cv2.bilateralFilter(img,ksize,sigma_color,sigma_space)

	dst = np.zeros(img_gray.shape)

	dst = cv2.bitwise_and(img,img,mask=mask_eroded)

	return dst

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
