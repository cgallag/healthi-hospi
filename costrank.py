import dataprocessor as dp
import json

hosp_op_csv = 'Medicare_Provider_Charge_Outpatient_APC30_CY2011.csv'
hosp_ip_csv = 'Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv'

hosp_loc = dp.locdict_maker(hosp_op_csv)
hosp_op_conds = dp.hospdict_maker(hosp_op_csv)
hosp_ip_conds = dp.hospdict_maker(hosp_ip_csv)
op_conditions = dp.conddict_maker(hosp_op_csv)
ip_conditions = dp.conddict_maker(hosp_ip_csv)

def cost_ranker (conddict, hosp_op_conds):
    avgcharges = []
    avgpayments = []
    for cond in conddict:
        for hosp in hosp_op_conds:
            try:
                avgcharges.append((hosp_op_conds[hosp][cond]['avg_charge'], hosp))
                avgpayments.append((hosp_op_conds[hosp][cond]['avg_payment'], hosp))
            except:
                continue
        print 'avgcharges:', sorted(avgcharges)
        print 'avgpayments:', sorted(avgpayments)

def cost_rank (conddict, hosp_op_conds):
    for cond in conddict:
        moneylist = []
        for hosp in hosp_op_conds:
            cdata = hosp_op_conds[hosp].get(cond) #returns None if cond does not exist in dictionary
            if cdata is not None:
                moneylist.append({
                    'avgcharge': cdata['avg_charge'],
                    'avgpayment': cdata['avg_payment'],
                    'hosp': hosp
                })
        print json.dumps(sorted(moneylist, key=lambda x: x['avgcharge']), indent=4)
        break
        
cost_rank(ip_conditions, hosp_ip_conds)     
        
    

#print 'op_conditions'
#cost_ranker(op_conditions, hosp_op_conds)
#print 'ip_conditions'
#cost_ranker(ip_conditions, hosp_ip_conds)
        
    
    
