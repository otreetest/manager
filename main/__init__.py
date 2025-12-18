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
    FIXED_THRESHOLD = 8


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
        label="Please select your preferred painting from the options below:",
        choices=[
            ['Left', 'Left'],
            ['Right', 'Right']
        ],
        widget=widgets.RadioSelect
    )
    
    # Add the painter field to store the mapped painter name
    painter = models.StringField()
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
    def vars_for_template(player):
        player.threshold_integer = C.FIXED_THRESHOLD
        return {
            'round_robin_integer': C.FIXED_THRESHOLD
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


class Code(Page):
    def vars_for_template(self):
        return {
            'completion_code': 'C1BC94EY'
        }
    
class Painting(Page):
    form_model = 'player'
    form_fields = ['prefer']
   
page_sequence = [
    Intro,
    IQTest,
    StatePrev,
    MisreportingRule,
    State,
    Painting, 
    Result,
    Code
]