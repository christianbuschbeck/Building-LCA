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


if client.find(olca.Process,"B2"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B2").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"B2"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"B2").id)
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

#!!! Achtung hier wird osb als einizges als Fläche nicht Volumen behandelt 
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

osb_area =  float(comp.loc[comp.loc[:,"vars"]=="include","osb"])

huelle = osb_area

anstrichmenge_m3 = huelle * 0.003
anstrichmenge_kg = anstrichmenge_m3 * 1.1 * 1000 # Dichte = 1.1 AURO aqua holzlasur
haeufigkeit = 12
anstrichmenge_kg * haeufigkeit

########################
###     Flows      #####
########################

#schutz 
if not client.find(olca.Flow,"B2_flow"):            
    
    schutz_flow = olca.Flow()
    schutz_flow.id = str(uuid.uuid4())
    schutz_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    schutz_flow.name = "B2_flow"
    schutz_flow.description = ""
    schutz_flow.unit = items_unit
    schutz_flow.flow_properties = [item_factor]
    schutz_flow.olca_type = olca.schema.Flow.__name__

    client.insert(schutz_flow)

schutz_flow = client.get(olca.Flow,client.find(olca.Flow,"B2_flow").id)


holzschutzmittel_flow = client.get(olca.Flow,"af8b18f9-21b2-4587-8d78-870b1da8d7db") # wood preservative, organic, outdoor use, no ground contact
holzschutzmittel_process = client.get(olca.Process,"4f341013-e9f1-4d93-b4ac-a21df000c32e") # wood preservative production, organic, outdoor use, no ground contact | wood preservative, organic, outdoor use, no ground contact | EN15804, U


########################
###   Processes      ###
########################



ID = 1
exch=[]


schutz = olca.Process()
schutz.category = client.find(olca.Category,"B2")
schutz.process_type = olca.ProcessType.UNIT_PROCESS
schutz.id = str(uuid.uuid4())
schutz.name = "B2"
schutz.olca_type = olca.schema.Process.__name__

schutz_input_anstrich = olca.Exchange()
schutz_input_anstrich.input = True
schutz_input_anstrich.default_provider = holzschutzmittel_process
schutz_input_anstrich.flow = holzschutzmittel_flow
schutz_input_anstrich.flow_property = mass
schutz_input_anstrich.unit = kg
schutz_input_anstrich.amount = anstrichmenge_kg
schutz_input_anstrich.quantitative_reference = False
schutz_input_anstrich.internal_id =ID;ID = ID + 1 
schutz_input_anstrich.avoided_product = False
exch.append(schutz_input_anstrich)


schutz_output = olca.Exchange()
schutz_output.input = False
schutz_output.flow = schutz_flow
schutz_output.flow_property = item
schutz_output.unit = items_unit
schutz_output.amount = 1
schutz_output.quantitative_reference = True
schutz_output.internal_id = ID; ID = ID+1
schutz_output.avoided_product = False
exch.append(schutz_output)


schutz.exchanges= exch
client.insert(schutz)

