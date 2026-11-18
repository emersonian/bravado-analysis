import pandas as pd, sys
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
print(f.dtypes); print(f.head(8).to_string())
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,errors='coerce')
print(f.dt.min(), f.dt.max(), f.dt.isna().sum())
print(f.Source.value_counts().head(30))
print(f['Transaction Classification'].value_counts().head(40))
f['d']=f.dt.dt.date.astype(str)
print(f.groupby('d').size().head(5)); print(f.groupby('d').size().tail(8))
op=f[f.d<='2025-12-31']
print(len(op)); 
t=pd.DataFrame({'open':op.groupby('account').amount.sum(),'ytd':f[f.d>'2025-12-31'].groupby('account').amount.sum(),'end':f.groupby('account').amount.sum()}).fillna(0).round(2)
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv').set_index('Account')
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv').set_index('Account')
t['bs_idx']=bs['Ending Balance']; t['pl_idx']=pl['Year Total']
print(t.to_string())
t.to_csv('fin_tb.csv')
