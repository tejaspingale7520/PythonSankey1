#basics of python

# a=20
# if a > 10 :
#     print('a is greater than number')


# x=30 if 10 > 20 else 40
# print(x)

# swapping numbers a,b=10,20 ;a,b=b,a;print(a,b)

# x=int(input('enter 1st number:'))
# y=int(input('enter 2st number:'))
# z=x+y
# print(z)


# def sum(a,b):
#     print('the sum is:',a+b)

# sum(10,20)
# sum(20,30)

# sum(100,100)

#creating class and function

# class abc:
#     def add(self,a,b):
#         print('the sum is:',a+b)
# d=abc()
# d.add(500,1000)


###DB operations

#import sqlite3
# con=sqlite3.connect('hello.db')
# cur=con.cursor()
# #cur.execute("create table Student(e_id INTEGER PRIMARY KEY AUTOINCREMENT,e_name Text NOT NULL,salary REAL,mob_no INTEGER)")
# #print("table is created")

# cur.execute("INSERT INTO Student(e_name,salary,mob_no) VALUES('A',20000,9222222222)")
# cur.execute("INSERT INTO Student(e_name,salary,mob_no) VALUES('B',20000,9233333333)")
# cur.execute("INSERT INTO Student(e_name,salary,mob_no) VALUES('C',20000,944444444)")

# print(cur.)


# print("data inserted")
# con.commit()
# con.close()

# import sqlite3
# con=sqlite3.connect('hello.db')
# cur=con.cursor()

# print("e_id \t e_name \tsalary \tmob_no\n")
# xyz=cur.execute("SELECT * FROM Student")

# for row in xyz:
#     print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])

# con.close()

##if update operation 

# import sqlite3

# con =sqlite3.connect('hello.db')
# cur=con.cursor()

# c=cur.execute("UPDATE Student SET salary = salary + 500")
# con.commit()
# print("e_id \t e_name \t salary \t mob_no\n")
# co=cur.execute("SELECT * from Student")
# for e in co:
#     print(e[0],"\t",e[1],"\t",e[2],"\t",e[3])
# con.close()


# def greet(f_name,l_name):
#     print(f"hi {f_name} {l_name}")
#     print("how are you")

# greet("ram","Shyam")

# def get_greeting(name):
#     return f"hi {name}"

# mesg=get_greeting("onkar")


# def increment(number,by=1):
#     return number + by

# print(increment(2,5))

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number

#     return total
# print(multiply(1,2,3,4))

# def save_user(**user):
#     print(user["id"])

# save_user(id=1,name='jonny',age=10)
# def fizz_buzz(input):
#     if input % 3 ==0:
#         return "fizz"
#     if input % 5 ==0:
#         return "buzz"
#     if (input %3 ==0) and (input % 5==0):
#         return "fizzbuzz"
#     return input
 
# a=fizz_buzz(17)
# print(a)


##strings

# course="abcd"
# print(course.upper())

# var="this is new journey"
# print("is" in var)

# weight=int(input("weight:"))
# unit=input("(K)g or (L)bs:")
# if unit.upper()=="K":
#     converted=weight/0.45
#     print("weight in lbs:"+str(converted))
# else:
#     converted=weight*0.45
#     print("weight in kgs:"+str(converted))

# i=1
# while i<=5:
#     print(i * "*")
#     i=i+1
# try:
#     names=["a","b","c"]
#     print(names[2])
# except:
#     print("sorry the given alphabates not in list")



# numbers=[1,2,3,4,5,6]
# #numbers.append(7)
# #print(len(numbers))

# for i in numbers:
#     print(i)
# num=range(1,100,10)
# for number in num:
#     print(number)
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import User  # Assuming User is your model for users

# @csrf_exempt
# def user_details(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User not found'}, status=404)

#     if request.method == 'PUT':
#         try:
#             data = json.loads(request.body)  # Load the JSON data from the request body
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)

#         user.name = data.get('name', user.name)  # Assuming 'name' is a field in the User model
#         user.email = data.get('email', user.email)  # Assuming 'email' is a field in the User model
#         user.save()

#         return JsonResponse({
#             'id': user.id,
#             'name': user.name,
#             'email': user.email,
#         }, status=200)

#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)

#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)


##Filter 

# l=[1,2,3,4,5,6]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)

##Map

# l=[1,2,3,4,5]
# l1=list(map(lambda x:x*2,l))
# print(l1)

##Reduce
#from functools import *
# l=[1,2,3,4,5,6]
# l1=reduce(lambda x,y:x+y,l)
# print(l1)
# l=reduce(lambda x,y:x+y,range(1,101))
# print(l)

###decorator

# def logged(function):
#     def wrapper(*args,**kwargs):
#         value=function(*args,**kwargs)
#         with open('logfile.txt','a+') as f:
#             fname=function.__name__
#             print(f"{fname} return value {value}")
#             f.write(f"{fname} return value{value}\n")
#         return value
#     return wrapper

# @logged
# def add(x,y):
#     return x+y
# print(add(10,20))
# import time
# def timed(function):
#     def wrapper(*args,**kwargs):
#         before=time.time()
#         value=function(*args,**kwargs)
#         after=time.time()
#         fname=function.__name__
#         print(f"{fname} took {after-before} seconds to execute")
#         return value
#     return wrapper

# @timed
# def my_function(x):
#     result=1
#     for i in range(1,x):
#         result=result*i
#     return result

# my_function(90000)


###Generator

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values=mygenerator(90000)

print(next(values))
print(next(values))

print(next(values))


