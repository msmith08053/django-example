from django.conf.urls import url, include
from basic_app import views

#for template tagging, set global variable
app_name = 'basic_app'

urlpatterns=[
    url(r'relative/$',views.relative,name='relative'),
    url(r'other/$',views.other,name='other'),
]
