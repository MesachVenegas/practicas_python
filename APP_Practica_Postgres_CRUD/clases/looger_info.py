import logging as log

_FILE = "C:\\Users\\mesas\\OneDrive\\Documentos\\APP_Practica\\log\\app.log"

log.basicConfig(
    level= log.WARNING,
    format = "%(asctime)s: %(levelname)s [%(processName)s] %(filename)s [%(funcName)s]: %(message)s",
    datefmt = '%I:%M:%S|%p',
    handlers = [
        log.FileHandler(_FILE),
        log.StreamHandler()
    ],
)


if __name__ == '__main__':
    log.debug('Mensaje debug')
    log.info('Mensaje Info')
    log.warning("Mensaje Warming")
    log.error('Mensaje error')
    log.critical('Error Critico')