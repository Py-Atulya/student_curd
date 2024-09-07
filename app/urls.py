from django.urls import path
from app import views

urlpatterns = [
      path('',views.student_curd,name='student_curd'),
      path('student/',views.student_table,name='student_table'),
      path('student_delete/<int:roll_number>',views.student_delete,name='student_delete'),
      path('student_edit/<int:roll_number>',views.student_edit,name='student_edit'),
      path('student_download/<int:roll_number>',views.student_download,name='student_download')
]
