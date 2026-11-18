import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',70); pd.set_option('display.float_format','{:,.2f}'.format)
def qb():
    g=pd.read_csv(D+'qb_gl.csv',dtype={'num':str}); g['date']=pd.to_datetime(g['date']); return g
def bb():
    b=pd.read_csv(D+'qb_beginning_balances.csv'); b.columns=['account','bb']; return b.set_index('account')['bb']
def fl():
    f=pd.read_csv(D+'finaloop_gl.csv'); f['dt']=pd.to_datetime(f['datetime_utc']); return f
