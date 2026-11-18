from ld import *
pv=q.pivot_table(index='account',columns='y',values='amount',aggfunc='sum').fillna(0)
pv.insert(0,'bb',bb.reindex(pv.index).fillna(0))
cum=pv.cumsum(axis=1)
keys=['33500 Due to Jeremiah','Due from Jer',"53000 Jer's Draw",'Wages Due to Jeremiah','Member Equity - Tallerine','Due from James',"54000 James' Draw",'Member Equity - Nelson','Loan From Nguyen','Member Equity - Nguyen','Member Equity - Coinbase','Member Equity - Clark','Loan From Mark Clark','33100 Anthony Tallerine LOC','31000 Accounts Payable','SBA Disaster Loan','Retained Earnings','73902 Salaries & Wages','75500 Reimbursements','12000 Accounts Receivable','Debt to Equity - Hugh and Christy Nguyen','Debt to Equity - Mark Clark','Accrued Expense']
print('ACTIVITY');print(pv.loc[keys].round(2).to_string())
print('YE BAL');print(cum.loc[keys].round(2).to_string())
