# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:44:50 2020

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

if client.find(olca.Process,"C1"):
    todelete = client.get(olca.Process,client.find(olca.Process,"C1").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"C1"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"C1").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)

########################
###   Anteile        ###
########################


sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

########################
###     Units      #####
########################

from units import items_unit,item_factor,item,time,h

########################
###   BIM - Daten    ###
########################

    
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

machine_small_time = float(serv.loc[serv.loc[:,"vars"]=="abbau","werkzeug"])
bagger_time = float(serv.loc[serv.loc[:,"vars"]=="abbau","bagger"])

kran_time = float(serv.loc[serv.loc[:,"vars"]=="abbau","kran"])

leistung_kran = 67.5 *0.8* 0.5 #KW * gleichzeitigkeitsfaktor * gesamtbewegung
energie_kran = (leistung_kran * kran_time) # in kwh



########################
###     Flows      #####
########################

#Construction 
if not client.find(olca.Flow,"C1_flow"):
        
    C1_flow = olca.Flow()
    C1_flow.id = str(uuid.uuid4())
    C1_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    C1_flow.name = "C1_flow"
    C1_flow.unit = items_unit
    C1_flow.flow_properties = [item_factor]
    C1_flow.olca_type = olca.schema.Flow.__name__

    client.insert(C1_flow)

C1_flow = client.get(olca.Flow,client.find(olca.Flow,"C1_flow").id)
########################
###   Processes      ###
########################
exch = []
ID = 1


if machine_small_time > 0:
    
    machine_small_flow = client.get(olca.Flow,"4ded4b10-8c5a-41bf-9098-0194fc46b639")#machine operation, diesel, < 18.64 kW, low load factor
    machine_small_proc = client.get(olca.Process,"e4650ebb-dd11-4e9c-8b86-10dc46e80f87") # machine operation, diesel, < 18.64 kW, low load factor | machine operation, diesel, < 18.64 kW, low load factor | EN15804, U

    C1_input_machine_small = olca.Exchange()
    C1_input_machine_small.input = True
    C1_input_machine_small.flow = machine_small_flow
    C1_input_machine_small.amount = machine_small_time
    C1_input_machine_small.default_provider = machine_small_proc
    C1_input_machine_small.unit = h 
    C1_input_machine_small.flow_property = time
    C1_input_machine_small.internal_id = ID;ID=ID+1
    C1_input_machine_small.avoided_product = False
    exch.append(C1_input_machine_small)




if kran_time > 0:
    
    kran_flow = client.get(olca.Flow,"030944cf-3547-4c0a-9966-43e937518207")# machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state
    kran_proc = client.get(olca.Process,"ba7aea94-dd55-46c7-980f-da85bae19567") # machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state | machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state | Cutoff, U
    
    C1_input_kran = olca.Exchange()
    C1_input_kran.input = True
    C1_input_kran.flow = kran_flow
    C1_input_kran.amount = kran_time
    C1_input_kran.default_provider = kran_proc
    C1_input_kran.unit = h 
    C1_input_kran.flow_property = time
    C1_input_kran.internal_id = ID;ID=ID+1
    C1_input_kran.avoided_product = False
    exch.append(C1_input_kran)



if bagger_time > 0:

    bagger_flow = client.get(olca.Flow,"08fee6e0-0099-4c24-accb-6091eab79734")# machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor
    bagger_proc = client.get(olca.Process,"6c0c40f8-978f-428b-ba9e-2cf95cdfc776") # machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor | machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor | Cutoff, U

    C1_input_bagger = olca.Exchange()
    C1_input_bagger.input = True
    C1_input_bagger.flow = bagger_flow
    C1_input_bagger.amount = bagger_time
    C1_input_bagger.default_provider = bagger_proc
    C1_input_bagger.unit = h 
    C1_input_bagger.flow_property = time
    C1_input_bagger.internal_id = ID;ID=ID+1
    C1_input_bagger.avoided_product = False
    exch.append(C1_input_bagger)

if len(exch)==0:
    
    dummy_flow  = client.get(olca.Flow,client.find(olca.Flow,"dummy").id)
    
    C1_input_dummy = olca.Exchange()
    C1_input_dummy.input = True
    C1_input_dummy.flow = dummy_flow
    C1_input_dummy.amount = 1 
    C1_input_dummy.unit = items_unit
    C1_input_dummy.flow_property = item 
    C1_input_dummy.internal_id = ID;ID = ID + 1
    C1_input_dummy.avoided_product = False
    exch.append(C1_input_dummy)


C1 = olca.Process()
C1.category = client.find(olca.Category,"C1")
C1.process_type = olca.ProcessType.UNIT_PROCESS
C1.id = str(uuid.uuid4())
C1.name = "C1"
C1.olca_type = olca.schema.Process.__name__


C1_output = olca.Exchange()
C1_output.input = False
C1_output.flow = C1_flow
C1_output.flow_property = item
C1_output.unit = items_unit
C1_output.amount = 1
C1_output.quantitative_reference = True
C1_output.internal_id = ID;ID=ID+1
C1_output.avoided_product = False
exch.append(C1_output)


C1.exchanges= exch

client.insert(C1)
