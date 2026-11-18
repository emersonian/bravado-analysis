from ld import *
def show(x):
    for _,r in x.sort_values('datetime_utc').iterrows():
        print(str(r.datetime_utc)[:10], f"{r.amount:>10.2f}", '|', r.account[:45], '|', str(r.Source)[:42], '|', str(r.Description)[:110])
for a in ['Loan payable - Ondeck Capital','Long-term loan payable - Small Business Administration','Loan payable - American Express','Unidentified payouts & transfers']:
    print('==',a); show(f[f.account==a])
x=f[f.account=='Loan payable - Shopify Capital']; print('Shopify cap by month'); print(x.groupby(x.datetime_utc.dt.to_period('M')).amount.sum().round(2).to_string())
# July bank lines: big inflows/outflows after Jul 1
bank=f[f.account.str.startswith(('Checking','Savings'))]
print('== bank lines |amt|>=1500 from Jun 15'); show(bank[(bank.amount.abs()>=1500)&(bank.datetime_utc>='2026-06-15')])
print('== transfers to 5820 / Capital One, Jul'); show(bank[(bank.datetime_utc>='2026-07-01')&bank.Description.astype(str).str.contains('5820|CAPITAL ONE|Petal|CITI|APPLE',case=False)])
