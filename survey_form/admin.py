from django.contrib import admin

from survey_form.models import BusinessCreator, SecondStep, ThirdStep, FourthStep, FifthStep
from survey_form.forms import StepFirstForm, StepSecondForm, StepThirdForm, StepFourthForm, StepFifthForm

class SecondInline(admin.StackedInline):
	model = SecondStep
	form = StepSecondForm


class ThirdInline(admin.StackedInline):
	model = ThirdStep
	form = StepThirdForm


class FourthInline(admin.StackedInline):
	model = FourthStep
	form = StepFourthForm


class FifthInline(admin.StackedInline):
	model = FifthStep
	form = StepFifthForm


@admin.register(BusinessCreator)
class CreatorAdmin(admin.ModelAdmin):
	form = StepFirstForm
	list_display = ('email', 'created_at', 'updated_at')
	inlines = [
		SecondInline,
		ThirdInline,
		FourthInline,
		FifthInline
	]
	
	class Meta:
		fields = '__all__'
