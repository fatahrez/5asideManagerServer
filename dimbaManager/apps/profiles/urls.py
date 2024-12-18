from django.urls import path

import dimbaManager.apps.profiles.views as views


urlpatterns = [
    path("profile/", views.GetProfileAPIVIew.as_view(), name="get-profile"),
    path("profile/update/<str:username>/", views.UpdateProfileAPIView.as_view(), name="update-profile"),
]