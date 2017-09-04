import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset': 'utf8mb4',
    'database': 'spider',
    #'cursorclass':pymysql.cursors.DictCursor
    }
def InsertData(table_name):
    """
    toPyModel(model_ptr) -> svm_model
    Convert a ctypes POINTER(svm_model) to a Python svm_model
    """
    try:
        conn = pymysql.connect(**config)
        conn.autocommit(1)
        #conn.select_db(spider)
        cursor = conn.cursor()
        #COLstr = ' '    #列字段
        ROWstr = ''    #行字段
        #arr = dict(ds)

            # COLstr = (COLstr+' '+key+COLstyle+' ')
        ROWstr = (ROWstr+'"%s"'+',') % ('111')

        #推断表是否存在，存在运行try。不存在运行except新建表，再insert
        try:
            cursor.execute("SELECT * FROM  %s " % (table_name))
            cursor.execute("INSERT INTO %s VALUES (%s)" % (table_name, ROWstr[:-1]))

        except pymysql.Error as e:
            cursor.execute("CREATE TABLE %s (id int auto_increment primary key,title varchar(300),link varchar(500))" % (table_name))
            cursor.execute("INSERT INTO %s VALUES (%s) " % (table_name, ROWstr[:-1]))
        conn.commit()
        cursor.close()
        conn.close()

    except pymysql.Error as e:
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
# if __name__=='__main__':
#     data =p
InsertData('test')
