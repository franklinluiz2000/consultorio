from .settings import *
DEBUG = True
# Crie a secret key para seu ambiente de produção
SECRET_KEY = 'ixb62hb#ts=ab532u%p1_62-!5w2j==j6d^2-j$!z(@*m+-h'
ALLOWED_HOSTS = ['https://consultorio-frankstark.herokuapp.com/']
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}
