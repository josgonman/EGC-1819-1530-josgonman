ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://localhost:8010',
    'base': 'http://localhost:8010',
    'booth': 'http://localhost:8010',
    'census': 'http://localhost:8010',
    'mixnet': 'http://localhost:8010',
    'postproc': 'http://localhost:8010',
    'store': 'http://localhost:8010',
    'visualizer': 'http://localhost:8010',
    'voting': 'http://localhost:8010',
}

BASEURL = 'http://localhost:8010'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decidedb',
        'USER': 'decide',
        'PASSWORD': 'decide',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
