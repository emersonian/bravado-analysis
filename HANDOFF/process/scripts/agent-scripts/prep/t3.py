from ld import *
def show(x,cols=('account','datetime_utc','amount','Source','Description')):
    for _,r in x.sort_values('datetime_utc').iterrows():
        print(str(r.datetime_utc)[:10], f"{r.amount:>10.2f}", '|', r.account[:45], '|', str(r.Source)[:42], '|', str(r.Description)[:95])
print('== Reimbursements to owners'); x=f[f.account=='Reimbursements to owners']; show(x); print(round(x.amount.sum(),2))
print('== Operational vendors bills 2026'); show(f[(f.account=='Operational vendors - bills')&(f.datetime_utc>='2026-01-01')])
# Q9: 7500 / 8500 / 4600, Capital One inflows
print('== amounts 7500/8500/4600'); show(f[f.amount.abs().isin([7500,8500,4600,3750])])
bank=f[f.account.str.startswith(('Checking','Savings'))]
print('== bank inflows >=1000, Apr 15-May 31 2026'); show(bank[(bank.amount>=1000)&(bank.datetime_utc>='2026-04-15')&(bank.datetime_utc<='2026-05-31')])
print('== bank lines mentioning CAPITAL ONE inflow'); show(bank[(bank.amount>0)&bank.Description.astype(str).str.contains('CAPITAL ONE|Blake|Benthall|Comatri|Zelle|Venmo',case=False)])
print('== any mention Benthall/Comatri/Nguyen/Tallerine/Veronica'); show(f[f.Description.astype(str).str.contains('Benthall|Comatri|Nguyen|Tallerine|Veronica|Anthony',case=False)|f.Source.astype(str).str.contains('Benthall|Comatri|Nguyen|Veronica',case=False)])
print('== loan accounts'); 
for a in sorted(f.account.unique()):
    if 'oan' in a or 'Line of credit' in a or 'Unidentified' in a:
        x=f[f.account==a]; print(a, round(x[x.datetime_utc<'2026-01-01'].amount.sum(),2), round(x.amount.sum(),2), len(x))
