from django.urls import path
from .views import ContactList, ContactdetailView


urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactdetailView.as_view())
]
