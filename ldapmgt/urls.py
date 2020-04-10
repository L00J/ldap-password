#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:  LJ
Email:   admin@attacker.club
Time:    2020/4/8 08:11
Description: 
"""

from django.urls import path, re_path
# re_path方法相当于 django1.11 url正则表达式
from . import views

# 载入视图模块

app_name = 'ldaomgt'

urlpatterns = [
    path('', views.index, name="index"),
    # re_path(r'^search/$', views.search, name='search'),
]



