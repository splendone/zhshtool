# -*- coding: utf-8 -*-
def sqlByItem(params):
    with open('sqls.json') as data_file:    
        data = json.load(data_file)
        print type(data)
        return data['sql1'].format(params['itemCode'], params['from'], params['to'], params['mount'])

#     sql = '''
# select patient_id, to_char(visit_id), to_char(mount), to_char(bdt, 'yyyy-mm-dd'), item_name, to_char(costs), dept_name, doctor_in_charge
#     from (select t.patient_id,
#                t.visit_id,
#                SUM(t.amount) mount,
#                trunc(t.billing_date_time) bdt,
#                t.item_name,
#                t.costs,
#                d.dept_name,
#                e.doctor_in_charge
#         from inp_bill_detail t, dept_dict d, pat_visit e
#         where t.item_code = '{}'
#             and t.billing_date_time between to_date('{}','yyyy-mm-dd') and to_date('{}','yyyy-mm-dd') 
#             and t.performed_by = d.dept_code
#             and t.patient_id = e.patient_id 
#             and t.visit_id = e.visit_id
#         group by t.patient_id, t.visit_id, trunc(t.billing_date_time), t.item_name, t.costs, d.dept_name, e.doctor_in_charge) TT
#     where TT.mount > '{}'
# '''.format(params['itemCode'], params['from'], params['to'], params['mount'])
    # return sql
    
def sqlByItemExcptDept(params):
    sql = '''
select t.patient_id,
        t.visit_id,
        item_name,
        costs,
        e.total_costs,
        billing_date_time,
        d.dept_name,
        e.doctor_in_charge
   from inp_bill_detail t, dept_dict d, pat_visit e
  where t.item_code = ('{}')
    and t.billing_date_time between to_date('{}','yyyy-mm-dd') and to_date('{}','yyyy-mm-dd') 
    and t.performed_by = d.dept_code
    and t.patient_id = e.patient_id
    and d.dept_code <> ('2212') 
    and d.dept_code <> ('221208') 
    and d.dept_code <> ('221201') 
    and d.dept_code <> ('221101') 
    and d.dept_code <> ('2211') 
    and d.dept_code <> ('221102') 
    and d.dept_code <> ('221103') 
    and d.dept_code <> ('2208')
    and d.dept_code <> ('220801')
  and d.dept_code <> ('220802')
'''.format(params['itemCode'], params['from'], params['to'], params['mount'])
    return sql