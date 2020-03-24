from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('country_news/sports/',views.sports,name="sports"),
    path('country_news/My_technology_news/',views.My_technology_news,name="My_technology_news"),
    path('country_news/My_sports_news/',views.My_sports_news,name="My_sports_news"),
    path('country_news/',views.index,name="root"),
    path('first/<int:id>', views.first,name="first"),
    path('first_s/<int:id>', views.first_s,name="first_s"),
    path('first_speech/<int:id>', views.first_speech,name="first_speech"), 
    path('second_speech/<int:id>', views.second_speech,name="second_speech"), 

] 