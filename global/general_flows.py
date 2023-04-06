# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:38:26 2020

@author: cbuschbeck
"""



import sys

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
import uuid
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)



sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import mass_factor,kg,MJ,energy_factor,items_unit,item_factor,item


carbonin_flow = olca.Flow()
carbonin_flow.id = str(uuid.uuid4())
carbonin_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
carbonin_flow.name = "Co2_Materialinhärent_in"
carbonin_flow.description = "bla"
carbonin_flow.unit = kg
carbonin_flow.flow_properties = [mass_factor]
carbonin_flow.olca_type = olca.schema.Flow.__name__


carbonout_flow = olca.Flow()
carbonout_flow.id = str(uuid.uuid4())
carbonout_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
carbonout_flow.name = "Co2_Materialinhärent_out"
carbonout_flow.description = "bla"
carbonout_flow.unit = kg
carbonout_flow.flow_properties = [mass_factor]
carbonout_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"Co2_Materialinhärent_in"):
    client.insert(carbonin_flow)

if not client.find(olca.Flow,"Co2_Materialinhärent_out"):
    client.insert(carbonout_flow)

energyin_flow = olca.Flow()
energyin_flow.id = str(uuid.uuid4())
energyin_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
energyin_flow.name = "Energie_Materialinhärent_in"
energyin_flow.description = "bla"
energyin_flow.unit = MJ
energyin_flow.flow_properties = [energy_factor]
energyin_flow.olca_type = olca.schema.Flow.__name__

energyout_flow = olca.Flow()
energyout_flow.id = str(uuid.uuid4())
energyout_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
energyout_flow.name = "Energie_Materialinhärent_out"
energyout_flow.description = "bla"
energyout_flow.unit = MJ
energyout_flow.flow_properties = [energy_factor]
energyout_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"Energie_Materialinhärent_in"):
    client.insert(energyin_flow)

if not client.find(olca.Flow,"Energie_Materialinhärent_out"):
    client.insert(energyout_flow)
    
energy_nr_flow = olca.Flow()
energy_nr_flow.id = str(uuid.uuid4())
energy_nr_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
energy_nr_flow.name = "Energie_Materialinhärent_nr"
energy_nr_flow.description = "bla"
energy_nr_flow.unit = MJ
energy_nr_flow.flow_properties = [energy_factor]
energy_nr_flow.olca_type = olca.schema.Flow.__name__


if not client.find(olca.Flow,"Energie_Materialinhärent_nr"):
    client.insert(energy_nr_flow)    



NECE_flow = olca.Flow()
NECE_flow.id = str(uuid.uuid4())
NECE_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
NECE_flow.name = "NECE"
NECE_flow.description = "bla"
NECE_flow.unit = kg
NECE_flow.flow_properties = [mass_factor]
NECE_flow.olca_type = olca.schema.Flow.__name__


if not client.find(olca.Flow,"NECE"):
    client.insert(NECE_flow)    
    


WFFA_flow = olca.Flow()
WFFA_flow.id = str(uuid.uuid4())
WFFA_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
WFFA_flow.name = "WFFA"
WFFA_flow.description = "bla"
WFFA_flow.unit = kg
WFFA_flow.flow_properties = [mass_factor]
WFFA_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"WFFA"):
    client.insert(WFFA_flow)    


#### Indikatoren von EN 15804


AP_flow = olca.Flow()
AP_flow.id = str(uuid.uuid4())
AP_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
AP_flow.name = "AP (EN15804)"
AP_flow.description = "bla"
AP_flow.unit = kg
AP_flow.flow_properties = [mass_factor]
AP_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"AP (EN15804)"):
    client.insert(AP_flow)    

ADPE_flow = olca.Flow()
ADPE_flow.id = str(uuid.uuid4())
ADPE_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
ADPE_flow.name = "ADPE (EN15804)"
ADPE_flow.description = "bla"
ADPE_flow.unit = kg
ADPE_flow.flow_properties = [mass_factor]
ADPE_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"ADPE (EN15804)"):
    client.insert(ADPE_flow)    


ADPF_flow = olca.Flow()
ADPF_flow.id = str(uuid.uuid4())
ADPF_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
ADPF_flow.name = "ADPF (EN15804)"
ADPF_flow.description = "bla"
ADPF_flow.unit = kg
ADPF_flow.flow_properties = [mass_factor]
ADPF_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"ADPF (EN15804)"):
    client.insert(ADPF_flow)    

EP_flow = olca.Flow()
EP_flow.id = str(uuid.uuid4())
EP_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
EP_flow.name = "EP (EN15804)"
EP_flow.description = "bla"
EP_flow.unit = kg
EP_flow.flow_properties = [mass_factor]
EP_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"EP (EN15804)"):
    client.insert(EP_flow)    

POCP_flow = olca.Flow()
POCP_flow.id = str(uuid.uuid4())
POCP_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
POCP_flow.name = "POCP (EN15804)"
POCP_flow.description = "bla"
POCP_flow.unit = kg
POCP_flow.flow_properties = [mass_factor]
POCP_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"POCP (EN15804)"):
    client.insert(POCP_flow)    

ODP_flow = olca.Flow()
ODP_flow.id = str(uuid.uuid4())
ODP_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
ODP_flow.name = "ODP (EN15804)"
ODP_flow.description = "bla"
ODP_flow.unit = kg
ODP_flow.flow_properties = [mass_factor]
ODP_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"ODP (EN15804)"):
    client.insert(ODP_flow)    

GWP_flow = olca.Flow()
GWP_flow.id = str(uuid.uuid4())
GWP_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
GWP_flow.name = "GWP (EN15804)"
GWP_flow.description = "bla"
GWP_flow.unit = kg
GWP_flow.flow_properties = [mass_factor]
GWP_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"GWP (EN15804)"):
    client.insert(GWP_flow)    

FW_flow = olca.Flow()
FW_flow.id = str(uuid.uuid4())
FW_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
FW_flow.name = "FW (EN15804)"
FW_flow.description = "bla"
FW_flow.unit = kg
FW_flow.flow_properties = [mass_factor]
FW_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"FW (EN15804)"):
    client.insert(FW_flow)    



PERM_flow = olca.Flow()
PERM_flow.id = str(uuid.uuid4())
PERM_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PERM_flow.name = "PERM (EN15804)"
PERM_flow.description = "bla"
PERM_flow.unit = kg
PERM_flow.flow_properties = [mass_factor]
PERM_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PERM (EN15804)"):
    client.insert(PERM_flow)    


PENRM_flow = olca.Flow()
PENRM_flow.id = str(uuid.uuid4())
PENRM_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PENRM_flow.name = "PENRM (EN15804)"
PENRM_flow.description = "bla"
PENRM_flow.unit = kg
PENRM_flow.flow_properties = [mass_factor]
PENRM_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PENRM (EN15804)"):
    client.insert(PENRM_flow)    


PERT_flow = olca.Flow()
PERT_flow.id = str(uuid.uuid4())
PERT_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PERT_flow.name = "PERT (EN15804)"
PERT_flow.description = "bla"
PERT_flow.unit = kg
PERT_flow.flow_properties = [mass_factor]
PERT_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PERT (EN15804)"):
    client.insert(PERT_flow)    


PENRT_flow = olca.Flow()
PENRT_flow.id = str(uuid.uuid4())
PENRT_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PENRT_flow.name = "PENRT (EN15804)"
PENRT_flow.description = "bla"
PENRT_flow.unit = kg
PENRT_flow.flow_proPENRTies = [mass_factor]
PENRT_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PENRT (EN15804)"):
    client.insert(PENRT_flow)  
    
    
PERE_flow = olca.Flow()
PERE_flow.id = str(uuid.uuid4())
PERE_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PERE_flow.name = "PERE (EN15804)"
PERE_flow.description = "bla"
PERE_flow.unit = kg
PERE_flow.flow_properties = [mass_factor]
PERE_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PERE (EN15804)"):
    client.insert(PERE_flow)      
    
    
PENRE_flow = olca.Flow()
PENRE_flow.id = str(uuid.uuid4())
PENRE_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
PENRE_flow.name = "PENRE (EN15804)"
PENRE_flow.description = "bla"
PENRE_flow.unit = kg
PENRE_flow.flow_properties = [mass_factor]
PENRE_flow.olca_type = olca.schema.Flow.__name__

if not client.find(olca.Flow,"PENRE (EN15804)"):
    client.insert(PENRE_flow)      


##### D U M M Y S 

dummy_flow = olca.Flow()
dummy_flow.id = str(uuid.uuid4())
dummy_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
dummy_flow.name = "dummy"
dummy_flow.description = "bla"
dummy_flow.unit = items_unit
dummy_flow.flow_properties = [item_factor]
dummy_flow.olca_type = olca.schema.Flow.__name__


if not client.find(olca.Flow,"dummy"):
    client.insert(dummy_flow)    


dummy_out_flow = olca.Flow()
dummy_out_flow.id = str(uuid.uuid4())
dummy_out_flow.flow_type = olca.FlowType.PRODUCT_FLOW
dummy_out_flow.name = "dummy_out"
dummy_out_flow.description = "bla"
dummy_out_flow.unit = items_unit
dummy_out_flow.flow_properties = [item_factor]
dummy_out_flow.olca_type = olca.schema.Flow.__name__


if not client.find(olca.Flow,"dummy_out"):
    client.insert(dummy_out_flow)    


dummy_in_flow = olca.Flow()
dummy_in_flow.id = str(uuid.uuid4())
dummy_in_flow.flow_type = olca.FlowType.ELEMENTARY_FLOW
dummy_in_flow.name = "dummy_in"
dummy_in_flow.description = "bla"
dummy_in_flow.unit = items_unit
dummy_in_flow.flow_properties = [item_factor]
dummy_in_flow.olca_type = olca.schema.Flow.__name__


if not client.find(olca.Flow,"dummy_in"):
    client.insert(dummy_in_flow)    
       
dummy_in = olca.Exchange()
dummy_in.input = True
dummy_in.flow = dummy_in_flow
dummy_in.amount = 1
dummy_in.unit = items_unit 
dummy_in.flow_property = item
dummy_in.internal_id = 1
dummy_in.avoided_product = False

dummy_out = olca.Exchange()
dummy_out.input = False
dummy_out.flow = dummy_out_flow
dummy_out.flow_property = item
dummy_out.unit = items_unit
dummy_out.amount = 1
dummy_out.quantitative_reference = True
dummy_out.internal_id = 1
dummy_out.avoided_product = False


dummy_proc = olca.Process()
dummy_proc.category = client.find(olca.Category,"myProcesses")
dummy_proc.process_type = olca.ProcessType.UNIT_PROCESS
dummy_proc.id = str(uuid.uuid4())
dummy_proc.name = "dummy"
dummy_proc.olca_type = olca.schema.Process.__name__

dummy_proc.exchanges= [dummy_in,dummy_out]
client.insert(dummy_proc)

