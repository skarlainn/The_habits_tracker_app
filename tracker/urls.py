from django.urls import path
from rest_framework.routers import DefaultRouter

from config.urls import urlpatterns
from tracker.apps import TrackerConfig
from tracker.views import (PleasantHabitViewSet, UsefulHabitCreateView, UsefulHabitDetailView, UsefulHabitDeleteView, UsefulHabitListView)


app_name = TrackerConfig.name

router = DefaultRouter()
router.register(r'plesant-habits', PleasantHabitViewSet)
urlpatterns = [
    path("useful-habits/create/", UsefulHabitCreateView.as_view(), name="create_useful_habit"),
    path("useful-habits/", UsefulHabitListView.as_view(), name="useful_habits"),
    path("useful-habits/<int:pk>/", UsefulHabitDetailView.as_view(), name="useful_habit"),
    path("useful-habits/<int:pk>/delete/", UsefulHabitDeleteView.as_view(), name="delete_useful_habit"),
] + router.urls