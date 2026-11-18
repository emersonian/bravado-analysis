from common import *
f=fl()
print(f.dt.min(), f.dt.max(), len(f), f.account.nunique())
print(f.Source.value_counts().head(40))
op=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
print(len(op), op.dt.unique()[:5])
print(op.sort_values(['Source','Description'])[['account','dt','amount','Source','Description']].to_string(index=False))
