import EMP_CONNECTION


class Employee_DAO:
    #1
    def __init__(self):
        # Get the cursor and connection from CONNECTION module
        self.cur, self.con = EMP_CONNECTION.connection.getconnection()
    #2       
    def insertemployee(self,emp):
        try:
            sql = "INSERT INTO EMPLOYEE_DATA VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
            values =(emp.getid(),emp.getname(),emp.getgender(),emp.getcontact(),emp.getemail(),emp.getsalary(),emp.getdoj(),emp.getetype(),emp.getpos(),emp.getdept(),emp.getpass())
            self.cur.execute(sql%values)
            self.con.commit()  # Commit the transaction
            return True 

        except Exception as e:
            self.con.rollback()  # Rollback in case of error
            print(f"Error occurred: {e}")
    #3     
    def id_exist(self, eid):
    # Use a tuple for the parameter
        self.cur.execute("SELECT COUNT(*) FROM EMPLOYEE_DATA WHERE id = %s", (eid,))
        result = self.cur.fetchone()
        return result[0] > 0
    # #4
    def showall(self):
        # self.cur.execute("Select * from DATA")
        # self.cur.execute("SELECT * FROM DATA ORDER BY ID ASC")
        self.cur.execute("SELECT * FROM EMPLOYEE_DATA ORDER BY CAST(SUBSTRING(ID, 4) AS UNSIGNED)")
        # SUBSTRING(ID, 4) extracts the numeric part of EID. This assumes that the ID always starts with EMP (3 characters), so it takes the substring starting from the 4th character.
        # CAST(... AS UNSIGNED) converts the numeric part from a string to an integer for proper numeric sorting.
        result=self.cur.fetchall()
        return result
    # #5
    def update_data(self,emp):
        eid=emp.getid()
        self.cur.execute("SELECT * FROM EMPLOYEE_DATA WHERE id = %s", (eid,))
        current_data= self.cur.fetchone()
        current_data=current_data[1:]
        value=(emp.getname(),emp.getgender(),emp.getcontact(),emp.getemail(),emp.getsalary(),emp.getdoj(),emp.getetype(),emp.getpos(),emp.getdept(),emp.getpass())
        if current_data==value:
            return(0)
        else:
            sql=("update EMPLOYEE_DATA set name=%s,gender=%s,contacts=%s,email=%s,salary=%s,doj=%s,E_type=%s,position=%s,dept=%s,password=%s where id=%s")
            value=(emp.getname(),emp.getgender(),emp.getcontact(),emp.getemail(),emp.getsalary(),emp.getdoj(),emp.getetype(),emp.getpos(),emp.getdept(),emp.getpass(),emp.getid())
            self.cur.execute(sql,value)
            self.con.commit()
            return(1)
    # # #6
    def delete_by_id(self,eid):
        self.cur.execute("DELETE from EMPLOYEE_DATA where id=%s",(eid,))
        self.con.commit()
    # # #7
    def delete_all(self):
        self.cur.execute("DELETE from EMPLOYEE_DATA")
        self.con.commit() 
    # # #8
    def search(self,option,value):
        self.cur.execute(f"SELECT * from EMPLOYEE_DATA where {option} LIKE %s",(f"%{value}%",))
        result=self.cur.fetchall()
        return result
    # # #9
    def get_employee_count(self):
        self.cur.execute("SELECT COUNT(*) FROM EMPLOYEE_DATA")
        result = self.cur.fetchone()
        return result[0]
    # # #10
    def get_next_id(self):
        self.cur.execute("SELECT MAX(CAST(SUBSTRING(id, 4) AS UNSIGNED)) FROM EMPLOYEE_DATA")
        result = self.cur.fetchone()
        next_number = (result[0] + 1) if result[0] is not None else 1
        return f"EMP{next_number}"
