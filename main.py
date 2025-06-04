import uvicorn

from core.logger import app_logger as logger
from config import cnf


if __name__ == "__main__":   
    try:
        uvicorn.run(
            app='core.app:app',
            host=cnf.app.HOST,
            port=cnf.app.PORT,
            reload=True
        )
    except KeyboardInterrupt:
        logger.info('Exit app')

