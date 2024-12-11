from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="add_show"),
    path('delete_data/<int:id>/',views.delete_data,name="delete_data"),
    path('<int:id>/', views.update_date, name="update_date"),
]