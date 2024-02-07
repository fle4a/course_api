from os import cpu_count

import uvicorn

import config
from config.logging import LOGGING


def main():
    uvicorn.run('initializer:create_app', factory=True, access_log=True, log_config=LOGGING, reload=config.APP_AUTORELOAD, workers=cpu_count())


if __name__ == '__main__':
    main()
