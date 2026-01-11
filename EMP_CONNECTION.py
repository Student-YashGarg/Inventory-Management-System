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
            CREATE TABLE IF NOT EXISTS EMPLOYEE_DATA (
                Id VARCHAR(20),
                Name VARCHAR(50),
                Gender VARCHAR(10),
                contacts VARCHAR(30),
                Email VARCHAR(100),
                salary VARCHAR(50),
                doj VARCHAR(30),
                E_type VARCHAR(30),
                position VARCHAR(30),
                dept VARCHAR(40),
                password VARCHAR(50)
            )
        """)
        print("Database ready")
        
        return cur, con

# # Initialize the connection
# A = connection.getconnection()
