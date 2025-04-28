#views.py updated 1.0
#view fixes
#sprint models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt