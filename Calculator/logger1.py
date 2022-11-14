from datetime import datetime
from genericpath import exists

SEP = ' '
TAB = 8
LOG_FILE = 'calculator.log'


def logger(n1, op, res,  n2=''):
    global TAB
    global SEP
    dt_format = "%D"+SEP + '-' + SEP+"%H:%M:%S"
    if n2 !='':
        t = datetime.now().strftime(dt_format) + SEP*TAB + \
            str(n1) + SEP + op + SEP + str(n2) + SEP + '=' + SEP + str(res)
    else:
        t = datetime.now().strftime(dt_format) + SEP*TAB + \
            str(n1) + SEP + op + SEP + '=' + SEP + str(res)
    write_log('\n'+t)
    # print("\n"+t)
    pass


def write_log(l: str):
    if exists(LOG_FILE):
        with open(LOG_FILE, 'a', encoding='utf-8') as lf:
            lf.write(l)
    else:
        with open(LOG_FILE, 'w', encoding='utf-8') as lf:
            lf.write(l)

# logger(9, 'sqrt', 3)

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)
