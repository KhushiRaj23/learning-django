from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("<h1 style='color:red'>Welcome to homepage</h1>")

def homepage(request):
    return HttpResponse("""<h1 style='color:red'>Welcome to homepage</h1>
                        <h2 style='color:teal'>Welcome to homepage khushi</h2>
                        """)

def menuitem(request):
    item="cake"
    # return HttpResponse("The name of the item is: "+item)
    return HttpResponse(f"The name of the item is {item}")

def menuitems(request):
    items={
        'pizza':'Pizza costs Rs. 500',
        'Burger':'Burger costs Rs. 40',
        'noodles':'Noodles costs Rs. 120',
    }
    content ='<h1>Menu items</h1>'
    for item,description in items.items():
        content+=f'<li>{item} : {description}</li>'
    return HttpResponse(content)


def greet(req,name):
    return HttpResponse(f'Hello {name} ! Welcome to our website')    

def menuitems1(request,dish):
    items={
        'pizza':'Pizza costs Rs. 500',
        'burger':'Burger costs Rs. 40',
        'noodles':'Noodles costs Rs. 120',
    }
    description=items[dish]
    return HttpResponse(f'<h2>{dish}</h2>'+description)

def menuitems5(request,dish):
    items={
        'pizza':'Pizza costs Rs. 500',
        'burger':'Burger costs Rs. 40',
        'noodles':'Noodles costs Rs. 120',
    }
    if dish in items:
        description=items[dish]
        return HttpResponse(f'<h2>{dish}</h2>'+description)
    else:
        return HttpResponse(f'<h2>{dish}</h2>'+'Not found on the menu')



#  Dynamic UrL (Query Parameter)  => http://127.0.0.1:8000/recipe/?food=Biryani
def recipe(request):
    food=request.GET.get('food')
    if not food:
        return HttpResponse('<span style="color:red">Food parameter is missing</span>',status=404)
    return HttpResponse(f'Recipe is available for {food}')

def addition(request):
    val1=request.GET.get('v1')
    val2=request.GET.get('v2')
  # result=val1+val2
    result=int(val1)+int(val2)
    return HttpResponse(f'Result of addition is {result}')

def calculate(request,operation,v1,v2):
    
    if isinstance(v1,int) and isinstance(v2,int):
        if operation=='add':
            result=v1+v2
            return HttpResponse(f'{operation} result is {result}')
        elif operation=='subtract':
            result=v1 - v2
            return HttpResponse(f'{operation} result is {result}')
        elif operation=='multiply':
            result=v1*v2
            return HttpResponse(f'{operation} result is {result}')    
        elif operation=='divide':
            if v2==0:
                return HttpResponse("Cannot divide by zero")    
            else:
                result=v1/v2
                return HttpResponse(f'{operation} result is {result}')   
        else:
            return HttpResponse('Choose valid operation') 
    else:
        return HttpResponse("Enter number")            
                
        
def calculator(request):
    operation=request.GET.get('operation')
    val1=request.GET.get('v1')
    val2=request.GET.get('v2')
    
    try:
        val1=float(val1)
        val2=float(val2)
    except ValueError:
        return HttpResponse("Invalid value")
    
    if operation=='add':
        result=val1+val2
    elif operation=='subtract':
        result=val1-val2
    elif operation=='multiply':
        result=val1*val2
    elif operation=='divide':
        if val2==0:
            return HttpResponse("Cannot divide by ZERO!")
        else:
            result=val1/val2
    else:
        return HttpResponse("Invalid operation")
    return HttpResponse(f'Result of {operation} operation: {result}')

def user_profile(request,username):
    return HttpResponse(f'User profile: {username}')

def item_detail(request,item_id):
    return HttpResponse(f'Item ID: {item_id}')      
   
def restro_detail(request,category,subcategory):
    if subcategory=='':
        return HttpResponse(f'Category: {category} and Subcategory:Not provided')        
        
        # return HttpResponse(f'Category: {category} and Subcategory:<span style="color:red">Not provided</span>',status=404)        
    else:
        return HttpResponse(f'Category: {category} and Subcategory: {subcategory}')        
    
def home1(request):
    return render(request,'home.html') 


def menu(request):
    menuitem={'name':'noodles'}
    return render(request,'menu.html',menuitem)


def menu1(request):
    newmenu=[
        {'name':'noodles','price':65},
        {'name':'pizza','price':279},
        {'name':'Garlic Bread','price':'free'}
    ]
    return render(request,'menu1.html',{'mains':newmenu})


# template inheritance

items=[
    {'name':'Noodles','Cost':400,'Details':'Details for Noodles'},
    {'name':'Pizza','Cost':379,'Details':'Details for Pizza'},
    {'name':'Momos','Cost':'free','Details':'Details for Momos'},
    {'name':'Juice','Cost':68,'Details':'Details for Juice'},
    
]

def home2(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def menus(request):
    return render(request,'menuitems.html',{'items':items})
    

def menuitems2(request,item):
    singleItem={}
    for food in items:
        if food['name'] == item:
            singleItem=food
            break
    data={
        'item':singleItem
    }
    return render(request,'menuitems2.html',data)
          
# Returning form as HTTP response

from django.middleware.csrf import get_token

def simpleform(request):
    csrf_token=get_token(request)
    if request.method=="POST":
        textbox1=request.POST.get("textbox1")
        textbox2=request.POST.get("textbox2")
        return HttpResponse(f"The values are {textbox1} and {textbox2}")
    else:
        return HttpResponse(f"""
            <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}" >
                <label for="textbox1">Box 1:</label>
                <input id="textbox1" type="text" name="textbox1"><br><br>
                
                <label for="textbox2">Box 2:</label>
                <input id="textbox2" type="text" name="textbox2"><br><br>
                
                <input type="submit" value="Submit">
            </form>
        """) 
 

# HTML forms with Django templates

def templateform(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        if name and email and password:
            return HttpResponse(f"{name} your form submitted succefully")
    return render(request,'form.html')    

# Django forms
from .forms import InputForm

def formDjango(request):
    if request.method=="POST":
        form=InputForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            return HttpResponse(f" {name} Form Submitted successfully")
        return render(request,'djangoform.html',{'form':form})
    form=InputForm()
    return render(request,'djangoform.html',{'form':form})

# Form validation using customised error message with simple template 

def validation(request):
    Submitted_details=None
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        name_error=email_error=password_error=None
        if not name:
            name_error="Name is mandatory."
        if not email:
            email_error="Email is mandatroy."
        if not password:
            password_error="Password is mandatroy."
        if len(password)<6:
            password_error="password must be more than 6 characters"
        
        if name_error or email_error or password_error:
            return render(request,'validationform.html',{'name':name,'email':email,'password':password, 'name_error':name_error,'email_error':email_error,'password_error':password_error})
        Submitted_details={'name':name,'email':email,'password':password}
    return render(request,'validationform.html',{'Submitted_details':Submitted_details})
               
