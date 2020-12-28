import pymysql as my

def db_selectcastList( curPageId=1 , onePage_dataNum=30):
    conn = None
    rows  = None


    try:
        conn= my.connect(   host    ='localhost',  
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                SELECT * FROM busancasts Limit %s, %s;
                '''
            amt       = onePage_dataNum
            srartPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( srartPage, amt ))
            rows =cursor.fetchall()
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows