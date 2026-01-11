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
            CREATE TABLE IF NOT EXISTS PRODUCT_DATA (
                id INT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(100),
                supplier VARCHAR(100),
                name VARCHAR(100),
                price DECIMAL(10,2),
                discount INT,
                discounted_price DECIMAL(10,2),
                quantity INT,
                status VARCHAR(50)
            )
        """)

        print("Database ready")
        
        return cur, con