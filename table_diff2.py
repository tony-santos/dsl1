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
    """calculate column widths for a text table
    sets column width to the longest of the values in either dataframe or the label if lable is longer than any entry
    Arguments:
        df1 {dataframe} -- dataframe of expected data
        df2 {dataframe} -- dataframe of actual data
        column_list {list} -- list of columns to be included in text table
    
    Returns:
        list -- list containing the length of each column
    """
    # column_widths, column_widths1, column_widths2, label_lengths = [], [], [], []
    column_widths, column_widths1, column_widths2 = [], [], []

    # get length of lable for each column
    label_lengths = [len(col) for col in column_list]

    for ix, _ in enumerate(column_list):
        # get length of longest column entry in each dataframe
        column_widths1.append(max(len(str(row[ix])) for row in df1[column_list].itertuples(index=False)))    
        column_widths2.append(max(len(str(row[ix])) for row in df2[column_list].itertuples(index=False)))    

    # for each column, take longest of entry in either dataframe or length of label
    column_widths = [max(column_widths1[ix], column_widths2[ix], label_lengths[ix]) for ix, _ in enumerate(column_list)]

    return column_widths


def convert_df_to_table(df, column_list, column_widths):
    table = []

    # header row
    line = '|'
    for ix, item in enumerate(column_list):
        line = line + f" {item.ljust(column_widths[ix])} |"
    # print(f"{line}")
    table.append(f"{line}\n")

    # data rows
    for _, row in enumerate(df[column_list].itertuples(index=False), 1):
        line = '|'
        for ix, item in enumerate(list(row)):
            line = line + f" {str(item).ljust(column_widths[ix])} |"

        table.append(f"{line}\n")

    # return table as list of strings
    return table

def print_table(table, label):
    print(f"\n{label}:")
    for row in table:
        print(f"  {row.rstrip()}")

def compare_tables(expected_df, actual_df, column_list, sort_by=None):
    if sort_by is None:
        sort_by = column_list
    
    column_widths = get_column_widths2(df1, df2, column_list)
    expected = convert_df_to_table(expected_df.sort_values(by=sort_by), column_list, column_widths)
    actual = convert_df_to_table(actual_df.sort_values(by=sort_by), column_list, column_widths)
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
    df1['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-02']
    df1['calories'] = [2200, 2100, 1500, 2100]
    df1['sleep_hours'] = [2200, 2100, 1500, 2200]
    df1['gym'] = [True, False, False, True]

    df2 = pd.DataFrame()
    df2['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-02']
    df2['calories'] = [2200, 2200, 1500, 1500]
    df2['sleep_hours'] = [2200, 2100, 1600, 1500]
    df2['gym'] = [True, True, False, True]

    df3 = pd.DataFrame()
    df3['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03']
    df3['calories'] = [2200, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500]
    df3['sleep_hours'] = [2200, 2100, 1500, 2200, 2100, 2200, 2100, 2200, 2100, 2200, 2100, 2200, 2100]
    df3['gym'] = [True, False, False, True, False, True, False, True, False, True, False, True, False]

    df4 = pd.DataFrame()
    df4['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03']
    df4['calories'] = [2200, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500]
    df4['sleep_hours'] = [2200, 2100, 1500, 2200, 2100, 2200, 2100, 2200, 2100, 2200, 2100, 2200, 2100]
    df4['gym'] = [True, False, False, True, False, True, False, True, False, True, False, True, False]

    df5 = pd.DataFrame()
    df5['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02', '2016-04-03', '2016-04-02']
    df5['calories'] = [2200, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100, 1500, 2100]
    df5['sleep_hours'] = [2200, 2100, 1500, 2200, 2100, 2200, 2100, 2200, 2100, 2200, 2100, 2200]
    df5['gym'] = [True, False, False, True, False, True, False, True, False, True, False, True]

    compare_tables(df1, df2, column_list, ['date'])
    compare_tables(df1, df1, column_list, ['sleep_hours', 'calories' ])

    compare_tables(df3, df4, column_list, ['date', 'gym'])
    compare_tables(df3, df5, column_list, ['date', 'gym'])
    compare_tables(df5, df3, column_list, ['date', 'gym'])
    # compare_tables(df1, df1, column_list, ['sleep_hours', 'calories' ])
