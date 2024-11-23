# Lesson40 (Using Lesson38 Database to demonstrate QuerySet)

20.09.2024-02:58

## QuerySet:
py manage.py shell
from members.models import Member 
Member.objects.all()
m1 = Member.objects.all()[1]
m1.firstname
Member.objects.all().values()
Member.objects.all().values_list()
Member.objects.all().values_list('firstname')
list(Member.objects.all().values_list('firstname'))
Member.objects.all().values_list('firstname',flat=True)
Member.objects.all().values_list('id',flat=True)
Member.objects.filter(firstname='Emil')                                           (Gets all values)   
Member.objects.get(firstname='Emil')                                              (Gets specific value)
Member.objects.filter(firstname='Emil', id=1)                                     (AND-Operator)
Member.objects.filter(firstname='Emil') | Member.objects.filter(firstname='Cij')  (OR-Operator)
Member.objects.filter(firstname__startswith='A')                                  (Field Lookup)
Member.objects.filter(lastname__startswith='T')
Member.objects.filter(lastname__contains='e')                                     (Contains)
Member.objects.filter(lastname__icontains='e')                                    (Same as contains, but case-insensitive)
Member.objects.filter(id__in=[1,4])                                               (Filter by list of ID)
Member.objects.filter(firstname__in=['Sergey','Cij'])
Member.objects.filter(id__gt=2)                                                   (Greater then)
Member.objects.filter(firstname__startswith='C').filter(lastname='Temkin')        (Adding another filter)
Member .objects.filter(joined_date__lt=timezone.now().date())                     (Less than)
Member .objects.filter(joined_date__lte=timezone.now().date())                    (Less than, or equal to)
Member.objects.all().order_by('id')                                               (Order by)  
Member.objects.all().order_by('-id')                                              (Descending Order)
Member.objects.filter(lastname__startswith='T').order_by('firstname')
Member.objects.filter(court=1)                                                    (All Members in court-1)
Member.objects.filter(court__is_occupied=1)                                       (All Courts that occupied)
Member.objects.filter(court__number__in=[1,2])                                    (All Members in Courts:1,2)

## Update all joined_date values in Database
from django.utils import timezone
members = Member.objects.all()
for member in members:
    member.joined_date = timezone.now().date()
    member.save()

## Update Member joined_date value in Database
from datetime import timedelta
new_date = timezone.now() - timedelta(days=3)     
member. joined_date = new_date.date()
member.save()



# Django
## Initialize application:
pip install django
django-admin startproject (Name of project)  .  (Don't forget space and dot at the end!!!)
py manage.py startapp (Name of folder)
py manage.py runserver

## Admin:
py manage.py runserver
py manage.py createsuperuser

## Migration to Database:
py manage.py makemigrations  
py manage.py migrate

## Shell,I-python commends:
py manage.py shell

## Adding to Database:
from courts.models import Court
c = Court(number1)
c.save()

from members.models import Member
m = Member(firstname='Emil', lastname='Refsnes', phone='111111')
m.save()

court = Court.objects.first()
m = Member(firstname='Emil', lastname='Refsnes', phone='111111', court=court)
m.save()
court2 = Court.objects.get(id=2)
m = Member(firstname='Emil', lastname='Refsnes', phone='111111', court=court2)
m.save()

## Delete from Database:
x = Member.objects.all()[0]       [0] --Witch index to delete
x.firstname                       Check the name of the index to delete(Optional)
x.delete()

## Delete all:
Member.objects.all().delete()

## Change id:
x = Member.objects.all()[0]
x.id                         (Lets say it's:7)
x.id = 1 
x.save()

## Reset the Auto-increment Sequence of ID in DB:
Member.objects.all().delete()
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="@@@@"')     (change: "@@@" to the table name in DB, Example:"members_member") 

## Work with Ipython Shell
1. In main project folder, in settings folder add the line: SHELL_PLUS ='ipython'
2. pip install ipython
3. python manage.py shell
4. exit()

## Virtual Environment
python -m venv venv
source venv/Scripts/activate
deactivate

## VScode path
PC:
cd "C:\Users\USER\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/"
Laptop:
cd "C:\Users\sergh\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/"

## Uninstall all packages in a virtual environment
pip freeze | xargs pip uninstall -y
deactivate
pip cache purge
DELETE VENV FILE!!!

## GIT add
git add . 
git status 
git commit -m " " 
git push

## Remove last commit on GIT
git reset HEAD~1
git push -f origin main

## Requirements
pip freeze > requirements.txt 
pip install -r requirements.txt

## Packages
pip install django
pip install flask
pip install flask-cors
pip install sqlalchemy 
pip install psycopg2
pip install mysqlclient

http://127.0.0.1:500
http://127.0.0.1:5500
http://127.0.0.1:8000/