from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import executive_required
from ..forms import ExecutiveSignUpForm
from ..models import User

class ExecutiveSignUpView(CreateView):
	model = User
	form_class = ExecutiveSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 3
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('executive:home')

@method_decorator([login_required, executive_required], name='dispatch')
class HomeView(ListView):
	template_name = 'userAuth/executives/home.html'

	def get_queryset(self):
		return []