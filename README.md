<h1>COURSE CONTENT</h1>

[<h2>1.1 Course Description</h2>](#one)

<li>1.2 Why learn Django?</li>

[<h2>2 Django Course Content</h2>](#two)
[<p>2.1 Introduction to Web</p>](#three)
[<p>2.2 Django Web Framework</p>](#four)
[<p>2.3 Getting Started with Django</p>](#five)
[<p>2.4 URLs and Views</p>](#six)
[<p>2.5 URL dispatcher</p>](#seven)
[<p>2.6 Django Templates</p>](#eight)
[<p>2.7 Working with Static Files</p>](#nine)
[<p>2.8 DJANGO MODEL</p>](#ten)
[<p>2.9 Relationships in Django Models</p>](#eleven)
[<p>2.10 Django Forms or Model Forms</p>](#twelve)
[<p>2.11 Django Form Validation</p>](#thirteen)
[<p>2.12 Django’s Inbuilt Core Validators</p>](#fourteen)
[<p>2.13 Model Based Forms</p>](#fifteen)
[<p>2.14 Advanced Templates</p>](#sixteen)
[<p>2.15 Session Management in Django</p>](#seventeen)
[<p>2.16 Authentication & Authorization</p>](#eighteen)
[<p>2.17 Class Based Views (CBV)</p>](#nineteen)
[<p>2.18 Django File Upload</p>](#twenty)
[<p>2.19 Django CRUD Operations</p>](#twenty_one)
[<p>2.20 Django Middleware</p>](#twenty_two)
[<p>2.21 How to Send Email in a Django</p>](#twenty_three)
[<p>2.22 Outputting CSV with Django</p>](#twenty_four)
[<p>2.23 Outputting PDF with Django</p>](#twenty_five)
https://simpleisbetterthancomplex.com/tutorial/2016/08/08/how-to-export-to-pdf.html
[<p>2.24 Django Crispy Forms</p>](#twenty_six)
[<p>2.25 GIT & Github</p>](#twenty_seven)
[<p>2.26 Bitbucket</p>](#twenty_eight)
[<p>2.27 Deploying Django Apps & Heroku</p>](#twenty_nine)
[<p>2.28 Introduction to Web Services</p>](#thirty)
[<p>2.29 Introduction to XML</p>](#thirty_one)
[<p>2.30 Introduction to REST API(Restful Services)</p>](#thirty_two)
[<p>2.31 Connect with MySql</p>](#thirty_three)
[<p>2.32 Connecting with PostgreSql(Restful Services)</p>](#thirty_four)
[<p>List of errors when performing the practical</p>](#thirty_five)
[<p>Extra</p>](#thirty_six)

-----------------------------
<a name="one"><h2>1.1 Course Description</h2></a><br>
Django is PYTHON MVT web framework. It highly demands in the current market to build rapid web applications. It is suitable to develop large projects in less time. It is highly secured and scalable. Django is a Python based full stack web development framework means it is used to develop full-fledged websites in Python. It encourages rapid development and advocates pragmatic and clean code. Attend Django training demo by our real time experts with real time scenarios.<br>

1.2 Why learn Django?<br>
Django takes care of much of the hassle of Web development. It’s free and open source. Django Course was designed to help developers take applications from concept to completion as quickly as possible.<br>

<a name="two"><h2>2 Django Course Content</h2></a><br>
<a name="three"><h2>2.1 Introduction to Web</h2></a>
  
HTML5, CSS3, BOOTSTRAP5 -> link : <br>
  
<a name="four"><h2>2.2 Django Web Framework</h2></a><br>
![Django-Architecture-Diagram](https://user-images.githubusercontent.com/59610617/127650199-5c3b68a8-f16d-43f5-bb7c-909bd13f37e4.jpg)<br>
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.<br>

<b>Ridiculously fast.</b><br>
Django was designed to help developers take applications from concept to completion as quickly as possible.

<b>Reassuringly secure.</b><br>
Django takes security seriously and helps developers avoid many common security mistakes.

<b>Exceedingly scalable.</b><br>
Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

<a name="five"><h2>2.3 Getting Started with Django</h2></a><br>
Django Project structure.<br>
![structure_drawing2_new](https://user-images.githubusercontent.com/59610617/127651090-718b540a-754a-4f72-9f3a-7c6081edf9dc.png)<br>
Creating first project in VS code editor.<br>
<pre>
Step 1: create project folder -> ctrl+right click -> open Windows PowerShell here
Step 2: in powershell type >django-admin startproject ProjectName(eg GymProject)
It will create a project name folder : and inside it there will be:
<li>GymProject</li>
<li>manage.py</li>
NOTE: type django-admin to see all commands<br>
django-admin is Django's command-line utility for administrative tasks. ... In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project's settings.py file.<br>

Now open this project in vscode
Inside GymProject folder it will have.
<li>__init__.py</li>
<li>asgi.py</li>
<li>settings.py</li>
<li>urls.py</li>
<li>wsgi.py</li>
<li>manage.py</li>
</pre>

Description of all the files are:<br>
>__init__.py<br>
The __init__.py file lets the Python interpreter know that a directory contains code for a Python module. An __init__.py file can be blank.<br><br>
>asgi.py<br>
Asynchronous Server Gateway Interface, used for deploying purpose.<br><br>
>wsgi.py<br>
web server getway interface, It is used to forward requests from a web server (such as Apache or NGINX) to a backend Python web application or framework. From there, responses are then passed back to the webserver to reply to the requestor.<br>
>urls.py<br>
List of urls. It's where you define the mapping between URLs and views.<br><br>
>manage.py<br>
A command-line utility that lets you interact with this Django project in various ways.<br><br>
>settings.py<br>

Django Request Response life cycle<br>
wsgi.py acts as the interface between web server and django application<br>

![request-response](https://user-images.githubusercontent.com/59610617/128341168-1a2a9e77-0356-4cef-ac50-30ae958e6266.png)<br>

What is django-admin and manage.py and explain its commands?<br>
django-admin is Django's command-line utility for administrative tasks. In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project's settings.py file.<br>
Some commands are: all commands can be done using django-admin or manage.py<br>
1)django-admin help<br>
2)django-admin makemigration<br>
3)django-admin migrate<br>
4)django-admin version<br>

Django directory structure:<br>
![Django-file-structure-normal-image](https://user-images.githubusercontent.com/59610617/127732323-8a3079a8-bb32-4cb8-a04e-0d7a9e63a2e4.jpg)<br>


Creating first app:<br>
<pre>
Step 1: Open vscode terminal type >django-admin startapp firstApp	OR	python manage.py startapp thirdApp<br>
Step 2: Register this app in settings.py file:<br>
>INSTALLED_APPS = [
    'firstApp'
]
</pre>

Running in the browser.<br>
<pre>On terminal >python manage.py runserver </pre>


<a name="six"><h2>2.4 URLs and Views</h2></a><br>
What is URL?<br>
In Django, we use something called URLconf (URL configuration). URLconf is a set of patterns that Django will try to match the requested URL to find the correct view.<br>
We can have n number of apps in one project. Example Amazon website has different apps for outfit, grocery, application etc.<br>

What is View?<br>
Django Views are one of the vital participants of MVT Structure of Django. A View is the user interface — what you see in your browser when you render a website. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, anything that a web browser can display.<br>
Types of views<br>
1)class based view<br>
2)function based view<br>

Creating a very basic view:<br>
HttpResponse can be text, xml, json, redirect, html, if not found(404)<br>
<pre>
views.py
from django.shortcuts import render, HttpResponse

def firstview(request):
    return HttpResponse("Hello from first app")
    
This view will return http response.
</pre>

<b>How GET & POST request works in view.</b>
<pre>
def showformdata(request):
    if request.method == "POST":
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['product_name']
            ph = fm.cleaned_data['product_purchase']
            cd = fm.cleaned_data['product_code']
            reg = Product(product_name=nm, product_purchase=ph, product_code=cd)
            reg.save()
    else:
        fm = ProductDetails()
    return render(request, 'demo.html',{"form":fm})
</pre>
In the above code when we hit the url defined the urls.py the get request get called meaning the else part will run and bcoz of that we can see the blank form, When the request is post 'if'  part runs, meaning when we click the 'submit' button the post method gets called.<br>
NOTE: Whenever we hit the url the get method called always and when click on input submit button post method called.<br>
<b>To get the two different templates for same view</b>
<pre>
views.py
def myview(request, template_name):
    mytemp = template_name
    form = ContactForm()
    return render(request, mytemp , {'form':form})

urls.py
path('class1/',views.myview, {'template_name':'index.html'}, name="class1"),
path('class2/',views.myview, {'template_name':'index2.html'}, name="class2"),
</pre>



<a name="seven"><h2>2.5 URL dispatcher</h2></a><br>
Syntax : path(route, view, kwargs=None, name=None)<br>

Creating two apps in one project<br>
<pre>
Project:                #this is root project
django-admin startapp firstApp<br>
django-admin startapp secondApp<br>

Here Project is the root folder and it has two app firstApp, secondApp.<br>
</pre>

URL Patterns App Level and Project Level<br>
1)Project Level: not recommended.<br>
The url which is common in all the application we can defined them in project level url.
<pre>
  from firstApp import views
  from secondApp import views as vw	    #if we give same 'views' name to both the app then it'll give error to resolve this use alias on other views.
 
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('',views.firstview, name="message"),
      path('datedisp/',vw.secondview, name="date"),
  ]
  
</pre>

2)App Level: recommended<br>
instead of giving all urls in one file, give urls in every app:<br>
Advantages of giving urls for each app are application reusability, redable format, reduce code complexity.<br>
<pre>
Step 1:create urls.py in every app and import the path, views
For firstApp:
  from django.urls import path
  from firstApp import views
  
  urlpatterns = [
      path('',views.display/, name="hello"),
  ]

For secondApp:
  from django.urls import path
  from secondApp import views
  
  urlpatterns = [
      path('',views.dispDate/, name="date"),
  ]

Do this for every app

Step 2: Include these in main project url file.
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('firstApp/',include('firstApp.urls')),
      path('secondApp/',include('secondApp.urls')),
  ]

Step 3:Now run the files in the application manner.
  Example:
  for firstApp use (http://127.0.0.1:8000/firstApp/) followed by urls given, same for other apps
</pre>

<a name="eight"><h2>2.6 Django Templates</h2></a><br>
The Django template language<br>
A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.<br>

Variables<br>
A variable outputs a value from the context, which is a dict-like object mapping keys to values.<br>
Variables are surrounded by {{ and }} like this:

Use of context?<br>
A context is a variable name -> variable value mapping that is passed to a template.<br>

Example of context and variable:
<pre>
views.py
def studentDetailView(request):
    name="Fareen"
    roll_no=101
    data={'Name':name, 'RollNo':roll_no}
    return render(request,'firstApp/studentdetail.html',context=data)
    
studentdetail.html
    &lt;h1 class="myheading">Name:{{Name}}&lt;/h1&gt;
    &lt;h1&gt;RollNo:{{RollNo}}&lt;/h1&gt;
    &lt;h1&gt;data:{{data}}&lt;/h1&gt;       &lt;!--It wont print anything, we access using key--&gt;
    &lt;!--We access name using its key--&gt;
</pre>

<b>For loop in view</b>
<pre>
views.py
	def getcolors(request):
	    data={'colors':['red','yellow','blue','green']}
	    return render(request,'firstApp/demo.html',context=data)
    
demo.html
	&lt;h1&gt;Printing colors using for loop:&lt;/h1&gt;
	{%for i in colors%}
	&lt;h4&gt;{{i}}&lt;/h4&gt;
	{%endfor%}
</pre>

Tags<br>
<pre>
Tags are surrounded by {% and %} like this:

{% csrf_token %}
Most tags accept arguments:

{% cycle 'odd' 'even' %}
Some tags require beginning and ending tags:

{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}
</pre>

Filters<br>
<pre>
Filters transform the values of variables and tag arguments.

They look like this:

{{ django|title }}          #returns the title case
With a context of {'django': 'the web framework for perfectionists with deadlines'}, this template renders to:

The Web Framework For Perfectionists With Deadlines
Some filters take an argument:

{{ my_date|date:"Y-m-d" }}
</pre>

Uppercase the colors name:
<pre>
views.py
	def getcolors(request):
	    data={'colors':['red','yellow','blue','green']}
	    return render(request,'firstApp/demo.html',context=data)
    
demo.html
	&lt;h1&gt;Printing colors using for loop:&lt;/h1&gt;
	{%for i in colors%}
	&lt;h4&gt;{{i|upper}}&lt;/h4&gt;
	{%endfor%}
</pre>
<b>List of filters</b>:<br>
{{django | length}} : returns length<br>
{{djangi | slice:'no. of characters'}} : slice the character eg:3 to display 3 chars<br>
{{django | truncatechars:'no. of characters'}} : returns the given character and rest all in dot...<br>
Example: hello world<br>
{{django | truncatechars:'3'}}<br>
hell...
{{django | upper/lower}}<br>
<b>Using both slice and upper</b><br>
{{django|upper|slice:'3'}}<br>

MORE FILTERS (https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatefilter-addslashes)

<b>Formating date</b><br>
views.py<br>
    p=datetime.datetime.now()<br>
    return render(request,'firstApp/studentdetail.html',{'p':p})<br>

{{variable | default:'default value'}}<br>
D=day in text format<br>
d=01 return date in form 01,02...09<br>
j=return 1,2,3...910<br>

DATE_FORMAT: return in format like this: Aug. 1, 2021<br>
DATE_TIME: return in format like this: SunPMUTCAugust_UTC0AugAugust<br>
SHORT_DATE_FORMAT: return in format like this: 08/01/2021<br>
<b>float format</b><br>
{{django | 'floatformat':'3' }}<br>

<b>Conditional statement</b><br>
<pre>
views.py 
    s='string'
    f=20.5
    return render(request,'firstApp/studentdetail.html',{'s':s,'f':f})

Example:
{'studentname':sname}
Here studentname is key and sname is value. so we only provide the key in the html.

Syntax:
1)if
Syntax
{{% if variable %}}
{{% endif %}}

Example:
{% if s %}
    value is {{s}}
{%endif%}

2)if else
Syntax
{% if variable is defined %}
    value of variable: {{ variable }}
{% else %}
    variable is not defined
{% endif %}

Example:
{% if s %}
    value of variable: {{ s }}
{% else %}
    variable is not defined
{% endif %}

3)if elseif else
Example:
Note: Always give space after variable s and value 'fareen' or it'll give error
{% if s == 'fareen' %}
    value of variable: fareen
{%elif s == 'annu' %}
    value of variable: annu
{% else %}
    value of variable: roma
{% endif %}
</pre>

<b>Operators</b>
<pre>
1)AND operator
Example:
views.py 
    name="fareen"
    age=23
    return render(request,'firstApp/studentdetail.html',{'sname':name,'sage':age})

demo.html
{% if sname == 'fareen' and sage == 23 %}
    Name and age is: fareen and 23
{% else %}
    Invalid name and age
{% endif %}

1)OR operator
{% if sname == 'fareen' or sname == 'Fareen' %}
    Name and age is: fareen and 23
{% else %}
    Invalid name and age
{% endif %}
</pre>


Comments<br>
<pre>
Comments look like this:

{# this won't be rendered #}
A {% comment %} tag provides multi-line comments.
</pre>

Creating Template<br>
<pre>
Create templates file create same app name folder for every app inside the templates only:
	->firstApp ->demo.html
	->secondApp

include in the settings.py
step1: import os

step2 : use the join function
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')

step3 : now give this variable name inside the templates 
'DIRS': [TEMPLATES_DIR],

OR
directly include:
'DIRS': [os.path.join(BASE_DIR,'templates')],
</pre>

Designing template view:
<pre>
render() function:

def tempDemo(request):
    return render(request,'firstApp/demo.html')
</pre>

Define ContextProcessor?

<a name="nine"><h2>2.7 Working with Static Files</h2></a><br>
Static files are: css, js, images, files.<br>
Working with static file:
<pre>
Step1: create static folder:
		|
		->static
			|
			->css
			->js
			->img

Step2: include the path:
We used to give pattern like this.
STATIC_DIR=os.path.join(BASE_DIR,'static')	//Here we are basically joining the path of static folder and providing the variable name inside the settings.py syntax
						//We can directly give join the path inside the setting.py syntax like this:
						STATICFILES_DIRS=[
    							os.path.join(BASE_DIR,'static')
						]
In new version we'll give like this:
STATIC_DIR = BASE_DIR / 'static'		#now adding this static_dir variable in staticfiles_dirs

Step3: create list of STATICFILES_DIRS name and give static file inside that list:
STATICFILES_DIRS=[
    STATIC_DIR
]

Step4: creating stylesheet.css and include these inside the html
Where ever we'll use the static files inside the html we must load static folder using:
<!DOCTYPE html>
{% load static %}
Right below the doctype html
</pre>

Linking css file using static:
<pre>
    &lt;link rel="stylesheet" href="{% static 'css/style.css' %}"&gt;
</pre>

Linking img using static:
<pre>
    &lt;img src="{% static 'img/track.jpg' %}"&gt;
</pre>


<a name="ten"><h2>2.8 DJANGO MODEL</h2></a>
What is Model?<br>

Configuration of MySQL Database<br>
SQLite.<br>
Django provides the SQLite connection by default, we can change database by providing database name, password<br>

<b>Migrate vs Makemigration</b><br>
makemigrations auto generates migration files containing changes that need to be applied to the database, but doesn't actually change anyhting in your database. migrate will make the actual modifications to your database, based on the migration files.<br>
Everytime we make some changes in models.py we have to run migration command and then 
Migrate command will migrate all the tables in the migration file, and now we can check the table<br>
To check the commands which django send to database to communicate with database:<br>
>python manage.py sqlmigrate app_name 0001_initial<br>
Example: 
<pre>
>python manage.py sqlmigrate Students 0001_initial
--
-- Create model Product
--
CREATE TABLE `Students_product` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
</pre>

When we run the app and try to access the admin we won't get that page because we did'nt crete the super user yet.<br>
NOTE: Before creating any model we have to run the migration commands<br>

<b>Creation of Super User</b><br>
To create super user use this command:<br>
>python manage.py createsuperuser<br>
>Enter username
>Enter password, email(optional)<br>
We can create many super users using this command<br>
If in case super admin forget the password we cannot log in without password in this case we can create the another super user and log in and check or change the password<br>
Super user created, now we can check on browser by providing username, password. We can see Groups and Users tables<br>

<b>Register Model Inside Admin Interface</b><br>
We have created super user, now we make the first model and we must register that model to admin or we won't we able to see that model in the admin panel<br>
<pre>
models.py
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc =  models.CharField(max_length=50)
    
admin.py
from firstApp.models import Product

class ProductAdmin(admin.ModelAdmin):
	pass
admin.site.register(Product, ProductAdmin)

By creating this we can see product name, desc. Here we cannot see product Id we have created bcoz it is autogenerated. To add these in the product table on admin panel:<br>
class ProductAdmin(admin.ModelAdmin):
	list_display=['product_id','product_name','desc']
</pre>
In this list display whatever we add will be visible in the product table on admin panel
If we remove something as in 'desc' from this list it won't be visible table on the panel but when we add product it will be there.<br>
In list_display we can control what we want to see on the table. It won't be deleted but just hidden on that panel<br>
It should be the same name list_display<br>

<b>Adding the dunder method</b>
<pre>
class Product(models.Model):
	p_name = models.CharField()
	
	def __str__(self):
		return self.p_name
		
We can concat str with email or anything we want.
return self.name + " " + self.email
</pre>

<b>Adding the Search filter</b>
<pre>
search_fields = ['name','location']	//it will search by name and location
</pre>

<b>Editable list</b>
<pre>
editable_list = ['password','city']	//these can be directily editable.
</pre>

<b>Adding filter option</b>
<pre>
list_filter=['department']   //this will show filter option just like we get in user model
</pre>

<b>Creating Custom filter</b>
<pre>
class filter(simpleListFilter)

cclass CustomFilter(admin.SimpleListFilter):
    title = 'salary'
    parameter_name='salary'
    def lookups(self, request, model_admin):
        return (('lowSalary','Salary below 40000'),('highSalary','salary above 40000'))
    
    def queryset(self,request,queryset):
        if self.value()=='lowSalary':
            return queryset.filter(salary__lt=40000) 	#lte for less than and equal to

        elif self.value()=='highSalary':
            return queryset.filter(salary__gt=40000)

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_purchase','product_code','salary']
    list_filter = [CustomFilter]

admin.site.register(Product, ProductAdmin)

Now in the product model we can see filer where sal less than 40000 and greater than 40000.
Title will be visible on the product model, and parameter_name will be.
With the help of lookup we'll get the filter list visible on the browser. 
</pre>

<b>Ordering</b>
<pre>
ordering=['age'] 
</pre>

<b>To change admin pswd</b>
python manage.py changepassword model_name

Creating the first model.<br>
<pre>
Step 1:
on models.py create models
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc =  models.CharField(max_length=50)
    
Go to apps.py copy the class name add in settings.py installed apps:
//AppName	//copy here
'firstApp.apps.FirstAppConfig'

Step 2:
Run migration commands:
>python manage.py make migration
>python manage.py migrate

Step 3:
Create super user:
>python manage.py createsuperuser
enter username, email(optional), give password

Step 4:
Register the model in admin.py
admin.py
from firstApp.models import Product

class ProductAdmin(admin.ModelAdmin):
      pass      
admin.site.register(Product, ProductAdmin)

instead of pass we can use list_diaplay=[//list of columns]

Note: django always create a id field with each model (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
</pre>


Defining Django Models<br>
Django Model Fields<br>
1)AutoField()
<pre>
autofiled = models.AutoField()

An IntegerField that automatically increments. In one model we can only have one autofield
</pre>
2)BigAutoField: It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.<br>
3)BigIntegerField: It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.<br>
4)BinaryField()
<pre>

</pre>
5)BooleanField()
<pre>
boolean=models.BooleanField(default=True, verbose_name="this is boolean filed")

If default=True it will be checked
</pre>
6)CharField(max_length=len)
<pre>
charfield = models.CharField(max_length=50, verbose_name="New name",unique=True,help_text="added help text")
    
max_length=required, rest all optional
</pre>
7)DateField()
<pre>
from django.utils import timezone
date = models.DateField(default=timezone.now())

It will set the date to current date, if we dont need that ignore the default parameter. 
</pre>
8)DecimalField(max_digits=5, decimal_places=2)
<pre>
decimalfield = models.DecimalField(max_digits=5, decimal_places=2)

max digits will be 5 and decimal place will be 2,
Example: 555.55
</pre>
9)DurationField()
<pre>

</pre>
10)EmailField(max_length=len)
<pre>
email = models.EmailField(max_length=200)
</pre>
11)FileField(upload_to), ImageField()<br>
upload_to: optional<br>
<pre>
Whenever we add images or files the django will serach for media folder:

Step 1:
Create FileField()
file = models.FileField(upload_to='files/', blank=True) 		
upload_to: destination to keep the files, blank=if true allow field to be blank.
Here django will always upload the files inside the media folder so, media -> files is the destination for files. Files can be image.
We have already defined media in root, now if we give location like 'media/files' django will create media -> media -> files.

Create ImageField()
file = models.ImageField(upload_to='files/', blank=True) 		

Step 2:
Create a media name folder inside the root folder where manage.py file is there.Just like we make folder for static, templates in the project root folder.

Step 3:
In settings.py at the end write this:
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

If we won't create the media_url, then the files will be upload to the current root directory.

Step 4:
In urls.py add the following line:
if settings.DEBUG:		//for developer mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Note: we need to make some changes in form if the data coming from form. For model above steps will work.

Follow Steps : https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

</pre>
12)FloatField(): It is a floating-point number represented in Python by a float instance.
<pre>
floatfield = models.FloatField() 
</pre>
13)ImageField()
<pre>

</pre>
14)IntegerField(): It is an integer field. Values from -2147483648 to 2147483647 
<pre>
integerfield = models.IntegerField() 
</pre>
15)GenericIPAddressField: An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).<br>
16)NullBooleanField: Like a BooleanField, but allows NULL as one of the options.
<pre>
</pre>
17)PositiveIntegerField: Like an IntegerField, but must be either positive or zero (0).vales from 0 to 2147483647.
<pre>
positiveint1 = models.PositiveIntegerField()
</pre>
18)PositiveSmallIntegerField: Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point. vales from 0 to 32767.
<pre>
positiveint2 = models.PositiveSmallIntegerField()
</pre>
19)SlugField: Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
<pre>
</pre>
20)SmallIntegerField: It is like an IntegerField, but only allows values under a certain (database-dependent) point.
<pre>
</pre>
21)TextField: A large text field. The default form widget for this field is a Textarea.
<pre>
text = models.TextField(max_length=2)

will only allow 2 characters.
</pre>
22)TimeField: A time, represented in Python by a datetime.time instance.
<pre>
time_field = models.TimeField(auto_now=False, auto_now_add=False)
</pre>
23)URLField: A CharField for a URL, validated by URLValidator.
<pre>
url = models.URLField()
</pre>
24)UUIDField: A field for storing universally unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32).
<pre>
</pre>
To take phone number from the user we can use regex and charfield or PhoneNumberField<br>
25)DateTimeField(auto_now_add=True), DateTimeField(auto_now)
<pre>
created_at =  models.DateTimeField(auto_now_add=True)
updated_at =  models.DateTimeField(auto_now=True)

This is usefull for post, like when the post is created the auto_now_add will add the current date and time, and when updated auto_now() will update according to new date.
</pre>
26)To achieve drop down
<pre>
option= [
        ('malad (e)', 'Malad (E)'),
        ('malad (w)', 'Malad (W)'),
        ('goregoan', 'Goregoan'),
        ('andheri (e)', 'Abdheri (E)'),
        ('andheri (w)', 'Abdheri (W)'),
        ]
	
Branch=models.CharField(max_length=100, choices=option)
</pre>

<h3>ORM in django.</h3>
One of the most powerful features of Django is its Object-Relational Mapper (ORM), which enables you to interact with your database, like you would with SQL. In fact, Django's ORM is just a pythonical way to create SQL to query and manipulate your database and get results in a pythonic fashion. ORM basically convert your model class in Sql queries <br>
Benefit of using ORM is anyone who don't know what SQL, MySql, Oracle is can also work with models.<br>
We can change the database anytime we want, we don't need to write the seperate sql queries for that example if today i use MySql and tmrw i want my application to work in PostgreSql then i don't need to write queries for PostgreSql i can use the same model, and ORM will help me to convert it in postgresql queries.<br>

![orm](https://user-images.githubusercontent.com/59610617/128343962-c7c584e0-7ff2-4add-8734-8724e8d6fe19.png)<br>

<h3>Queryset in django.</h3>
A QuerySet represents a collection of objects from your database. It can have zero, one or many filters. Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT .<br>
<pre>
Step 1: open python interactive shell
>python manage.py shell

Step 2: import the model which you in which we want to apply query.
from home.models import Contact

Step 3: Query the queryset you want

To get all the objects in db.
>>>Contact.objects.all() 

To get the first object.
Contact.objects.all()[0]

To get the name of the first object.
Contact.objects.all()[0].name

To get first and last Entry:
Contact.objects.all().first() 
Contact.objects.all().last() 

USING FILTER: to filter records.
To filter the query by name
Contact.objects.filter(name='annu') 

filter query where name='fareen' and contact='999999999'
Contact.objects.filter(name='fareen',contact='999999999')

To filter based on text search:
 Contact.objects.filter(desc__startswith="this") 
<QuerySet [<Contact: fareen>, <Contact: sam>]>

ADDING DATA:
We can add and edit the record in db using filters.
To add the record 
 joe = Address.objects.create(email="Joe@123",city="mumbai").save()		//it'll without save() too
</pre>
For more queryset: making queries django, on google.<br> 

<b>CONSTRAINTS IN MODEL</b><br>
<b>1)primary key</b><br>
By default django add 'id' primary key on every models, we can define our own primary key. When we define our own primary key, the primary created by django will be removed.
<pre>
product_id = models.IntegerField(primary_key=True)

Now when we run the migartion it'll do the following:
    - Remove field id from product
    - Add field product_id to product
</pre>

<b>1)default</b>
<pre>
class Location(models.Model):
    location = models.CharField(max_length=20, default='Mumbai')
</pre>
<b>Null vs Blank</b>
<pre>
If True, Django will store empty values as NULL in the database. Default is False.
For both string-based and non-string-based fields, you will also need to set blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage (see blank).

null=True meaning database accept null value.
blan=True says the field can be empty in a form.

So to achieve the null values in django use:
case 1:null=True, blank=True
In this case database will store 'NULL' values.
MariaDB [djangoProject]> select * from faculty_checkcon;
+----+-----+----------+
| id | age | location |
+----+-----+----------+
| 18 |   1 | NULL     |
+----+-----+----------+
1 row in set (0.000 sec)

case 2:null=False, blank=True
In this case database will store 'BLANK' values not 'NULL' values:
MariaDB [djangoProject]> select * from faculty_checkcon where location=NULL;
Empty set (0.019 sec)

MariaDB [djangoProject]> select * from faculty_checkcon where location='';
+----+-----+----------+
| id | age | location |
+----+-----+----------+
| 14 |   2 |          |
| 15 |   3 |          |
| 16 |   4 |          |
| 17 |   5 |          |
+----+-----+----------+
4 rows in set (0.000 sec)

case 3:null=True, blank=False
In this case the field can't be empty, but database can accept null values. So this case won't allow record basically.
</pre>

<b>unique</b>
<pre>
location = models.CharField(max_length=20, unique=True)
</pre>
<b>check</b><br>
There is nothing for check in django. We can use if else or something else.<br>
<b>Some other parameter in models we can use</b>
<pre>
1)help_text: Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.
Example:
	Name = models.CharField(max_length=20, help_text="Enter same name as displayed on your aadhar card")
	
2)editable: If False, the field will not be displayed in the admin or any other ModelForm. Default is True.
Example:
	location = models.CharField(max_length=20, help_text="enter your location", editable=False)
	
They are also skipped during model validation.In this case it will store location to '' in db:
MariaDB [djangoProject]> select * from faculty_checkcon;
+----+-----+----------+
| id | age | location |
+----+-----+----------+
| 21 |   1 |          |
+----+-----+----------+
1 row in set (0.000 sec)

3)verbose_name: Is a human-readable name for the field. If the verbose name isn't given, Django will automatically create it using the field's attribute name, converting underscores to spaces. This attribute in general changes the field name in admin interface.
Example:
	location = models.CharField(max_length=20, verbose_name="Customer Location")
	
In admin interface the label will be 'Customer Location'.

4)db_column:db_column. The name of the database column to use for this field. If this isn't given, Django will use the field's name. If your database column name is an SQL reserved word, or contains characters that aren't allowed in Python variable names – notably, the hyphen – that's OK.
Example: 
	location = models.CharField(max_length=20, verbose_name="Customer Location", db_column="cust_location")

This will change the database column name:
MariaDB [djangoProject]> select * from faculty_checkcon;
+----+-----+---------------+
| id | age | cust_location |
+----+-----+---------------+
| 22 |   1 | Mumbai        |
+----+-----+---------------+
1 row in set (0.025 sec)

5)validators
This is model level validation, when we work on admin user interface these validation will work on that, if form is coming from html then this validation won't work, for that we use form level validation or html validations.

from django.db import models
from django.core.exceptions import ValidationError

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "yourdomain.com" in value:
        raise ValidationError("Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")

model:
important_email = models.EmailField(validators=[validate_domainonly_email], max_length=30)

This validation is reusable we can apply this validation on mant email fields present in the model.

6)error_messages

</pre>
Define QuerySet<br>
The Python Template Engine<br>
Define Jinja2<br>
Faker Module<br>

<b>Display model data in html.</b>
<pre>
views.py
def showval(request):
    data = Product.objects.all()
    return render(request,'index.html', {'data':data})
  
index.html
<html>
<body>
<form action="" method="POST" novalidate="">
    {% for i in data %}
    {{i}}
    <br>
    {%endfor%}
</form>
</body>
</html>

Output:
Product object (1)
Product object (2)
Product object (3)
Product object (4)
</pre>

Here the output showing the object to convert it into name, we have to use __str__ method in models.<br>
<pre>
 def __str__(self):
        return self.product_name
</pre>

<a name="eleven"><h2>2.9 Relationships in Django Models</h2></a><br>
<b>Relationship fields</b><br>
<b>1)ForeignKey()</b>
<pre>
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=20)

class Order(models.Model):
				//pk table_name, which is Product
    order_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
whenever we delete a record from product, the related order record will be deleted simultaneously, bcoz we have given on_delete=models.CASCADE, just like we give in mysql.
Like if user delete the account his all account info in another table gets deleted.

There is no on_update=CASCADE in django
</pre>

<b>2)OneToOneField(parent_table, on_delete, parent_link=False,  **options)</b>
<pre>
Here one to one relation meaning one person can have only one passport
One user can have only one account.

class Person(models.Model):
    person_name = models.CharField(max_length=30)
    person_age = models.IntegerField()

class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=CASCADE)
    passport_no = models.IntegerField()
    
Suppose we've added one passport for the record where id=1, and now we try to add another passport for the same id it'll give error:
'Passport with this Person already exists.'

Now when we delete person record where id=1, it will delete the following record:
Persons: 1
Passports: 1
</pre>
Example of on_delete=PROTECTED
<pre>
On the same above example change on_delete=PROTECTED
 
Now when we delete the person record it won't delete, first we have to delete the passport record then we can delete this record as well.
</pre>
Example of limit_choices_to={}
<pre>
If we want only some users to create account we can use limit option

user = models.OneToOneField(User, on_delete=PROTECT, limit_choice_to={'is_staff':True})
Now only those users whose staff status is checked can create account.
</pre>

<h1>Use of signal</h1>
We saw in above case when we delete the person then its related record passpord gets deleted automatacally. Now if we want that if passport gets deleted the its related parent table record gets deleted too<br>
In above table parent deleted then child gets deleted automaticalle<br>
Here we want if child deleted then parent get automatically deleted too. In this case we can use of signals<br>
<pre>
To create signal:
Step 1:
create signals.py in the app:

Step 2:
from .models import Passport
from django.db.models.signals import post_delete
from django.db.models.deletion import CASCADE, PROTECT
from django.dispatch import receiver   # to connect signals

@receiver(post_delete, sender=Passport)
def delete_related_user(sender, instance, **kwargs):
    instance.person.delete()
        
Here instance.person.delete(), person=parent table name

Step 3:
apps.py
class FacultyConfig(AppConfig):
    name = 'Faculty'

    def ready(selft):
        import Faculty.signals

Step 4:
__init__.py
default_app_config = 'Faculty.apps.FacultyConfig'

Now we can delete the parent record on deleting child record.
</pre><br>
What is signal?<br>
Signals allow certain senders to notify a set of receivers that some action has taken place.<br>
Sender : who will send signal<br>
Signal : signal<br>
Receiver: who receive signal<br>
Example: in train signal, there must be a guy who sends the signal which is red flag to the train, here signal is send by signal guy, and signal dispacher is red flag and receiver is train. That guy must know whom to send the signal same in django we must know to whom we send signal.<br>
Receiver signal:<br>
>Signal Syntax: def receiver_fun(sender, request, user, **kwargs): <br>

Connecting/Registering receiver function: two ways:<br>
>Manual connect route: we use Signal.connect(receiver_func, sender=NOne, weak=True, dispatch_uid=None) method in this.<br>
>Decorator: @receiver(signal or list of signal, sender)<br><br>

Types of signals<br>
1)Login and Logout signal:<br>
>user_logged_in(sender, request, user): sent when user log in successfully. Where sender=class of the user just logged in, request=current HTTPRequest instance, user=The user instance that just logged in<br>

>user_logged_out(sender, request, user): sent when the logout method is called. Where sender=class of the user just logged out, request=current HTTPRequest instance, user=The user instance that just logged out or None if user not authentocated.<br>

>user_login_failed(sender, credential, request): send when the user failed to login successfully.<br><br>
Example:
<pre>
Step 1: create signals.py in the app

Step 2: import the necessary files
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

Step 3:override the ready methon inside apps.py
class App1Config(AppConfig):
    name = 'App1'

    def ready(self):
        import App1.signals
	
Step 4:__init__.py or settings.py
__init__.py
defaut_app_config = 'App1.apps.App1Config'

OR
settings.py
'App1.apps.App1Config'

Step 5:register receiver signal 
Manual connect
def login_success(sender, request, user, **kwargs):
    print("User:",user)

user_logged_in.connect(login_success,sender=User)

OR
Decorator
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
# Create your models here.
def login_success(sender, request, user, **kwargs):
    print("User:",user)

BOTH WILL WORK SAME:

signals.py for all three
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("Login User:",user)
#We can perform many tasks like: counting the number of times user login, session & caches storing
#Every task which we want to trigger right after user login

@receiver(user_logged_out, sender=User)
def logout(sender, request, user, **kwargs):
    print("Logout User:",user)
#We can perform many tasks like: Bye text etc

@receiver(user_login_failed, sender=User)
def login_failed(sender, credentials, request, **kwargs):
    print("Login failed User:",sender)
    print("credential:",credentials)
#We can perform many tasks like: as in we want to store all who are trying to log in, and want to store in log files etc.
#login permission as in how many times a particular user can log in etc
</pre>

2)Model Signals<br>
A list of signals sent by the model system. We import django.db.models.signals<br>
>pre_init(sender, *args, **kwargs)<br>

>post_init(sender, *args, **kwargs)<br>

>pre_save(sender, instance, raw, using, update_fields)<br>

>post_save(sender, instance, created, raw, using, update_fields)<br>

>pre_delete(sender, instance, using)<br>

>post_delete(sender, instance, using)<br>

>m2m_changed(sender, instance, action, reverse, model, pk_set, using)<br>

>class_prepared(sender)<br>

To check all other signals import the model signals and then vs code will suggest a list of all signals.
<pre>
Step 1:import
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete

Step 2:create signals
@receiver(pre_save, sender=User)
def startofsave(sender, instance, **kwargs):
    print("Sender:",sender)
    print("Instance:",instance)
    print(f"Kwargs: {kwargs}")
    
This will run before the data gets saved in the db. And it will also run  when record updated and save.

@receiver(post_save, sender=User)
def endofsave(sender, instance, created, **kwargs):
    if created:     #if created run this
        print("Created:",created)
    else:           #if update run this
        print("Created:",created)

This will run after the data gets saved in the db.If the data save in the database then if will run and created will be True, if data is updated and saved then the else part will run and created will be False.

@receiver(pre_delete, sender=User)
def startofdelete(sender, instance, **kwargs):
    print("Pre delete, Sender:",sender)

@receiver(post_delete, sender=User)
def endofdelete(sender, instance, **kwargs):
    print("Post delete, Sender:",sender)
    
Pre init, post init: used when django model instiantiate:
@receiver(pre_init, sender=User)
def startofpre(sender, *args, **kwargs):
    print("Pre init, Sender:",sender)

@receiver(post_init, sender=User)
def endofpre(sender, *args, **kwargs):
    print("Post init, Sender:",sender)

</pre>
3)Managemenet Signals: sent by django-admin, We use django.db.models.signals<br>
>pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps)

>post_migrate(sender, app_config, verbosity, interactive, using, plan, apps)

<pre>
from django.db.models.signals import pre_migrate, post_migrate

@receiver(pre_migrate)
def beforemigrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("Before migrate:",sender)

@receiver(post_migrate)
def aftermigrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("After migrate:",sender)
    
Output: It will run for all migrations
  Apply all migrations: admin, auth, contenttypes, sessions
Before migrate: <AdminConfig: admin>
Before migrate: <AuthConfig: auth>
Before migrate: <ContentTypesConfig: contenttypes>
Before migrate: <SessionsConfig: sessions>
Before migrate: <App1Config: App1>
Running migrations:
  No migrations to apply.
After migrate: <AdminConfig: admin>
After migrate: <AuthConfig: auth>
After migrate: <ContentTypesConfig: contenttypes>
After migrate: <SessionsConfig: sessions>
After migrate: <App1Config: App1>
</pre>

4)Request/Response Signal: send on request and response<br>

>request_started(sender, environ)

>request_finished(sender)

>got_request_exception(sender,request)

<pre>
from  django.core.signals import request_started, request_finished, got_request_exception

@receiver(request_started)
def request_started(sender, environ, **kwargs):
    print("Request started, sender:",sender)

@receiver(request_finished)
def request_finished(sender, **kwargs):
    print("Request ended, sender:",sender)

@receiver(got_request_exception)
def got_request_exception(sender,request, **kwargs):
    print("sender:",sender)
    #whenever we got exception run this
</pre>

5)Test Signal: Signals only sent when running tests. We use django.test.signals<br>
>setting_changed(sender, setting, value, enter)<br>

6)Database Wrappers: signals sent by the database wrapper when a database connection is initiated. We use django.db.backends.signals<br>
>connection_created(sender, connection, **kwargs)

<pre>
@receiver(connection_created)
def conncreted(sender, connection, **kwargs):
    print("Connection created:")
    print("Sender:",sender)
    
Output: Will run as soon as conncetion to the database created
Connection created:
Sender: <class 'django.db.backends.mysql.base.DatabaseWrapper'>
</pre>
Custome Signals<br><br>

Built-in signals<br>



<b>ManyToManyField()</b></br>
![mmr](https://user-images.githubusercontent.com/59610617/128026876-50217874-c421-4309-bc6b-38be47dacfe7.png)<br>

<pre>
Step 1:
models.py
from django.contrib.auth.models import User
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=20)
    song_duration = models.IntegerField()

    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])

An extra function which return who all have sang that song
admin.py
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['song_name','song_duration','written_by']
</pre>
Output:<br>
![op](https://user-images.githubusercontent.com/59610617/128031073-f688a338-e7ba-4546-9822-dfcf4f02862d.png)<br>

Here we can see one song is sang by many singers and many songs is sang by one user<br>
On deleting the fareen singer<br>
![op2](https://user-images.githubusercontent.com/59610617/128031719-f066ec79-92d1-4276-9bf7-bcbd0a1c5d2a.png)<br>

<a name="twelve"><h2>2.10 Django Forms or Model Forms</h2></a><br>
<b>Creating normal html form(data coming from raw html)</b>
<pre>
Step 1: models.py
class Product(models.Model):
    product_name = CharField(max_length=30)
    product_purchase = CharField(max_length=10)
    product_code = IntegerField()

Step 2: demo.html
&lt;form action="" method="POST" novalidate=""&gt;
{% csrf_token %}
	&lt;p&gt;&lt;label for="id_product_name"&gt;Product name:&lt;/label&gt; &lt;input type="text" name="product_name" maxlength="30" required="" id="id_product_name"&gt;&lt;/p&gt;
	&lt;p&gt;&lt;label for="id_product_purchase"&gt;Product purchase:&lt;/label&gt; &lt;input type="text" name="product_purchase" maxlength="10" required="" id="id_product_purchase">&lt;/p&gt;
	&lt;p&gt;&lt;label for="id_product_code"&gt;Product code:&lt;/label&gt; &lt;input type="number" name="product_code" required="" id="id_product_code"&gt;&lt;/p&gt;
	&lt;input type="submit" values="submit"&gt;
&lt;/form&gt;

Step 3: views.py
from .models import Product

def showformdata(request):
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        product_purchase=request.POST.get('product_purchase')
        product_code=request.POST.get('product_code')
        reg=Product(product_name=product_name,product_purchase=product_purchase,product_code=product_code)
        reg.save()
    return render(request,'demo.html')
</pre>


<b>Django form using form api</b>
<pre>
Step 1:models.py
class Product(models.Model):
    product_name = CharField(max_length=30)
    product_purchase = CharField(max_length=10)
    product_code = IntegerField()
    
Step 2: create forms.py
from django import forms

class ProductDetails(forms.Form):
    product_name = forms.CharField(max_length=30)     #product_name will become the label name with p uppercase
    product_purchase = forms.CharField(max_length=10)
    product_code = forms.IntegerField()
    
Here product_name will become the name which comes from html.

Step 3: demo.html
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;Hello&lt;/h1&gt;
&lt;form action="" method="POST" novalidate&gt;
{% csrf_token %}
{{form.as_p}}
&lt;input type="submit" values="submit"&gt;
&lt;/body&gt;
&lt;/html&gt;

Step 4:views.py
from .forms import ProductDetails
from .models import Product

# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['product_name']
            ph = fm.cleaned_data['product_purchase']
            cd = fm.cleaned_data['product_code']
            reg = Product(product_name=nm, product_purchase=ph, product_code=cd)
            reg.save()
    else:
        fm = ProductDetails()
    return render(request, 'demo.html',{"form":fm})
</pre>
<b>Form Rendering Options</b><br>
{{form}} will render them all.<br>
{{form.as_table}} will render them as table cells wrapped in &lt;tr&gt; tags.<br>
{{form.as_p}} will render then wrapped in &lt;p&gt; tag.<br>
{{form.as_ul}} will render them wrapped in &lt;li&gt; tags<br>
{{form.name_of_field}} will render field manually as given.<br>

<p>Django form using ModelForm:</b><br>
What is ModelForm?<br>
Django ModelForm is a class that is used to directly convert a model into a Django form. If you're building a database-driven app, chances are you'll have forms that map closely to Django models.<br>
Steps to create Model Form
<pre>
Step 1: create models
class Product(models.Model):
    product_name = CharField(max_length=30)
    product_purchase = CharField(max_length=10)
    product_code = IntegerField()
    
Step 2:create forms.py inside the app
from .models import Product

class ProductDetails(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_purchase','product_code']		# we can specify what all fileds we need if we need all the fields use fileds=__all__'
        labels = {'product_name':'Enter product Name',
                  'product_purchase':'Enter product purchase date',
                  'product_code':'Enter product code'}
        error_messages = {
            'product_name':{'required':'Name is required'},
            'product_purchase':{'required':'purchase date is required is required'}
        }
        widgets = {
            'product_code':forms.PasswordInput({'placeholder':'passcode'})
        }

creating form for the product, now the data coming in this form will be send to views and cleaned data will be saved to db.

Step 3: views.py
from .forms import ProductDetails
from .models import Product

def showformdata(request):
    if request.method == "POST":
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['product_name']
            ph = fm.cleaned_data['product_purchase']
            cd = fm.cleaned_data['product_code']
            reg = Product(product_name=nm, product_purchase=ph, product_code=cd)
            reg.save()
    else:
        fm = ProductDetails()
    return render(request, 'demo.html',{"form":fm})
    
Here we don't need the cleaned data miss taught in lecture. We can direclty write:
form = ProductForm()
if request.method=="POST":
	form.save()  	 
else:
        form = ProductDetails()
    return render(request, 'demo.html',{"form":form})
    
def addCourse(request):
	form=CourseModelForm()
	if request.method=="POST":
		form=CourseModelForm(request.POST)
		if form.is_valid():
			form.save(commit=TRUE)		#by default commit will be true so it is exceptional.
	return render(request, 'App1/addcourse.html',{'data':data})

The 'form' key will pass in html form like we use {{form.as_p}}
    
 Step 4: demo.html
&lt;html&gt;
&lt;body&gt;
	&lt;h1&gt;Hello&lt;/h1&gt;
	&lt;form action="" method="POST" novalidate&gt;     //django form does not provide the form tag and button so we have to write it.
	{% csrf_token %}
	{{form.as_p}}
	&lt;input type="submit" values="submit"&gt;
&lt;/body&gt;
&lt;/html&gt;

No validation bcoz we want to see the django form validation.
</pre>
<b>To success message after the form submission</b>
<pre>
Step 1: in views.py
After the save method write the message code.

from django.contrib import messages
            reg = Address(email=email, password=password)
            reg.save()
            messages.success(request, 'Your message has been inserted.')
	    
index.html
{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissible fade show my=0" role="alert">
    {{ message }}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  {% endfor %}
{% endif %}
</pre>

<a name="thirteen"><h2>2.11 Django Form Validation</h2></a><br>
<a name="fourteen"><h2>2.12 Django’s Inbuilt Core Validators</h2></a><br>






































<a name="fifteen"><h2>2.13 Model Based Forms</h2></a><br>
<a name="sixteen"><h2>2.14 Advanced Templates</h2></a><br>
<b>Template Inheritance</b><br>
Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.<br>
<pre>
base.html	//common for all the pages
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt; {% block title %} {% endblock title %} | XYZ School&lt;/title&gt;
&lt;/head&gt;
&lt;body>
&lt;h1&gt;XYZ School&lt;/h1&gt;
&lt;nav&gt;
&lt;a href="/home">Home&lt;/a&gt; |
&lt;a href="/contact"&gt;Contact&lt;/a&gt; |
&lt;/nav&gt;
&lt;!--Header will be same--&gt;

{% block body %} {% endblock body %}    &lt;!--Body will change--&gt;

&lt;!--Footer will be same--&gt;
&lt;footer&gt;Copywrite xyz company 2021&lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;

base.html have header and footer defined. Now this header and footer will be common for all the pages.

home.html
{% extends 'base.html' %}
{% block title %}Home{% endblock title %}

{% block body %}  
&lt;h1&gt;This is Home page&lt;/h1&gt;
{% endblock body %}

contact.html
{% extends 'base.html' %}
{% block title %}Contact{% endblock title %}

{% block body %}  
&lt;h1&gt;This is Contact page&lt;/h1&gt;
{% endblock body %}
</pre>

Template Filters: https://docs.djangoproject.com/en/3.2/ref/templates/builtins/

Template tags for relative URLs<br>
Advantages of Template Inheritance<br>
Why Template Filters?<br>
What is Template Filter?<br>
How to Create Customized Template Filters?<br>

<a name="seventeen"><h2>2.15 Session Management in Django</h2></a><br>
<a name="eighteen"><h2>2.16 Authentication & Authorization</h2></a><br>
Authentication vs Authorization:<br>
Authentication confirms that users are who they say they are.Example username & password<br>
Authorization gives those users permission to access a resource. Example i only can access my facebook settings, privacy etc.<br>

![Authentication_vs_Authorization](https://user-images.githubusercontent.com/59610617/128353973-5dc9e5fe-951a-46db-852b-40b27b4c78aa.png)<br>

What all django admin provides?<br>
Django comes with a built-in admin interface. With Django's admin you can authenticate users, display and handle forms, and validate input; all automatically. Django also provides a convenient interface to manage model data.<br><br>
What is not included in django admin?<br>
Django does'nt provide all these tho we can use if else or third party, or other way to achieve all these.<br>
1)Password strength checking <br>
2)Throttling of login attemps: it means someone trying to access the site with different name and combinations of different name, number etc., So django does'nt provide this.<br>
3)Authentication against third-parties(OAuth, for example): example login by fb,google etc.<br>
4)Object-level permission: permission like only some members can access particular models etc.<br>
<br>
Customizing the django admin interface.<br>
<pre>
admin.site.site_header = "Welcome Fareen"       #visible on login header
admin.site.site_title = "Welcom to fareens dashbord"    #title of the site
admin.site.index_title = "welcome to this portal"       #After login the the header will be this
</pre>

<a name="nineteen"><h2>2.17 Class Based Views (CBV)</h2></a><br>
Base Class-Based Views / Base View<br>
Generic Class-Based Views / Generic View<br>

Advantages:<br>
1)Organization of code related to specific HTTP methods(GET, POST, etc) can be addressed by seperate methods instead of conditional branching.<br>
2)Can use inheritance.<br>

Basic example of class vs function based view.<br>
In function based view we don't write get method, bcoz when we hit url get method is called. But in class based view we must get method. See below example.
<pre>
views.py
function view:
from django.http import HttpResponse
def myview(request):
	return HttpResponse("Hello")

urls.py
from django.urls import path
from school import views
urlpattern = [
		path('hello/',views.myview, name='hello'),
	]

class view:
from django.views import View
class MyView(View):
	def get(self,request):
		return HttpResponse("Hello")

urls.py
from django.urls import path
from school import views
urlpattern = [
		path('hello/',views.MyView(), name='hellohello	]
</pre>

<h2>Base Class-Based Views / Base View</h2><br>
In this we have View, TemplateView, RedirectView.<br
To see the code of parent 'VIEW' go to :<br> C:\Users\faree\AppData\Local\Programs\Python\Python39\Lib\site-packages\djongo\views\generic<br>
<pre>
>>To return name from class:
class MyClassView(View):
    name="fareen"
    def get(self,request):
        return HttpResponse(self.name)
	
>>Or we can directly pass this in class:
path('class/',views. MyClassView.as_view(name="ansari"), name="class")

For this to run we must defind name inside the class.

>>To reuse the class, inherit it:
class MyClassView(View):
    name="fareen"
    def get(self,request):
        return HttpResponse(self.name)

class ChildView(MyClassView):		#accessing the name in child class.
    def get(self,request):
        return HttpResponse(self.name)

Create url for both.

>>To render html in class based view:
class MyClassView(View):
    def get(self,request):
        return render(request, 'index.html')

>>To return the context:
class MyClassView(View):
    def get(self,request):
        context = {'msg':'welcome to my page'}
        return render(request, 'index.html', context)

index.html
&lt;h1&gt; {{msg}} &lt;/h1&gt;
</pre>

<b>Class based view returning post method</b><br>
GET, POST request.<br>
In the above code when we hit the url defined the urls.py the get request get called meaning the else part will run and bcoz of that we can see the blank form, When the request is post 'if'  part runs, meaning when we click the 'submit' button the post method gets called.<br>
But in class based view we have to define every method. So we have to defined get request for blank form and we get this form when we hit the url. And POST method for form data.<br>
<pre>
class MyClassView(View):
    #here we'll write function based view's else part which we write for get method 
    def get(self,request):
        form = ContactForm()
        return render(request, 'index.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse('Form submitted')

index.html
&lt;form action="" method="POST"&gt;
	{% csrf_token %}
	{{form.as_p}}
	&lt;input type="submit" value="SUBMIT"&gt;
&lt;/form&gt;
</pre>

<b>To get the two different templates for same view</b><br>
In case we want to write two templaes for the same view, in this case instead of writing the two same views for two different templates write one view and give templates on url.
<pre>
class MyClassView(View):
    template_name = ''
    def get(self,request):
        form = ContactForm()
        return render(request, self.template_name , {'form':form})

urls.py
path('class1/',views.MyClassView.as_view(template_name='index.html'), name="class1"),
path('class2/',views.MyClassView.as_view(template_name='index2.html'), name="class2"),

Whenever we hit the url, it search for template_name variable and assign the value we given in url which is index1, index2 and pass that to render function.
</pre>

<h2>Generic Class-Based Views / Generic View<br></h2
In every application we use CRUD, so django gave some setup code which we can reuse.<br>
For example when we want to add data we use create view. These are common task which we can use.<br>
1)Display View: ListView, DetailView.<br>
2)Editing View: FormView, CreateView, UpdateView, DeleteView.<br>
3)Data View: ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView,TodayArchiveView, DateDetailView.<br>

<h3>Display View</h3>
ListView: page representing a list of objects.<br>
This view inherits methods and attributes from the following views: django.views.generic.list.MultipleObjectTemplateResponseMixin, django.views.generic.base.TemplateResponseMixin, django.views.generic.list.BaseListView, django.views.generic.list.MultipleObjectMixin, django.views.generic.base.View<br>

 1)ListView:
 <pre>
 Step 1: views.py
from django.views.generic.list import ListView
from .models import Student

class StudentList(ListView):
    model=Student
    template_name = 'school/student.html'	#default name is student_list.html
    context_object_name = 'students'

    def get_template_names(self):
        if self.request.user.is_superuser:
            tempmate_name = 'school/fareen.html'
        else:
            tempmate_name =self.template_name
        return [tempmate_name]

#after running the applictaion it'll show template does'nt exist school/student_list.html the same template we have to make
# this code has student_list key which we cant see and in html we'll pass it

# instead of all these lines we're only writing one line
# stud=Student.objects.all()
# context={'student_list':stud}     This student_list key will be passed to html
# return render(request,'demo.html',context)

VARIABLES:
1)Default name is student_list.html. To change the name of the _list add one line after model=Student
template_name_suffix='_get', now it'll search for student_get

2)To give custom name to the template
template_name="school/student.html"
now we can use both student_list or student both will work 
custom one has high priority over default one if both custom and default present then custom will get the priority

3)To change the ordering eg order by name then use
ordering = ['name']  or roll or anything

4)To give default context name which we pass in html student_list or object_list we can chage that too:
context_object_name = 'students' now we can pass students and it'll work
now we must use students in html default student_list won't work in this case

# METHODS
1) get_queryset(self):
Example: to filter based on name
   def get_queryset(self):
        return Student.objects.filter(name='fareen')

2) get_context_data(self, *args, **kwargs)
Example: to use order_by
    def get_context_data(self, *args, **kwargs):
        context =super().get_context_data(*args, **kwargs)
        context['students'] = Student.objects.all().order_by('name')
        return context

3) get_template_names(self)
Example: to render the html based on the cookie
def get_template_names(self):
        if self.request.COOKIES['user'] == 'fareen':        #if the cookie name is fareen, fareen.html will run else the default 'student.html' one we gave will run
            tempmate_name = 'school/fareen.html'
        else:
            tempmate_name =self.template_name
        return [tempmate_name]
	
Step 2: students.html
  {% for s in students%}        //Default is student_list & object_list both will work, but we've given context_object as students
  {{s.name}}
  {{s.roll}}
  {%endfor%}
</pre>

<h3>Editing View</h3>

![updateview](https://user-images.githubusercontent.com/59610617/129467693-177ab80f-f51e-4560-bad9-7fa84fa959e7.png)<br>

<pre>
METHOD 1:

Step 1: views.py
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django import forms

# Create
class StudentEdit(CreateView):			#this will create a form and accept data as well
    model=Student				#createview will create a form with the given fields but won't create submit button we've to add it ourself in html.
    fields=['name','roll']
    success_url = 'thanks'			
    
    def get_form(self):         #copy same form for update
        form = super().get_form()
        form.fields['name'].widget =forms.TextInput()
        form.fields['roll'].widget =forms.PasswordInput(render_value=True, attrs={'class':'myclass'})		#render_value=True for password to be visible 
        widgets={'name':forms.TextInput(attrs={'class':'myclass'})}
        return form,widgets


#update based on pk
class StudetUpdate(UpdateView):		#this will update the data 
    model=Student
    fields=['name','roll']
    success_url = 'thanks'		#in this we can pass function too 
   
[
success_url = 'display'
def display(request):
    return HttpResponse("Registered!!")
 
 path('display/',views.display,name="display")
]

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'


Step 2: student_form.html	#this name must be same if we want different name use the variables example given above in list view

  &lt;form action="" method="POST"&gt;
  {% csrf_token %}
  {{form.as_p}}
  &lt;input type="submit" value="Submit"&gt;		#createview creating input fields but not button that's why we've given button here
  &lt;/form&gt;
 
Step 3: urls.py
    path('',views.StudentEdit.as_view()),
    path('thanks',views.ThanksTemplateView.as_view()),
    path('update/thanks',views.ThanksTemplateView.as_view()),
    path('update/<int:pk>',views.StudetUpdate.as_view())
    
    

METHOD 2:
Step 1: forms.py create django model form
from .models import Student
from django import forms

class StudentForm(froms.ModelForm):
	class Meta:
	model = Student
	fields = ['name','roll']	#or fields = '__all__'
        widgets={'name':forms.TextInput(attrs={'class':'myclass'}), 'roll':
	forms.PasswordInput(attrs={'class':'myclass'})}

Step 2: views.py
#form create
class StudentCreateView(CreateView):		#import create view first
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = 'thanks'

#for update
class StudentUpdateView(CreateView):		#import create view first
	model = Student
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = 'update/thanks'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'
	
Step 3: create urls
    path('',views.StudentCreateView.as_view()),
    path('thanks',views.ThanksTemplateView.as_view()),
    path('update/<int:pk>',views.StudetUpdate.as_view()),
    path('update/thanks',views.ThanksTemplateView.as_view()),
</pre>
Lecture notes:
<pre>
  {% for i in student_list%}
  {{i.name}}
  &lt;a href = "update/{{i.id}}"&gt;Edit&lt;/a&gt;
  {% endfor %}
  
path('list/update/<int:pk>',views.StudetUpdate.as_view()),
</pre>
















PENDING





















<a name="twenty"><h2>2.18 Django File Upload</h2></a><br>
<a name="twenty_one"><h2>2.19 Django CRUD Operations</h2></a><br>
<a name="twenty_two"><h2>2.20 Django Middleware</h2></a><br>
<a name="twenty_three"><h2>2.21 How to Send Email in a Django</h2></a><br>
<a name="twenty_four"><h2>2.22 Outputting CSV with Django</h2></a><br>
<a name="twenty_five"><h2>2.23 Outputting PDF with Django</h2></a><br>
<pre>
Step 1: views.py
from django.http import HttpResponse, response
from django.template.loader import get_template		#for pdf
from django.views.generic import View
from .utils import render_to_pdf 

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
	
Step 2: create a utils.py inside the app
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

Step 3:urls.py
path('pdf/',views.GeneratePDF.as_view()),
</pre>
Output:

![pdfop](https://user-images.githubusercontent.com/59610617/129466279-22e531eb-5202-4587-b663-e2b78cf4d984.png)<br>


<a name="twenty_six"><h2>2.24 Django Crispy Forms</h2></a><br>
What is django crispy forms?<br>
Django-crispy-forms is an application that helps to manage Django forms. It allows adjusting forms' properties (such as method, send button or CSS classes) on the backend without having to re-write them in the template.<br>
Django from with bootstrap 4 form and it's validation.<br>
<pre>
Step 1:
install crispy forms:
>pip install django-crispy-forms

Step 2:
Add it to your INSTALLED_APPS and select which styles to use:
INSTALLED_APPS = [
    ...

    'crispy_forms',
]

#add this in the end of settings.py
CRISPY_TEMPLATE_PACK = 'bootstrap4'

Step 3:
forms.py

from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
    
Step 4:
demo.html

Here use the boostrap starter template and put the form code inside the starter template conatiner

&lt;form method="post"&gt;
    {% csrf_token %}
     {{ form.as_p}}
    &lt;button type="submit">Sign in&lt;/button&gt;
  &lt;/form&gt;
</pre>
This is just the bootstrap form with django default validation.<br>

![before](https://user-images.githubusercontent.com/59610617/128303260-6db049ae-0913-43e6-a5d3-f35ea6d91a37.png)


Bootstrap form with validation using crispy form.<br>
<pre>
Just change the demo.html

{% load crispy_forms_tags %}
&lt;div class="container"&gt;
 &lt;form method="post" novalidate=""&gt;
    {% csrf_token %}
    {{ form|crispy }}
    &lt;button type="submit" class="btn btn-primary"&gt;Sign in&lt;/button&gt;
  &lt;/form&gt;
 &lt;/div&gt;
</pre>

![after](https://user-images.githubusercontent.com/59610617/128303285-2269bf18-b84c-48f2-a829-be2e0b76f363.png)<br>

Custom Fields Placement with Crispy Forms<br>
<pre>
	code in boostrap.txt
</pre>

![b1](https://user-images.githubusercontent.com/59610617/128303355-65ef7352-0b23-4dcd-9254-ed52de8c8054.png)<br>

![b2](https://user-images.githubusercontent.com/59610617/128303368-4c43a3e1-7e97-4095-b38b-b77bb567ef88.png)<br>

<h1></h1>
In-built validation<br>
If we want our own validtion to apply on particular filed use the validator.
<pre>
We can either define the validation for particular filed or reuse it using validation.
Method 1: For email field only
forms.py

from django import forms

class ContactForm(forms.Form): 
    email       = forms.EmailField()

    def clean(self):
        # form level cleaning
        cleaned_data = super(ContactForm, self).clean()
        email_passed = cleaned_data.get("email")
        if not "yourdomain.com" in email_passed:
            raise forms.ValidationError("Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")
	
Method 2: For all the emails in the entire form

In forms.py
Define your custome validation before creating the validation:

from django import forms 
from django.core.exceptions import ValidationError

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "yourdomain.com" in value:
        raise ValidationError("Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")

field:
important_email = forms.EmailField(validators=[validate_domainonly_email], max_length=30)
customer_email = forms.EmailField(validators=[validate_domainonly_email], max_length=30)
</pre>

![b3](https://user-images.githubusercontent.com/59610617/128307624-2bc59903-f933-4f48-b29f-32e915f4adc3.png)<br>


<a name="twenty_seven"><h2>2.25 GIT & Github</h2></a><br>
<a name="twenty_eight"><h2>2.26 Bitbucket</h2></a><br>
<a name="twenty_nine"><h2>2.27 Deploying Django Apps & Heroku</h2></a><br>
<a name="thirty"><h2>2.28 Introduction to Web Services</h2></a><br>
<a name="thirty_one"><h2>2.29 Introduction to XML</h2></a><br>
<a name="thirty_two"><h2>2.30 Introduction to REST API(Restful Services)</h2></a><br>
<a name="thirty_three"><h2>2.31 Connecting with Mysql</h2></a><br>
<pre>
Step 1:
pip install mysqlclient

Step 2:
Creating database in mysql

Step 3:
Give the database name, password etc
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'djangoProject',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER':'root',
        'PASSWORD':'',
    }
}

Step 4:
Run migration commands
>python manage.py makemigrations
>python manage.py migrate

Now if we check the djangoProject database we'll get all the migrated tables. 

</pre>
<a name="thirty_four"><h2>2.32 Connecting with PostgreSql</h2></a><br>
<a name="thirty_five"><h2>List of errors when performing the practical</h2></a><br>
Error in fiels:
<pre>
You are trying to add a non-nullable field 'positiveint1' to product without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing 
rows with a null value for this column)
 2) Quit, and let me add a default in models.py
 
This error is bcoz we have added some data in the database, now the new column we added and the old column need some data that is why it asks for default data.

To remove this error we can delete the all the (migartions files added+__pycache__ in both app and migrations).
</pre>

<a name="thirty_six"><h2>Extra</h2></a><br>
<h2>To redirect</h2>
<pre>
Step 1: import the redirect from shortcut:
def addCourse(request):
	form=CourseModelForm()
	if request.method=="POST":
		form=CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/App1/courseList')
	return render(request,'studentapp/addCourse.html',{'data':data})
</pre>

<h2>Show data in table format</h2>

![table](https://user-images.githubusercontent.com/59610617/129444980-b08c193b-0e80-4871-9719-7e4f831e524f.png)<br>

<h2>To select data using id</h2>
<pre>
as in select * from emwhere id=1

in word file


get() it will return single record
filter() it will return multiple record 

</pre>

<h2>To add bootstrap form</h2>
downloaded the bootstrap cdn and paste it in static css folder and link using {% load static %} then in models.py <br>
