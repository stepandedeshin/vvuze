from pydantic_settings import BaseSettings

class App(BaseSettings):
    HASHING_KEY: str
    HASHING_ALGORITHM: str
    HOST: str
    PORT: int

    class Config:
        env_prefix = 'APP_'
        env_file = '.env'
        extra = 'ignore'


class JwtToken(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    
    class Config:
        env_prefix = 'JWT_'
        env_file = '.env'
        extra = 'ignore'

    

class PSQL(BaseSettings):
    HOST: str 
    PORT: str
    USER: str
    PASSWORD: str
    NAME: str

    @property
    def URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    class Config:
        env_prefix = 'PSQL_'
        env_file = '.env'
        extra = 'ignore'


class Redis(BaseSettings):
    HOST: str
    PORT: str
    DB: int

    @property
    def URL(self):
        return f"redis://{self.HOST}:{self.PORT}"

    class Config:
        env_prefix = 'REDIS_'
        env_file = '.env'
        extra = 'ignore'


class Settings(BaseSettings):
    app: App = App()
    psql: PSQL = PSQL()
    redis: Redis = Redis()
    jwt_token: JwtToken = JwtToken()

cnf = Settings()