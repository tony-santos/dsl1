import difflib
import sys
import pandas as pd
import pprint

def get_column_widths(df, column_list):
    column_widths = []
    label_lengths = []

    # for i, row in enumerate(df[column_list].itertuples(index=False), 1):
    # get length of lable for each column
    for col in column_list:
        label_lengths.append(len(col))

    # get length of longest value in each column
    for ix, _ in enumerate(column_list):
        # column_widths.append(max(len(str(row[ix])) for _, row in enumerate(df[column_list].itertuples(index=False), 1)))    
        column_widths.append(max(len(str(row[ix])) for row in df[column_list].itertuples(index=False)))    

    # adjust column width if label is longer than all column entries
    for ix, _ in enumerate(column_widths):
        column_widths[ix] = max(column_widths[ix], label_lengths[ix])

    return column_widths


def get_column_widths2(df1, df2, column_list):
    column_widths = []
    column_widths1 = []
    column_widths2 = []
    # elements_in_tuple = len(column_list)
    label_lengths = []

    # for i, row in enumerate(df[column_list].itertuples(index=False), 1):
    # get length of lable for each column
    for col in column_list:
        label_lengths.append(len(col))

    # get length of longest value in each column
    for ix, _ in enumerate(column_list):
        # column_widths.append(max(len(str(row[ix])) for _, row in enumerate(df[column_list].itertuples(index=False), 1)))    
        column_widths1.append(max(len(str(row[ix])) for row in df1[column_list].itertuples(index=False)))    
        column_widths2.append(max(len(str(row[ix])) for row in df2[column_list].itertuples(index=False)))    

    # adjust column width if label is longer than all column entries
    for ix, _ in enumerate(column_list):
        column_widths.append(max(column_widths1[ix], column_widths2[ix], label_lengths[ix]))

    return column_widths


def convert_df_to_table(df, column_list, column_widths):
    table = []

    # print header row
    line = '|'
    for ix, item in enumerate(column_list):
        line = line + f" {item.ljust(column_widths[ix])} |"
    # print(f"{line}")
    table.append(f"{line}\n")

    # print data row
    for _, row in enumerate(df[column_list].itertuples(index=False), 1):
        line = '|'
        for ix, item in enumerate(list(row)):
            line = line + f" {str(item).ljust(column_widths[ix])} |"
        # print(f"{line}")
        table.append(f"{line}\n")

    # return table as list of strings
    return table

def print_table(table, label):
    print(f"\n{label}:")
    for row in table:
        print(f"  {row.rstrip()}")

def compare_tables(expected_df, actual_df, column_list):
    column_widths = get_column_widths2(df1, df2, column_list)
    expected = convert_df_to_table(expected_df, column_list, column_widths)
    actual = convert_df_to_table(actual_df, column_list, column_widths)
    diff = difflib.ndiff(expected, actual)

    print_table(expected, "expected")
    print_table(actual, "actual")

    if expected == actual:
        print(f"\ntables match")
    else:
        print(f"\nexpected vs actual:")
        sys.stdout.writelines(diff)

if __name__ == "__main__":
    # column_list = ['date', 'calories', 'sleep hours', 'gym']
    column_list = ['gym', 'date', 'calories', 'sleep_hours']
    df1 = pd.DataFrame()
    df1['date'] = ['2016-04-01', '2016-04-02', '2016-04-03']
    df1['calories'] = [2200, 2100, 1500]
    df1['sleep_hours'] = [2200, 2100, 1500]
    df1['gym'] = [True, False, False]

    df2 = pd.DataFrame()
    df2['date'] = ['2016-04-01', '2016-04-02', '2016-04-03']
    df2['calories'] = [2200, 2200, 1500]
    df2['sleep_hours'] = [2200, 2100, 1600]
    df2['gym'] = [True, True, False]

    compare_tables(df1, df2, column_list)
    compare_tables(df1, df1, column_list)
