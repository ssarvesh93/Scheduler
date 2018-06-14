from django.conf.urls import url
from django.urls import path
from .views import IndexView,AddTask,UserFormView,TaskDelete,DetailView,TaskUpdate
from django.contrib.auth import views as auth_views

app_name = 'sdlrs'

urlpatterns = [
    # /scheduler/
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^add/$',AddTask.as_view(),name='task-add'),
    url(r'^register/$',UserFormView.as_view(), name='register'),
    #/scheduler/sch_id
    url(r'detail/(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-update'),
    url(r'detail/(?P<pk>[0-9]+)/$',DetailView.as_view(),name='detail'),

    url(r'^(?P<pk>[0-9]+)/delete/$',TaskDelete.as_view(), name='task-delete'),
    url(r'^login/$',auth_views.LoginView.as_view(),{'template_name':'scheduler/login.html'},name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),{'template_name':'scheduler/logout.html'},name='logout'),
    #url(r'^register/$',views.UserFormView.as_view(), name='register'),
]