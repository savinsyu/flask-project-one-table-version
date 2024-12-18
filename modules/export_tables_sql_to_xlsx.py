import pandas as pd
from flask import Blueprint

from modules import connect

bp = Blueprint("export_tables_sql_to_xlsx", __name__)


def export_tables_sql_to_xlsx():
    conn = connect.get_db_connection()
    main_list = conn.execute("SELECT * FROM main").fetchall()
    df_main_list = pd.DataFrame(main_list)
    with pd.ExcelWriter('files/database_table.xlsx') as writer:
        df_main_list.to_excel(writer, sheet_name='Main', header=False, index=False)
    conn.close()
    print('Выгружены таблицы excel!!')




