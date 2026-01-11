import MySQLdb

class connection:
    @staticmethod
    def getconnection():
        # Connect to the MySQL server
        con = MySQLdb.connect(host="localhost", user="root", password="YASH@3315",autocommit=True)
        cur = con.cursor()
        
        # Create the database if it doesn't exist
        cur.execute("CREATE DATABASE IF NOT EXISTS INVENTORY_MANAGEMENT")
        cur.execute("USE INVENTORY_MANAGEMENT")
        
        # Create the table with properly defined columns
        cur.execute("""
            CREATE TABLE IF NOT EXISTS SUPPLIER_DATA (
                Id VARCHAR(20),
                Name VARCHAR(50),
                contacts VARCHAR(30),
                description VARCHAR(200)
                )
        """)
        print("Database ready")
        
        return cur, con