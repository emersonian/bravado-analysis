import openpyxl, sys, re, glob
for p in glob.glob('/home/user/bravado-analysis/Jer to Investors/2026-0*/*.xlsx'):
    wb=openpyxl.load_workbook(p,data_only=True)
    print('#####',p, wb.sheetnames)
    for ws in wb:
        for row in ws.iter_rows():
            for c in row:
                v=c.value
                if isinstance(v,str) and re.search(r'(?i)veronica|anthony|tallerine|blake|benthall|nguyen|forgiv|new borrow|loan',v):
                    r=[x.value for x in ws[c.row]]
                    print(ws.title,c.coordinate, [x for x in r if x is not None][:12])
