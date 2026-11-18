from common import *
pd.set_option('display.max_colwidth',70)
ar=g[g.account=='12000 Accounts Receivable']
x=ar[ar.date>='2026-01-01']
b=x[x.name.str.contains("Buc-ee")]
print('Bucees 2026 payments',b[b.type=='Payment'].amount.sum(), (b.type=='Payment').sum(),'invoices',b[b.type=='Invoice'].amount.sum())
print(b[b.type=='Payment'].groupby('date').amount.agg(['sum','count']))
# Bucee's balance at 12/31/2025 by store vs 2026 payments
bal=ar[(ar.date<='2025-12-31')&ar.name.str.contains("Buc-ee")].groupby('name').amount.sum()
pay=b[b.type=='Payment'].groupby('name').amount.sum()
t=pd.DataFrame({'bal2025':bal,'pay2026':pay}).fillna(0); t=t[(t.bal2025.abs()>0.5)|(t.pay2026.abs()>0.5)]
t['match']=(t.bal2025+t.pay2026).abs()<0.01
print(t.to_string()); print(t.sum(numeric_only=True)); print('matched sum',t[t.match].bal2025.sum(), t.match.sum())
# Are payments linked to late-2025 invoices? list Buc-ee's invoices dated Nov-Dec 2025
inv=ar[(ar.date>='2025-10-01')&(ar.date<='2025-12-31')&ar.name.str.contains("Buc-ee")&(ar.type=='Invoice')]
print('Bucees invoices Q4 2025',inv.amount.sum(),len(inv), inv.date.min(), inv.date.max())
print(x[x.name.str.contains('KeHE|Kehe')][['date','type','num','name','amount']].to_string())
k=ar[(ar.date>='2025-10-01')&(ar.date<='2025-12-31')&ar.name.str.contains('KeHE|Kehe',case=False)]
print(k.groupby(['name','type']).amount.agg(['sum','count']))
# Finaloop wholesale invoices: sources
w=f[f.account=='Accounts receivable (A/R) - Wholesale']
print(w.groupby('Source').amount.sum().sort_values().to_string()[:2500])
print(f[f.Description.str.contains("Buc-ee|BUC-EE",case=False)].groupby('account').amount.agg(['sum','count']))
print(f[f.Description.str.contains("kehe",case=False)].groupby('account').amount.agg(['sum','count']))
