# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:25:18 2020

@author: cbuschbeck
"""
import sys
home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
from datetime import datetime
import pytz
    
def cps_fun(processname):
    
    client = olca.Client(8080)
    
    if client.find(olca.ProductSystem,processname):
        todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,processname).id)
        todelete.olca_type = olca.schema.ProductSystem.__name__
        client.delete(todelete)
        

    proc = client.get(olca.Process,client.find(olca.Process,processname).id)
    
    datetime_str = datetime.now(pytz.utc).isoformat()
    
    new_system_ref = client.create_product_system(
    process_id=proc.id,
    default_providers="prefer",
    preferred_type="UNIT_PROCESS",
    ) #This returns a reference, not an olca.ProductSystem
    new_system=client.get(olca.ProductSystem,new_system_ref.id)
    new_system.olca_type = olca.schema.ProductSystem.__name__
     
    new_system.description = (f"Some description you want")
    #name the product system the same as your process
    new_system.name = proc.name
    model_type_str = f"{olca.ModelType.PRODUCT_SYSTEM}"
    new_system.version = "1.0.0"
    new_system.olca_type = olca.schema.ProductSystem.__name__
    new_system.category_path = []
    new_system.last_change=datetime_str
    client.update(new_system)
    
    print("product system created:"+processname)
    
    

