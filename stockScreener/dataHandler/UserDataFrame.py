from django.conf import settings
from main import main 



class DataContext:
    
    
    def __init__(self, request):
        
        self.session = request.session
        Data = self.session.get('data_cookie')
        if 'data_cookie' not in request.session:
            Data = self.session['data_cookie'] = {}
        self.data = Data
        
        
    def populateDataContext(self):
        
        dataToAdd = main()
        dataToAdd = dataToAdd.to_dict()
        
        
        self.data['fields'] = dataToAdd
        
        self.save()
        
    def __iter__(self):
        
        row = {}
        
        #fix
        
        for key in self.data['fields']:
            row[key] = self.data['fields'].values()
            yield row
        
            
            
                
    
    def save(self):
        self.session.modified = True
        
    def clearSession(self):
        
        del self.session['data_cookie']
        self.save()
        
        