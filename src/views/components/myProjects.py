# import <
from ..body import body

from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class myProjects(body):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         children = None,
         id = 'myProjectsRowId'
         
      )