from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):

    host: str
    port: int
    name: str
    user: str
    
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='DB_',
                                      extra='ignore')

class DjangoSettings(BaseSettings):

    secret_key: str
    
    model_config = SettingsConfigDict(env_file='.env',
                                      env_prefix='DJANGO_',
                                      extra='ignore')

class Settings(BaseSettings):
    
    db: DbSettings = DbSettings()
    django: DjangoSettings = DjangoSettings()

    model_config = SettingsConfigDict(env_file='.env',
                                      extra='ignore')


settings = Settings()
