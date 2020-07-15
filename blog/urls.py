from django.urls import path
from . import views
from .views import PostCreateView,ReportView,ResultView,DietView,ListUsers


urlpatterns = [
    path('', views.homepage, name='sugar-home'),
    path('input/', PostCreateView.as_view(), name='blog-home'),
    path('result/<str:username>', ResultView.as_view(), name='blog-result'),
    path('diet/<str:username>', DietView.as_view(), name='blog-diet'),
    path('report/<str:username>', ReportView.as_view(), name='blog-reports'),
    path('bars/', views.bars, name='blog-bars'),
    path('glycemic/', views.glycemic,name='glycemic-index'),
    path('api/chart/data/', ListUsers.as_view()),

    ]