from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
   return  render(request,'home.html')
def task1(request):
    if request.method== "POST":
        string1=request.POST['string']
        l1="abcdefghijklmnopqrstuvwxyz"
        l2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        l3="1234567890"
        c=0
        for i in string1:
            if i in l1 :
                c=c+1
                break
        for i in string1:
            if i in l2:
                c = c + 1
                break
        for i in string1:
            if i in l3:
                c = c + 1
                break
        if c==3:
            return HttpResponse("yes,the string contains all characters")
        else:
            return HttpResponse("No the string doest not contain all characters")
def task2(request):
    if request.method == "POST":
        num1=request.POST['num1']
        num2=request.POST['num2']
        try:
            c=float(num1)/float(num2)
            return HttpResponse(c)
        except :
            return HttpResponse(" Mathematical error")
def task3(request):
    if request.method=="POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
        num1=int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        c1=complex(num1,num2)
        c2=complex(num3,num4)
        add=c1+c2
        sub=c1-c2
        product=c1*c2
        div=c1/c2
        s1="the adddition is {} and subraction is {} and product is {} and division is {}".format(add,sub,product,div)
        return HttpResponse (s1)






