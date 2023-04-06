# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:29:52 2020

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



if client.find(olca.Process,"B6_wohn"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B6_wohn").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)
    
if client.find(olca.Process,"B6_park"):
    todelete = client.get(olca.Process,client.find(olca.Process,"B6_park").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)


########################
###     Units      #####
########################

sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import MJ,energy,item_factor,items_unit,item,kwh


#############################
###    Daten              ###
#############################
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

pv_qm = float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
pv_strom_erzeugt_einjahr = 18243

#hp_number = float(comp.loc[comp.loc[:,"vars"]=="include","hp"])
#hp_leistung = float(comp.loc[comp.loc[:,"vars"]=="leistung","hp"])
#hp_waerme_erzeugt_einjahr = 324000
#hp_strom_fac = 0.33 # https://www.energie-experten.org/heizung/waermepumpe/leistung/stromverbrauch

strom_year = float(serv.loc[serv.loc[:,"vars"]=="include","strom"])
#############################
###   Energiesimulation   ###
#############################


#!!! Muss noch skaliert werden !!

heizwaermebedarf = 45056 # kwh / a
lueftung = 52 + 600 + 3.154  + 36 # kwh / a 

importierter_strom_w = heizwaermebedarf + lueftung - pv_strom_erzeugt_einjahr


exportierter_strom_w=0
if(importierter_strom_w<0):
    exportierter_strom_w = abs(importierter_strom_w)
    importierter_strom_w = 0 

importierter_strom_w = importierter_strom_w * strom_year
exportierter_strom_w = exportierter_strom_w * 0.95 * 3.6 * strom_year # in MJ



############################
###   Aufzug  - Daten    ###
#############################
# https://www.heinze.de/ausschreibungstext/elektrischer-kettenaufzug-fuer-pkw-transport-typ-pegasos/40549200/

l = 60 # [kw]
h = 9 # [m]
t = 20 #[s]
t = 20 / (60 * 60) #[h]
e1 = t*l #[kwh]

I = 134 
U = 220
e2 = U*I*t #[wh]
e2 = e2/(1000) #[kwh]

fahrtenzahl = 85000 #[pro jahr]

e3 = 0.013 * 2 # aus ökobaudat

strom_aufzug_einjahr = (e2 * fahrtenzahl) + 1200  # fahrten + standby , standby daten aus ökobaudat

importierter_strom_p = strom_aufzug_einjahr - pv_strom_erzeugt_einjahr
exportierter_strom_p = 0
if(importierter_strom_p<0):
    exportierter_strom_p = abs(importierter_strom_p)
    importierter_strom_p = 0 


importierter_strom_p = importierter_strom_p * strom_year
exportierter_strom_p =exportierter_strom_p * 0.95 *3.6 * strom_year # in MJ 

serv.loc[serv.loc[:,"vars"]=="ee","strom"] = exportierter_strom_p + exportierter_strom_w
serv.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv",index=False,sep=";")



########################
###     Flows      #####
########################

#Construction 
        
if not client.find(olca.Flow,"B6_flow"):    

    ev_flow = olca.Flow()
    ev_flow.id = str(uuid.uuid4())
    ev_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    ev_flow.name = "B6_flow"
    ev_flow.description = "An awesome new building"
    ev_flow.unit = items_unit
    ev_flow.flow_properties = [item_factor]
    
    client.insert(ev_flow)
ev_flow = client.get(olca.Flow,client.find(olca.Flow,"B6_flow").id)




########################
###   Processes      ###
########################
exch_p=[]
exch_w=[]
ID =1


heizen_flow = client.get(olca.Flow,client.find(olca.Flow,"heat, district or industrial, other than natural gas").id)
heizen_process = client.get(olca.Process,"d5838ad8-be06-3995-b8ea-05d70eea4263")

strom_flow =  client.get(olca.Flow,client.find(olca.Flow,"electricity, high voltage").id)
strom_process = client.get(olca.Process,"2038b03e-2ac4-3196-87b3-af1234412395") #market for electricity, medium voltage | electricity, medium voltage | Cutoff, U 

EEE_flow =  client.get(olca.Flow,"a7f36cfc-1e9b-43f7-9ecf-b48278771f82") #exported energy, electrical

#gilt für wohn und park:
ev_output = olca.Exchange()
ev_output.input = False
ev_output.flow = ev_flow
ev_output.flow_property = item
ev_output.unit = items_unit
ev_output.amount = 1
ev_output.quantitative_reference = True
ev_output.internal_id = ID; ID = ID + 1
ev_output.avoided_product = False
exch_p.append(ev_output)
exch_w.append(ev_output)

#PARK
ev_park_input_strom = olca.Exchange()
ev_park_input_strom.input = True
ev_park_input_strom.flow = strom_flow
ev_park_input_strom.amount = importierter_strom_p 
ev_park_input_strom.default_provider = strom_process
ev_park_input_strom.unit = kwh 
ev_park_input_strom.flow_property = energy
ev_park_input_strom.internal_id = ID; ID = ID + 1
ev_park_input_strom.avoided_product = False
exch_p.append(ev_park_input_strom)


ev_park = olca.Process()
ev_park.category = client.find(olca.Category,"B6")
ev_park.process_type = olca.ProcessType.UNIT_PROCESS
ev_park.id = str(uuid.uuid4())
ev_park.name = "B6_park"
ev_park.olca_type = olca.schema.Process.__name__

ev_park_output_strom = olca.Exchange()
ev_park_output_strom.input = False
ev_park_output_strom.flow = EEE_flow
ev_park_output_strom.amount = exportierter_strom_p 
ev_park_output_strom.unit = MJ
ev_park_output_strom.flow_property = energy
ev_park_output_strom.internal_id = ID; ID = ID + 1
ev_park_output_strom.avoided_product = False
exch_p.append(ev_park_output_strom)



ev_park.exchanges= exch_p
client.insert(ev_park)


#WOHN


ev_wohn_input_strom = olca.Exchange()
ev_wohn_input_strom.input = True
ev_wohn_input_strom.flow = strom_flow
ev_wohn_input_strom.amount = importierter_strom_w 
ev_wohn_input_strom.default_provider = strom_process
ev_wohn_input_strom.unit = kwh 
ev_wohn_input_strom.flow_property = energy
ev_wohn_input_strom.internal_id = ID; ID = ID + 1
ev_wohn_input_strom.avoided_product = False
exch_w.append(ev_wohn_input_strom)

ev_wohn_output_strom = olca.Exchange()
ev_wohn_output_strom.input = False
ev_wohn_output_strom.flow = EEE_flow
ev_wohn_output_strom.amount = exportierter_strom_p  
ev_wohn_output_strom.unit = MJ 
ev_wohn_output_strom.flow_property = energy
ev_wohn_output_strom.internal_id = ID; ID = ID + 1
ev_wohn_output_strom.avoided_product = False
exch_w.append(ev_wohn_output_strom)



ev_wohn = olca.Process()
ev_wohn.category = client.find(olca.Category,"B6")
ev_wohn.process_type = olca.ProcessType.UNIT_PROCESS
ev_wohn.id = str(uuid.uuid4())
ev_wohn.name = "B6_wohn"
ev_wohn.olca_type = olca.schema.Process.__name__

ev_wohn.exchanges= exch_w
client.insert(ev_wohn)






