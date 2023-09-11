from django.urls import path

from .views import TeacherList, TeacherDetail, MeView, TeacherProfileImageView

app_name = "teachers"
urlpatterns = [
    path("professores", TeacherList.as_view(), name='list'),
    path("professores/<int:pk>", TeacherDetail.as_view(), name='detail'),
    path("me", MeView.as_view(), name='me'),
    path("professores/foto", TeacherProfileImageView.as_view(), name='profile_image'),
]
