from .UserDataFrame import DataContext

def data(request): 
    
    return {'data': DataContext(request)}