import sys

sys.path.append('/home/lxpollara/pyvpic')
sys.path.append('/home/lxpollara/Adas_Proj')
from sql_alchemy_engine import session, Base
from sqlalchemy import func
from create_db import AccidentMaster, Vehicle
import pandas as pd
from ipywidgets import widgets, HBox, VBox
from IPython.display import display, Image
import numpy as np

class DashBoard:
    def __init__(self):
        # retrieve list of vehicle makes
        query = session.query(Vehicle.make).distinct()
        self.makes= pd.read_sql(query.statement,query.session.bind)
        self.makes.sort_values('make', inplace=True)
        
        self.accidents1 = None
        
        
        # create widgets
        self.make1 = widgets.Dropdown(options=self.makes.make.values, description='Make:', disabled=False)
        
        self.model1 = widgets.Dropdown(description='Model:', disabled=False)
        
        self.year1 = widgets.Dropdown(description='Year:',disabled=False)
        
        self.run = widgets.Button(description='Run', disabled=True)
        
        
        # connect widgets to commands
        self.make1.observe(self.update_model1, "value")
        
        self.model1.observe(self.update_year1, "value")
        
        self.run.on_click(self.get_accidents)
        
        display(VBox([HBox([self.make1]),
                HBox([self.model1]),
                HBox([self.year1]),
                     HBox([self.run])]))

        
    def update_model1(self, selection):
        query = session.query(Vehicle.model).filter(Vehicle.make==selection['new']).distinct()
        models = pd.read_sql(query.statement,query.session.bind)
        models.sort_values('model', inplace=True)
        self.model1.options = models.model.values
        self.model1.selected_label = models.model.values[0]
        
    
        
    def update_year1(self, selection):
        query = session.query(Vehicle.year).filter(Vehicle.make==self.make1.value, Vehicle.model==selection['new']).distinct()
        years = pd.read_sql(query.statement,query.session.bind)
        y =years.year.values
        y.sort()
        self.year1.options = y
        self.year1.selected_label = y[0]
        self.run.disabled = False
    
        
    def get_accidents(self, message):
        self.run.disabled = True

        query = session.query(AccidentMaster.injuries, func.count(AccidentMaster.injuries)).filter(AccidentMaster.vin==Vehicle.vin,
                                                                                           Vehicle.make==self.make1.value,
                                                                                           Vehicle.model==self.model1.value,
                                                                                           Vehicle.year==int(self.year1.value),
                                                                                           AccidentMaster.vehicles_involved<=2
                                                                                          ).group_by(AccidentMaster.injuries)
        self.accidents1= pd.read_sql(query.statement, query.session.bind)

        
        self.run.disabled = False
        
        
class TimeSeriesDashBoard:
    def __init__(self):
        # retrieve list of vehicle makes
        query = session.query(Vehicle.make).distinct()
        self.makes= pd.read_sql(query.statement,query.session.bind)
        self.makes.sort_values('make', inplace=True)
        
        self.accidents1 = None
        
        # create widgets
        self.make1 = widgets.Dropdown(options=self.makes.make.values, description='Make:', disabled=False)
        self.model1 = widgets.Dropdown(description='Model:', disabled=False)
        self.year1 = widgets.Dropdown(description='Start Year:',disabled=False)
        self.year2 = widgets.Dropdown(description='End Year:',disabled=False)
        self.run = widgets.Button(description='Run', disabled=True)
        
        
        # connect widgets to commands
        self.make1.observe(self.update_model1, "value")
        self.model1.observe(self.update_year1, "value")
        self.year1.observe(self.update_year2, "value")
        self.run.on_click(self.get_accidents)
        
        display(VBox([HBox([self.make1]),
                HBox([self.model1]),
                HBox([self.year1, self.year2]),
                     HBox([self.run])]))

        
    def update_model1(self, selection):
        query = session.query(Vehicle.model).filter(Vehicle.make==selection['new']).distinct()
        models = pd.read_sql(query.statement,query.session.bind)
        models.sort_values('model', inplace=True)
        self.model1.options = models.model.values
        self.model1.selected_label = models.model.values[0]
        
    def update_year1(self, selection):
        query = session.query(Vehicle.year).filter(Vehicle.make==self.make1.value, Vehicle.model==selection['new']).distinct()
        years = pd.read_sql(query.statement,query.session.bind)
        y =years.year.values
        y.sort()
        self.year1.options = y
        self.year1.selected_label = y[0]
        
    def update_year2(self, selection):
        y = np.array([i for i in self.year1.options if i>selection['new']])
        y.sort()
        self.year2.options = y
        self.year2.selected_label = y[0]
        self.run.disabled = False
        
    def get_accidents(self, message):
        self.run.disabled = True
        query = session.query(AccidentMaster, Vehicle.year).filter(Vehicle.make==self.make1.value,
                                            Vehicle.model==self.model1.value,
                                            Vehicle.year>=int(self.year1.value),
                                            Vehicle.year<=int(self.year2.value)).filter(Vehicle.vin==AccidentMaster.vin)
        self.accidents1= pd.read_sql(query.statement, query.session.bind)

       
        self.accidents1.sort_values('report_date', inplace=True)

        self.run.disabled = False