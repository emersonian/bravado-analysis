from ld import *
x=q[(q.date>='2024-11-15')&(q.date<='2024-12-05')&(q.account.str.contains('Equity|Loan|Due|Draw'))]
print(x[['date','account','type','num','name','memo','amount']].to_string())
print(7000/10700, 1000/10700, 10700-7000-2000-500-1000)
