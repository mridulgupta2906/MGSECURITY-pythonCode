
# for understanding the code contact https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/




from pyimagesearch.anpr import PyImageSearchANPR
from imutils import paths
import argparse
import imutils
import cv2
import requests
from PIL import Image
import base64
# import pybase64 as base64
from io import BytesIO


def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input directory of images")
ap.add_argument("-c", "--clear-border", type=int, default=-1,
	help="whether or to clear border pixels before OCR'ing")
ap.add_argument("-p", "--psm", type=int, default=7,
	help="default PSM mode for OCR'ing license plates")
ap.add_argument("-d", "--debug", type=int, default=-1,
	help="whether or not to show additional visualizations")
args = vars(ap.parse_args())

# initialize our ANPR class
anpr = PyImageSearchANPR(debug=args["debug"] > 0)

# grab all image paths in the input directory
imagePaths = sorted(list(paths.list_images(args["input"])))

# loop over all image paths in the input directory
url='https://mgsecurity.herokuapp.com/vehicleEntryInLogs'
uro='http://localhost:3000/image'
for imagePath in imagePaths:
	# load the input image from disk and resize it
	image = cv2.imread(imagePath)



	 # create image buffer
	image1 = open(imagePath,'rb')
	# image_read=image1.read()
	imgbuffer=base64.b64encode(image1.read()).decode('utf-8')
	# imgbuffer=base64.encodestring(image_read)
	# print("image buffer  ",imgbuffer)


	image = imutils.resize(image, width=600)
	# print(image)
	# apply automatic license plate recognition
	(lpText, lpCnt) = anpr.find_and_ocr(image, psm=args["psm"],
		clearBorder=args["clear_border"] > 0)

	# only continue if the license plate was successfully OCR'd
	if lpText is not None and lpCnt is not None:

		# show the output ANPR image
		myobj={'numberplate':format(lpText),'imgbuffer':imgbuffer}
		# print("hello ",format(lpText))
		print("[INFO] {}".format(lpText))
		x = requests.post(url, data=myobj)
		# cv2.imshow("Output ANPR", image)
		cv2.waitKey(0)



# python ocr_license_plate.py --input license_plates/group2 --clear-border 1

