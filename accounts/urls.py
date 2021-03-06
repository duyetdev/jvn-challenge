from django.conf.urls import url

from .views import RegistrationView, profile, settings
from django.contrib.auth import views

urlpatterns = [
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    
    url(r'^register/done/$', views.password_reset_done, {
        'template_name': 'accounts/initial_done.html',
    }, name='register-done'),

    # url(r'^register/password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, {
    #     'template_name': 'accounts/initial_confirm.html',
    #     'post_reset_redirect': 'accounts:register-complete',
    # }, name='register-confirm'),
    # url(r'^register/complete/$', views.password_reset_complete, {
    #     'template_name': 'accounts/initial_complete.html',
    # }, name='register-complete'),

    url(r'^profile/$', profile, name='profile'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/(?P<setting>[A-z-]+)/$', settings, name='settings_p'),
]