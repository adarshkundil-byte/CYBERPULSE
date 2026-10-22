import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///cyberpulse.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB cap on request bodies
    WTF_CSRF_ENABLED = True
    DEBUG = False


class DevConfig(BaseConfig):
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-not-for-production")
    DEBUG = True


class ProdConfig(BaseConfig):
    SESSION_COOKIE_SECURE = True

    @property
    def SECRET_KEY(self):
        key = os.environ.get("SECRET_KEY")
        if not key:
            raise RuntimeError("SECRET_KEY must be set in production")
        return key


class TestConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


CONFIGS = {"development": DevConfig, "production": ProdConfig, "testing": TestConfig}
