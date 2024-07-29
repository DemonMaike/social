from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = '.env'


class DbSettings(BaseSettings):

    host: str
    port: int
    name: str
    user: str
    
    model_config = SettingsConfigDict(env_file=env_path,
                                      env_prefix='DB_',
                                      extra='ignore')

class DjangoSettings(BaseSettings):

    secret_key: str
    
    model_config = SettingsConfigDict(env_file=env_path,
                                      env_prefix='DJANGO_',
                                      extra='ignore')
    
    
class OAuthGoogleSettings(BaseSettings):
    key: str
    sec: str
    
    model_config = SettingsConfigDict(env_file=env_path,
                                      env_prefix='OAUTH_GOOGLE_',
                                      extra='ignore')

class Settings(BaseSettings):
    
    db: DbSettings = DbSettings()
    django: DjangoSettings = DjangoSettings()
    oauth_google: OAuthGoogleSettings = OAuthGoogleSettings()

    model_config = SettingsConfigDict(env_file='.env',
                                      extra='ignore')


settings = Settings()
