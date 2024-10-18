from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Teacher,Student
from django.core.exceptions import ValidationError
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

# Create your views here.
def teacher_list(request):
    try:
        #teachers=Teacher.objects.all()
        teachers = Teacher.objects.all().values()
        #teachers_info=[{"id": teacher.id, "name": teacher.name, "subject": teacher.subject, "email": teacher.email} for teacher in teachers]
        #return JsonResponse(teachers_info,safe=False)
        # 
        # #  # you can  Searching  teachers/?name=
        name_query = request.GET.get('name', None)
        if name_query:
            teachers = teachers.filter(name__icontains=name_query)

        # # Sorting
        sort_by = request.GET.get('sort_by', None)
        if sort_by in ['name', 'subject', 'email']:
            teachers = teachers.order_by(sort_by)

        return JsonResponse(list(teachers), safe=False)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=500)




def teacher_detail(request, pk):
    try:
        #teacher = get_object_or_404(Teacher, id=pk)
        teacher=Teacher.objects.get(id=pk)
        return JsonResponse({"id": teacher.id, "name": teacher.name, "subject": teacher.subject, "email": teacher.email})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@csrf_exempt
def add_teacher(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
           
            teacher=Teacher.objects.create(name=data['name'],subject=data['subject'],email=data['email'])
            #teacher = Teacher(**data)  #for passing varialble argumennt list ,so our code will be  less and  more optimise
            teacher.full_clean()  # Validate the model  method is called on model instances before saving them. 
            #This method checks for validation errors according to the model fields, ensuring that only valid data is saved.
            #teacher.is_valid()  #it will show error bcz we dont have any serializer or valid attribute
            teacher.save()
            return JsonResponse({"record inserted for id": teacher.id}, status=201)
       
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
@csrf_exempt
def update_teacher(request, pk):
    try:
        #teacher = get_object_or_404(Teacher, id=pk)
        teacher=Teacher.objects.get(id=pk)
        if request.method == 'PUT'or 'PATCH':
            data = json.loads(request.body)

            # for key, value in data.items():  #to get k v in 
            #     setattr(teacher, key, value)

            teacher.name=data.get('name',teacher.name)
            teacher.subject=data.get('subject',teacher.subject)
            teacher.email=data.get('email',teacher.email)
            

            teacher.full_clean()  # Validate the model
            teacher.save()
            return JsonResponse({"id": teacher.id})
    except ValidationError as ve:
        return JsonResponse({"errors": ve.messages}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
@csrf_exempt
def delete_teacher(request, pk):
    try:
        teacher = get_object_or_404(Teacher, id=pk)
        teacher.delete()
        return HttpResponse({'msg':'item deleted successfully'},status=204)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    



def student_list(request):
    try:
        students = Student.objects.all().values()

        # Searching
        name_query = request.GET.get('name', None)
        if name_query:
            students = students.filter(name__icontains=name_query)

        # Filtering by enrolled date  /students/?name=    &enrolled_date=
        enrolled_date_query = request.GET.get('enrolled_date', None)
        if enrolled_date_query:
            try:
                enrolled_date = datetime.strptime(enrolled_date_query, '%Y-%m-%d').date()
                students = students.filter(enrolled_date=enrolled_date)
            except ValueError:
                return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

        # Filtering by teacher name  students/?teacher_name=
        teacher_name_query = request.GET.get('teacher_name', None)
        if teacher_name_query:
            students = students.filter(teacher__name__icontains=teacher_name_query)

        # Sorting  /students/?sort_by=name
        sort_by = request.GET.get('sort_by', None)
        if sort_by in ['name', 'enrolled_date', 'teacher']:
            students = students.order_by(sort_by)

        return JsonResponse(list(students), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def student_detail(request, pk):
    try:
        student = get_object_or_404(Student, id=pk)
        return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "enrolled_date": student.enrolled_date, "teacher_id": student.teacher.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def add_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student(**data)
            student.full_clean()  # Validate the model
            student.save()
            return JsonResponse({"id": student.id}, status=201)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.messages}, status=400)
       
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def update_student(request, pk):
    try:
        student = get_object_or_404(Student, id=pk)
        if request.method == 'PUT':
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(student, key, value)
            student.full_clean()  # Validate the model
            student.save()
            return JsonResponse({"id": student.id})
    except ValidationError as ve:
        return JsonResponse({"errors": ve.messages}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def delete_student(request,pk):
    try:
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return HttpResponse(status=204)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)