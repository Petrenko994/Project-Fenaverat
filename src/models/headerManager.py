# import <
from .resourceManager import resourceManager

# >


class headerManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'header', 
         loadType = 'local'
         
      )
      
      self.content = super().fetchContent()

      
   def getTitle(self): return self.content['title']
   
   
   def getImages(self): return self.content['images']