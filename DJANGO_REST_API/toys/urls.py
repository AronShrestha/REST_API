
from django.urls import path,re_path
from toys import views

urlpatterns = [
    # path('bio/',views.name_list),
    path('toys/',views.toy_list),
    # re_path(r'toys/(?P<pk>[0-9]+)$',views.toy_detail)
    path('toys/<int:pk>',views.toy_detail)
]
