import pandas as pd, re
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
g['memo']=g.memo.fillna('').str[:105]
C=['account','date','type','num','name','memo','split','amount']
def acct(a,cond=None):
    x=g[g.account==a]
    if cond is not None: x=x[cond(x)]
    print('#####',a, round(x.amount.sum(),2)); print(x[C[1:]].to_string())
def je(num,date=None):
    x=g[g.num==num]
    if date: x=x[x.date==date]
    print('=====',num, round(x.amount.sum(),2)); print(x[['account','date','memo','amount']].to_string())
acct('Due from James')
for n in ['AJE-173','AJE-135','AJE-175','AJE-397','AJE-39','CPA AJE 1 - 2024','AJE-307','AJE-229','AJE-253','AJE-270','CPA-WSA1','AJE-311','CPA AJE 2 - 2025','AJE-35','AJE-131','AJE-308','AJE-180','AJE-169','AJE-303','AJE-455','AJE-456','AJE-422','AJE-380']:
    je(n)
acct('Credit card (9532)',lambda x:x.y>=2024)
acct('Gains/Loss on Asset Sale/Disposal')
acct('73110 Office Rent',lambda x:x.y==2024)
acct('80005 Rent Income')
acct('80000 Interest Earned',lambda x:x.y==2024)
acct('29000 Company Vehicle - Box Truck')
acct('27000 Machinery & Equipment')
acct('35000 Loan Payable - Chevrolet',lambda x:x.y>=2023)
acct('Member Equity - Coinbase'); acct('Member Equity - Clark'); acct('Member Equity - Nguyen'); acct('Loan From Nguyen'); acct('Debt to Equity - Hugh and Christy Nguyen')
acct('Chase 5039',lambda x:x.y>=2025)
acct('66000 Other Income',lambda x:(x.y==2023)&(x.amount.abs()>=1000))
