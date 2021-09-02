from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # 메인페이지
    path('', views.index),

    # 로그인페이지
    path('login', views.login),

    # 로그아웃
    path('logout', views.logout),

    # 회원가입 페이지
    path('join', views.join),

    # 회원가입완료 페이지
    path('joinSuccess', views.joinSuccess),

    # 프로필
    path('profile', views.profile),

    # setting
    path('setting', views.setting),

    # Insight
    path('insight', views.insight),
    
    # Recipe
    path('recipe', views.recipe),
    
    # Question
    path('question', views.question),
    
    # 실천여부변경
    path('planaction', views.planaction),
    
    # 대기페이지
    path('waiting', views.waiting),

    # 스토어
    path('store', views.store),
]