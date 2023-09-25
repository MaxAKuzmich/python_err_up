# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def percent(part, whole):
    per = round(100 * float(part) / float(whole), 2)
    per
    return str(per) + '%'

def load_data (up_date):
    df=pd.read_csv ('./DB/data.csv')
    df=df[df['up_date'] == up_date]
    nodes=df.node.unique().tolist()

    for node in nodes:
        err_msg = ''
        df_select = df[df['node'] == node]
        df_err = df_select[df_select['_merge'] == 'left_only']

        df_bsp = df_select[df_select['part'] == 'BSP']
        bsp_na = len(df_bsp[df_bsp['Status'] == 'N-A'])
        bsp_ok = len(df_bsp[df_bsp['Status'] == 'OK'])
        bsp_tbd = len(df_bsp[df_bsp['Status'] == 'TBD'])
        bsp_nok = len(df_bsp[df_bsp['Status'] == 'NOK'])
        bsp_total = len(df_bsp.index)

        df_hwmw = df_select[df_select['part'] == 'HW+MW']
        hwmw_na = len(df_hwmw[df_hwmw['Status'] == 'N-A'])
        hwmw_ok = len(df_hwmw[df_hwmw['Status'] == 'OK'])
        hwmw_tbd = len(df_hwmw[df_hwmw['Status'] == 'TBD'])
        hwmw_nok = len(df_hwmw[df_hwmw['Status'] == 'NOK'])
        hwmw_total = len(df_hwmw.index)

        df_red = df_select[df_select['part'] == 'Redundancy']
        red_na = len(df_red[df_red['Status'] == 'N-A'])
        red_ok = len(df_red[df_red['Status'] == 'OK'])
        red_tbd = len(df_red[df_red['Status'] == 'TBD'])
        red_nok = len(df_red[df_red['Status'] == 'NOK'])
        red_total = len(df_red.index)

        df_tr = df_select[df_select['part'] == 'Traffic']
        tr_na = len(df_tr[df_tr['Status']=='N-A'])
        tr_ok = len(df_tr[df_tr['Status'] == 'OK'])
        tr_tbd = len(df_tr[df_tr['Status'] == 'TBD'])
        tr_nok = len(df_tr[df_tr['Status'] == 'NOK'])
        tr_total = len(df_tr.index)
        
        df_pool = df_select[df_select['part'] == 'MSS Poll']
        pool_na = len(df_pool[df_pool['Status'] == 'N-A'])
        pool_ok = len(df_pool[df_pool['Status'] == 'OK'])
        pool_tbd = len(df_pool[df_pool['Status'] == 'TBD'])
        pool_nok = len(df_pool[df_pool['Status'] == 'NOK'])
        pool_total = len(df_pool.index)
        
        df_cmn = df_select[df_select['part'] == 'CMN_GMSC']
        cmn_na = len(df_cmn[df_cmn['Status'] == 'N-A'])
        cmn_ok = len(df_cmn[df_cmn['Status'] == 'OK'])
        cmn_tbd = len(df_cmn[df_cmn['Status'] == 'TBD'])
        cmn_nok = len(df_cmn[df_cmn['Status'] == 'NOK'])
        cmn_total = len(df_cmn.index)

        err = len(df_err)
        if err > 0: err_msg = 'Errors: ' + str(err)

        todo = bsp_nok + bsp_tbd + hwmw_nok + hwmw_tbd + red_nok + red_tbd + tr_nok + tr_tbd + pool_nok + pool_tbd + cmn_nok + cmn_tbd

        print(f'''Test progress analysing for {node}
BSP ({bsp_total-bsp_ok-bsp_na} / {bsp_total}): NA: {bsp_na} ({percent(bsp_na,bsp_total)}) , OK: {bsp_ok} ({percent(bsp_ok,bsp_total)}), TBD: {bsp_tbd} ({percent(bsp_tbd,bsp_total)}), NOK: {bsp_nok} ({percent(bsp_nok,bsp_total)}) 
HW+MW ({hwmw_total-hwmw_ok-hwmw_na} / {hwmw_total}): NA: {hwmw_na} ({percent(hwmw_na,hwmw_total)}) , OK: {hwmw_ok} ({percent(hwmw_ok,hwmw_total)}), TBD: {hwmw_tbd} ({percent(hwmw_tbd,hwmw_total)}), NOK: {hwmw_nok} ({percent(hwmw_nok,hwmw_total)})
Redundancy ({red_total-red_ok-red_na} / {red_total}): NA: {red_na} ({percent(red_na,red_total)}) , OK: {red_ok} ({percent(red_ok,red_total)}), TBD: {red_tbd} ({percent(red_tbd,red_total)}), NOK: {red_nok} ({percent(red_nok,red_total)})
Traffic ({tr_total-tr_ok-tr_na} / {tr_total}): NA: {tr_na} ({percent(tr_na,tr_total)}) , OK: {tr_ok} ({percent(tr_ok,tr_total)}), TBD: {tr_tbd} ({percent(tr_tbd,tr_total)}), NOK: {tr_nok} ({percent(tr_nok,tr_total)})
MSC in Pool ({pool_total-pool_ok-pool_na} / {pool_total}): NA: {pool_na} ({percent(pool_na,pool_total)}) , OK: {pool_ok} ({percent(pool_ok,pool_total)}), TBD: {pool_tbd} ({percent(pool_tbd,pool_total)}), NOK: {pool_nok} ({percent(pool_nok,pool_total)})
CMN ({cmn_total-cmn_ok-cmn_na} / {cmn_total}): NA: {cmn_na} ({percent(cmn_na,cmn_total)}) , OK: {cmn_ok} ({percent(cmn_ok,cmn_total)}), TBD: {cmn_tbd} ({percent(cmn_tbd,cmn_total)}), NOK: {cmn_nok} ({percent(cmn_nok,cmn_total)})
ToDo: {todo} from {len(df_select.index)} ({percent(todo,len(df_select.index))}) {err_msg}
''')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_data('2023-9-20')






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
