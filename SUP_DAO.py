import SUP_CONNECTION


class Supplier_DAO:
    #1
    def __init__(self):
        # Get the cursor and connection from CONNECTION module
        self.cur, self.con = SUP_CONNECTION.connection.getconnection()
    #2       
    def insertsupplier(self,sup):
        try:
            sql = "INSERT INTO SUPPLIER_DATA VALUES ('%s', '%s', '%s', '%s')"
            values =(sup.getid(),sup.getname(),sup.getcontact(),sup.getdesc())
            self.cur.execute(sql%values)
            self.con.commit()  # Commit the transaction
            return True 

        except Exception as e:
            self.con.rollback()  # Rollback in case of error
            print(f"Error occurred: {e}")
    #3     
    def id_exist(self, sid):
    # Use a tuple for the parameter
        self.cur.execute("SELECT COUNT(*) FROM SUPPLIER_DATA WHERE id = %s", (sid,))
        result = self.cur.fetchone()
        return result[0] > 0
    # #4
    def showall(self):
        # self.cur.execute("Select * from DATA")
        # self.cur.execute("SELECT * FROM DATA ORDER BY ID ASC")
        self.cur.execute("SELECT * FROM SUPPLIER_DATA ORDER BY CAST(SUBSTRING(ID, 4) AS UNSIGNED)")
        # SUBSTRING(ID, 4) extracts the numeric part of EID. This assumes that the ID always starts with EMP (3 characters), so it takes the substring starting from the 4th character.
        # CAST(... AS UNSIGNED) converts the numeric part from a string to an integer for proper numeric sorting.
        result=self.cur.fetchall()
        return result
    # #5
    def update_data(self,sup):
        sid=sup.getid()
        self.cur.execute("SELECT * FROM SUPPLIER_DATA WHERE id = %s", (sid,))
        current_data= self.cur.fetchone()
        current_data=current_data[1:]
        value=(sup.getname(),sup.getcontact(),sup.getdesc())
        if current_data==value:
            return(0)
        else:
            sql=("update SUPPLIER_DATA set name=%s,contacts=%s,description=%s where id=%s")
            value=(sup.getname(),sup.getcontact(),sup.getdesc(),sup.getid())
            self.cur.execute(sql,value)
            self.con.commit()
            return(1)
    # # #6
    def delete_by_id(self,sid):
        self.cur.execute("DELETE from SUPPLIER_DATA where id=%s",(sid,))
        self.con.commit()
    # # #7
    def delete_all(self):
        self.cur.execute("DELETE from SUPPLIER_DATA")
        self.con.commit() 
    # # #8
    def search(self,option,value):
        self.cur.execute(f"SELECT * from SUPPLIER_DATA where {option} LIKE %s",(f"%{value}%",))
        result=self.cur.fetchall()
        return result
    # # #9
    def get_supplier_count(self):
        self.cur.execute("SELECT COUNT(*) FROM SUPPLIER_DATA")
        result = self.cur.fetchone()
        return result[0]
    # # #10
    def get_next_id(self):
        self.cur.execute("SELECT MAX(CAST(SUBSTRING(id, 4) AS UNSIGNED)) FROM SUPPLIER_DATA")
        result = self.cur.fetchone()
        next_number = (result[0] + 1) if result[0] is not None else 1
        return f"SUP{next_number}"