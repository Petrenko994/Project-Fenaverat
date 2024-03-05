# import <
from .framework import framework

from dash import html
import dash_bootstrap_components as dbc

# >


class header(framework):
   
   def __init__(self): super().__init__()
   
   
   def component(
      
      self,
      pStyle,
      pContent,
      pUpdateRate
   
   ):
      '''  '''

      return dbc.Col(
         
         style = {
            
            'paddingTop' : '1%',
            'minWidth' : self.colWidth,
            'maxWidth' : self.colWidth,
            'backgroundColor' : '#F7F5F1'
            
         },
         children = dbc.Row(
               
            justify = 'between',
            children = [
               
               # title <
               # loader <
               dbc.Col(
                  
                  width = 'auto',                  
                  children = html.H1(
                     
                     children = pContent['title'],
                     style = {
                                                      
                        'padding' : 0,
                        'fontSize' : 85,
                        'lineHeight' : 0.9,
                        'color' : '#181A1B',
                        'margin' : '0 0 -10px 0',
                        'fontFamily' : 'Helveticamazing'
                        
                     }
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  style = {'marginTop' : -5},
                  children = [
                     
                     html.Div(
                        
                        id = 'headerTargetId',
                        style = {'padding' : '0.25%'},
                        children = dbc.Spinner(
                           
                           size = 'sm',
                           color = '#181A1B',
                           id = 'headerSpinnerId',
                           spinner_style = {
                              
                              'border-width' : 1.5,
                              'animation-play-state' : 'running'
                              
                           }
                           
                        )
                        
                     ),
                     dbc.Tooltip(
                        
                        placement = 'bottom',
                        target = 'headerTargetId',
                        children = html.P(
                           
                           children = f'Updated every {pUpdateRate} minutes',
                           style = {
                              
                              'margin' : 0,
                              'fontFamily' : 'helvetica'
                              
                           }
                        
                        )
                           
                     )
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
                     
      )