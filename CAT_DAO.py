import CAT_CONNECTION


class Category_DAO:
    #1
    def __init__(self):
        # Get the cursor and connection from CONNECTION module
        self.cur, self.con = CAT_CONNECTION.connection.getconnection()
    #2       
    def insertcategory(self,cat):
        try:
            sql = "INSERT INTO CATEGORY_DATA VALUES ('%s', '%s', '%s', '%s')"
            values =(cat.getid(),cat.getname(),cat.getquantity(),cat.getdesc())
            self.cur.execute(sql%values)
            self.con.commit()  # Commit the transaction
            return True 

        except Exception as e:
            self.con.rollback()  # Rollback in case of error
            print(f"Error occurred: {e}")
    #3     
    def id_exist(self, cid):
    # Use a tuple for the parameter
        self.cur.execute("SELECT COUNT(*) FROM CATEGORY_DATA WHERE id = %s", (cid,))
        result = self.cur.fetchone()
        return result[0] > 0
    # #4
    def showall(self):
        # self.cur.execute("Select * from DATA")
        # self.cur.execute("SELECT * FROM DATA ORDER BY ID ASC")
        self.cur.execute("SELECT * FROM CATEGORY_DATA ORDER BY CAST(SUBSTRING(ID, 4) AS UNSIGNED)")
        # SUBSTRING(ID, 4) extracts the numeric part of EID. This assumes that the ID always starts with EMP (3 characters), so it takes the substring starting from the 4th character.
        # CAST(... AS UNSIGNED) converts the numeric part from a string to an integer for proper numeric sorting.
        result=self.cur.fetchall()
        return result
    # #5
    def update_data(self,cat):
        cid=cat.getid()
        self.cur.execute("SELECT * FROM CATEGORY_DATA WHERE id = %s", (cid,))
        current_data= self.cur.fetchone()
        current_data=current_data[1:]
        value=(cat.getname(),cat.getquantity(),cat.getdesc())
        if current_data==value:
            return(0)
        else:
            sql=("update CATEGORY_DATA set name=%s,quantity=%s,description=%s where id=%s")
            value=(cat.getname(),cat.getquantity(),cat.getdesc(),cat.getid())
            self.cur.execute(sql,value)
            self.con.commit()
            return(1)
    # # #6
    def delete_by_id(self,cid):
        self.cur.execute("DELETE from CATEGORY_DATA where id=%s",(cid,))
        self.con.commit()
    # # #7
    def delete_all(self):
        self.cur.execute("DELETE from CATEGORY_DATA")
        self.con.commit() 
    # # #8
    def search(self,option,value):
        self.cur.execute(f"SELECT * from CATEGORY_DATA where {option} LIKE %s",(f"%{value}%",))
        result=self.cur.fetchall()
        return result
    # # #9
    def get_category_count(self):
        self.cur.execute("SELECT COUNT(*) FROM CATEGORY_DATA")
        result = self.cur.fetchone()
        return result[0]
    # # #10
    def get_next_id(self):
        self.cur.execute("SELECT MAX(CAST(SUBSTRING(id, 4) AS UNSIGNED)) FROM CATEGORY_DATA")
        result = self.cur.fetchone()
        next_number = (result[0] + 1) if result[0] is not None else 1
        return f"CAT{next_number}"
