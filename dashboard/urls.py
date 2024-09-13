from django.urls import path
from .views import  DashboardView, FacultyListCreateAPIView, FacultyRetrieveUpdateDestroyAPIView, DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView, GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView, SubjectListCreateAPIView, SubjectRetrieveUpdateDestroyAPIView, TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('faculties/', FacultyListCreateAPIView.as_view(), name='faculty-list-create'),
    path('faculties/<int:pk>/', FacultyRetrieveUpdateDestroyAPIView.as_view(), name='faculty-detail'),

    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-detail'),

    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view(), name='group-detail'),

    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDestroyAPIView.as_view(), name='subject-detail'),

    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-detail'),

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]
