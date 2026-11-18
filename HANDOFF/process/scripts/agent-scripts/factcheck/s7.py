import pandas as pd, re
pd.set_option('display.width',320); pd.set_option('display.max_colwidth',130); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
pat=r'(?i)tallerine|5820|360 checking|capital one|citi|petal|apple ?card|applecard|credit one|bk of amer|bank of america|onemain|chase credit|check # ?75|epay|jeremiah|synchrony|discover|barclay|amex|american express|zelle|venmo|cash app|paypal inst|affirm|klarna|upstart|sofi|navient|nelnet|student'
m=f[f.Description.fillna('').str.contains(pat)]
# bank-side accounts only
print(m.account.value_counts().to_string())
