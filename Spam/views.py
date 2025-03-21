from django.shortcuts import render
from django.http import HttpResponse
import os
import joblib 

# If we're building a Django machine learning API, these imports help:

# render - Display results on a web page.
# HttpResponse - Send responses for API calls.
# os - Handle file paths for models or logs.
# joblib - Load and use trained machine learning models.

model1 = joblib.load(os.path.dirname(__file__) + "\\myModel.pk1")
model2 = joblib.load(os.path.dirname(__file__) + "\\mySVCModel2.pk1")

# Create your views here.
def index(request):
    return render(request, 'index.html')

def checkSpam(request):
    if(request.method =="POST"):
        finalAns = None
        algo = request.POST.get("algo")
        rawdata = request.POST.get("rawdata")

        if(algo == "Algo-1"):
            finalAns = model1.predict([rawdata])[0]
            param = {"answer" : finalAns}
        elif(algo == "Algo-2"):
            finalAns = model2.predict([rawdata])[0]
            param = {"answer" : finalAns}
        
        print(finalAns)
        return render(request, 'output.html', param)
    
    else:
        return render(request, 'index.html')
    

