from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
import numpy
import scrypt

# Create your views here.
@csrf_exempt
def uploadImage(request):
    if request.method == "POST":
        # img = cv2.imread(r'D:\ocr_learning\ocr pics\1.jpg') # r is used to escape symbols

        pic = request.FILES['image_name']
        # print(pic)
        img = cv2.imdecode(numpy.fromstring(pic.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        image_name = request.FILES['image_name'].name
        extension = (image_name.split('.'))[1]

        upload_folder= r'\upload'
        current_working_directory =os.getcwd()
        location = "".join([current_working_directory, upload_folder])
        os.chdir(location)

        # empty upload folder before saving new pic
        dir = location
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        
        cv2.imwrite('image.'+extension,img)
        os.chdir(current_working_directory)
        return HttpResponse("Done")

@csrf_exempt
def runScrypt(request):
    if request.method == "POST":
        output = scrypt.runScriptPy()
        
        run_folder= r'\run'
        current_working_directory =os.getcwd()
        location = "".join([current_working_directory, run_folder])
        os.chdir(location)

        # need to send base64 image to frontend
        import base64
        image_path = os.listdir(location)[0]
        with open(image_path, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        json_data = {'output': output['out_str'], 'img': my_string.decode('utf-8') , 'ext':output['ext']}
        os.chdir(current_working_directory)
        return JsonResponse(json_data)