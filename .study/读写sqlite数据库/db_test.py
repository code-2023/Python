
import sqlite3 as sqlite
from xlwt import *
import sys


def sqlite_get_col_names(cur, select_sql):
    cur.execute(select_sql)
    return cur.fetchone()
    # return [tuple[0] for tuple in cur.description]


def query_by_sql(cur, select_sql):
    cur.execute(select_sql)
    return cur.fetchall()


def sqlite_to_workbook_with_head(cur, table, select_sql, workbook):
    ws = workbook.add_sheet(table)
    print('create table %s.' % table)
    # enumerate针对一个可迭代对象，生成的是序号加上内容

    for colx, heading in enumerate(sqlite_get_col_names(cur, select_sql)):
        ws.write(0, colx, heading)  # 在第1行的colx列写上头部信息

    for rowy, row in enumerate(query_by_sql(cur, select_sql)):
        for colx, text in enumerate(row):  # row是一行的内容
            ws.write(rowy + 1, colx, text)  # 在rowy+1行，colx写入数据库内容text


def dump_db_to_excel(cur, workbook):
    for tbl_name in [row[0] for row in query_by_sql(cur, \
    "select tbl_name FROM sqlite_master where type = 'table'AND tbl_name ='bookmarks'")]:
        print(tbl_name)
        select_sql = "select title,url from '%s'" % tbl_name
        # sqlite_to_workbook_with_head(cur, tbl_name, select_sql, workbook)


def main(dbpath):
    xlspath = dbpath[:dbpath.rfind('.')] + '.xls'
    print("<%s> --> <%s>" % (dbpath, xlspath))

    db = sqlite.connect(dbpath)
    cur = db.cursor()
    w = Workbook()

    data=query_by_sql(cur,"select title,url from bookmarks")
    print("游标查询结果类型：", type(data))
    print(data)
    dump_db_to_excel(cur, w)  # 把所有的db中的表数据导出到excel中，每个table对应一个sheet页

    # 按照条件查询数据并导出到excel中
    # sheet_name = '测试'
    # query_data_sql = "select 100-id as used from cpu_info where cpu_name = '%Cpu0'"
    # sqlite_to_workbook_without_head(cur, sheet_name, query_data_sql, w)

    cur.close()
    db.close()

    # w.save(xlspath)


if __name__ == "__main__":
    # arg == database path
    # main(sys.argv[1])
    main("browser2.db")