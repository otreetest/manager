import random

from otree.api import *

doc = """
Your app description
"""



briefing_answers = [4, 2, 6, 3, 5, 6, 4, 3, 4, 5, 3, 7, 5, 1, 3, 7, 8, 4, 2, 2]


class C(BaseConstants):
    NAME_IN_URL = 'main'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    consent = models.BooleanField(
    label="I consent to participate in this study"
    )
    stated_amount = models.IntegerField(
        label="Please enter the number of points you have achieved in this task:",
        min=0,
        max=20
    )

    briefing_correct_amount = models.IntegerField()
    # briefing_1~20
    briefing_1 = models.IntegerField(
        label="1、<img src='/static/img/briefing/1.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_2 = models.IntegerField(
        label="2、<img src='/static/img/briefing/2.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_3 = models.IntegerField(
        label="3、<img src='/static/img/briefing/3.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_4 = models.IntegerField(
        label="4、<img src='/static/img/briefing/4.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_5 = models.IntegerField(
        label="5、<img src='/static/img/briefing/5.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_6 = models.IntegerField(
        label="6、<img src='/static/img/briefing/6.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_7 = models.IntegerField(
        label="7、<img src='/static/img/briefing/7.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_8 = models.IntegerField(
        label="8、<img src='/static/img/briefing/8.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_9 = models.IntegerField(
        label="9、<img src='/static/img/briefing/9.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_10 = models.IntegerField(
        label="10、<img src='/static/img/briefing/10.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 7),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_11 = models.IntegerField(
        label="11、<img src='/static/img/briefing/11.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_12 = models.IntegerField(
        label="12、<img src='/static/img/briefing/12.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_13 = models.IntegerField(
        label="13、<img src='/static/img/briefing/13.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_14 = models.IntegerField(
        label="14、<img src='/static/img/briefing/14.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_15 = models.IntegerField(
        label="15、<img src='/static/img/briefing/15.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_16 = models.IntegerField(
        label="16、<img src='/static/img/briefing/16.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_17 = models.IntegerField(
        label="17、<img src='/static/img/briefing/17.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_18 = models.IntegerField(
        label="18、<img src='/static/img/briefing/18.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_19 = models.IntegerField(
        label="19、<img src='/static/img/briefing/19.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    briefing_20 = models.IntegerField(
        label="20、<img src='/static/img/briefing/20.png' style='width: 300px; max-width: 100%;'>",
        choices=range(1, 9),
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

    did_misreport = models.BooleanField(
        label="Did you misreport your accuracy?",
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect,
    )

    misreport_reason = models.LongStringField(
        label="Please briefly describe why you did/didn't misreport",
    )
# PAGES


class Briefing(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if not player.consent:
            return 'end'
        
class Intro(Page):
    pass

class IQTest(Page):
    timeout_seconds = 180
    form_model = 'player'
    form_fields = [
        'briefing_1', 'briefing_2', 'briefing_3', 'briefing_4', 'briefing_5', 'briefing_6', 'briefing_7',
        'briefing_8', 'briefing_9', 'briefing_10', 'briefing_11', 'briefing_12', 'briefing_13', 'briefing_14',
        'briefing_15', 'briefing_16', 'briefing_17', 'briefing_18', 'briefing_19', 'briefing_20'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        briefing_correct_amount = 0
        for i, field in enumerate(IQTest.form_fields):
            if briefing_answers[i] == player.field_maybe_none(field):
                briefing_correct_amount += 1
        player.briefing_correct_amount = briefing_correct_amount



class StatePrev(Page):
    pass

class MisreportingRule(Page):
    pass

class State(Page):
    form_model = 'player'
    form_fields = ['stated_amount']

class Result(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.stated_amount <= 16:
            player.payoff = 2
        else:
            player.payoff = 2 + 0.5 * (player.stated_amount - 16)
            
        return {
            'correct_amount': player.briefing_correct_amount,
            'stated_amount': player.stated_amount,
            'payoff': player.payoff
        }

class Survey(Page):
    form_model = 'player'
    form_fields = ['did_misreport', 'misreport_reason']
    
    def error_message(self, values):
        errors = {}
        
        import re
        if values['misreport_reason']:
            if not re.match(r'^[a-zA-Z\s]*$', values['misreport_reason']):
                errors['misreport_reason'] = 'Please enter only letters'
        
        # 如果 misreport_reason 为空，添加错误消息
        if not values['misreport_reason'].strip():
            errors['misreport_reason'] = 'This field is required'
            
        return errors if errors else None 
    
class Code(Page):
    def vars_for_template(self):
        return {
            'completion_code': 'CIEYNDAF'
        }

page_sequence = [
    Briefing,
    Intro,
    IQTest,
    StatePrev,
    MisreportingRule,
    State,
    Result,
    Survey,
    Code
]
