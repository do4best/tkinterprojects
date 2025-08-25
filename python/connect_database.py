import mysql.connector
class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "user"
        self._password = "user"
        self._database = "db_student_2"
        self.con = None
        self.cursor = None

    def connect_db(self):
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )
        self.cursor = self.con.cursor(dictionary=True)

    def add_info(self,student_id,firstname,lastname,state,city,roll_no):
        self.connect_db()

        sql=f"""
            INSERT INTO student_info (student_id,firstname,lastname,state,city,roll_no)
            VALUES({student_id},'{first_name}','{last_name}','{state}','{city}','{roll_no}')
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            return e
        finally:
            self.con.close()

    def update_info(self,student_id,first_name,last_name,state,city,roll_no):
        self.connect_db()
        sql =f"""
        SET firstname='{first_name}',lastname='{last_name}',state='{state}',city='{city}',roll_no='{roll_no}' 
        WHERE student_id='{student_id}'  
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            return e
        finally:
            self.con.close()
    
    def delete_student_info(self,studentId):
        sql=f"""
        DELETE from student_info where student_id={studentId}"""
        try:
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()