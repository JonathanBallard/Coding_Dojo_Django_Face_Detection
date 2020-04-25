from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
import cv2 as cv
import sys
from django.conf.urls.static import static



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




















