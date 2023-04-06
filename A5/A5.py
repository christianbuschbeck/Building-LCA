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

if client.find(olca.Process,"A5"):
    todelete = client.get(olca.Process,client.find(olca.Process,"A5").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)

if client.find(olca.ProductSystem,"A5"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"A5").id)
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

machine_small_time = float(serv.loc[serv.loc[:,"vars"]=="aufbau","werkzeug"])

bagger_time = float(serv.loc[serv.loc[:,"vars"]=="aufbau","bagger"])

kran_time = float(serv.loc[serv.loc[:,"vars"]=="aufbau","kran"])


leistung_kran = 67.5 *0.8 * 0.5 #KW * gleichzeitigkeitsfaktor * gesamtbewegung
energie_kran = (leistung_kran * kran_time) # in kwh



########################
###     Flows      #####
########################

#Construction 
if not client.find(olca.Flow,"A5_flow"):
        
    A5_flow = olca.Flow()
    A5_flow.id = str(uuid.uuid4())
    A5_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    A5_flow.name = "A5_flow"
    A5_flow.unit = items_unit
    A5_flow.flow_properties = [item_factor]
    A5_flow.olca_type = olca.schema.Flow.__name__

    client.insert(A5_flow)

A5_flow = client.get(olca.Flow,client.find(olca.Flow,"A5_flow").id)
########################
###   Processes      ###
########################
exch = []
ID = 1



if machine_small_time > 0:
    
    machine_small_flow = client.get(olca.Flow,"4ded4b10-8c5a-41bf-9098-0194fc46b639")#machine operation, diesel, < 18.64 kW, low load factor
    machine_small_proc = client.get(olca.Process,"e4650ebb-dd11-4e9c-8b86-10dc46e80f87") # machine operation, diesel, < 18.64 kW, low load factor | machine operation, diesel, < 18.64 kW, low load factor | EN15804, U

    A5_input_machine_small = olca.Exchange()
    A5_input_machine_small.input = True
    A5_input_machine_small.flow = machine_small_flow
    A5_input_machine_small.amount = machine_small_time
    A5_input_machine_small.default_provider = machine_small_proc
    A5_input_machine_small.unit = h 
    A5_input_machine_small.flow_property = time
    A5_input_machine_small.internal_id = ID;ID=ID+1
    A5_input_machine_small.avoided_product = False
    exch.append(A5_input_machine_small)




if kran_time > 0:
    
    kran_flow = client.get(olca.Flow,"030944cf-3547-4c0a-9966-43e937518207")# machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state
    kran_proc = client.get(olca.Process,"ba7aea94-dd55-46c7-980f-da85bae19567") # machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state | machine operation, diesel, >= 18.64 kW and < 74.57 kW, steady-state | Cutoff, U
    
    A5_input_kran = olca.Exchange()
    A5_input_kran.input = True
    A5_input_kran.flow = kran_flow
    A5_input_kran.amount = kran_time
    A5_input_kran.default_provider = kran_proc
    A5_input_kran.unit = h 
    A5_input_kran.flow_property = time
    A5_input_kran.internal_id = ID;ID=ID+1
    A5_input_kran.avoided_product = False
    exch.append(A5_input_kran)


if bagger_time > 0:

    bagger_flow = client.get(olca.Flow,"08fee6e0-0099-4c24-accb-6091eab79734")# machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor
    bagger_proc = client.get(olca.Process,"6c0c40f8-978f-428b-ba9e-2cf95cdfc776") # machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor | machine operation, diesel, >= 18.64 kW and < 74.57 kW, high load factor | Cutoff, U

    A5_input_bagger = olca.Exchange()
    A5_input_bagger.input = True
    A5_input_bagger.flow = bagger_flow
    A5_input_bagger.amount = bagger_time
    A5_input_bagger.default_provider = bagger_proc
    A5_input_bagger.unit = h 
    A5_input_bagger.flow_property = time
    A5_input_bagger.internal_id = ID;ID=ID+1
    A5_input_bagger.avoided_product = False
    exch.append(A5_input_bagger)



if len(exch)==0:
    
    dummy_flow  = client.get(olca.Flow,client.find(olca.Flow,"dummy").id)
    
    A5_input_dummy = olca.Exchange()
    A5_input_dummy.input = True
    A5_input_dummy.flow = dummy_flow
    A5_input_dummy.amount = 1 
    A5_input_dummy.unit = items_unit
    A5_input_dummy.flow_property = item 
    A5_input_dummy.internal_id = ID;ID = ID + 1
    A5_input_dummy.avoided_product = False
    exch.append(A5_input_dummy)


A5 = olca.Process()
A5.category = client.find(olca.Category,"A5")
A5.process_type = olca.ProcessType.UNIT_PROCESS
A5.id = str(uuid.uuid4())
A5.name = "A5"
A5.olca_type = olca.schema.Process.__name__


A5_output = olca.Exchange()
A5_output.input = False
A5_output.flow = A5_flow
A5_output.flow_property = item
A5_output.unit = items_unit
A5_output.amount = 1
A5_output.quantitative_reference = True
A5_output.internal_id = ID;ID=ID+1
A5_output.avoided_product = False
exch.append(A5_output)


A5.exchanges= exch

client.insert(A5)
