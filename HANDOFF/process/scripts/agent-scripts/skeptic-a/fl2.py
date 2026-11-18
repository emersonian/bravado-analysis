from common import *
import sys
pd.set_option('display.max_colwidth',70)
def show(acct, n=45):
    x=f[f.account==acct].sort_values('dt')
    x=x.assign(Source=x.Source.str[:45],Description=x.Description.str[:70],cls=x['Transaction Classification'].str[:30])
    print('\n###',acct,len(x),round(x.amount.sum(),2)); print(x[['dt','amount','Source','Description','cls']].head(n).to_string())
for a in sys.argv[1:]:
    show(a)
