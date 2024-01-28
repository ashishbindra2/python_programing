import logging
logging.basicConfig(filename="exception_zero.log",format = '%(asctime)s %(levelname)s',filemode='w')
logging.info('New Request Come')
try:
    x=int(input("enter x "))
    y=int(input("enter y "))
    print(x/y)
except ZeroDivisionError as msg:
    print(msg)
    logging.exception(msg)
except TypeError as msg:
    print("vslur id in tring")
    logging.exception(msg)
except ValueError as msg:
    print("please enter in interge or float")
    
    logging.exception(msg)
logging.info('Request Complete!!')