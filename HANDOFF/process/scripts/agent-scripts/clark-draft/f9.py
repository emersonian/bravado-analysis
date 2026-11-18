import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',100)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
x=f[f.Description.astype(str).str.contains('Specialty|John Henry|Berlin|Bottling|Pratt|Mammoth|Imprimus|Endorphin|co-pack|copack',case=False)|f.Source.astype(str).str.contains('Specialty|John Henry|Berlin|Bottling|Endorphin',case=False)]
print(x.drop(columns=['dt','m','d']).sort_values('datetime_utc').to_string()[:9000])
ip=f[(f.Source=='Inventory purchase')]
print(ip.groupby('account').amount.agg(['sum','count']))
print(ip.sort_values('dt').drop(columns=['dt','m','d']).head(40).to_string())
# counter accounts on the same timestamps
ts=set(ip.datetime_utc)
y=f[f.datetime_utc.isin(ts)&(f.Source!='Inventory purchase')]
print(y.groupby(['account','Source']).amount.agg(['sum','count']).to_string()[:3000])
print(f[f['Transaction Classification'].isin(['Packaging materials','Supplies & materials','Inventory','Raw materials','Finished goods'])].groupby(['account','Transaction Classification']).amount.agg(['sum','count']))
print(f[f['Transaction Classification'].astype(str).str.contains('nventor|aterial|roduct',case=False)].groupby(['account','Transaction Classification']).amount.agg(['sum','count']))
