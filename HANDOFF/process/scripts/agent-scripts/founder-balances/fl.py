import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False); f['dt']=pd.to_datetime(f['datetime_utc'])
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv'); pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
ASSET_PREFIX=('Accounts receivable','Checking','Savings','Paypal','Money in transit','Undeposited','Inventory','Prepaid','Due to/from owner','Related party balance','Other current assets','Equipment','Unidentified','Cash payments','Uncleared invoices')
INC=('Gift wrap','Sales -','Shipping income','Fulfillment services reimbursement','Inventory reimbursement','Interest income','Cashback','Money-in','Auto-class in progress - Money received')
def typ(a):
    if a in set(bs.Account):
        if a.startswith('Inventory vendors'): return 'L'
        if a.startswith(ASSET_PREFIX): return 'A'
        if a.startswith(('Capital','Distributions','Retained')): return 'E'
        return 'L'
    if a.startswith(INC): return 'I'
    return 'X'
f['typ']=f.account.map(typ)
f['dr']=f.amount.where(f.typ.isin(['A','X']),-f.amount)   # debit-positive
def show(x):
    for _,r in x.sort_values('dt').iterrows():
        print(f"{r.datetime_utc}|{r.account[:50]}|{r.amount:.2f}|{r.typ}|{str(r.Source)[:40]}|{str(r.Description)[:140]}|{str(r['Transaction Classification'])[:30]}")
