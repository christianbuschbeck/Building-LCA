# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:36:33 2020

@author: cbuschbeck
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:29:12 2020

@author: cbuschbeck
"""

import sys

home_dir = "C:/Users/cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
import pandas as pd

#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"verb_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"verb_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,mass,MJ,energy



########################
###     Amounts    #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
verb_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","verb"])



########################
###     Flows      #####
########################

if not client.find(olca.Flow,"verb_sekundaer"):
    verb_flow = olca.Flow()
    verb_flow.id = str(uuid.uuid4())
    verb_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    verb_flow.name = "verb_sekundaer"
    verb_flow.description = "verbindungen des Holzhybrides"
    verb_flow.unit = kg
    verb_flow.olca_type = olca.schema.Flow.__name__

    client.insert(verb_flow)

verb_flow = client.get(olca.Flow,client.find(olca.Flow,"verb_sekundaer").id)

SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)



########################
###     Processes  #####
########################
exch = []
ID=1

verb_input_SM = olca.Exchange()
verb_input_SM.input = True
verb_input_SM.flow = SM_flow
verb_input_SM.amount =  verb_dichte # in kg
verb_input_SM.unit = kg  
verb_input_SM.flow_property = mass
verb_input_SM.internal_id =ID;ID = ID + 1 
verb_input_SM.avoided_product = False
verb_input_SM.quantitative_reference = False
exch.append(verb_input_SM)


verb_process = olca.Process()
verb_process.category = client.find(olca.Category,"A1-A3")
verb_process.process_type = olca.ProcessType.UNIT_PROCESS
verb_process.id = str(uuid.uuid4())
verb_process.name = "verb_sekundaer"
verb_process.olca_type = olca.schema.Process.__name__


verb_output_verb = olca.Exchange()
verb_output_verb.input = False
verb_output_verb.flow = verb_flow
verb_output_verb.flow_property = mass
verb_output_verb.unit = kg
verb_output_verb.amount = 1
verb_output_verb.quantitative_reference = True
verb_output_verb.internal_id =ID;ID = ID + 1 
verb_output_verb.avoided_product = False
exch.append(verb_output_verb)



verb_process.exchanges= exch
client.insert(verb_process)
