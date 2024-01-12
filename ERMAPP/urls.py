from django.urls import path,path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.emp_form,name='employee_insert'),
    path('<int:id>/',views.emp_form,name='employee_update'),
    path('delete<int:id>/',views.emp_delete,name='employee_delete'),
    path('list/',views.emp_list,name='employee_list')
]