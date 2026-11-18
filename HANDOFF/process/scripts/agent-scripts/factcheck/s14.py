import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',100); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings'))]
b=f[f.account.isin(banks)&(f.dt<'2026-07-23')].copy()
d=b.Description.fillna('')
xfer=b[d.str.contains(r'Transfer to Capital One Personal Checking 5820|^Transfer to 360 Checking')]
fee=b[d.str.contains(r'Transfer fee for Transfer to 360 Checking')]
capcard=b[d.str.contains(r'CAPITAL ONE.*(ONLINE PMT|MOBILE PMT|ONLINE PMTSEC|MOBILE PMTSEC)')]
citi=b[d.str.contains(r'CITI (CARD|AUTOPAY)')]
petal=b[d.str.contains('Petal Card')]
chk=b[d.str.contains(r'CHECK # ?75(88|90)')]
print('transfers to 5820', xfer.amount.sum().round(2), len(xfer), ' by acct', xfer.groupby('account').amount.sum().round(2).to_dict())
print('fees', fee.amount.sum().round(2), len(fee))
print('capone card', capcard.amount.sum().round(2), len(capcard))
print('citi', citi.amount.sum().round(2), len(citi)); print(citi[['dt','amount','Description']])
print('petal', petal.amount.sum().round(2), len(petal))
print(chk[['dt','amount','Description']])
# personal txn in owner acct
o=f[(f.account.str.contains('Due to/from owner'))&(f.Source.fillna('').str.contains('Personal transaction'))&(f.dt<'2026-07-23')]
print('personal charges', o.amount.sum().round(2), len(o))
card=-(capcard.amount.sum()+citi.amount.sum()+petal.amount.sum())
tr=-xfer.amount.sum()
print('card',round(card,2),'transfers',round(tr,2),'checks',-chk.amount.sum(),'personal',o.amount.sum().round(2))
print('TOTAL', round(card+tr-chk.amount.sum()+o.amount.sum(),2))
print('inflows from capital one transfer:', b[d.str.contains('CAPITAL ONE.*TRANSFER RT')][['dt','amount','Description']])
# Where were Citi, 7588, July transfers classified? find counter-lines by amount/date
for amt,day in [(25,'2026-02-23'),(120,'2026-04-08'),(432.52,'2026-04-09'),(402.90,'2026-04-10'),(250,'2026-01-14'),(25,'2026-07-02'),(495,'2026-07-07'),(75,'2026-07-10'),(300,'2026-07-15'),(3250,'2026-01-27'),(300,'2026-04-24')]:
    t=f[(f.amount.abs().round(2)==amt)&(f.dt.dt.strftime('%Y-%m-%d')==day)]
    print(amt,day); print(t[['account','amount','Description','Transaction Classification']].to_string())
