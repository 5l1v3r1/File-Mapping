SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pass@localhost:3306/dbname'

SECRET_KEY = ''
ADMIN_PASSWORD = ''
LOGIN_SALT = ''
UPLOAD_PATH = ''
MAX_PREVIEW_SIZE = 1048576  # 1 MB
URL_PREFIX = ''