from django import forms
from django.forms import ModelForm, Field

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML, Hidden
from crispy_forms.bootstrap import InlineRadios

from .models import BusinessCreator, SecondStep, ThirdStep, FourthStep, FifthStep

Field.default_error_messages = {
	'required': 'Esta pergunta é obrigatória'
}

class CustomInlineRadios(InlineRadios):
	"""
	Customized bootstrap4 inline radio without label
	"""
	template = '%s/layout/custom_radioselect_inline.html'


class VirticalInlineRadio(InlineRadios):
	"""
	Customized bootstrap4 inline radio with label above control
	"""
	template = '%s/layout/virtical_radioselect_inline.html'


class CustomHidden(InlineRadios):
	"""
	Customized bootstrap4 hidden field
	"""
	template = "%s/layout/hidden_field.html"


class StepFirstForm(ModelForm):
	"""
	Start form
	"""
	email = forms.EmailField(
		label="Endereço de e-mail",
		error_messages={
			'invalid': 'Precisa ser um endereço de e-mail válido'
		}
	)
	class Meta:
		model = BusinessCreator
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.field_template = "bootstrap4/field_custom.html"
		self.helper.form_action = 'step1'
		self.helper.layout = Layout(
			'email',
			ButtonHolder(
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)


class StepSecondForm(ModelForm):
	"""
	2nd step form
	"""
	market = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=SecondStep.MARKET_CHOICES,
		label='¿Qué quieres comercializar?'
	)
	classification = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=SecondStep.CLASSIFICATION_CHOICES,
		required=False,
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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'step2'
		self.helper.layout = Layout(
			Div(
				Div(
					'consists',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'market',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'industry',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'classification',
					Div(
						'classification_other_detail',
						css_class='detail-input-container'
					),
					css_class='block-body position-relative pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿Cuánto tiempo quieres dedicarle a definir tu producto o servicio y su propuesta de valor? <span class="asteriskField">*</span>
					"""),
					Div(
						HTML("""
							<div class="flex-grow text-center pr-1 mt-4 pt-2" style="max-width: 35%">Mínimo indispensable. Quiero empezar a vender ya con lo que tengo pensado y/o definido.</div>
						"""),
						VirticalInlineRadio('time_spend'),
						HTML("""
							<div class="flex-grow text-center pl-1 mt-4 pt-2" style="max-width: 35%">Lo que sea necesario. Prefiero tomarme el tiempo para definir y evaluar mi producto o servicio hasta que me sienta completamente seguro</div>
						"""),
						css_class='font-size-14px mt-4 d-flex'
					),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			ButtonHolder(
				HTML('<a href="/step1/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)

	def clean(self):
		cleaned_data = super().clean()
		msg = "Esta pergunta é obrigatória"
		classification = cleaned_data.get("classification")
		classification_other_detail = cleaned_data.get("classification_other_detail")

		if (not classification) or (classification == '6' and classification_other_detail == ''):
			self.add_error('classification_other_detail', msg)


class StepThirdForm(ModelForm):
	"""
	3rd step form
	"""
	trait1 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Soy el alma de la fiesta'
	)
	trait2 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Siento poca preocupación por los demás'
	)
	trait3 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Siempre estoy preparado'
	)
	trait4 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me estreso fácilmente'
	)
	trait5 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo un amplio vocabulario'
	)
	trait6 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No hablo mucho'
	)
	trait7 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me interesan las personas'
	)
	trait8 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Dejo mis pertenencias cerca'
	)
	trait9 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Estoy relajado la mayoría del tiempo'
	)
	trait10 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me cuesta trabajo entender ideas abstractas'
	)
	trait11 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me siento cómodo rodeado de gente'
	)
	trait12 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Insulto a la gente'
	)
	trait13 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Pongo atención a los detalles'
	)
	trait14 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me preocupan las cosas'
	)
	trait15 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo una imaginación vívida'
	)
	trait16 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me mantengo en segundo plano'
	)
	trait17 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Simpatizo con los sentimiento de los demás'
	)
	trait18 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Hago las cosas muy grandes'
	)
	trait19 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Rara vez me siento triste'
	)
	trait20 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No estoy interesado en ideas abstractas'
	)
	trait21 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Comienzo conversaciones'
	)
	trait22 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No estoy interesado en los problemas de los demás'
	)
	trait23 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Hago mis pendientes en el momento'
	)
	trait24 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me molesto fácilmente'
	)
	trait25 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo ideas excelentes'
	)
	trait26 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo poco que decir'
	)
	trait27 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo un corazón suave'
	)
	trait28 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='A menudo olvido de poner las cosas en su lugar'
	)
	trait29 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me enojo fácilmente'
	)
	trait30 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No tengo buena imaginación'
	)
	trait31 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Hablo con muchas personas diferentes en las fiestas'
	)
	trait32 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No estoy realmente interesado en los demás'
	)
	trait33 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me gusta el orden'
	)
	trait34 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Cambio mucho de humor'
	)
	trait35 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Soy rápido para entender las cosas'
	)
	trait36 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No me gusta atraer la atención hacia mi'
	)
	trait37 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me tomo tiempo para los demás'
	)
	trait38 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Eludo mis deberes'
	)
	trait39 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Tengo cambios de humor frecuentes'
	)
	trait40 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Uso palabras rebuscadas'
	)
	trait41 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='No me molesta ser el centro de atención'
	)
	trait42 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Siento las emociones de los demás'
	)
	trait43 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Sigo un horario'
	)
	trait44 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Me irrito fácilmente'
	)
	trait45 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Dedico tiempo para reflexionar sobre diversos temas'
	)
	trait46 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Soy tranquilo cuando estoy rodeado de extraños'
	)
	trait47 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Hago que la gente se sienta cómoda'
	)
	trait48 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Soy exigente en mi trabajo'
	)
	trait49 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='A menudo me siento triste'
	)
	trait50 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		label='Estoy lleno de ideas'
	)

	motivate1 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		label='Ganar dinero'
	)
	motivate2 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		label='Dedicarme a lo que me gusta'
	)
	motivate3 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		label='Cambiar/mejorar el mundo'
	)
	motivate4 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		label='Tener flexibilidad en mi vida en general'
	)
	motivate5 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		label='Ser reconocido como exitoso'
	)

	priority = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.PRIORITY_CHOICES,
		label='¿A que le darías más prioridad? ¿A alcanzar tus objetivos o a disfrutar el proceso?'
	)

	learning_group = forms.CharField(required=False);

	class Meta:
		model = ThirdStep
		fields = '__all__'
		exclude = ('co_creator',)
		labels = {
			'learning_visual': 'Visual: aprendes principalmente a través de imágenes y/o videos. También puede ser leyendo, escribiendo, tomando apuntes o haciendo mapas mentales',
			'learning_auditory': 'Auditivo: recuerdas información siguiendo y rememorando explicaciones orales. Se te facilita recordar frases específicas y definición de conceptos.',
			'learning_kinesthetic': 'Kinestésico: aprendes a través de la práctica. Requieres experiencias sensoriales y mover el cuerpo',
			'learning_not_clear': 'No lo tengo claro en este momento.',
			'exp_finace': 'Finanzas',
			'exp_Sales': 'Ventas',
			'exp_marketing': 'Mercadotecnia',
			'exp_technology': 'Tecnología',
			'exp_operations': 'Operaciones',
			'exp_human_resources': 'Recursos Humanos',
			'exp_legal': 'Legal',
			'exp_other': 'Outro:',
			'exp_other_detail': '',
			'undertake': 'Completa la siguiente frase: Para mi, emprender es .....',
			'diff_undertake': 'Completa la siguiente frase: Los más difícil de emprender es ....',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'step3'
		self.helper.layout = Layout(
			Div(
				Div(
					HTML("""
						Evaluación Big 5 de Rasgos de Personalidad. Selecciona que tanto aplican en tu caso cada una de las siguientes situaciones <span class="asteriskField">*</span>
					"""),
					HTML("""
						<div class="row font-size-14px mt-3 text-center">
							<div class="col pr-0" style="flex-grow: 1.5"></div>
							<div class="col px-0">Totalmente en desacuerdo</div>
							<div class="col px-0">En desacuerdo</div>
							<div class="col px-0">Neutral</div>
							<div class="col px-0">De acuerdo</div>
							<div class="col pl-0">Totalmente de acuerdo</div>
						</div>
					"""),
					CustomInlineRadios('trait1'),
					CustomInlineRadios('trait2'),
					CustomInlineRadios('trait3'),
					CustomInlineRadios('trait4'),
					CustomInlineRadios('trait5'),
					CustomInlineRadios('trait6'),
					CustomInlineRadios('trait7'),
					CustomInlineRadios('trait8'),
					CustomInlineRadios('trait9'),
					CustomInlineRadios('trait10'),
					CustomInlineRadios('trait11'),
					CustomInlineRadios('trait12'),
					CustomInlineRadios('trait13'),
					CustomInlineRadios('trait14'),
					CustomInlineRadios('trait15'),
					CustomInlineRadios('trait16'),
					CustomInlineRadios('trait17'),
					CustomInlineRadios('trait18'),
					CustomInlineRadios('trait19'),
					CustomInlineRadios('trait20'),
					CustomInlineRadios('trait21'),
					CustomInlineRadios('trait22'),
					CustomInlineRadios('trait23'),
					CustomInlineRadios('trait24'),
					CustomInlineRadios('trait25'),
					CustomInlineRadios('trait26'),
					CustomInlineRadios('trait27'),
					CustomInlineRadios('trait28'),
					CustomInlineRadios('trait29'),
					CustomInlineRadios('trait30'),
					CustomInlineRadios('trait31'),
					CustomInlineRadios('trait32'),
					CustomInlineRadios('trait33'),
					CustomInlineRadios('trait34'),
					CustomInlineRadios('trait35'),
					CustomInlineRadios('trait36'),
					CustomInlineRadios('trait37'),
					CustomInlineRadios('trait38'),
					CustomInlineRadios('trait39'),
					CustomInlineRadios('trait40'),
					CustomInlineRadios('trait41'),
					CustomInlineRadios('trait42'),
					CustomInlineRadios('trait43'),
					CustomInlineRadios('trait44'),
					CustomInlineRadios('trait45'),
					CustomInlineRadios('trait46'),
					CustomInlineRadios('trait47'),
					CustomInlineRadios('trait48'),
					CustomInlineRadios('trait49'),
					CustomInlineRadios('trait50'),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿Cuál de estos estilos de aprendizaje te funciona mejor? Puedes tener más de un estilo <span class="asteriskField">*</span>
					"""),
					Div(
						'learning_visual',
						'learning_auditory',
						'learning_kinesthetic',
						'learning_not_clear',
						css_class='font-size-14px mt-3'
					),
					CustomHidden('learning_group'),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿En cuáles de estas áreas tienes experiencia y/o conocimientos? <span class="asteriskField">*</span>
					"""),
					Div(
						'exp_finace',
						'exp_Sales',
						'exp_marketing',
						'exp_technology',
						'exp_operations',
						'exp_human_resources',
						'exp_legal',
						'exp_other',
						Div(
							'exp_other_detail',
							css_class='detail-input-container'
						),
						css_class='font-size-14px mt-3'
					),
					css_class='block-body position-relative pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿Qué te está motivando a emprender? <span class="asteriskField">*</span>
					"""),
					HTML("""
						<div class="row font-size-14px mt-3 text-center">
							<div class="col pr-0" style="flex-grow: 1.5"></div>
							<div class="col px-0">Esta es la razón por la que emprendo.</div>
							<div class="col px-0">Secundario. También quiero lograr esto.</div>
							<div class="col px-0">Me gustaría si pasara, pero no es indispensable.</div>
							<div class="col px-0">Me es indiferente</div>
						</div>
					"""),
					CustomInlineRadios('motivate1'),
					CustomInlineRadios('motivate2'),
					CustomInlineRadios('motivate3'),
					CustomInlineRadios('motivate4'),
					CustomInlineRadios('motivate5'),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿A que le darías más prioridad? ¿A alcanzar tus objetivos o a disfrutar el proceso? <span class="asteriskField">*</span>
					"""),
					Div(
						HTML("""
							<div class="flex-grow text-center pr-1 mt-4 pt-3" style="max-width: 35%">Disfrutar la experiencia de emprender</div>
						"""),
						VirticalInlineRadio('priority'),
						HTML("""
							<div class="flex-grow text-center pl-1 mt-4 pt-3" style="max-width: 35%">Lograr mis objetivos</div>
						"""),
						css_class='font-size-14px mt-4 d-flex'
					),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'undertake',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'diff_undertake',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			ButtonHolder(
				HTML('<a href="/step2/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)

	def clean(self):
		cleaned_data = super().clean()
		msg = "Esta pergunta é obrigatória"
		
		learning_visual = cleaned_data.get("learning_visual")
		learning_auditory = cleaned_data.get("learning_auditory")
		learning_kinesthetic = cleaned_data.get("learning_kinesthetic")
		learning_not_clear = cleaned_data.get("learning_not_clear")

		if not (learning_visual or learning_auditory or learning_kinesthetic or learning_not_clear):
			self.add_error('learning_group', msg)

		exp_finace = cleaned_data.get("exp_finace")
		exp_Sales = cleaned_data.get("exp_Sales")
		exp_marketing = cleaned_data.get("exp_marketing")
		exp_technology = cleaned_data.get("exp_technology")
		exp_operations = cleaned_data.get("exp_operations")
		exp_human_resources = cleaned_data.get("exp_human_resources")
		exp_legal = cleaned_data.get("exp_legal")
		exp_other = cleaned_data.get("exp_other")

		if not (exp_finace or exp_Sales or exp_marketing or exp_technology or exp_operations or exp_human_resources or exp_legal) or exp_other and exp_other_detail == '':
			self.add_error('exp_other_detail', msg)


class StepFourthForm(ModelForm):
	"""
	4th step form
	"""
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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'step4'
		self.helper.layout = Layout(
			Div(
				Div(
					'goals',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					HTML("""
						¿Cuánto tiempo te es posible dedicarle a tu proyecto de emprendimiento? <span class="asteriskField">*</span>
					"""),
					Div(
						HTML("""
							<div class="flex-grow text-center pr-1 mt-4 pt-2" style="max-width: 35%">Este es un proyecto alternativo al que le puedo dedicar nada más unas pocas horas a la semana.</div>
						"""),
						VirticalInlineRadio('dedicate'),
						HTML("""
							<div class="flex-grow text-center pl-1 mt-4 pt-2" style="max-width: 35%">Lo que sea necesario. Estoy tiempo completo en este proyecto y dispuesto a sacrificar otras áreas de mi vida.</div>
						"""),
						css_class='font-size-14px mt-4 d-flex'
					),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'objective',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'measure',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'obstacle',
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			ButtonHolder(
				HTML('<a href="/step3/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)


class StepFifthForm(ModelForm):
	"""
	Final step form
	"""
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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'step5'
		self.helper.field_template = 'bootstrap4/field_custom.html'
		self.helper.layout = Layout(
			'full_name',
			'gender',
			'age',
			'more',
			ButtonHolder(
				HTML('<a href="/step4/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button submit" value="Enviar">')
			)
		)