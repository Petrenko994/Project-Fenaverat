# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.myServers import myServers
from ..controllers.bodyCallback import bodyCallback
from ..models.myServersManager import myServersManager

# >


class myServersCallback(bodyCallback):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
      
      self.id = 'myServers'
      self.title = 'my servers'
      
      self.myServers = myServers()
      self.myServersManager = myServersManager()
   
   
   def getProperty(self): return self.myServers.property
   
   
   def registerCallbacks(self):
      '''  '''
      
      self.callbackRow()
   
   
   def callbackRow(self):
      '''  ''' 
      
      @app.callback(
         
         inputs = [Input('myServersDivId', 'children')],
         output = Output('myServersStackId', 'children')
         
      )
      def func(*args):

         return [

            self.myServers.buildMyServerCard(
               
               name = name,
               properties = properties,
               iconOS = self.myServersManager.getIconOS(properties['os']),
               iconHost = self.myServersManager.getIconHost(properties['host'])
               
            )
            
         for name, properties in self.myServersManager.getServers().items()]