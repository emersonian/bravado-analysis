import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',120)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str)
x=f[(f.d=='2026-04-07')&(~f.Source.astype(str).str.contains('Amazon|Shopify|AMAZON|SHOPIFY|Bravado Spice - United'))]
print(x.drop(columns=['dt','d']).to_string())
print('==== Prior year adjustment'); print(f[f.account=='Prior year adjustment'].drop(columns=['dt','d']).to_string())
print('==== Jan 17'); x=f[(f.d=='2026-01-17')&(~f.Source.astype(str).str.contains('Amazon|Shopify|AMAZON|SHOPIFY|Bravado Spice - United'))]
print(x.drop(columns=['dt','d']).to_string())
