from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from .utils import rand,formatInputData
import pandas as pd
import os

# Create your views here.

def home(request):
    
    if request.method == "POST":
        #file root
        root = os.path.dirname(os.path.abspath(__file__))

        fixedVar1 = request.POST["Fixed Var 1"]
        fixedVar1 = formatInputData(fixedVar1)
        
        fixedVar2 = request.POST["Fixed Var 2"]
        fixedVar2 = formatInputData(fixedVar2)

        var1 = request.POST["Var 1"]
        var1 = formatInputData(var1)

        var2 = request.POST["Var 2"]
        var2 = formatInputData(var2)

        var3 = request.POST["Var 3"]
        var3 = formatInputData(var3)

        if var2[0] <= var1[0] or var3[0] <= var2[0]:
            return render(request, 'core/result.html')
        
        value = []
        for i in fixedVar1:
            for j in fixedVar2:
                #check if value of first col is greater than the second col
                if i >= j :
                    continue
                # create a dataframe for each value if i and j and append it to the existing csv
                value.append(rand(i,j,var1,var2,var3))

        df1 = pd.DataFrame(value)
        df1.to_csv(f"{root}\static\core\combinations.csv",index=False)
        
        
        return redirect('result')
        
    context = {}
    return render(request, 'core/index.html',context)


def result(request):
    root = os.path.dirname(os.path.abspath(__file__))
    file_location = f"{root}\static\core\combinations.csv"
    return serve(request, os.path.basename(file_location), os.path.dirname(file_location))