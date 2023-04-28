from django.shortcuts import render

# Create your views here.
def Built_in_Filter(request):
    import datetime
    DT=datetime.datetime.now()
    dt='How ArE you my DEaR FrIeND'
    d={'dt':dt,'DT':DT}
    return render (request,'Built_in_Filter.html',d)