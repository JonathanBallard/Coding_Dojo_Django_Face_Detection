from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
import cv2 as cv
import sys
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import os














# Create your views here. 
def index(request): 
    return render(request, 'face_app/index.html') 



def faceCheck(request):

    imgLoc = "C:\\Users\\Tax\Desktop\\CODING_DOJO\\Python\\django\\django_full_stack\\Face_Detection\\apps\\face_app\\static\\img\\pic.jpg"

    print("...................................................................")
    print(imgLoc)

    # read the image from filepath
    img = cv.imread(imgLoc)


    if img is None:
        print("************************************************************")
        print("Couldn't read image")
    else:
        print("==================================================================")
        print("Read image")

    # make a copy of the image
    cv.imwrite("saved_img.jpg", img)
    context = {
        "img" : img,
    }

    return render(request, 'face_app/face.html', context)





# define the path to the face detector
# FACE_DETECTOR_PATH = "{base_path}\\cascades\\haarcascade_frontalface_default.xml".format(
# 	base_path=os.path.abspath(os.path.dirname(__file__)))
    
FACE_DETECTOR_PATH = "C:\\Users\\Tax\\Desktop\\CODING_DOJO\\Python\\django\\django_full_stack\\Face_Detection\\apps\\face_app\\cascades\\haarcascade_frontalface_default.xml"
@csrf_exempt

def detect(request):
	print('base path')
	print(FACE_DETECTOR_PATH)
	# initialize the data dictionary to be returned by the request
	data = {"success": False}
	# check to see if this is a post request
	# if request.method == "POST":
	if request.method == "GET":
		print('___________________________________________________________________')
		print('METHOD GET')
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])
		# otherwise, assume that a URL was passed in
		else:
			print('___________________________________________________________________')
			print('ELSE')
			# grab the URL from the request
			# url = request.POST.get("url", None)
			# # if the URL is None, then return an error
			# if url is None:
			# 	data["error"] = "No URL provided."
			# 	return JsonResponse(data)
			# load the image and convert
			image = _grab_image(url="https://pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg")
		# convert the image to grayscale, load the face cascade detector,
		# and detect faces in the image
		image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
		detector = cv.CascadeClassifier(FACE_DETECTOR_PATH)
		rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv.CASCADE_SCALE_IMAGE)
		# construct a list of bounding boxes from the detection
		rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
		# update the data dictionary with the faces detected
		print('___________________________________________________________________')
		print('face IDENTIFIED')
		data.update({"num_faces": len(rects), "faces": rects, "success": True})
	# return a JSON response
	return JsonResponse(data)


def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv.imread(path)
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.request.urlopen(url)
			data = resp.read()
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv.imdecode(image, cv.IMREAD_COLOR)
	url = 'https://pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg'
	resp = urllib.request.urlopen(url)
	data = resp.read()
	image = np.asarray(bytearray(data), dtype="uint8")
	image = cv.imdecode(image, cv.IMREAD_COLOR)
    
    
 
	# return the image
	return image














