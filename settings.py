from os import environ

SESSION_CONFIGS = [
    dict(
        name='main',
        app_sequence=[ 'pre', 'main', 'end', 'end2'],
        num_demo_participants=30,
    )
]

DEBUG = False
PRODUCTION = True


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7321273217604'

PARTICIPANT_FIELDS = ['prolific_id']

ROOMS = [
    dict(
        name='prolific_room',
        display_name='Prolific Experiment Room',
    ),
]

SESSION_CONFIGS = [
    dict(
        name='your_experiment',
        display_name="Your Experiment",
        num_demo_participants=3,
        app_sequence=['pre', 'main',"end","end2"], 
    ),
<<<<<<< HEAD
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'otree_db',         # 刚才在 pgAdmin 里起的名
        'USER': 'postgres',         # 默认都是 postgres
        'PASSWORD': '20220602',      # 你安装软件时设置的密码
        'HOST': '127.0.0.1', 
        'PORT': '4023',
    }
}
=======
]
>>>>>>> e2e3bb9641d033353645f1d052a111168045d133
