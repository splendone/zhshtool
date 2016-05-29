# -*- coding: utf-8 -*-
def sqlByItem(params):
    sql = '''
select *
  from (select patient_id,
               visit_id,
               SUM(t.amount) mount,
               trunc(t.billing_date_time)
          from inp_bill_detail t
         where t.item_code = ('{}')
           and t.billing_date_time between to_date('{}','yyyy-mm-dd') and to_date('{}','yyyy-mm-dd')
         group by patient_id, visit_id, trunc(t.billing_date_time)) TT
 where TT.mount > '{}'
'''.format(params['itemCode'], params['from'], params['to'], params['mount'])
    return sql