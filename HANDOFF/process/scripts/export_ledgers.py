import csv, sys, pandas as pd
from numbers_parser import Document
repo, out = sys.argv[1], sys.argv[2]
# ---- QuickBooks GL -> flat CSV (signs are account-natural as exported)
rows=[]; acct=None; beg={}
def num(a):
    a=a.replace(',','').replace('$','').strip()
    if not a: return 0.0
    return -float(a[1:-1]) if a.startswith('(') else float(a)
with open(f"{repo}/Financials/Quickbooks/BRAVADO SPICE LLC_General Ledger - full.csv", newline='') as f:
    for row in csv.reader(f):
        if len(row)<10: continue
        c0,dist,date,ttype,n,name,desc,split,amt,bal=row[:10]
        if c0 and not c0.startswith('Total for') and not dist and not date: acct=c0; continue
        if c0.startswith('Total for'): continue
        if dist=='Beginning Balance': beg[acct]=num(bal); continue
        if not date or date=='Transaction date': continue
        rows.append(dict(account=acct,date=pd.to_datetime(date).date(),type=ttype,num=n,name=name,memo=' '.join(desc.split()),split=split,amount=num(amt),running_balance=bal))
q=pd.DataFrame(rows); q.to_csv(f"{out}/qb_gl.csv",index=False)
pd.Series(beg,name='beginning_balance_2020-01-01').to_csv(f"{out}/qb_beginning_balances.csv")
print('QB rows',len(q),q.date.min(),q.date.max(),'accounts',q.account.nunique())
# ---- Finaloop -> flat CSV
doc=Document(f"{repo}/Financials/Finaloop/Bravado - General_Ledger_2026_YTD Finaloop - Unlocked.numbers")
rows=[]
for s in doc.sheets:
    for t in s.tables:
        rr=t.rows(values_only=True)
        if s.name in ('Balance Sheet Index','Profit & Loss Index'):
            pd.DataFrame(rr[1:],columns=[str(h) for h in rr[0]]).dropna(how='all',axis=1).to_csv(f"{out}/finaloop_{s.name.replace(' ','_').replace('&','and')}.csv",index=False); continue
        hdr=rr[0]; acct=s.name
        for r in rr[1:]:
            if r[0] and isinstance(r[0],str) and r[0].startswith('Account: '): acct=r[0][9:]; continue
            dt=pd.to_datetime(r[0],errors='coerce',utc=True) if r[0] is not None else pd.NaT
            if pd.isna(dt): continue
            try: amt=float(r[1])
            except: continue
            rec=dict(account=acct,datetime_utc=str(dt)[:19],amount=amt)
            for i,h in enumerate(hdr):
                if h and h not in ('Event Time (UTC)','Amount','Currency') and i<len(r): rec[str(h)]=(' '.join(str(r[i]).split()) if r[i] is not None else '')
            rows.append(rec)
fl=pd.DataFrame(rows); fl.to_csv(f"{out}/finaloop_gl.csv",index=False)
print('Finaloop rows',len(fl),fl.datetime_utc.min(),fl.datetime_utc.max(),'accounts',fl.account.nunique(),list(fl.columns))
