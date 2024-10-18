from django.urls import path
from .views import teacher_list,teacher_detail,add_teacher,delete_teacher,update_teacher,student_list,student_detail,add_student,update_student,delete_student


urlpatterns = [
    path('teachers/',teacher_list,name='teacher list'),
    path('teacher/<int:pk>/',teacher_detail,name='get teacher'),
    path('add-teacher/',add_teacher,name='adding teacher'),
    path('update-teacher/<int:pk>/',update_teacher,name='update teacher'),
    path('delete-teacher/<int:pk>/',delete_teacher,name='delete teacher'),


    path('students/',student_list,name='student_list '),
    path('student/<int:pk>/',student_detail,name='get student_detail'),
    path('add-student/',add_student,name=' add_student'),
    path('update-student/<int:pk>/',update_student,name='update student'),
    path('delete-student/<int:pk>/',delete_student,name='delete student'),
    
    
]