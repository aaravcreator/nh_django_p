from django.urls import path

from .views import create_person,edit_person

urlpatterns = [
    path('create-person/',create_person,name="createperson"),
    path('edit_person/<int:id>/',edit_person,name="editperson")
    #/myapp/edit_person/1/
]