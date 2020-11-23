from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from django.core.exceptions import ObjectDoesNotExist

from .models import BusinessCreator, SecondStep, ThirdStep, FourthStep, FifthStep
from .forms import StepFirstForm, StepSecondForm, StepThirdForm, StepFourthForm, StepFifthForm


class StepFirstView(CreateView):
	"""Step1 View"""
	template_name = 'step1.html'
	form_class = StepFirstForm
	success_url = '/step2/'

	def get_object(self):
		if self.request.session.get('creator_id', None):
			return BusinessCreator.objects.get(pk=self.request.session['creator_id'])
		return None

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return self.render_to_response(self.get_context_data())

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save()
		self.request.session['creator_id'] = self.object.id
		self.request.session['step1'] = True;
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		self.request.session['step1'] = False;
		return self.render_to_response(self.get_context_data(form=form))


class StepSecondView(CreateView):
	"""Step2 View"""
	template_name = 'step2.html'
	form_class = StepSecondForm
	success_url = '/step3/'

	def get_object(self):
		if self.request.session.get('creator_id', None):
			try:
				return SecondStep.objects.get(co_creator_id=self.request.session['creator_id'])
			except ObjectDoesNotExist:
				return None
		return None

	def get(self, request, *args, **kwargs):
		if self.request.session.get('step1', False):
			self.object = self.get_object()
			return self.render_to_response(self.get_context_data())
		return HttpResponseRedirect('/step1/')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.co_creator_id = self.request.session.get('creator_id', None)
		self.object.save()
		self.request.session['step2'] = True;
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		self.request.session['step2'] = False;
		return self.render_to_response(self.get_context_data(form=form))


class StepThirdView(FormView):
	template_name = 'step3.html'
	form_class = StepThirdForm
	success_url = '/step4/'

	def get_object(self):
		if self.request.session.get('creator_id', None):
			try:
				return ThirdStep.objects.get(co_creator_id=self.request.session['creator_id'])
			except ObjectDoesNotExist:
				return None
		return None

	def get(self, request, *args, **kwargs):
		if self.request.session.get('step2', False):
			self.object = self.get_object()
			return self.render_to_response(self.get_context_data())
		return HttpResponseRedirect('/step1/')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.co_creator_id = self.request.session.get('creator_id', None)
		self.object.save()
		self.request.session['step3'] = True;
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		self.request.session['step3'] = False;
		return self.render_to_response(self.get_context_data(form=form))


class StepFourthView(FormView):
	template_name = 'step4.html'
	form_class = StepFourthForm
	success_url = '/step5/'

	def get_object(self):
		if self.request.session.get('creator_id', None):
			try:
				return FourthStep.objects.get(co_creator_id=self.request.session['creator_id'])
			except ObjectDoesNotExist:
				return None
		return None

	# def get(self, request, *args, **kwargs):
	#     if self.request.session.get('step3', False):
	#         self.object = self.get_object()
	#         return self.render_to_response(self.get_context_data())
	#     return HttpResponseRedirect('/step1/')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.co_creator_id = self.request.session.get('creator_id', None)
		self.object.save()
		self.request.session['step4'] = True;
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		self.request.session['step4'] = False;
		return self.render_to_response(self.get_context_data(form=form))


class StepFifthView(FormView):
	template_name = 'step5.html'
	form_class = StepFifthForm
	success_url = '/success/'

	def get_object(self):
		if self.request.session.get('creator_id', None):
			try:
				return FifthStep.objects.get(co_creator_id=self.request.session['creator_id'])
			except ObjectDoesNotExist:
				return None
		return None

	def get(self, request, *args, **kwargs):
	    if self.request.session.get('step4', False):
	        self.object = self.get_object()
	        return self.render_to_response(self.get_context_data())
	    return HttpResponseRedirect('/step1/')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.co_creator_id = self.request.session.get('creator_id', None)
		self.object.save()
		self.request.session['step5'] = True;
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		self.request.session['step5'] = False;
		return self.render_to_response(self.get_context_data(form=form))


class SuccessView(TemplateView):
	template_name = 'success.html'

	def get(self, request, *args, **kwargs):
		if self.request.session.get('step5', False):
			context = self.get_context_data(**kwargs)
			return self.render_to_response(context)
		return HttpResponseRedirect('/step1/')