from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),

    # path(
    #     'password_reset_done/',
    #     views.PasswordResetDoneView,
    #     name='password_reset_done'
    # ),
    #
    # path(
    #     'reset/<uidb64>/<token>/',
    #     views.PasswordResetConfirmView,
    #     name='password_reset_confirm'
    # ),
    #
    # path(
    #     'reset_done/',
    #     views.PasswordResetCompleteView,
    #     name='password_reset_complete'
    # ),
]