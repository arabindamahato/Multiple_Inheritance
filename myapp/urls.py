from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name = "base1"),
    path('child1/', views.child1, name = "child11"),
    path('child2/', views.child2, name = "child22"),
    path('form/', views.form, name = "form"),


]