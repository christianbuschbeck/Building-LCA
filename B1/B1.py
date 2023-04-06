# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:44:21 2020

@author: cbuschbeck
"""

import sys
import pandas as pd

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"B1"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B1").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"B1"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"B1").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
    
########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
from units import mass,kg,items_unit,item_factor,item


########################
###     Amounts    #####
########################
    
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
con_vol =  float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])

carbonatisiert = con_vol * 10  


########################
###     Flows      #####
########################

#nutz 
if not client.find(olca.Flow,"B1_flow"):            
    
    nutz_flow = olca.Flow()
    nutz_flow.id = str(uuid.uuid4())
    nutz_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    nutz_flow.name = "B1_flow"
    nutz_flow.description = ""
    nutz_flow.unit = items_unit
    nutz_flow.flow_properties = [item_factor]
    nutz_flow.olca_type = olca.schema.Flow.__name__

    client.insert(nutz_flow)

nutz_flow = client.get(olca.Flow,client.find(olca.Flow,"B1_flow").id)


########################
###   Processes      ###
########################

GWP_flow = client.get(olca.Flow,"7ae371aa-8532-11e0-9d78-0800200c9a66") # Carbon dioxide


ID = 1
exch=[]


nutz = olca.Process()
nutz.category = client.find(olca.Category,"B1")
nutz.process_type = olca.ProcessType.UNIT_PROCESS
nutz.id = str(uuid.uuid4())
nutz.name = "B1"
nutz.olca_type = olca.schema.Process.__name__

nutz_input_carbon = olca.Exchange()
nutz_input_carbon.input = True
nutz_input_carbon.flow = GWP_flow
nutz_input_carbon.flow_property = mass
nutz_input_carbon.unit = kg
nutz_input_carbon.amount = -carbonatisiert
nutz_input_carbon.quantitative_reference = False
nutz_input_carbon.internal_id =ID;ID = ID + 1 
nutz_input_carbon.avoided_product = False
exch.append(nutz_input_carbon)


nutz_output = olca.Exchange()
nutz_output.input = False
nutz_output.flow = nutz_flow
nutz_output.flow_property = item
nutz_output.unit = items_unit
nutz_output.amount = 1
nutz_output.quantitative_reference = True
nutz_output.internal_id = ID; ID = ID+1
nutz_output.avoided_product = False
exch.append(nutz_output)


nutz.exchanges= exch
client.insert(nutz)

