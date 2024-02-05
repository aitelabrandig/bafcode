import os
from dotenv import load_dotenv
load_dotenv()

class AppConfig:
    # Flask Configuration
    FASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = os.environ.get('DEBUG', True)
    SECRET_KEY = os.environ.get('FRAMEWORK_SECRET_KEY', 'default_secret_key')  # Ensure to use a strong secret key in production

    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


    # Port Configuration
    PORT = int(os.environ.get('PORT', 5000))

    # Any other global configurations or settings can be added below


    # Database Configuration
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')
