from django.contrib import admin
from django.urls import path
from boards import views
from accounts.views import signup
from django.contrib.auth.views import (LogoutView,LoginView,PasswordResetView,PasswordResetDoneView,
    PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView)

urlpatterns = [
    path('', views.home, name='boards-home'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), #LOGOUT_REDIRECT_URL = 'home'@seetings.py
    path('boards/<int:pk>/', views.board_topics, name="boards-topics"),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<topic_pk>/', views.topic_posts, name='topic_posts'),
    path('boards/<int:pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('reset/',PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html',subject_template_name='password_reset_subject.txt'),name='password_reset'),
    path('reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('settings/password/',PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('settings/password/done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    path('admin/', admin.site.urls),
]
