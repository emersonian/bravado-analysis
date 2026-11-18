exec(open('fl.py').read())
BANKACC=f.account.str.startswith(('Checking','Savings','Credit card','Paypal'))
g=f[(f.dt>='2026-01-01')].copy()
g['key']=g.Description.astype(str).str.rstrip('. ').str[:60]
bank=g[BANKACC[g.index]].copy(); other=g[~BANKACC[g.index]].copy()
# map counter account: same Source,date,key,abs amount
other['k']=list(zip(other.Source.astype(str),other.datetime_utc,other.key,other.amount.abs().round(2)))
cm=other.groupby('k').account.agg(lambda s:' / '.join(sorted(set(s))))
bank['k']=list(zip(bank.Source.astype(str),bank.datetime_utc,bank.key,bank.amount.abs().round(2)))
bank['counter']=bank.k.map(cm)
pat=r'CAPITAL ONE|5820|360 CHECKING|PETAL|APPLE ?CARD|APPLECARD|GOLDMAN|CITI ?CARD|CITIBANK|BANK OF AMERICA|BK OF AMER|CREDIT ONE|ONEMAIN|CREDIT CRD|CHECK #|ZELLE|VENMO|CASH APP|TALLERINE|USDC|COINBASE|BENTHALL|COMATRI|ATM |WITHDRAW|WIRE|8965|3360|CHK \.\.\.0002|0002'
x=bank[bank.Description.astype(str).str.contains(pat,case=False,regex=True)]
x=x[~x.Description.astype(str).str.contains('ORIG CO NAME:Found|Online Transfer (from|to) (CHK|MMA) \.\.\.(8733|3580|5189)',regex=True)]
print(x.groupby(x.counter.astype(str)).amount.agg(['sum','count']).round(2).to_string())
for _,r in x.sort_values('dt').iterrows():
    print(f"{r.datetime_utc[:10]}|{r.account[-22:]}|{r.amount:9.2f}|{str(r.counter)[:45]}|{str(r.Description)[:150]}")
