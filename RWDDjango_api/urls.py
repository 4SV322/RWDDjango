from django.conf.urls import url
from django.urls import path, include
from .views import (InstituteListView,
                    SkillListView,
                    GroupListView)

urlpatterns = [
    path('institutes/', InstituteListView.as_view()),
    path('skills/', SkillListView.as_view()),
    path('groups/', GroupListView.as_view())
]
