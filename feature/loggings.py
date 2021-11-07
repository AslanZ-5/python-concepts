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
print('level : ' + logging.getLevelName(rootlog.getEffectiveLevel()))
rootlog.setLevel(logging.INFO) # setting new level of logging
test()


# log to file
# basicConfig only works if the logger has not been configured before
# logging.basicConfig(filename='app.txt',filemode='w',format='%(levelname)s:%(message)s',level=logging.DEBUG)
# logging.debug('hellooooo')

handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('tessssttt')
test()