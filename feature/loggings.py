import logging

def test():
    print('-'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel()) # current level
    print(f'log level: {level}')
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-'*20)


rootlog = logging.getLogger()
rootlog.setLevel(logging.INFO) # setting new level of logging
test()