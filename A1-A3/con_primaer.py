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


if client.find(olca.Process,"concrete_primaer"):
    todelete = client.get(olca.Process,client.find(olca.Process,"concrete_primaer").id)
    todelete.olca_type = olca.schema.Process.__name__
    client.delete(todelete)




########################
###     Units      #####
########################
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")

from units import m3,vol

########################
###     Flows      #####
########################

if not client.find(olca.Flow,"concrete_primaer"):
    con_flow = olca.Flow()
    con_flow.id = str(uuid.uuid4())
    con_flow.flow_type = olca.FlowType.PRODUCT_FLOW
    con_flow.name = "concrete_primaer"
    con_flow.description = "conindungen des Holzhybrides"
    con_flow.unit = m3
    con_flow.olca_type = olca.schema.Flow.__name__

    client.insert(con_flow)

con_flow = client.get(olca.Flow,client.find(olca.Flow,"concrete_primaer").id)
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, quoting = 3)


concrete_flow = client.get(olca.Flow,"eee95138-58c8-4172-9b1f-754ba074325d") #concrete, normal

########################
###     Processes  #####
########################
concrete_process = client.get(olca.Process,"856837d8-29e2-4f89-a61a-6c17a72fa7c9") #concrete, all types to generic market for concrete, normal strength | concrete, normal | EN15804, U


exch = []
ID= 1


con_input_concrete = olca.Exchange()
con_input_concrete.input = True
con_input_concrete.flow = concrete_flow
con_input_concrete.default_provider = concrete_process
con_input_concrete.flow_property = vol
con_input_concrete.unit = m3
con_input_concrete.amount = 1
con_input_concrete.quantitative_reference = True
con_input_concrete.internal_id =ID;ID = ID + 1
con_input_concrete.avoided_product = False
exch.append(con_input_concrete)



con_process = olca.Process()
con_process.category = client.find(olca.Category,"A1-A3")
con_process.process_type = olca.ProcessType.UNIT_PROCESS
con_process.id = str(uuid.uuid4())
con_process.name = "concrete_primaer"
con_process.olca_type = olca.schema.Process.__name__


con_output_con = olca.Exchange()
con_output_con.input = False
con_output_con.flow = con_flow
con_output_con.flow_property = vol
con_output_con.unit = m3
con_output_con.amount = 1
con_output_con.quantitative_reference = True
con_output_con.internal_id =ID;ID = ID + 1 
con_output_con.avoided_product = False
exch.append(con_output_con)





con_process.exchanges= exch
client.insert(con_process)
