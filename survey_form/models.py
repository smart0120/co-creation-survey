from django.db import models


class BusinessCreator(models.Model):
    """
    Email address for Co-creator of business
    """
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SecondStep(models.Model):
    """
    Model used for 2nd Step Page
    """
    MARKET_CHOICES = [
        (1, 'Productos'),
        (2, 'Servicios'),
    ]
    CLASSIFICATION_CHOICES = [
        (1, 'Freelancer: soy especialista en hacer algo y eso es lo quiero ofrecer sin la necesidad de realizar tareas de las diferentes áreas relacionadas con una empresa'),
        (2, 'Autoempleo: la operación diaria de mi negocio dependerá principalmente de que yo trabaje'),
        (3, 'Microempresa: quiero crear una empresa que genere valor a través de colaboradores contratados y mi trabajo diario (hasta 10 empleados)'),
        (4, 'Empresa: quiero crear una empresa que genere valor principalmente a través de colaboradores contratados (más de 10 empleados)'),
        (5, 'Empresa con necesidad de inversiones: quiero crear una empresa con socios inversionistas porque requiere (o requirió) mucho capital'),
        (6, 'Outro:')
    ]
    TIME_SPEND_CHOICE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    co_creator = models.OneToOneField(BusinessCreator, on_delete=models.CASCADE)
    consists = models.TextField()
    market = models.IntegerField(
        choices=MARKET_CHOICES
    )
    industry = models.CharField(max_length=256)
    classification = models.IntegerField(
        choices=CLASSIFICATION_CHOICES
    )
    classification_other_detail = models.CharField(blank=True, max_length=256)
    time_spend = models.IntegerField(
        choices=TIME_SPEND_CHOICE
    )


class ThirdStep(models.Model):
    """
    Model used for 3rd step
    """
    TRAIT_CHOICES = [
        (1, 'Totalmente en desacuerdo'),
        (2, 'En desacuerdo'),
        (3, 'Neutral'),
        (4, 'De acuerdo'),
        (5, 'Totalmente de acuerdo'),
    ]
    MOTIVATE_CHOICES = [
        (1, 'Esta es la razón por la que emprendo.'),
        (2, 'Secundario. También quiero lograr esto.'),
        (3, 'Me gustaría si pasara, pero no es indispensable.'),
        (4, 'Me es indiferente'),
    ]
    PRIORITY_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    co_creator = models.OneToOneField(BusinessCreator, on_delete=models.CASCADE)
    trait1 = models.IntegerField(choices=TRAIT_CHOICES)
    trait2 = models.IntegerField(choices=TRAIT_CHOICES)
    trait3 = models.IntegerField(choices=TRAIT_CHOICES)
    trait4 = models.IntegerField(choices=TRAIT_CHOICES)
    trait5 = models.IntegerField(choices=TRAIT_CHOICES)
    trait6 = models.IntegerField(choices=TRAIT_CHOICES)
    trait7 = models.IntegerField(choices=TRAIT_CHOICES)
    trait8 = models.IntegerField(choices=TRAIT_CHOICES)
    trait9 = models.IntegerField(choices=TRAIT_CHOICES)
    trait10 = models.IntegerField(choices=TRAIT_CHOICES)
    trait11 = models.IntegerField(choices=TRAIT_CHOICES)
    trait12 = models.IntegerField(choices=TRAIT_CHOICES)
    trait13 = models.IntegerField(choices=TRAIT_CHOICES)
    trait14 = models.IntegerField(choices=TRAIT_CHOICES)
    trait15 = models.IntegerField(choices=TRAIT_CHOICES)
    trait16 = models.IntegerField(choices=TRAIT_CHOICES)
    trait17 = models.IntegerField(choices=TRAIT_CHOICES)
    trait18 = models.IntegerField(choices=TRAIT_CHOICES)
    trait19 = models.IntegerField(choices=TRAIT_CHOICES)
    trait20 = models.IntegerField(choices=TRAIT_CHOICES)
    trait21 = models.IntegerField(choices=TRAIT_CHOICES)
    trait22 = models.IntegerField(choices=TRAIT_CHOICES)
    trait23 = models.IntegerField(choices=TRAIT_CHOICES)
    trait24 = models.IntegerField(choices=TRAIT_CHOICES)
    trait25 = models.IntegerField(choices=TRAIT_CHOICES)
    trait26 = models.IntegerField(choices=TRAIT_CHOICES)
    trait27 = models.IntegerField(choices=TRAIT_CHOICES)
    trait28 = models.IntegerField(choices=TRAIT_CHOICES)
    trait29 = models.IntegerField(choices=TRAIT_CHOICES)
    trait30 = models.IntegerField(choices=TRAIT_CHOICES)
    trait31 = models.IntegerField(choices=TRAIT_CHOICES)
    trait32 = models.IntegerField(choices=TRAIT_CHOICES)
    trait33 = models.IntegerField(choices=TRAIT_CHOICES)
    trait34 = models.IntegerField(choices=TRAIT_CHOICES)
    trait35 = models.IntegerField(choices=TRAIT_CHOICES)
    trait36 = models.IntegerField(choices=TRAIT_CHOICES)
    trait37 = models.IntegerField(choices=TRAIT_CHOICES)
    trait38 = models.IntegerField(choices=TRAIT_CHOICES)
    trait39 = models.IntegerField(choices=TRAIT_CHOICES)
    trait40 = models.IntegerField(choices=TRAIT_CHOICES)
    trait41 = models.IntegerField(choices=TRAIT_CHOICES)
    trait42 = models.IntegerField(choices=TRAIT_CHOICES)
    trait43 = models.IntegerField(choices=TRAIT_CHOICES)
    trait44 = models.IntegerField(choices=TRAIT_CHOICES)
    trait45 = models.IntegerField(choices=TRAIT_CHOICES)
    trait46 = models.IntegerField(choices=TRAIT_CHOICES)
    trait47 = models.IntegerField(choices=TRAIT_CHOICES)
    trait48 = models.IntegerField(choices=TRAIT_CHOICES)
    trait49 = models.IntegerField(choices=TRAIT_CHOICES)
    trait50 = models.IntegerField(choices=TRAIT_CHOICES)

    learning_visual = models.BooleanField(default=False);
    learning_auditory = models.BooleanField(default=False);
    learning_kinesthetic = models.BooleanField(default=False);
    learning_not_clear = models.BooleanField(default=False);

    exp_finace = models.BooleanField(default=False);
    exp_Sales = models.BooleanField(default=False);
    exp_marketing = models.BooleanField(default=False);
    exp_technology = models.BooleanField(default=False);
    exp_operations = models.BooleanField(default=False);
    exp_human_resources = models.BooleanField(default=False);
    exp_legal = models.BooleanField(default=False);
    exp_other = models.BooleanField(default=False);

    exp_other_detail = models.CharField(blank=True, max_length=256)

    motivate1 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate2 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate3 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate4 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate5 = models.IntegerField(choices=MOTIVATE_CHOICES)

    priority = models.IntegerField(choices=PRIORITY_CHOICES)

    undertake = models.TextField()
    diff_undertake = models.TextField()
    

class FourthStep(models.Model):
    """
    Model used for 4th Step
    """
    DEDICATE_CHOICE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    co_creator = models.OneToOneField(BusinessCreator, on_delete=models.CASCADE)
    goals = models.TextField()
    dedicate = models.IntegerField(choices=DEDICATE_CHOICE)
    objective = models.TextField()
    measure = models.TextField()
    obstacle = models.TextField()


class FifthStep(models.Model):
    """
    Model used for Final Step
    """
    GENDER_CHOICES = [
        (1, 'Hombre'),
        (2, 'Mujer'),
        (3, 'Prefiero no especificar'),
    ]
    co_creator = models.OneToOneField(BusinessCreator, on_delete=models.CASCADE)
    full_name = models.TextField()
    gender = models.IntegerField(
        choices=GENDER_CHOICES,
        default=3,
        blank=True
    )
    age = models.IntegerField(blank=True)
    more = models.TextField(blank=True)
