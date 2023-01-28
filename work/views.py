from django.shortcuts import render
from django.http import HttpResponse
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
import numpy
import scrypt
# Create your views here.
@csrf_exempt
def uploadImage(request):
    if request.method == "POST":
        # pic = request.FILES['image']
        # print(pic)
        # img = cv2.imread(r'D:\ocr_learning\ocr pics\1.jpg') # r is used to escape symbols
        img = cv2.imdecode(numpy.fromstring(request.FILES['image'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)

        upload_folder= r'\upload'
        current_working_directory =os.getcwd()
        location = "".join([current_working_directory, upload_folder])
        os.chdir(location)
        print(location)

        # dir = location
        # for f in os.listdir(dir):
        #     os.remove(os.path.join(dir, f))
        
        cv2.imwrite('image.jpg',img)
        os.chdir(current_working_directory)
        return HttpResponse("Done")

@csrf_exempt
def runScrypt(request):
    if request.method == "POST":
        output = scrypt.runScriptPy()
        return HttpResponse(output)