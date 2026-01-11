import MySQLdb
try:
    con = MySQLdb.connect(host="localhost", user="root", password="YASH@3315",database='INVENTORY_MANAGEMENT')
    cur = con.cursor()
    cur.execute("USE INVENTORY_MANAGEMENT")
    cur.execute("select tax from tax_table where id=1")
    tax=cur.fetchone()
    print(tax)
except Exception as e:
    print(e)