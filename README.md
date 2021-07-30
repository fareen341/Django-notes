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
[<p>2.24 Django Crispy Forms</p>](#twenty_six)
[<p>2.25 GIT & Github</p>](#twenty_seven)
[<p>2.26 Bitbucket</p>](#twenty_eight)
[<p>2.27 Deploying Django Apps & Heroku</p>](#twenty_nine)
[<p>2.28 Introduction to Web Services</p>](#thirty)
[<p>2.29 Introduction to XML</p>](#thirty_one)
[<p>2.30 Introduction to REST API(Restful Services)</p>](#thirty_two)


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
Django App structure.<br>
![structure_drawing2_new](https://user-images.githubusercontent.com/59610617/127651090-718b540a-754a-4f72-9f3a-7c6081edf9dc.png)<br>
Creating first project in VS code editor.<br>
<pre>
Step 1: create project folder -> ctrl+right click -> open Windows PowerShell here
Step 2: in powershell type >django-admin startproject ProjectName(eg GymProject)
It will create a project name folder : and inside it there will be:
<li>GymProject</li>
<li>manage.py</li>

Now open this project in vscode
Inside GymProject folder it will have.
<li>__init__.py</li>
<li>asgi.py</li>
<li>settings.py</li>
<li>urls.py</li>
<li>wsgi.py</li>
<li>manage.py</li>
</pre>

NOTE: type django-admin to see all commands<br>
django-admin is Django's command-line utility for administrative tasks. ... In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project's settings.py file.<br>

Creating first app:<br>
<pre>
Step 1: Open vscode terminal type >django-admin startapp firstApp<br>
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
<pre>
views.py
from django.shortcuts import render, HttpResponse

def firstview(request):
    return HttpResponse("Hello from first app")
    
This view will return http response.
</pre>

Developing different views<br>

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
1)Project Level: not recommended.
<pre>
  from firstApp import views
  from secondApp import views as vw	    #if we give same 'views' name to both the app then it'll give error to resolve this use alias on other views.
 
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('',views.firstview, name="message"),
      path('datedisp/',vw.secondview, name="date"),
  ]
  
</pre>

2)App Level: recommended
<pre>
instead of giving all urls in one file, give urls in every app:
Advantages of giving urls for each app are application reusability, redable format, reduce code complexity.

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
STATIC_DIR=os.path.join(BASE_DIR,'static')	//Here we are basically joining the path of static folder and providing the variable name inside the settings.py syntax
						//We can directly give join the path inside the setting.py syntax like this:
						STATICFILES_DIRS=[
    							os.path.join(BASE_DIR,'static')
						]		

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


<a name="ten"><h2>2.8 DJANGO MODEL</h2></a><br>
Define Database?
Define DBMS, RDBMS?
What is Model?
Database Configuration
How to Check Django Database Connection
Configuration of MySQL Database
SQLite
Defining Django Models
Django Model Fields
Field Options
What is a Migration?
migrate Command
Creation of Super User
Register Model Inside Admin Interface
Difference between makemigrations and migrate
Define QuerySet
The Python Template Engine
Define Jinja2
Faker Module
<a name="eleven"><h2>2.9 Relationships in Django Models</h2></a><br>
<a name="twelve"><h2>2.10 Django Forms or Model Forms</h2></a><br>
<a name="thirteen"><h2>2.11 Django Form Validation</h2></a><br>
<a name="fourteen"><h2>2.12 Django’s Inbuilt Core Validators</h2></a><br>
<a name="fifteen"><h2>2.13 Model Based Forms</h2></a><br>
<a name="sixteen"><h2>2.14 Advanced Templates</h2></a><br>
<a name="seventeen"><h2>2.15 Session Management in Django</h2></a><br>
<a name="eighteen"><h2>2.16 Authentication & Authorization</h2></a><br>
<a name="nineteen"><h2>2.17 Class Based Views (CBV)</h2></a><br>
<a name="twenty"><h2>2.18 Django File Upload</h2></a><br>
<a name="twenty_one"><h2>2.19 Django CRUD Operations</h2></a><br>
<a name="twenty_two"><h2>2.20 Django Middleware</h2></a><br>
<a name="twenty_three"><h2>2.21 How to Send Email in a Django</h2></a><br>
<a name="twenty_four"><h2>2.22 Outputting CSV with Django</h2></a><br>
<a name="twenty_five"><h2>2.23 Outputting PDF with Django</h2></a><br>
<a name="twenty_six"><h2>2.24 Django Crispy Forms</h2></a><br>
<a name="twenty_seven"><h2>2.25 GIT & Github</h2></a><br>
<a name="twenty_eight"><h2>2.26 Bitbucket</h2></a><br>
<a name="twenty_nine"><h2>2.27 Deploying Django Apps & Heroku</h2></a><br>
<a name="thirty"><h2>2.28 Introduction to Web Services</h2></a><br>
<a name="thirty_one"><h2>2.29 Introduction to XML</h2></a><br>
<a name="thirty_two"><h2>2.30 Introduction to REST API(Restful Services)</h2></a><br>
