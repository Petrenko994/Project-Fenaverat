# import <
from .resourceManager import resourceManager

# >


class myProjectsManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'myProjects',
         loadType = 'remote'
         
      )
      
      self.content = super().fetchContent()
      print(self.content) # remove