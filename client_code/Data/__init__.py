from ._anvil_designer import DataTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Data(DataTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def drop_down_1_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    pass

    
    

    
