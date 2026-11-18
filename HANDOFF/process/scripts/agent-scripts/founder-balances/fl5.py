exec(open('fl.py').read())
import re
BANK=f.account.str.startswith(('Checking','Savings','Credit card','Paypal'))
pat=r'CAPITAL ONE|5820|APPLE ?CARD|APPLECARD|GS BANK|GOLDMAN|CITI|BANK OF AMERICA|BK OF AMER|CREDIT ONE|PETAL|3360|8965|0002|ZELLE|VENMO|CASH APP|TALLERINE|JEREMIAH|CHECK #|CHECK$|WIRE|USDC|COINBASE|BENTHALL|BLAKE|COMATRI|ATM|WITHDRAW|EPAY|CRD|CARD ENDING|ONEMAIN|DISCOVER|AMEX|AMERICAN EXPRESS|SYNCHRONY|AFFIRM|KLARNA|UPSTART|SOFI|LOAN'
g=f[(f.dt>='2026-01-01')]
# non-bank legs whose Source is a bank/card account and description matches
x=g[~BANK & g.Description.astype(str).str.contains(pat,case=False,regex=True)]
x=x[~x.account.isin(['Distributions - Jeremiah Tallerine','Reimbursements to owners'])]
print(x.groupby('account').amount.agg(['sum','count']).round(2).to_string())
show(x[~x.account.str.startswith(('Sales','Undeposited','Accounts receivable','Deferred','Shipping income','Discount'))])
