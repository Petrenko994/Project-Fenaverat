# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.footer import footer
from ..models.footerManager import footerManager

# >


class footerCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.footer = footer()
      self.footerManager = footerManager()
      
   
   def register(self):
      '''  '''
      
      self.callbackConnections()
      
      return self.footer.property
   
   
   def callbackConnections(self):
      '''  '''
      
      @app.callback(
         
         inputs = [Input('footerColId', 'children')],
         output = Output('footerConnectionsRowId', 'children')
         
      )
      def func(*args):

         connections = self.footerManager.getConnections()
         return self.footer.buildConnections(connections)