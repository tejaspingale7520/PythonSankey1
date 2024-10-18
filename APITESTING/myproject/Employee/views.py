
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
import json
from django.contrib.auth import authenticate
from .models import Employee



# def authenticate_user(request):
#     username=request.headers.get('Username')
#     password=request.headers.get('Password')
#     user=authenticate(username=username,password=password)
#     return user

# Create your views here.
# def create_employee(request):
#     user=authenticate_user(request)
#     if user is None:
#         return HttpResponseForbidden('Unauthorized')

def create_employee(request):
    # user=authenticate_user(request)  #for authentication 
    # if user is None:
    #     return HttpResponseForbidden('Unauthorized')
    
    if request.method =='POST':
        data=json.loads(request.body)

        if not data.get('name') or not data.get('position') or not data.get('salary') or not data.get('hired_date'):
            return HttpResponseBadRequest('Missing required field')


        employee=Employee.objects.create(name=data['name'],position=data['position'],salary=data['salary'],hired_date=data['hired_date'])
        return JsonResponse({'id':employee.id},status=201)



def get_employee_details(request):
    # user=authenticate_user(request)
    # if user is None:
    #     return HttpResponseForbidden('Unauthorised')

    employees=Employee.objects.all()
    # empinfo=[]
    # for employee in employees:
    #     data={'name':employee.name,
    #           'position':str(employee.position),
    #           'hired_date':str(employee.hired_date)}
    #     empinfo.append(data)
    empinfo=[{'id':employee.id,'name':employee.name,'position':str(employee.position),'hired_date':str(employee.hired_date)} for employee in employees]

    return JsonResponse(empinfo,safe=False)

    



def get_employee(request,pk):
    # user =authenticate_user(request)
    # if user is None:
    #     return HttpResponseForbidden('Unauthorised')
    try:
        emoployee=Employee.objects.get(id=pk)
        data={'id':emoployee.id,
              'name':emoployee.name,
              'position':emoployee.position,
              'salary':str(emoployee.salary),
              'hired_date':str(emoployee.hired_date)}
        return JsonResponse(data)
    
    except Employee.DoesNotExist:
        return JsonResponse({'error':f'Employee with id:{pk} not found'},status=404)
    
    
def update_employee(request,pk):
    # user=authenticate_user(request)
    # if user is None:
    #     return HttpResponseForbidden('Unauthorised')
   
    try:
      employee=Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
       return JsonResponse({'error':f"Employee with id:{pk} not found"},status=404)
    
    if request.method =="PUT" or "PATCH":
      data=json.loads(request.body)
      if not data:
        return HttpResponseBadRequest('Missing required field')

      employee.name=data.get('name',employee.name)
      employee.position=data.get('position',employee.position)
      employee.salary=data.get('salary',employee.salary)
      employee.hired_date=data.get('hired_date',employee.hired_date)
      employee.save()
      return JsonResponse({'data updated with id':employee.id},status=201)
    
# def pupdate_employee(request, pk):   #for partial update
#     # user = authenticate_user(request)
#     # if user is None:
#     #     return HttpResponseForbidden('Unauthorized')
    
#     try:
#         employee = Employee.objects.get(id=pk)
#     except Employee.DoesNotExist:
#         return JsonResponse({'error': f"Employee with id:{pk} not found"}, status=404)
    
#     if request.method == "PATCH":
#         data = json.loads(request.body)
#         if not data:
#             return HttpResponseBadRequest('Missing required fields')
        
#         employee.name = data.get('name', employee.name)
#         employee.position = data.get('position', employee.position)
#         employee.salary = data.get('salary', employee.salary)
#         employee.hired_date = data.get('hired_date', employee.hired_date)
#         employee.save()
        
#         return JsonResponse({'id': employee.id,'msg':'data updated'}, status=200)
    
   
    

def delete_employee(request,pk):
    # user=authenticate_user(request)
    # if user is None:
    #     return HttpResponseForbidden('Unauthorized')

    try:
        employee=Employee.objects.get(id=pk)
        employee.delete()
        return JsonResponse({'message':f'Employee for {pk} deleted successfully'},status=204)
       
    except Employee.DoesNotExist:
        return JsonResponse({'error':f'Employee for {pk} not found'},status=404)
       



def search_employee(request):
    
    # user = authenticate_user(request)
    # if user is None:
    #     return HttpResponseForbidden('Unauthorized')
    
    query = request.GET.get('query', '')
    employees = Employee.objects.filter(name__icontains=query) | Employee.objects.filter(name__startswith=query) |  Employee.objects.filter(position__icontains=query) ## you can serach with name
    #employees=Employee.objects.filter(name__startswith=query)    ##you can seacrch with start letter
    #employees=Employee.objects.filter(position__icontains=query) ## search by position
    
    
    # empinfo = []
    # for employee in employees:
    #     data = {
    #         'name': employee.name,
    #         'position': employee.position,
    #         'hired_date': str(employee.hired_date)
    #     }
    #     empinfo.append(data)
    empinfo=[{
            'name': employee.name,
            'position': employee.position,
            'hired_date': str(employee.hired_date)
        } for employee in employees]
        
    
    return JsonResponse(empinfo, safe=False)

      
