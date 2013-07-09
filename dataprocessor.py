import csv
from collections import defaultdict
import json

def locdict_maker (csvfilename):
    hosp_loc = {}
    with open(csvfilename,'rb') as csvfile:
        locreader = csv.reader(csvfile,delimiter=',')
        for ind, row in enumerate(locreader):
            if ind == 0:
                continue
            provid = row[1]
            provname = row[2]
            provstreet = row[3]
            provcity = row[4]
            provstate = row[5]
            provzip = row[6]
            provhrr = row[7]
            hosp_loc[provid] = {'name': provname, 'street': provstreet, 'city': provcity, 'state': provstate, 'zipcode': provzip, 'hrr': provhrr}
    return hosp_loc

#hosp_loc = locdict_maker('Medicare_Provider_Charge_Outpatient_APC30_CY2011.csv')
#print hosp_loc

def hospdict_maker (csvfilename):
    hosp_conds = defaultdict(dict)
    with open(csvfilename, 'rb') as csvfile:
        condreader = csv.reader(csvfile,delimiter=',')
        for ind, row in enumerate(condreader):
            if ind == 0:
                #print row
                continue
            conditiondata = row[0].split('-')
            condid = conditiondata[0].strip()
            condname = conditiondata[1].strip()
            provid = row[1]
            numserv = int(row[8])
            avgcharge = float(row[9])
            avgpayment = float(row[10])
            hosp_conds[provid][condid] = {'name':condname, 'num_services':numserv, 'avg_charge':avgcharge, 'avg_payment':avgpayment}
    return hosp_conds
 
#op_conds = hospdict_maker('Medicare_Provider_Charge_Outpatient_APC30_CY2011.csv')
#ip_conds = hospdict_maker('Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv')

#for provid in op_conds.keys():
#   print hosp_loc[provid]['name']
    #print op_conds[provid], ip_conds[provid]
    #print json.dumps(op_conds[provid], indent=4)

def conddict_maker (csvfilename):
    conddict = {}
    with open(csvfilename, 'rb') as csvfile:
        condreader = csv.reader(csvfile,delimiter=',')
        for ind, row in enumerate(condreader):
            if ind == 0:
                continue
            conditiondata = row[0].split('-')
            condid = conditiondata[0].strip()
            condname = conditiondata[1].strip()
            conddict[condid] = condname
    return conddict

#op_conddict = conddict_maker('Medicare_Provider_Charge_Outpatient_APC30_CY2011.csv')
#ip_conddict = conddict_maker('Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv')

#for condid in op_conddict:
#   print condid, '-', op_conddict[condid]

#for condid in ip_conddict:
#   print condid, '-', ip_conddict[condid]
        
    


                
                
            
