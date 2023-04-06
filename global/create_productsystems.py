from java.io import File

from org.openlca.core.database.derby import DerbyDatabase
from org.openlca.core.matrix  import LinkingConfig
from org.openlca.core.matrix.cache import MatrixCache
from org.openlca.core.matrix import ProductSystemBuilder
from org.openlca.core.database import ImpactMethodDao, ProcessDao, ProductSystemDao
db_dir = File('C:/Users/cbuschbeck/openLCA-data-1.4/databases/ecoinvent_Holzhybrid')
db = DerbyDatabase(db_dir)

print(db.name)

processDao = ProcessDao(db)
systemDao = ProductSystemDao(db)
methodDao = ImpactMethodDao(db)

def create(processname):
    
    oldsystems = systemDao.getForName(processname)
    for oldsystem in oldsystems:
        systemDao.delete(oldsystem)
        
    process = processDao.getForName(processname)[0]
    print(process.name)
    
    linkingConfig = LinkingConfig()
    dasCache=MatrixCache.createLazy(db)
    builder = ProductSystemBuilder(dasCache,linkingConfig)
    system = builder.build(process)
    ProductSystemDao(db).insert(system)

create("A1-A3")
#create("A4")
#create("A5")
#create("B1")
#create("B2")
#create("B3")
#create("B4")
#create("B5")
#create("B6_wohn")
#create("B6_park")
#create("B7")
#create("C1")
#create("C2")
#create("C3")
#create("C4")
#create("D_e_g")
#create("D_e_k")
#create("D_s_g")
#create("D_s_k")
#create("D_w_g")
#create("D_w_k")
