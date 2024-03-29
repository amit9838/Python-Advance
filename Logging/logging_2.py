import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# Stream handler

def sub(x,y):
    return x-y

res = sub(2,3)
logger.debug(f'Sub 2-3: {res}')

def div(a,b):
    try:
        return a/b 
    except ZeroDivisionError as e:
        logger.exception('Tried division by zero')

    except Exception as e:
        logger.warning("division failed!")

div(1,0)