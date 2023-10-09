import logging
import logging_2

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

# Stream handler

logger.addHandler(file_handler)

def add(x,y):
    return x+y

res = add(2,3)
logger.debug(f'Add 2,3: {res}')

 
summary = {
    "collections_added":5,
    "total_items_addedd":6
}
import  datetime

d = datetime.datetime.today()
print(d)

logger.info(summary)