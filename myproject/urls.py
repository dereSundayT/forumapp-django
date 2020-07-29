from django.contrib import admin
from django.urls import path
from boards import views
from accounts.views import signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='boards-home'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'), #LOGOUT_REDIRECT_URL = 'home'@seetings.py
    path('boards/<int:pk>/', views.board_topics, name="boards-topics"),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
]
