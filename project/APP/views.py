from django.shortcuts import render

# Create your views here.

def home(request, pk):
    data={
       "data1":pk,
    }
    return render(request, 'home1.html', data )

def integer(request, pk):
    data=pk
    return render(request, 'home.html', {'key':data})

def string(request, pk):
    data=pk
    return render(request, 'home.html', {'key':data})

def slugs(request, pk):
    data=pk
    return render(request, 'home.html', {'key':data})

def paths(request, pk):
    data=pk
    return render(request, 'home.html', {'key':data})

def combination(request,pk,abcst,abc,st):

    data={'data1':pk,
          'data2':abcst,
          'data3':abc,
          'data4':st, 
        }
    return render(request, 'home1.html', data)