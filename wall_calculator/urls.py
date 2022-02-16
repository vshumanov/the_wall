from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from wall_calculator import views

urlpatterns = [
    path("<int:profile_num>/days/<int:day>", views.ProfileDay.as_view()),
    path("<int:profile_num>/overview/<int:day>", views.ProfileOverview.as_view()),
    path("overview/", views.FullOverview.as_view()),
    path("overview/<int:day>/", views.FullOverviewDay.as_view()),
]
