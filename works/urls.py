from django.urls import path
from .views import worklist, workdetail,workcreate,workupdate,workdelete,worklogin,workregister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',worklogin.as_view(),name="login"),
    path('register/',workregister.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('', worklist.as_view(), name='works'),
    path('work/<int:pk>/', workdetail.as_view() , name='detail'),
    path('work_create/', workcreate.as_view() , name='create'),
    path('work_update/<int:pk>/', workupdate.as_view() , name='update'),
    path('work_delete/<int:pk>/', workdelete.as_view() , name='delete'),
]