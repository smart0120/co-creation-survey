from django import forms
from django.forms import ModelForm, Field

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import InlineRadios

from .models import BusinessCreator, SecondStep, ThirdStep, FourthStep, FifthStep

Field.default_error_messages = {
	'required': 'Esta pergunta é obrigatória'
}
InlineRadios.template = "%s/layout/custom_radioselect_inline.html"

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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.field_template = "bootstrap4/field_custom.html"
		self.helper.form_action = ''
		self.helper.layout = Layout(
			'email',
			ButtonHolder(
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)


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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = ''
		self.helper.layout = Layout(
			Div(
				Div(
					'consists',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'market',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'industry',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'classification',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					InlineRadios('time_spend'),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			ButtonHolder(
				HTML('<a href="/step1/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)


class StepThirdForm(ModelForm):
	trait1 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Soy el alma de la fiesta'
	)
	trait2 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Siento poca preocupación por los demás'
	)
	trait3 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Siempre estoy preparado'
	)
	trait4 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me estreso fácilmente'
	)
	trait5 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo un amplio vocabulario'
	)
	trait6 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No hablo mucho'
	)
	trait7 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me interesan las personas'
	)
	trait8 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Dejo mis pertenencias cerca'
	)
	trait9 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Estoy relajado la mayoría del tiempo'
	)
	trait10 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me cuesta trabajo entender ideas abstractas'
	)
	trait11 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me siento cómodo rodeado de gente'
	)
	trait12 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Insulto a la gente'
	)
	trait13 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Pongo atención a los detalles'
	)
	trait14 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me preocupan las cosas'
	)
	trait15 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo una imaginación vívida'
	)
	trait16 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me mantengo en segundo plano'
	)
	trait17 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Simpatizo con los sentimiento de los demás'
	)
	trait18 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Hago las cosas muy grandes'
	)
	trait19 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Rara vez me siento triste'
	)
	trait20 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No estoy interesado en ideas abstractas'
	)
	trait21 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Comienzo conversaciones'
	)
	trait22 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No estoy interesado en los problemas de los demás'
	)
	trait23 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Hago mis pendientes en el momento'
	)
	trait24 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me molesto fácilmente'
	)
	trait25 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo ideas excelentes'
	)
	trait26 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo poco que decir'
	)
	trait27 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo un corazón suave'
	)
	trait28 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='A menudo olvido de poner las cosas en su lugar'
	)
	trait29 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me enojo fácilmente'
	)
	trait30 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No tengo buena imaginación'
	)
	trait31 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Hablo con muchas personas diferentes en las fiestas'
	)
	trait32 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No estoy realmente interesado en los demás'
	)
	trait33 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me gusta el orden'
	)
	trait34 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Cambio mucho de humor'
	)
	trait35 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Soy rápido para entender las cosas'
	)
	trait36 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No me gusta atraer la atención hacia mi'
	)
	trait37 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me tomo tiempo para los demás'
	)
	trait38 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Eludo mis deberes'
	)
	trait39 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Tengo cambios de humor frecuentes'
	)
	trait40 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Uso palabras rebuscadas'
	)
	trait41 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='No me molesta ser el centro de atención'
	)
	trait42 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Siento las emociones de los demás'
	)
	trait43 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Sigo un horario'
	)
	trait44 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Me irrito fácilmente'
	)
	trait45 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Dedico tiempo para reflexionar sobre diversos temas'
	)
	trait46 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Soy tranquilo cuando estoy rodeado de extraños'
	)
	trait47 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Hago que la gente se sienta cómoda'
	)
	trait48 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Soy exigente en mi trabajo'
	)
	trait49 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='A menudo me siento triste'
	)
	trait50 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.TRAIT_CHOICES,
		required=False,
		label='Estoy lleno de ideas'
	)

	motivate1 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		required=False,
		label='Ganar dinero'
	)
	motivate2 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		required=False,
		label='Dedicarme a lo que me gusta'
	)
	motivate3 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		required=False,
		label='Cambiar/mejorar el mundo'
	)
	motivate4 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		required=False,
		label='Tener flexibilidad en mi vida en general'
	)
	motivate5 = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.MOTIVATE_CHOICES,
		required=False,
		label='Ser reconocido como exitoso'
	)

	priority = forms.ChoiceField(
		widget=forms.RadioSelect,
		choices=ThirdStep.PRIORITY_CHOICES,
		label='¿A que le darías más prioridad? ¿A alcanzar tus objetivos o a disfrutar el proceso?'
	)

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
		self.helper.form_action = ''
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
					InlineRadios('trait1'),
					InlineRadios('trait2'),
					InlineRadios('trait3'),
					InlineRadios('trait4'),
					InlineRadios('trait5'),
					InlineRadios('trait6'),
					InlineRadios('trait7'),
					InlineRadios('trait8'),
					InlineRadios('trait9'),
					InlineRadios('trait10'),
					InlineRadios('trait11'),
					InlineRadios('trait12'),
					InlineRadios('trait13'),
					InlineRadios('trait14'),
					InlineRadios('trait15'),
					InlineRadios('trait16'),
					InlineRadios('trait17'),
					InlineRadios('trait18'),
					InlineRadios('trait19'),
					InlineRadios('trait20'),
					InlineRadios('trait21'),
					InlineRadios('trait22'),
					InlineRadios('trait23'),
					InlineRadios('trait24'),
					InlineRadios('trait25'),
					InlineRadios('trait26'),
					InlineRadios('trait27'),
					InlineRadios('trait28'),
					InlineRadios('trait29'),
					InlineRadios('trait30'),
					InlineRadios('trait31'),
					InlineRadios('trait32'),
					InlineRadios('trait33'),
					InlineRadios('trait34'),
					InlineRadios('trait35'),
					InlineRadios('trait36'),
					InlineRadios('trait37'),
					InlineRadios('trait38'),
					InlineRadios('trait39'),
					InlineRadios('trait40'),
					InlineRadios('trait41'),
					InlineRadios('trait42'),
					InlineRadios('trait43'),
					InlineRadios('trait44'),
					InlineRadios('trait45'),
					InlineRadios('trait46'),
					InlineRadios('trait47'),
					InlineRadios('trait48'),
					InlineRadios('trait49'),
					InlineRadios('trait50'),
					css_class='block-body pt-4 radio-box'
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
						css_class='font-size-14px mt-3'
					),
					css_class='block-body pt-4'
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
					InlineRadios('motivate1'),
					InlineRadios('motivate2'),
					InlineRadios('motivate3'),
					InlineRadios('motivate4'),
					InlineRadios('motivate5'),
					css_class='block-body pt-4'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'priority',
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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = ''
		self.helper.layout = Layout(
			Div(
				Div(
					'goals',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'dedicate',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'objective',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'measure',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			Div(
				Div(
					'obstacle',
					css_class='block-body pt-4 radio-box'
				),
				css_class='block-content mb-2'
			),
			ButtonHolder(
				HTML('<a href="/step3/" class="btn button">Voltar</a>'),
				HTML('<input type="submit" class="btn button" value="Próxima">')
			)
		)


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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = ''
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