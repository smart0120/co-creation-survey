from django.urls import path

from . import views

urlpatterns = [
    path('step1/', views.StepFirstView.as_view(), name='step1'),
    path('step2/', views.StepSecondView.as_view(), name='step2'),
    path('step3/', views.StepThirdView.as_view(), name='step3'),
    path('step4/', views.StepFourthView.as_view(), name='step4'),
    path('step5/', views.StepFifthView.as_view(), name='step5'),
]