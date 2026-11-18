from ld import *
def show(x):
    for _,r in x.sort_values('date').iterrows():
        print(str(r.date)[:10], f"{r.amount:>11.2f}", '|', r.account[:34], '|', str(r.type)[:12], '|', str(r.num)[:8], '|', str(r['name'])[:22], '|', str(r.memo)[:95], '|', str(r.split)[:30])
m=q['name'].astype(str).str.contains('Nguyen',case=False)|q.memo.astype(str).str.contains('Nguyen',case=False)
print('== Nguyen'); show(q[m])
m=q['name'].astype(str).str.contains('Tallerine',case=False)&~q['name'].astype(str).str.contains('Jeremiah',case=False)|q.memo.astype(str).str.contains('Anthony|Veronica',case=False)|(q.account=='73460 Line of Credit Fee | AT')
print('== Tallerine family'); show(q[m])
