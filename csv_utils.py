import pandas as pd
from tabulate import tabulate

def read_csv(file_path, property_names):
    try:
        df = pd.read_csv(file_path, usecols=property_names)
        return df
    except ValueError as e:
        print(f'Error: {e}')
        print(f'Error: The file "{file_path}" could not be read. Please check the file format and provided properties.')
        exit(1)

def compare_csv(base_df, compare_df, base_file, compare_file):
    group_column = None
    ID_column = None
    
    for column in base_df.columns:
        if base_df[column].nunique() != len(base_df):
            group_column = column
        elif base_df[column].nunique() == len(base_df):
            ID_column = column
    
    grouped_base = base_df.groupby(group_column)
    grouped_compare = compare_df.groupby(group_column)
    
    base_groups = {key: set(group[ID_column]) for key, group in grouped_base}
    compare_groups = {key: set(group[ID_column]) for key, group in grouped_compare}
    
    all_groups_match = True
    
    table_data = []
    mismatch_groups_base = []
    mismatch_groups_compare = []
    
    # Create a reverse mapping from sets of IDs to group names
    base_sets_to_groups = {frozenset(ids): group for group, ids in base_groups.items()}
    compare_sets_to_groups = {frozenset(ids): group for group, ids in compare_groups.items()}
    
    # Compare the sets of IDs from base_df
    for base_set, base_group in base_sets_to_groups.items():
        compare_group = compare_sets_to_groups.get(base_set)
        if compare_group is None:
            all_groups_match = False
            mismatch_groups_base.append([base_group, ', '.join(map(str, base_set))])
        else:
            table_data.append([base_group, compare_group, ', '.join(map(str, base_set))])
    
    # Compare the sets of IDs from compare_df
    for compare_set, compare_group in compare_sets_to_groups.items():
        base_group = base_sets_to_groups.get(compare_set)
        if base_group is None:
            all_groups_match = False
            mismatch_groups_compare.append([compare_group, ', '.join(map(str, compare_set))])
    
    if all_groups_match:
        print("All groups match between the files.")
        print(tabulate(table_data, headers=[f"base_file {group_column}", f"compare_file {group_column}", f"{ID_column} values"], tablefmt="grid"))
        exit(0)
    else:
        print("Mismatching groups found.")
        if mismatch_groups_base:
            print("Mismatching groups from base_file:")
            print(tabulate(mismatch_groups_base, headers=[f"base_file {group_column}", f"{ID_column} values"], tablefmt="grid"))
        if mismatch_groups_compare:
            print("Mismatching groups from compare_file:")
            print(tabulate(mismatch_groups_compare, headers=[f"compare_file {group_column}", f"{ID_column} values"], tablefmt="grid"))
        exit(1)

def check_df_size(df1, df2, base_file, compare_file):
    if df1.shape != df2.shape:
        print(f"Error: The files '{base_file}' and '{compare_file}' do not have the same size.")
        print(f"'{base_file}' size: {df1.shape}")
        print(f"'{compare_file}' size: {df2.shape}")
        exit(1)