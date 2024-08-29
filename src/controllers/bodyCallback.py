# import <
from time import sleep
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.body import body
from ..models.bodyManager import bodyManager

# >


class bodyCallback:
   
   
   def __init__(
      
      self, 
      components = None
   
   ):
      '''  '''
      
      self.body = body()
      self.sleepDuration = 1
      self.activeItem = 'myServers'
      self.components = components
      self.bodyManager = bodyManager()
      self.accordionItems = {
         
         '/' : 'aboutMe',
         '/aboutMe' : 'aboutMe',
         '/myServers' : 'myServers',
         '/myProjects' : 'myProjects'
         
      }
   
   
   def getProperty(self): return self.body.property
   
   
   def registerCallbacks(self):
      '''  '''
                  
      self.callbackAccordion()
      self.callbackActiveItem()
      [c.registerCallbacks() for c in self.components]
               
   
   def callbackActiveItem(self):
      '''  '''
      
      @app.callback(
         
         output = Output('bodyAccordionId', 'active_item'),
         inputs = [Input('layoutLocation', 'pathname')]
         
      )
      def func(pathname): 

         try:
            
            sleep(self.sleepDuration)
            return self.accordionItems[pathname]
         
         except: return self.accordionItems['/']
                  
   
   def callbackAccordion(self):
      '''  '''

      @app.callback(
         
         inputs = [Input('bodyDivId', 'children')],
         output = Output('bodyAccordionId', 'children')
         
      )
      def func(*args): return self.body.buildAccordion(self.components)