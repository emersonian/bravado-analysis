from common import *
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv'); pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
print(f.dt.min(), f.dt.max(), len(f), f.account.nunique())
s=f.groupby('account').amount.sum()
op=f[f.dt<'2026-01-01'].groupby('account').amount.sum()
j22=f[f.dt<'2026-07-23'].groupby('account').amount.sum()
bsx=bs.set_index('Account')['Ending Balance']; plx=pl.set_index('Account')['Year Total']
df=pd.DataFrame({'gl_total':s,'opening':op,'thruJul22':j22,'bs_idx':bsx,'pl_idx':plx})
df['diff']=df.gl_total-df.bs_idx.fillna(0)-df.pl_idx.fillna(0)
print(df.fillna(0).round(2).to_string())
print('accounts not in either index:',[a for a in s.index if a not in bsx.index and a not in plx.index])
print('max abs diff',df['diff'].abs().max())
print('sum bs idx',bsx.sum(),'sum pl idx',plx.sum())
print(f[f.dt>='2026-07-23'].groupby('account').amount.sum())
