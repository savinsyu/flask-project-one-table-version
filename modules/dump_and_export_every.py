from schedule import every, repeat, run_pending
import pandas as pd
import io
import sqlite3
import os.path
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@repeat(every(10).minutes)
def dump_and_export_every():
    db_path = os.path.join(BASE_DIR, '../database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    with io.open("files/database_dump.sql", 'w') as p:
        for line in conn.iterdump():
            p.write('%s\n' % line)
    main_list = conn.execute("SELECT * FROM main").fetchall()
    b_conn = sqlite3.connect('files/backup.db')
    conn.backup(b_conn)
    b_conn.close()
    df_main_list = pd.DataFrame(main_list)
    with pd.ExcelWriter('files/database_table.xlsx') as writer:
        df_main_list.to_excel(writer, sheet_name='Main', header=False, index=False)
    conn.close()


while True:
    run_pending()
    time.sleep(1)
