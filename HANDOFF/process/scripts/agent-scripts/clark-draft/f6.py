import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
inv=f[f.account=='Inventory']
print(inv.groupby(['m','Source']).amount.agg(['sum','count']).round(2).to_string())
print(inv[inv.Source.astype(str).str.contains('Inventory purchase|Finaloop|Adjust',case=False)].drop(columns=['dt','m','account']).sort_values('d').to_string()[:9000])
for a in ['Inventory vendors - bills','Operational vendors - bills','Loan payable - Ondeck Capital','Loan payable - American Express','Long-term loan payable - Small Business Administration','Line of credit - Anthony Tallerine','Related party balance - non interest bearing - Endorphin Farms','Bad debt','Other payroll deductions payable','Capital - Blake Benthall','Capital - Jeremiah Tallerine','Retained earnings','Accrued expenses - General','Interest & financing fees']:
    x=f[f.account==a].sort_values('dt')
    print('=====',a,len(x),round(x.amount.sum(),2))
    print(x.drop(columns=['dt','m','account','d']).head(60).to_string())
