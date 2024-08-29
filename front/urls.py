from django.contrib import admin
from django.urls import path
from .views import Log1,Log2,Log3,Pfront,Plist,Pcreate,Pdetail,Pdelete,Pupdate
from .views import loginview,logoutview

from .views import Encreate
urlpatterns=[
    path('admin/',admin.site.urls),
    path('log1/',Log1.as_view()),
    path('log2/',Log2.as_view()),
    path('log3/',Log3.as_view()),
    path('pfront/',Pfront.as_view()),
    path('plist/',Plist,name='plist'),
    path('pcreate/',Pcreate.as_view(),name='pcreate'),
    path('pdetail/<int:pk>/',Pdetail,name='pdetail'),
    path('pdelete/<int:pk>',Pdelete.as_view(),name='pdelete'),
    path('pupdate/<int:pk>',Pupdate.as_view(),name='pupdate'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),

    path('encreate/',Encreate.as_view(),name='encreate'),
]