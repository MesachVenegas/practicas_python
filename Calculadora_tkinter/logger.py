import logging as log
import os

if not os.path.exists('log/'):
    os.mkdir('log/')

_FILE = 'log/cal_log.log'

log.basicConfig(
    level=log.WARNING,
    format= "%(asctime)s: %(levelname)s [%(filename)s] <%(funcName)s>: %(message)s",
    datefmt='%I:%M:%S-%p',
    handlers= [
        log.FileHandler(_FILE),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('Test Message debug')
    log.info('Test Message info')
    log.warning('Test Message warming')
    log.error('Test Message error')
