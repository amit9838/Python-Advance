import logging
logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s : %(message)s" 
    )

add_res = sum([1,4])
logging.warning(f'Add [1,4] -> {add_res}')

resss = sum([3,4])
logging.debug(f'Add [1,4] -> {resss}')


 