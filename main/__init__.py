import random

from otree.api import *

doc = """
Manager Game
"""

briefing_answers = [2,1,3,1,3,2,3,4,6,[5,7],5,6,5,1,4]


class C(BaseConstants):
    NAME_IN_URL = 'main'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None
    CHOICES = range(1, 6)
    QUESTIONS = [
        '...is reserved',
        '...generally trusting',
        '...tends to be lazy',
        '...is relaxed, handles stress well',
        '...has few artistic interests',
        '...does things efficiently',
        '...is outgoing, sociable',
        '...tends to find fault with others',
        '...does a thorough job',
        '...gets nervous easily',
        '...has an active imagination',
        '...perseveres until the task is finished',
    ]

    COMPARISON_QUESTIONS = [
        'I always pay a lot of attention to how I do things compared with how others do things.',
        'I am not the type of person who compares often with others.',
        'I often compare how I am doing socially (e.g., social skills, popularity) with other people.',
        'I see myself as someone who enjoys winning and hates losing.',
        'I see myself as someone who enjoys competing, regardless of whether I win or lose.',
        'I see myself as a competitive person.',
        'Competition brings the best out of me.',
    ]

    DICTATOR_ENDOWMENT = 10
    AGE_LABEL = "What is your age?"
    
    GENDER_LABEL = "What is your gender?"
    GENDER_CHOICES = ["Male", "Female", "Non-binary","Prefer not to say"]
    
    EDUCATION_LABEL = "Please indicate the highest level of education completed"
    EDUCATION_CHOICES = [
        "Less than High School",
        "High School or equivalent",
        "Vocational/Technical School (2 years)",
        "Some College",
        "College Graduate (4 years)",
        "Master's Degree (MA)",
        "Doctoral Degree (PhD)"
    ]

    INCOME_LABEL = "What is your annual household income?"
    INCOME_CHOICES = [
        "Less than $25,000",
        "$25,000 - $49,999",
        "$50,000 - $74,999",
        "$75,000 - $99,999",
        "$100,000 - $149,999",
        "$150,000 or more",
        "Prefer not to say"
    ]
    
    # Demographics - Employment
    EMPLOYMENT_LABEL = "What is your current employment status?"
    EMPLOYMENT_CHOICES = [
        "Full-time employed",
        "Part-time employed",
        "Self-employed",
        "Unemployed",
        "Student",
        "Retired",
        "Unable to work",
        "Other"
    ]
    
    # Demographics - Occupation/Industry
    OCCUPATION_LABEL = "What industry do you work in (or most recently worked in)?"
    OCCUPATION_CHOICES = [
        "Education",
        "Healthcare",
        "Technology/IT",
        "Finance/Banking",
        "Retail/Sales",
        "Manufacturing",
        "Government/Public Service",
        "Arts/Entertainment",
        "Construction/Trades",
        "Transportation/Logistics",
        "Hospitality/Food Service",
        "Legal/Professional Services",
        "Non-profit/NGO",
        "Other"
    ]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    stated_amount = models.IntegerField(
        label="Please enter the number of points you have achieved in this task:",
        min=0,
        max=15
    )
    threshold_integer = models.IntegerField()
    briefing_correct_amount = models.IntegerField(initial=0)  # Changed to IntegerField
    # briefing_1~15
    briefing_1 = models.CharField(
        label="Question 1<br><br><img src='/static/img/briefing/1.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 4 options given to fill in the question mark:<br><br><img src='/static/img/briefing/1.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 5),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_2 = models.CharField(
        label="Question 2<br><br><img src='/static/img/briefing/2.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 4 options given to fill in the question mark:<br><br><img src='/static/img/briefing/2.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 5),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_3 = models.CharField(
        label="Question 3<br><br><img src='/static/img/briefing/3.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 4 options given to fill in the question mark:<br><br><img src='/static/img/briefing/3.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 5),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_4 = models.CharField(
        label="Question 4<br><br><img src='/static/img/briefing/4.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 4 options given to fill in the question mark:<br><br><img src='/static/img/briefing/4.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 5),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_5 = models.CharField(
        label="Question 5<br><br><img src='/static/img/briefing/5.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 4 options given to fill in the question mark:<br><br><img src='/static/img/briefing/5.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 5),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_6 = models.CharField(
        label="Question 6<br><br><img src='/static/img/briefing/6.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/6.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_7 = models.CharField(
        label="Question 7<br><br><img src='/static/img/briefing/7.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/7.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_8 = models.CharField(
        label="Question 8<br><br><img src='/static/img/briefing/8.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/8.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_9 = models.CharField(
        label="Question 9<br><br><img src='/static/img/briefing/9.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/9.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_10 = models.CharField(
        label="Question 10<br><br><img src='/static/img/briefing/10.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/10.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_11 = models.CharField(
        label="Question 11<br><br><img src='/static/img/briefing/11.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/11.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_12 = models.CharField(
        label="Question 12<br><br><img src='/static/img/briefing/12.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/12.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_13 = models.CharField(
        label="Question 13<br><br><img src='/static/img/briefing/13.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/13.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_14 = models.CharField(
        label="Question 14<br><br><img src='/static/img/briefing/14.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/14.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )

    briefing_15 = models.CharField(
        label="Question 15<br><br><img src='/static/img/briefing/15.png' style='width: 280px; max-width: 100%;'><br><br>Choose the most appropriate one from the 8 options given to fill in the question mark:<br><br><img src='/static/img/briefing/15.1.png' style='width: 280px; max-width: 100%;'><br><br>",
        choices=range(1, 9),
        widget=widgets.RadioSelect,
        blank=True
    )


    misreport_reason = models.LongStringField()

    accept_next_experiment = models.BooleanField(
        label="Would you like to participate in the additional experiment?",
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],
        widget=widgets.RadioSelect
    )

    prefer = models.StringField(
        label="Which painting do you prefer?",
        choices=[
            ['Left', 'Left'],
            ['Right', 'Right']
        ],
        widget=widgets.RadioSelect
    )
    
    # Add the painter field to store the mapped painter name
    painter = models.StringField()
    
    # Big5 questions 
    Q1 = models.IntegerField(label=C.QUESTIONS[0], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q2 = models.IntegerField(label=C.QUESTIONS[1], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q3 = models.IntegerField(label=C.QUESTIONS[2], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q4 = models.IntegerField(label=C.QUESTIONS[3], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q5 = models.IntegerField(label=C.QUESTIONS[4], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q6 = models.IntegerField(label=C.QUESTIONS[5], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q7 = models.IntegerField(label=C.QUESTIONS[6], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q8 = models.IntegerField(label=C.QUESTIONS[7], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q9 = models.IntegerField(label=C.QUESTIONS[8], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q10 = models.IntegerField(label=C.QUESTIONS[9], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q11 = models.IntegerField(label=C.QUESTIONS[10], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Q12 = models.IntegerField(label=C.QUESTIONS[11], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    
    # Comparison questions
    Comp1 = models.IntegerField(label=C.COMPARISON_QUESTIONS[0], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp2 = models.IntegerField(label=C.COMPARISON_QUESTIONS[1], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp3 = models.IntegerField(label=C.COMPARISON_QUESTIONS[2], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp4 = models.IntegerField(label=C.COMPARISON_QUESTIONS[3], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp5 = models.IntegerField(label=C.COMPARISON_QUESTIONS[4], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp6 = models.IntegerField(label=C.COMPARISON_QUESTIONS[5], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    Comp7 = models.IntegerField(label=C.COMPARISON_QUESTIONS[6], choices=C.CHOICES, widget=widgets.RadioSelectHorizontal)
    
    # Dictator game
    dictator_keep = models.CurrencyField(
        min=0, 
        max=C.DICTATOR_ENDOWMENT,
        label="(Please move the slider)"
    )
    
    # Demographic fields
    age = models.IntegerField(label=C.AGE_LABEL, min=18, max=100)
    gender = models.StringField(
        label=C.GENDER_LABEL,
        choices=C.GENDER_CHOICES
    )
    education = models.StringField(
        label=C.EDUCATION_LABEL,
        choices=C.EDUCATION_CHOICES
    )
    income = models.StringField(
        label=C.INCOME_LABEL,
        choices=C.INCOME_CHOICES
    )
    employment = models.StringField(
        label=C.EMPLOYMENT_LABEL,
        choices=C.EMPLOYMENT_CHOICES
    )
    occupation = models.StringField(
        label=C.OCCUPATION_LABEL,
        choices=C.OCCUPATION_CHOICES
    )
# PAGES


        
class Intro(Page):
    pass

class IQTest(Page):
    timeout_seconds = 180  
    form_model = 'player'
    form_fields = [
        'briefing_1', 'briefing_2', 'briefing_3', 'briefing_4', 'briefing_5', 'briefing_6', 'briefing_7',
        'briefing_8', 'briefing_9', 'briefing_10', 'briefing_11', 'briefing_12', 'briefing_13', 'briefing_14',
        'briefing_15'
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'timeout_seconds': IQTest.timeout_seconds  
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for field in IQTest.form_fields:
                if player.field_maybe_none(field) is None:
                    setattr(player, field, '8')
        
        briefing_correct_amount = 0
        for i, field in enumerate(IQTest.form_fields):
            player_answer = player.field_maybe_none(field)
            if player_answer is not None:
                try:
                    player_answer_int = int(player_answer)
                    if isinstance(briefing_answers[i], list):
                        if player_answer_int in briefing_answers[i]:
                            briefing_correct_amount += 1
                    elif briefing_answers[i] == player_answer_int:
                        briefing_correct_amount += 1
                except (ValueError, TypeError):
                    pass
        
        player.briefing_correct_amount = briefing_correct_amount

class StatePrev(Page):
    pass

class MisreportingRule(Page):
    @staticmethod
    def get_round_robin_integer(player):
        integers = [8, 10, 12, 100]
        index = (player.id_in_group - 1) % 4
        return integers[index]
    
    @staticmethod
    def vars_for_template(player):
        threshold = MisreportingRule.get_round_robin_integer(player)
        player.threshold_integer = threshold
        return {
            'round_robin_integer': threshold
        }

class State(Page):
    form_model = 'player'
    form_fields = ['stated_amount']

    @staticmethod
    def vars_for_template(player):
        return {
            'round_robin_integer': player.threshold_integer
        }
    
class Result(Page):
    @staticmethod
    def vars_for_template(player):
        threshold = player.threshold_integer
        max_bonus_points = 4  

        if player.stated_amount <= threshold:
            player.payoff = 1
        elif player.stated_amount <= threshold + max_bonus_points:
            player.payoff = 1 + 0.5 * (player.stated_amount - threshold)
        else:
            player.payoff = 3  

        return {
            'correct_amount': player.briefing_correct_amount,
            'stated_amount': player.stated_amount,
            'payoff': player.payoff,
            'threshold': threshold  
        }


class Survey(Page):
    form_model = 'player'
    form_fields = ['misreport_reason']
    
    def error_message(self, values):
        errors = {}
        
        import re
        if values['misreport_reason']:
            if not re.match(r'^[a-zA-Z0-9\s\.\,\!\?\;\:\-\'\"]*$', values['misreport_reason']):
                errors['misreport_reason'] = 'Please enter only letters, numbers, and punctuation'
        
        if not values['misreport_reason'].strip():
            errors['misreport_reason'] = 'This field is required'
            
        return errors if errors else None
    
class Code(Page):
    def vars_for_template(self):
        return {
            'completion_code': 'C1I5TIFN'
        }
    
class Painting(Page):
    form_model = 'player'
    form_fields = ['prefer']
   
class Big5(Page):
    form_model = 'player'
    form_fields = [f'Q{i + 1}' for i in range(len(C.QUESTIONS))]


class Comparison(Page):
    form_model = 'player'
    form_fields = [f'Comp{i}' for i in range(1, len(C.COMPARISON_QUESTIONS) + 1)]


class Dictator(Page):
    form_model = 'player'
    form_fields = ['dictator_keep']
    
    def vars_for_template(self):
        return {
            'endowment': C.DICTATOR_ENDOWMENT
        }


class Info(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income', 'employment', 'occupation']

page_sequence = [
    Intro,
    IQTest,
    StatePrev,
    MisreportingRule,
    State,
    Survey,
    Painting,
    Big5, 
    Comparison, 
    Dictator, 
    Info, 
    Result,
    Code
]