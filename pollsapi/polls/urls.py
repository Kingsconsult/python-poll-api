from django.urls import path
from .views import polls_detail, polls_list


app_name = "polls"


urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]
