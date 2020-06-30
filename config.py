import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config():

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(12).hex()


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(Config):
    TESTING = True


"""

{
    'PROPAGATE_EXCEPTIONS': None,
    'PRESERVE_CONTEXT_ON_EXCEPTION': None,
    'EXPLAIN_TEMPLATE_LOADING': False,
    'DEBUG_TB_PANELS': (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel'
    ),
    'MAX_CONTENT_LENGTH': None,
    'MAX_COOKIE_SIZE': 4093,
    'SESSION_COOKIE_DOMAIN': False,
    'PREFERRED_URL_SCHEME': 'http',
    'TESTING': False,
    'SQLALCHEMY_POOL_TIMEOUT': None,
    'BOOTSTRAP_QUERYSTRING_REVVING': True,
    'BOOTSTRAP_SERVE_LOCAL': False,
    'SERVER_NAME': None,
    'SESSION_COOKIE_PATH': None,
    'USE_X_SENDFILE': False,
    'ENV': 'development',
    'DEBUG_TB_HOSTS': (),
    'DEBUG': True,
    'SQLALCHEMY_POOL_RECYCLE': None,
    'TEMPLATES_AUTO_RELOAD': None,
    'SQLALCHEMY_COMMIT_ON_TEARDOWN': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////home/rom/work/fla/app.db',
    'BOOTSTRAP_LOCAL_SUBDOMAIN': None,
    'DEBUG_TB_INTERCEPT_REDIRECTS': False,
    'SECRET_KEY': '0289070a5a3df37292d2fd0b',
    'DEBUG_TB_ENABLED': True,
    'CSRF_ENABLED': True,
    'SESSION_COOKIE_NAME': 'session',
    'BOOTSTRAP_USE_MINIFIED': True,
    'SQLALCHEMY_ECHO': False,
    'TRAP_HTTP_EXCEPTIONS': False,
    'JSON_SORT_KEYS': True,
    'JSON_AS_ASCII': True,
    'SQLALCHEMY_RECORD_QUERIES': None,
    'JSONIFY_MIMETYPE': 'application/json',
    # 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200),
    'JSONIFY_PRETTYPRINT_REGULAR': False,
    'SESSION_COOKIE_SECURE': False,
    'TRAP_BAD_REQUEST_ERRORS': None,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31),
    'SQLALCHEMY_BINDS': None,
    'SQLALCHEMY_MAX_OVERFLOW': None,
    'APPLICATION_ROOT': '/',
    'SESSION_REFRESH_EACH_REQUEST': True,
    'SESSION_COOKIE_HTTPONLY': True,
    'BOOTSTRAP_CDN_FORCE_SSL': False,
    'SQLALCHEMY_NATIVE_UNICODE': None,
    'SQLALCHEMY_ENGINE_OPTIONS': {},
    'SESSION_COOKIE_SAMESITE': None,
    'SQLALCHEMY_POOL_SIZE': None
}
"""
