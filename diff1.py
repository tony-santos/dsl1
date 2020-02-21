import difflib
import sys


table1 = """    | column1  | column2  | column3  | column4  | column5  | column6 |
    | value01  | value02  | value03  | value04  | value05  | value06 |
    | value11  | value12  | value13  | value14  | value15  | value16 |
    | value21  | value22  | value23  | value24  | value25  | value26 |
    | value31  | value32  | value33  | value34  | value35  | value36 |
    | value41  | value42  | value43  | value44  | value45  | value46 |
    | value51  | value52  | value53  | value54  | value55  | value56 |""".splitlines(1)

table2 = """    | column1  | column2  | column3  | column4  | column5  | column6 |
    | value01  | value02  | value03  | value04  | value05  | value06 |
    | value11  | value12  | value13  | value14  | value15  | value16 |
    | value21  | value22  | value23  | value24  | value25  | value26 |
    | value31  | value3A  | value3  | value34Q  | value35  | value36 |
    | value51  | value52  | value53  | value54  | value55  | value56 |""".splitlines(1)

diff1 = difflib.ndiff(table1, table2)
diff2 = difflib.unified_diff(table1, table2)
diff3 = difflib.context_diff(table1, table2)
# use writelines to output generator
print("\n\n\n\nndiff")
sys.stdout.writelines(diff1)
print("\n\n\n\nunified_diff")
sys.stdout.writelines(diff2)
print("\n\n\n\ncontext_diff")
sys.stdout.writelines(diff3)
