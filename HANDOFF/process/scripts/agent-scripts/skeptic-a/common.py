import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',dtype=str,keep_default_na=False)
g['amount']=g['amount'].astype(float); g['date']=pd.to_datetime(g['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
f=pd.read_csv(D+'finaloop_gl.csv',dtype=str,keep_default_na=False)
f['amount']=f['amount'].astype(float); f['dt']=pd.to_datetime(f['datetime_utc'])
pd.set_option('display.width',300,'display.max_rows',1000,'display.max_columns',50,'display.max_colwidth',90,'display.float_format','{:,.2f}'.format)
