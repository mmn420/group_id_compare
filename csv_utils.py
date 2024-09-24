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

def group_csv(base_df, compare_df):
    group_column = None
    ID_column = None
    
    for column in base_df.columns:
        if base_df[column].nunique() == len(base_df):
            ID_column = column
        else:
            group_column = column
    
    grouped_base = base_df.groupby(group_column)
    grouped_compare = compare_df.groupby(group_column)
    
    base_grouped = {key: set(group[ID_column]) for key, group in grouped_base}
    compare_grouped = {key: set(group[ID_column]) for key, group in grouped_compare}
    # Create a reverse mapping from sets of IDs to group names
    base_sets_to_groups = {frozenset(ids): group for group, ids in base_grouped.items()}
    compare_sets_to_groups = {frozenset(ids): group for group, ids in compare_grouped.items()}
    return base_sets_to_groups, compare_sets_to_groups, group_column, ID_column


def check_df_size(df1, df2, base_file, compare_file):
    if df1.shape != df2.shape:
        print(f"Error: The files '{base_file}' and '{compare_file}' do not have the same size.")
        print(f"'{base_file}' size: {df1.shape}")
        print(f"'{compare_file}' size: {df2.shape}")
        exit(1)