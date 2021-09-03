import pymysql

class PyDB():
    def __init__(self):
        self.db = pymysql.connect(
            user = "admin",
            passwd = "sjmladks",
            host = "aa15mm1u2azepde.cwjspwjfimay.ap-northeast-2.rds.amazonaws.com",
            db = "gpsservice",
            charset = "utf8"
        )
        #DB와 상호작용을 하기 위한 cursor객체 생성
        #json형태의 dictionary로 상호작용을 할 것이기 때문에 DictCursor사용
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    

    def select_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    #insert, update, delete query
    def iud_query(self, query):
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()
    

    