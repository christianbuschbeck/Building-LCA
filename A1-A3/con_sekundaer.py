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

#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)


if client.find(olca.Process,"concrete_sekundaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"concrete_sekundaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import kg,mass


########################
###     Amounts    #####
########################

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, quoting = 3)
con_dichte = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"concrete_sekundaer"):
    con_flow = olca.Flow()
    con_flow.id = str(uuid.uuid4())
    con_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    con_flow.name = "concrete_sekundaer"
    con_flow.description = "conindungen des Holzhybrides"
    con_flow.unit = kg
    con_flow.olca_type = olca.schema.Flow.__name__

    client.insert(con_flow)

con_flow = client.get(olca.Flow,client.find(olca.Flow,"concrete_sekundaer").id)


SM_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") #secondary material (EN15804)

########################
###     Processes  #####
########################
exch = []
ID= 1




con_input_SM = olca.Exchange()
con_input_SM.input = True
con_input_SM.flow = SM_flow
con_input_SM.amount =  con_dichte # in kg
con_input_SM.unit = kg  
con_input_SM.flow_property = mass
con_input_SM.internal_id =ID;ID = ID + 1 
con_input_SM.avoided_product = False
con_input_SM.quantitative_reference = False
exch.append(con_input_SM)


con_process = olca.Process()
con_process.category = client.find(olca.Category,"A1-A3")
con_process.process_type = olca.ProcessType.UNIT_PROCESS
con_process.id = str(uuid.uuid4())
con_process.name = "concrete_sekundaer"
con_process.olca_type = olca.schema.Process.__name__

con_output_con = olca.Exchange()
con_output_con.input = False
con_output_con.flow = con_flow
con_output_con.flow_property = mass
con_output_con.unit = kg
con_output_con.amount = 1
con_output_con.quantitative_reference = True
con_output_con.internal_id =ID;ID = ID + 1 
con_output_con.avoided_product = False
exch.append(con_output_con)


con_process.exchanges= exch
client.insert(con_process)
