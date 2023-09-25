# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import shutil
import time
import pandas as pd
import glob
import hashlib
import os

def make_bus():
    bu = './DB/BUs/' + str(time.localtime().tm_year) + '_'+ str(time.localtime().tm_mon) + '_'+ str(time.localtime().tm_mday)+ '_'+ str(time.localtime().tm_hour)+ '_'+ str(time.localtime().tm_min) + '_data.csv'
    shutil.copyfile('./DB/data.csv', bu)
    print (f"Make BUs for DB - ? {time.localtime()}")

def load_excel ():
    up_date = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(
        time.localtime().tm_mday)
    file = './upload/VS37MSK_report.xlsx'
    df = pd.read_excel (file)
    df['up_date'] = up_date

    print(df.info())

def calculate_hash(row):
    # Concatenate the values of 'Column1' and 'Column2' as a string
    concatenated_values = str(row['Chapter'])

    # Encode the concatenated string to bytes
    concatenated_bytes = concatenated_values.encode('utf-8')

    # Calculate the SHA-256 hash
    hash_value = hashlib.md5(concatenated_bytes).hexdigest()

    return hash_value
def check_dir ():
    print('Checking DIR')
    file_paths = glob.glob('./upload/*.xlsx')

    for file_path in file_paths:
        print(file_path)
        node = []
        node = [file_path[file_path.find('VS'):file_path.find('VS') + 7], file_path]
        print(node)
        load_new_report(node)
        os.remove(file_path)

def load_new_report (node):

    up_date = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(
        time.localtime().tm_mday)

    print (f"Ready for DB Update {up_date}")
    print(f"Processing {node[0]} on file path:{node[1]}")
    data_frames = []

    file_path = node[1]

    hash_tc = pd.read_csv('./DB/hash.csv', usecols=['hash', 'Chapter','Test Case'])

    dtype_dict = {'Chapter': str}

    # Read the CSV files into pandas DataFrames with specified data types

    df_bsp = pd.read_excel(file_path, sheet_name='BSP')
    #remove Unnamed columns
    df_bsp = df_bsp.loc[:, ~df_bsp.columns.str.match("Unnamed")]
    df_bsp.rename(columns={'Subject': 'Type'}, inplace=True)
    df_bsp['part'] = 'BSP'
    # df_bsp['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_bsp['hash'] = df_bsp.apply(calculate_hash, axis=1)
    df_bsp.fillna({'Status': 'N-A'}, inplace=True)
    df_bsp.fillna({'Date': '01.01.2022'}, inplace=True)
    # print(df_bsp['Status'])

    df_hwmw = pd.read_excel(file_path, sheet_name='HW+MW')
    #remove Unnamed columns
    df_hwmw = df_hwmw.loc[:, ~df_hwmw.columns.str.match("Unnamed")]
    df_hwmw.rename(columns={'Subject': 'Type'}, inplace=True)
    df_hwmw['part'] = 'HW+MW'
    # df_hwmw['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_hwmw['hash'] = df_hwmw.apply(calculate_hash, axis=1)
    df_hwmw.fillna({'Status': 'N-A'}, inplace=True)
    df_hwmw.fillna({'Date': '01.01.2022'}, inplace=True)
    # print(df_hwmw)

    df_red = pd.read_excel(file_path, sheet_name='Redundancy', dtype=dtype_dict)
    # remove Unnamed columns
    df_red = df_red.loc[:, ~df_red.columns.str.match("Unnamed")]
    df_red.rename(columns={'Note': 'Type'}, inplace=True)
    df_red['part'] = 'Redundancy'
    # df_red['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_red['hash'] = df_red.apply(calculate_hash, axis=1)
    df_red.fillna({'Status': 'N-A'}, inplace=True)
    df_red.fillna({'Date': '01.01.2022'}, inplace=True)
    # print(df_red)

    #check additional raws
    df_tmp = pd.read_excel(file_path, sheet_name='Traffic')
    if df_tmp.iloc[0,1] == 'Traffic Test Cases':
        df_traf = pd.read_excel(file_path, sheet_name='Traffic')
    else:
        df_traf = pd.read_excel(file_path, sheet_name='Traffic', skiprows=[0, 1])

    #remove Unnamed columns
    df_traf = df_traf.loc[:, ~df_traf.columns.str.match("Unnamed")]
    df_traf['part'] = 'Traffic'
    df_traf['Type'] = 'Compact & Cluster'
    # df_traf['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_traf['hash'] = df_traf.apply(calculate_hash, axis=1)
    df_traf.fillna({'Status': 'N-A'}, inplace=True)
    df_traf.fillna({'Date': '01.01.2022'}, inplace=True)
    # print(df_traf)

    df_pool = pd.read_excel(file_path, sheet_name='MSS Pool')
    #remove Unnamed columns
    df_pool = df_pool.loc[:, ~df_pool.columns.str.match("Unnamed")]
    df_pool['part'] = 'MSS Poll'
    # df_pool['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_pool['hash'] = df_pool.apply(calculate_hash, axis=1)
    df_pool.fillna({'Status': 'N-A'}, inplace=True)
    df_pool.fillna({'Date': '01.01.2022'}, inplace=True)
    # print(df_pool)

    df_cmn = pd.read_excel(file_path, sheet_name='CMN_GMSC')
    #remove Unnamed columns
    df_cmn = df_cmn.loc[:, ~df_cmn.columns.str.match("Unnamed")]
    df_cmn['part'] = 'CMN_GMSC'
    # df_cmn['node'] = node [0]
    # Create a new column with the hash values for 'Column1'
    df_cmn['hash'] = df_cmn.apply(calculate_hash, axis=1)
    # print(df_cmn)
    df_cmn.fillna({'Status': 'N-A'}, inplace=True)
    df_cmn.fillna({'Date': '01.01.2022'}, inplace=True)

    data_frames.append(df_bsp)
    data_frames.append(df_hwmw)
    data_frames.append(df_red)
    data_frames.append(df_traf)
    data_frames.append(df_pool)
    data_frames.append(df_cmn)

    combined_df = pd.concat(data_frames, ignore_index=True)

    combined_df.drop(['Chapter', 'Comment', 'Test Case'], axis=1, inplace=True)


    merge_bsp = pd.merge (hash_tc, combined_df, on='hash', how='left', indicator=True)
    merge_bsp['node'] = node[0]
    merge_bsp['up_date'] = up_date

    file_name = './DB/CSVs/'+ up_date + '_' + node[0] + '.csv'

    merge_bsp.to_csv(file_name)

def make_bu():
    bu = './DB/BUs/' + str(time.localtime().tm_year) + '_'+ str(time.localtime().tm_mon) + '_'+ str(time.localtime().tm_mday)+ '_'+ str(time.localtime().tm_hour)+ '_'+ str(time.localtime().tm_min) + '_data.csv'
    # shutil.copyfile('./DB/data.csv',bu)
    print (f"Make BUs for DB {time.localtime()}")

def make_df_file ():
    print('Checking DIR')
    file_paths = glob.glob('./DB/CSVs/*.csv')
    data_frames = []
    for file_path in file_paths:

        df_tmp = pd.read_csv(file_path, usecols=['hash','Chapter','Test Case','Type','Date','Status','up_date','part','node','_merge'])
        data_frames.append(df_tmp)

    df = pd.concat(data_frames, ignore_index=True)
    df.to_csv('./DB/data.csv')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_bus()
    check_dir()
    make_df_file()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
