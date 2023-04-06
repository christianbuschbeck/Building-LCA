# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:33:55 2020

@author: cbuschbeck
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:44:50 2020

@author: cbuschbeck
"""

import sys
import pandas as pd
import os
import runpy
home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)

if client.find(olca.Process,"D_s_k"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_s_k").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)   
if client.find(olca.Process,"D_s_g"):
    todelete = client.get(olca.Process,client.find(olca.Process,"D_s_g").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)       
if client.find(olca.Process,"span"):
    todelete = client.get(olca.Process,client.find(olca.Process,"span").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)       


if client.find(olca.ProductSystem,"D_s_k"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"D_s_k").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
if client.find(olca.ProductSystem,"D_s_g"):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,"D_s_g").id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)



########################
###    Anteile    #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

anteile=runpy.run_module(mod_name="anteile")

lvl_sn_fac   =anteile.get("lvl_sn_fac")
bsh_sn_fac   =anteile.get("bsh_sn_fac")
timb_sn_fac   =anteile.get("timb_sn_fac")
con_sn_fac   =anteile.get("con_sn_fac")
verb_sn_fac   =anteile.get("verb_sn_fac")
glas_sn_fac   =anteile.get("glas_sn_fac")
bew_sn_fac   =anteile.get("bew_sn_fac")
gips_sn_fac   =anteile.get("gips_sn_fac")
lehm_sn_fac   =anteile.get("lehm_sn_fac")


lvl_wieder_fac   =anteile.get("lvl_wieder_fac")
bsh_wieder_fac   =anteile.get("bsh_wieder_fac")
timb_wieder_fac   =anteile.get("timb_wieder_fac")
con_wieder_fac   =anteile.get("con_wieder_fac")
verb_wieder_fac   =anteile.get("verb_wieder_fac")
glas_wieder_fac   =anteile.get("glas_wieder_fac")
bew_wieder_fac   =anteile.get("bew_wieder_fac")
lehm_wieder_fac   =anteile.get("lehm_wieder_fac")


########################
###     Units      #####
########################

from units import items_unit,item_factor,kg,item,mass,MJ,energy


########################
###     Amounts    #####
########################
    
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0,  quoting = 3)

lvl_vol = float(comp.loc[comp.loc[:,"vars"]=="include","lvl"])
lvl_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","lvl"])
lvl_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","lvl"])
lvl_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","lvl"])
lvl_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","lvl"])
lvl_kg = lvl_vol * lvl_gewicht  # vol*gewicht
lvl_sn_kg = lvl_kg * lvl_sn_fac
lvl_sn_vol = lvl_vol *lvl_sn_fac

bsh_vol = float(comp.loc[comp.loc[:,"vars"]=="include","bsh"])
bsh_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","bsh"])
bsh_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","bsh"])
bsh_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","bsh"])
bsh_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","bsh"])
bsh_kg = bsh_vol * bsh_gewicht  # vol*gewicht
bsh_sn_kg = bsh_kg * bsh_sn_fac
bsh_sn_vol = bsh_vol *bsh_sn_fac

timb_vol = float(comp.loc[comp.loc[:,"vars"]=="include","timb"])
timb_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","timb"])
timb_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","timb"])
timb_energy_inh = float(comp.loc[comp.loc[:,"vars"]=="energy_inh","timb"])
timb_holzanteil = float(comp.loc[comp.loc[:,"vars"]=="holzanteil","timb"])
timb_kg = timb_vol * timb_gewicht  # vol*gewicht
timb_sn_kg = timb_kg * timb_sn_fac
timb_sn_vol = timb_vol *timb_sn_fac


verb_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","verb"])
verb_sn_kg = verb_kg * verb_sn_fac

con_vol = float(comp.loc[comp.loc[:,"vars"]=="include","concrete"])
con_gewicht = float(comp.loc[comp.loc[:,"vars"]=="gewicht","concrete"])
con_co2_inh = float(comp.loc[comp.loc[:,"vars"]=="co2_inh","concrete"])
con_kg = con_vol * con_gewicht
con_sn_kg = con_kg * con_sn_fac

glas_qm = float(comp.loc[comp.loc[:,"vars"]=="include","glas"])
glas_gewicht =  float(comp.loc[comp.loc[:,"vars"]=="gewicht","glas"])
glas_kg = glas_qm * glas_gewicht
glas_sn_kg = glas_kg * glas_sn_fac

elev_no = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
elev_steel_kg = elev_no * 2095   # stahlinhalt aus ecoinvent

hp_no = float(comp.loc[comp.loc[:,"vars"]=="include","elev"])
hp_steel_kg = hp_no *1.6* 95   # stahlinhalt aus ecoinvent

bew_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","bew"])
bew_sn_kg = bew_kg * bew_sn_fac

pv_qm = float(comp.loc[comp.loc[:,"vars"]=="include","pv"])
pv_anteil_glas_kg = 10
pv_glas_sn_kg = pv_qm * pv_anteil_glas_kg

gips_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","gips"])
gips_sn_kg = gips_kg * gips_sn_fac

lehm_kg =  float(comp.loc[comp.loc[:,"vars"]=="include","lehm"])
lehm_sn_kg = lehm_kg * lehm_sn_fac


########################
##  Nettoflüsse      ###
########################

#Sekundär- oder brennstoffe: Holz ...
 
input_woodchips = 0 

#market for steel, low-alloyed | steel, low-alloyed | Cutoff, U    global : 
#stahl_scrap_anteil = 0.292204827206589* 1.105+ 0.00235961606207298 * 1.120889101 + 0.114832174510546 * 1.105 + 0.0234606540385759* 0.0956 + 0.0378979796007765* 0.15598 + 0.441139881564897 * 0.12501 + 0.0881048670165426* 0.12501
#edelstahl_scrap_anteil= 0.0716286008018808*0.52029 + 0.204305005873532 *0.52029 # ecoinvent market for chromium steel 18/8            < - >  #edelstahl_scrap_anteil = 0.637 #0.9212 # Ökbdt | EPD IBU : 0.637
edelstahl_scrap_anteil = 0.52029 *0.9212 

input_edelstahl_scrap = ((1-verb_wieder_fac)*verb_kg + (1-bew_wieder_fac)*bew_kg + elev_steel_kg + hp_steel_kg) * edelstahl_scrap_anteil
input_concrete = 0
input_glas = 0
input_gips = 0
input_lehm = 0

output_woodchips = lvl_sn_kg + bsh_sn_kg + timb_sn_kg
output_edelstahl_scrap = verb_sn_kg + hp_steel_kg + elev_steel_kg
output_concrete = con_sn_kg
output_glas = glas_sn_kg + pv_glas_sn_kg
output_stahl_scrap = bew_kg
output_gips = gips_sn_kg
output_lehm = lehm_sn_kg


netto_woodchips = output_woodchips- input_woodchips 
netto_edelstahl_scrap = output_edelstahl_scrap - input_edelstahl_scrap
netto_concrete = output_concrete - input_concrete
netto_glas = output_glas - input_glas
netto_gips = output_gips - input_gips
netto_lehm = output_lehm - input_lehm

## Was substituiert was ?!

span_amount = netto_woodchips
edelstahl_amount = netto_edelstahl_scrap / 0.52029 # #Der output von Schrott wird über Sekundärstahl abgewickelt. Hier ist der scrap als burden free einbezogen
gravel_amount = netto_concrete
glascullet_amount = netto_glas
recycle_gips_amount = netto_gips
recycle_lehm_amount = netto_lehm

########################
###     Flows      #####
########################

#Gutschrift/Kosten 
        
if not client.find(olca.Flow,"gk"):     
    gk_flow = olca.Flow()
    gk_flow.id = str(uuid.uuid4())
    gk_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    gk_flow.name = "gk"
    gk_flow.description = ""
    gk_flow.unit = items_unit
    gk_flow.flow_properties = [item_factor]
    gk_flow.olca_type = olca.schema.Flow.__name__
        
    client.insert(gk_flow)

gk_flow = client.get(olca.Flow,client.find(olca.Flow,"gk").id)

carbonin_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_in").id)
carbonout_flow = client.get(olca.Flow,client.find(olca.Flow,"Co2_Materialinhärent_out").id)

energyin_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_in").id)
energyout_flow = client.get(olca.Flow,client.find(olca.Flow,"Energie_Materialinhärent_out").id)


#######################
##### GK Prozesse    ###
#######################

kosten = olca.Process()
kosten.category = client.find(olca.Category,"D")
kosten.process_type = olca.ProcessType.UNIT_PROCESS
kosten.id = str(uuid.uuid4())
kosten.name = "D_s_k"
kosten.olca_type = olca.schema.Process.__name__

gutschrift = olca.Process()
gutschrift.category = client.find(olca.Category,"D")
gutschrift.process_type = olca.ProcessType.UNIT_PROCESS
gutschrift.id = str(uuid.uuid4())
gutschrift.name = "D_s_g"
gutschrift.olca_type = olca.schema.Process.__name__



########################
## Kosten             ##
########################
exch_k =  []
ID = 1

if edelstahl_amount  > 0:

    secondarysteel_flow = client.get(olca.Flow,"c33b5236-001e-49b5-aa3d-810c0214f9ce") #steel, chromium steel 18/8
    secondarysteel_process = client.get(olca.Process,"31676eda-d200-4b28-bdd1-de4f7f8113b7") # steel production, electric, chromium steel 18/8 | steel, chromium steel 18/8 | EN15804, U
    
    kosten_input_secondarysteel = olca.Exchange()
    kosten_input_secondarysteel.input = True
    kosten_input_secondarysteel.flow = secondarysteel_flow
    kosten_input_secondarysteel.amount = edelstahl_amount 
    kosten_input_secondarysteel.unit = kg
    kosten_input_secondarysteel.flow_property = mass
    kosten_input_secondarysteel.internal_id = ID; ID = ID + 1
    kosten_input_secondarysteel.default_provider= secondarysteel_process
    kosten_input_secondarysteel.avoided_product = False
    kosten_input_secondarysteel.quantitative_reference = False
    exch_k.append(kosten_input_secondarysteel)


if recycle_gips_amount  > 0:

    recycle_gips_flow = client.get(olca.Flow,"4058ca6d-92c0-4ce5-bdc9-a3a96eeade93") #waste gypsum plasterboard
    recycle_gips_process = client.get(olca.Process,"dee13fcd-9a55-40c7-bb71-fd13a064555a") # treatment of waste gypsum plasterboard, recycling | waste gypsum plasterboard | EN15804, U
    
    kosten_input_recycle_gips = olca.Exchange()
    kosten_input_recycle_gips.input = True
    kosten_input_recycle_gips.flow = recycle_gips_flow
    kosten_input_recycle_gips.amount = recycle_gips_amount
    kosten_input_recycle_gips.unit = kg
    kosten_input_recycle_gips.flow_property = mass
    kosten_input_recycle_gips.internal_id = ID; ID = ID + 1
    kosten_input_recycle_gips.default_provider= recycle_gips_process
    kosten_input_recycle_gips.avoided_product = False
    kosten_input_recycle_gips.quantitative_reference = False
    exch_k.append(kosten_input_recycle_gips)

########################
## Substituierte      ##
########################
exch_g= []


if span_amount > 0:
    
    span_flow = client.get(olca.Flow,"7fe99768-d571-4bc2-a272-7df585bd0d48") # wood chips, wet, measured as dry mass
    span_process = client.get(olca.Process,"c9643490-7fe9-42c0-870d-b0f78dbebf87")# wood chips production, softwood, at sawmill | wood chips, wet, measured as dry mass | EN15804, U
    
    gutschrift_input_span = olca.Exchange()
    gutschrift_input_span.input = True
    gutschrift_input_span.flow = span_flow
    gutschrift_input_span.amount = span_amount
    gutschrift_input_span.unit = kg  
    gutschrift_input_span.flow_property = mass
    gutschrift_input_span.default_provider = span_process
    gutschrift_input_span.internal_id = ID; ID = ID + 1
    gutschrift_input_span.avoided_product = False
    gutschrift_input_span.quantitative_reference = False
    exch_g.append(gutschrift_input_span)


if edelstahl_amount  > 0:

    edelstahl_flow = client.get(olca.Flow,"c33b5236-001e-49b5-aa3d-810c0214f9ce") # steel, chromium steel 18/8
    edelstahl_process = client.get(olca.Process,"192c5ce4-1742-4106-861a-20d466037af7") # market for steel, chromium steel 18/8 | steel, chromium steel 18/8 | EN15804, U
  

    gutschrift_input_stahl = olca.Exchange()
    gutschrift_input_stahl.input = True
    gutschrift_input_stahl.flow = edelstahl_flow
    gutschrift_input_stahl.amount = edelstahl_amount 
    gutschrift_input_stahl.unit = kg  
    gutschrift_input_stahl.flow_property = mass
    gutschrift_input_stahl.default_provider = edelstahl_process
    gutschrift_input_stahl.internal_id = ID; ID = ID + 1
    gutschrift_input_stahl.avoided_product = False
    gutschrift_input_stahl.quantitative_reference = False
    exch_g.append(gutschrift_input_stahl)


if gravel_amount > 0:
    
    gravel_flow = client.get(olca.Flow,"37eceabd-b33f-4757-a4b9-5c51dee1710d") # gravel, crushed
    gravel_process = client.get(olca.Process,"2eb51892-ec6a-471a-b09a-5bdbb13ce008") # gravel production, crushed | gravel, crushed | EN15804, U

    gutschrift_input_gravel = olca.Exchange()
    gutschrift_input_gravel.input = True
    gutschrift_input_gravel.flow = gravel_flow
    gutschrift_input_gravel.amount = gravel_amount
    gutschrift_input_gravel.unit = kg  
    gutschrift_input_gravel.flow_property = mass
    gutschrift_input_gravel.default_provider = gravel_process
    gutschrift_input_gravel.internal_id =ID; ID = ID + 1
    gutschrift_input_gravel.avoided_product = False
    gutschrift_input_gravel.quantitative_reference = False
    exch_g.append(gutschrift_input_gravel)

if glascullet_amount > 0:
    
    glascullet_flow = client.get(olca.Flow,"0a6c7524-9e23-41b8-ac7b-b0489ed4681c") # glass cullet, sorted
    glascullet_process = client.get(olca.Process,"e9421090-87c3-495d-87a5-5954dd91b658") # treatment of waste glass from unsorted public collection, sorting | glass cullet, sorted | EN15804, U

    gutschrift_input_glascullet = olca.Exchange()
    gutschrift_input_glascullet.input = True
    gutschrift_input_glascullet.flow = glascullet_flow
    gutschrift_input_glascullet.amount = glascullet_amount
    gutschrift_input_glascullet.unit = kg  
    gutschrift_input_glascullet.flow_property = mass
    gutschrift_input_glascullet.default_provider = glascullet_process
    gutschrift_input_glascullet.internal_id = ID; ID = ID + 1
    gutschrift_input_glascullet.avoided_product = False
    gutschrift_input_glascullet.quantitative_reference = False
    exch_g.append(gutschrift_input_glascullet)


if recycle_gips_amount  > 0:

    stucco_flow = client.get(olca.Flow,"a437eaa8-7560-4075-a24d-dd8534517845") #stucco
    stucco_process = client.get(olca.Process,"06937f7d-dc6e-4b84-9aa7-09a1fb932bd0") # market for stucco | stucco | EN15804, U
    
    gutschrift_input_stucco = olca.Exchange()
    gutschrift_input_stucco.input = True
    gutschrift_input_stucco.flow = stucco_flow
    gutschrift_input_stucco.amount = recycle_gips_amount
    gutschrift_input_stucco.unit = kg
    gutschrift_input_stucco.flow_property = mass
    gutschrift_input_stucco.internal_id = ID; ID = ID + 1
    gutschrift_input_stucco.default_provider= stucco_process
    gutschrift_input_stucco.avoided_product = False
    gutschrift_input_stucco.quantitative_reference = False
    exch_g.append(gutschrift_input_stucco)

if recycle_lehm_amount  > 0:

    lehm_flow = client.get(olca.Flow,"e89b4064-afcc-4f08-9481-651b7eaa90a1") #clay
    lehm_process = client.get(olca.Process,"0eb789ee-cf05-4340-a3a1-ffbb5227e4e3") # clay pit operation | clay | EN15804, U
    
    gutschrift_input_lehm = olca.Exchange()
    gutschrift_input_lehm.input = True
    gutschrift_input_lehm.flow = lehm_flow
    gutschrift_input_lehm.amount = recycle_lehm_amount
    gutschrift_input_lehm.unit = kg
    gutschrift_input_lehm.flow_property = mass
    gutschrift_input_lehm.internal_id = ID; ID = ID + 1
    gutschrift_input_lehm.default_provider= lehm_process
    gutschrift_input_lehm.avoided_product = False
    gutschrift_input_lehm.quantitative_reference = False
    exch_g.append(gutschrift_input_lehm)


###############
## Inhärent  ##
###############

# kosten

kosten_input_carbon = olca.Exchange()
kosten_input_carbon.input = True
kosten_input_carbon.flow = carbonin_flow
kosten_input_carbon.amount =  lvl_sn_vol * lvl_co2_inh + bsh_sn_vol * bsh_co2_inh + timb_sn_vol * timb_co2_inh  # in kg
kosten_input_carbon.unit = kg  
kosten_input_carbon.flow_property = mass
kosten_input_carbon.internal_id = ID; ID = ID + 1
kosten_input_carbon.avoided_product = False
kosten_input_carbon.quantitative_reference = False
exch_k.append(kosten_input_carbon)

sm_flow = client.get(olca.Flow,"e16068c8-8a94-45a3-9cf0-42bb89599274") 

kosten_input_sm = olca.Exchange()
kosten_input_sm.input = True
kosten_input_sm.flow = sm_flow
kosten_input_sm.amount =  lvl_sn_kg + bsh_sn_kg + timb_sn_kg + verb_sn_kg + con_sn_kg# in kg
kosten_input_sm.unit = kg  
kosten_input_sm.flow_property = mass
kosten_input_sm.internal_id = ID; ID = ID + 1
kosten_input_sm.avoided_product = False
kosten_input_sm.quantitative_reference = False
exch_k.append(kosten_input_sm)

kosten_input_energy = olca.Exchange()
kosten_input_energy.input = True
kosten_input_energy.flow = energyin_flow
kosten_input_energy.amount = lvl_sn_vol * lvl_energy_inh +  bsh_sn_vol * bsh_energy_inh +  timb_sn_vol * timb_energy_inh  # in kg
kosten_input_energy.unit = MJ  
kosten_input_energy.flow_property = energy
kosten_input_energy.internal_id = ID; ID = ID + 1
kosten_input_energy.avoided_product = False
kosten_input_energy.quantitative_reference = False
exch_k.append(kosten_input_energy)


kosten_output_carbon = olca.Exchange()
kosten_output_carbon.input = False
kosten_output_carbon.flow = carbonout_flow
kosten_output_carbon.amount = lvl_sn_vol * lvl_co2_inh + bsh_sn_vol * bsh_co2_inh + timb_sn_vol * timb_co2_inh  # in kg
kosten_output_carbon.unit = kg  
kosten_output_carbon.flow_property = mass
kosten_output_carbon.internal_id =ID; ID = ID + 1
kosten_output_carbon.avoided_product = False
kosten_output_carbon.quantitative_reference = False
exch_k.append(kosten_output_carbon)


kosten_output_energy = olca.Exchange()
kosten_output_energy.input = False
kosten_output_energy.flow = energyout_flow
kosten_output_energy.amount = lvl_sn_vol * lvl_energy_inh + bsh_sn_vol * bsh_energy_inh + timb_sn_vol * timb_energy_inh   # in kg
kosten_output_energy.unit = MJ  
kosten_output_energy.flow_property = energy
kosten_output_energy.internal_id = ID; ID = ID + 1
kosten_output_energy.avoided_product = False
kosten_output_energy.quantitative_reference = False
exch_k.append(kosten_output_energy)


# gutschrift 


gutschrift_input_carbon = olca.Exchange()
gutschrift_input_carbon.input = True
gutschrift_input_carbon.flow = carbonin_flow
gutschrift_input_carbon.amount =  lvl_sn_vol * lvl_co2_inh + bsh_sn_vol * bsh_co2_inh + timb_sn_vol * timb_co2_inh  # in kg
gutschrift_input_carbon.unit = kg  
gutschrift_input_carbon.flow_property = mass
gutschrift_input_carbon.internal_id = ID; ID = ID + 1
gutschrift_input_carbon.avoided_product = False
gutschrift_input_carbon.quantitative_reference = False
exch_g.append(gutschrift_input_carbon)


gutschrift_input_energy = olca.Exchange()
gutschrift_input_energy.input = True
gutschrift_input_energy.flow = energyin_flow
gutschrift_input_energy.amount = lvl_sn_vol * lvl_energy_inh +  bsh_sn_vol * bsh_energy_inh +  timb_sn_vol * timb_energy_inh   # in kg
gutschrift_input_energy.unit = MJ  
gutschrift_input_energy.flow_property = energy
gutschrift_input_energy.internal_id = ID; ID = ID + 1
gutschrift_input_energy.avoided_product = False
gutschrift_input_energy.quantitative_reference = False
exch_g.append(gutschrift_input_energy)

gutschrift_output_carbon = olca.Exchange()
gutschrift_output_carbon.input = False
gutschrift_output_carbon.flow = carbonout_flow
gutschrift_output_carbon.amount = lvl_sn_vol * lvl_co2_inh + bsh_sn_vol * bsh_co2_inh + timb_sn_vol * timb_co2_inh   # in kg
gutschrift_output_carbon.unit = kg  
gutschrift_output_carbon.flow_property = mass
gutschrift_output_carbon.internal_id =ID; ID = ID + 1
gutschrift_output_carbon.avoided_product = False
gutschrift_output_carbon.quantitative_reference = False
exch_g.append(gutschrift_output_carbon)


gutschrift_output_energy = olca.Exchange()
gutschrift_output_energy.input = False
gutschrift_output_energy.flow = energyout_flow
gutschrift_output_energy.amount = lvl_sn_vol * lvl_energy_inh + bsh_sn_vol * bsh_energy_inh + timb_sn_vol * timb_energy_inh    # in kg
gutschrift_output_energy.unit = MJ  
gutschrift_output_energy.flow_property = energy
gutschrift_output_energy.internal_id = ID; ID = ID + 1
gutschrift_output_energy.avoided_product = False
gutschrift_output_energy.quantitative_reference = False
exch_g.append(gutschrift_output_energy)





###############
## Exchanges ##
###############

gutschrift_kosten_output = olca.Exchange()
gutschrift_kosten_output.input = False
gutschrift_kosten_output.flow = gk_flow
gutschrift_kosten_output.flow_property = item
gutschrift_kosten_output.unit = items_unit
gutschrift_kosten_output.amount = 1
gutschrift_kosten_output.quantitative_reference = True
gutschrift_kosten_output.internal_id = ID; ID = ID + 1
gutschrift_kosten_output.avoided_product = False
exch_k.append(gutschrift_kosten_output)
exch_g.append(gutschrift_kosten_output)


kosten.exchanges= exch_k
gutschrift.exchanges= exch_g


client.insert(kosten)
client.insert(gutschrift)

