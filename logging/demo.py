import inspect
def get_info():
    # print(inspect.stack()[0])
    # print(inspect.stack()[1])
    print("caller Module Name",inspect.stack()[1][1])    
    print("caller Function Name",inspect.stack()[1][3])    
get_info()