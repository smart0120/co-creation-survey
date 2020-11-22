from django.db import models


class BusinessCreator(models.Model):
    """
    Email address for Co-creator of business
    """
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SecondStep(models.Model):
    MARKET_CHOICES = [
        (1, 'Products'),
        (2, 'Services'),
    ]
    CLASSIFICATION_CHOICES = [
        (1, 'Freelancer: I am a specialist in doing something and that is what I want to offer without the need to perform tasks in the different areas related to a company'),
        (2, 'Self-employment: the daily operation of my business will depend mainly on my working'),
        (3, 'Micro-company: I want to create a company that generates value through hired collaborators and my daily work (up to 10 employees)'),
        (4, 'Company: I want to create a company that generates value mainly through hired collaborators (more than 10 employees)'),
        (5, 'Company in need of investments: I want to create a company with investment partners because it requires (or required) a lot of capital'),
        (6, 'Other:')
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
    industry = models.TextField()
    classification = models.IntegerField(
        choices=CLASSIFICATION_CHOICES
    )
    classification_other_detail = models.TextField(null=True)
    time_spend = models.IntegerField(
        choices=TIME_SPEND_CHOICE
    )


class ThirdStep(models.Model):
    TRAIT_CHOICES = [
        (1, 'Strongly disagree'),
        (2, 'In disagreement'),
        (3, 'Neutral'),
        (4, 'Agree'),
        (5, 'Totally agree'),
    ]
    MOTIVATE_CHOICES = [
        (1, 'This is the reason why I undertake.'),
        (2, 'Secondary. I also want to achieve this.'),
        (3, 'I would like if it happened, but it is not essential.'),
        (4, 'It does not matter to me'),
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

    exp_other_detail = models.TextField(null=True)

    motivate1 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate2 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate3 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate4 = models.IntegerField(choices=MOTIVATE_CHOICES)
    motivate5 = models.IntegerField(choices=MOTIVATE_CHOICES)

    priority = models.IntegerField(choices=PRIORITY_CHOICES)

    undertake = models.TextField()
    diff_undertake = models.TextField()
    

class FourthStep(models.Model):
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
    GENDER_CHOICES = [
        (1, 'Man'),
        (2, 'Woman'),
        (3, 'I prefer not to specify'),
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