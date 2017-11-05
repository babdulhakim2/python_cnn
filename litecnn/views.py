from django.shortcuts import render
from django.http import JsonResponse

from .preprocessor import Preprocessor as img_prep
from .alpha_cnn_predict import LiteOCR



# Create your views here.


def home(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})



def post_img(request):
	# print("request")
	# print(request.GET.get('imgURI'))
	data = request.GET.get('imgURI')
	index = request.GET.get('index')
	# print("abdul")
	pp = img_prep(fn="dataset.txt")
	ocr = LiteOCR(fn="litecnn/alpha_weights.pkl")
	# print("result")
	char_prediction= ocr.predict(pp.preprocess(data))
	# print(char_prediction)
	# result = "You entered a: " + char_prediction
	data ={"result":char_prediction}
	return JsonResponse(data)