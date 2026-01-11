import PROD_CONNECTION


class Product_DAO:
    #1
    def __init__(self):
        # Get the cursor and connection from CONNECTION module
        self.cur, self.con = PROD_CONNECTION.connection.getconnection()
    #2       
    def insertproduct(self,prod):
        try:
            sql="INSERT INTO PRODUCT_DATA (category, supplier, name, price, discount, discounted_price, quantity, status)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values =(prod.getcategory(),prod.getsupplier(),prod.getname(),prod.getprice(),prod.getdiscount(),prod.getdiscounted_price(),prod.getquantity(),prod.getstatus())
            self.cur.execute(sql,values)
            self.con.commit()  # Commit the transaction
            return True 

        except Exception as e:
            self.con.rollback()  # Rollback in case of error
            print(f"Error occurred: {e}")
    #3
    def showall(self):
        self.cur.execute("SELECT * FROM PRODUCT_DATA ORDER BY id") 
        return self.cur.fetchall()
    #4
    def fetch_sup_catg(self):
        self.cur.execute("select name from CATEGORY_DATA")
        category_names=self.cur.fetchall()
        self.cur.execute("select name from SUPPLIER_DATA")
        supplier_names=self.cur.fetchall()
        
        return category_names,supplier_names
    #5
    def already_exist(self,prod):
        sql="select * from product_data where category=%s AND supplier=%s AND name=%s"
        values=(prod.getcategory(),prod.getsupplier(),prod.getname())
        self.cur.execute(sql,values)
        return self.cur.fetchone()   
    #6
    def search(self,option,value):
        self.cur.execute(f"SELECT * from PRODUCT_DATA where {option} LIKE %s",(f"%{value}%",))
        result=self.cur.fetchall()
        return result  
    #7
    def update_data(self,prod):
        pid=prod.getid()
        self.cur.execute("SELECT * FROM PRODUCT_DATA WHERE id = %s", (pid,))
        current_data= self.cur.fetchone()
        current_data=current_data[1:] # skip id
        value=(prod.getcategory(),prod.getsupplier(),prod.getname(),prod.getprice(),prod.getdiscount(),prod.getdiscounted_price(),prod.getquantity(),prod.getstatus())
        
        #modify value datatype first to match with current data
        from decimal import Decimal
        value = (str(prod.getcategory()),
                 str(prod.getsupplier()),
                 str(prod.getname()),
                 Decimal(prod.getprice()),
                 int(prod.getdiscount()),
                 Decimal(str(prod.getdiscounted_price())),
                 int(prod.getquantity()),
                 str(prod.getstatus())
                 )

        if current_data==value:
            return(0) # No changes detected
        else:
            sql=("update PRODUCT_DATA set category=%s,supplier=%s,name=%s,price=%s,discount=%s,discounted_price=%s,quantity=%s,status=%s where id=%s")
            value=(prod.getcategory(),prod.getsupplier(),prod.getname(),prod.getprice(),prod.getdiscount(),prod.getdiscounted_price(),prod.getquantity(),prod.getstatus(),prod.getid())
            self.cur.execute(sql,value)
            self.con.commit()
            return(1) # Data Updated
    #8   
    def delete_by_id(self,pid):
        self.cur.execute("DELETE from PRODUCT_DATA where id=%s",(pid,))
        self.con.commit()
        try:
          
            # Check if table is empty
            self.cur.execute("SELECT COUNT(*) FROM PRODUCT_DATA")
            count = self.cur.fetchone()[0]

            if count == 0:
                self.cur.execute("ALTER TABLE PRODUCT_DATA AUTO_INCREMENT = 1")
                self.con.commit()
                
        except Exception as e:
            print(e)
            
    #9   
    def get_product_count(self):
        self.cur.execute("SELECT COUNT(*) FROM PRODUCT_DATA")
        result = self.cur.fetchone()
        return result[0]