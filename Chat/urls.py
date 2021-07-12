from django.urls import path
from .import views

app_name="chat"

urlpatterns = [
    path('<str:roomname>/',views.chatroom,name="chat_room"),
    

]
