'''
Created on Jul 14, 2013

@author: cagallagher
'''
import dataprocessor as dp
import couchdb 

hosp_op_csv = 'data/Medicare_Provider/Medicare_Provider_Charge_Outpatient_APC30_CY2011.csv'
hosp_ip_csv = 'data/Medicare_Provider/Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv'

server = couchdb.Server()
db_hospitals = server['health_hospitals']

def create_hosp_dbdoc_loc():
    hosp_loc = dp.locdict_maker(hosp_op_csv)
    
    for hospid in hosp_loc:
        doc = {
            'name': hosp_loc[hospid]['name'],
            'location': hosp_loc[hospid]
        }
        
        db_hospitals[hospid] = doc
        
def add_cond_db():
    hosp_op_conds = dp.hospdict_maker(hosp_op_csv)
    hosp_ip_conds = dp.hospdict_maker(hosp_ip_csv)
    
    for hospid in hosp_op_conds:
        print hospid
        doc = db_hospitals[hospid]
        new_entries = {
            'outpatient': hosp_op_conds[hospid],
            'inpatient': hosp_ip_conds[hospid]
            }
        
        doc.update(new_entries)
        db_hospitals[hospid] = doc
        
def main():
    add_cond_db()

if __name__ == '__main__':
    main()