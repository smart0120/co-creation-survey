from django import forms
from django.forms import ModelForm, Field

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

from .models import BusinessCreator, SecondStep, ThirdStep, FourthStep, FifthStep

Field.default_error_messages = {
	'required': 'Esta pergunta é obrigatória'
}

class StepFirstForm(ModelForm):
	email = forms.EmailField(
		label="Endereço de e-mail",
		error_messages={
			'invalid': 'Precisa ser um endereço de e-mail válido'
		}
	)
	class Meta:
		model = BusinessCreator
		fields = '__all__'


class StepSecondForm(ModelForm):
	market = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=SecondStep.MARKET_CHOICES,
		label='¿Qué quieres comercializar?'
	)
	classification = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=SecondStep.CLASSIFICATION_CHOICES,
		label='¿Cuál de las siguientes clasificaciones aplica mejor para tu proyecto de emprendimiento?',
	)
	time_spend = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=SecondStep.TIME_SPEND_CHOICE,
		label='¿Cuánto tiempo quieres dedicarle a definir tu producto o servicio y su propuesta de valor?'
	)

	class Meta:
		model = SecondStep
		fields = '__all__'
		exclude = ('co_creator',)
		labels = {
			'consists': 'Describe en qué consiste tu proyecto de emprendimiento',
			'industry': '¿A que industria pertenece?',
			'classification_other_detail': '',
		}


class StepThirdForm(ModelForm):
	trait1 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait2 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait3 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait4 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait5 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait6 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait7 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait8 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait9 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait10 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait11 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait12 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait13 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait14 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait15 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait16 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait17 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait18 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait19 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait20 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait21 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait22 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait23 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait24 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait25 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait26 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait27 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait28 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait29 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait30 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait31 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait32 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait33 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait34 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait35 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait36 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait37 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait38 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait39 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait40 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait41 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait42 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait43 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait44 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait45 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait46 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait47 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait48 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait49 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)
	trait50 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.TRAIT_CHOICES)

	motivate1 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.MOTIVATE_CHOICES)
	motivate2 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.MOTIVATE_CHOICES)
	motivate3 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.MOTIVATE_CHOICES)
	motivate4 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.MOTIVATE_CHOICES)
	motivate5 = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.MOTIVATE_CHOICES)

	priority = forms.ChoiceField(widget=forms.RadioSelect, choices=ThirdStep.PRIORITY_CHOICES)

	class Meta:
		model = ThirdStep
		fields = '__all__'
		exclude = ('co_creator',)
		labels = {
			'consists': 'Describe en qué consiste tu proyecto de emprendimiento',
			'industry': '¿A que industria pertenece?',
			'classification_other_detail': '',
		}


class StepFourthForm(ModelForm):
	dedicate = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=FourthStep.DEDICATE_CHOICE,
		label='¿Cuánto tiempo te es posible dedicarle a tu proyecto de emprendimiento?'
	)

	class Meta:
		model = FourthStep
		fields = '__all__'
		exclude = ('co_creator',)
		labels = {
			'goals': '¿Cuáles son tus objetivos en el mediano y largo plazo?',
			'objective': '¿Cuál sería el objetivo que quisieras alcanzar al finalizar tu programa de acompañamiento?',
			'measure': '¿Cómo quisieras medir el progreso y cumplimiento de los objetivos de tu programa?',
			'obstacle': '¿Cuál es tu mayor obstáculo en este momento?'
		}


class StepFifthForm(ModelForm):
	gender = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=FifthStep.GENDER_CHOICES,
		required=False,
		label='Género'
	)

	class Meta:
		model = FifthStep
		fields = '__all__'
		exclude = ('co_creator',)
		labels = {
			'full_name': 'Nombre completo',
			'age': 'Edad',
			'more': 'Con más información que tengamos sobre ti podremos personalizar mejor tu itinerario de aprendizaje y plan de acción. ¿Quieres comentar algo más sobre ti o sobre tu proyecto?'
		}