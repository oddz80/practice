import mysql.connector
from mysql.connector import errorcode

# We first open a connection to the MySQL server and store the connection object in the variable cnx. 
# We then create a new cursor, by default a MySQLCursor object, using the connection's cursor() method.

class Database:

    def __init__(self) -> None:
        self.cnx = None
        self.cur = None
        self.tables= {}

    def init_db(self):
        try:
            self.cnx = mysql.connector.connect(user='user', password='secret',
                                 host='localhost',
                                 database='foracs')
            self.cur = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()
        
    def create_employee_table(self):
        self.tables['employees'] = (
            "CREATE TABLE `employees` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `name` varchar(14) NOT NULL,"
            "  `address` varchar(16) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")
        self.cur.execute()
        
    def get_one_by_ObjId(self, post_id: str):
        # Convert from string to ObjectId:
        document = self.db.employees.find_one({"_id": ObjectId(post_id)})
        print(document)

    def insert_one(self, employ_obj: dict):
        post_id = self.db.employees.insert_one(employ_obj).inserted_id
        print(f"Employee with id : {post_id} inserted to db")

    def find_one_by_name(self, name: str):
        one = self.db.employees.find_one({"name": name})
        print(one)


employeee = {
    "name": "Fred",
    "position": "Test Leader",
    "text": "My first db post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}


db_obj = Database()
db_obj.init_db()
db_obj.insert_one(employeee)
db_obj.find_one_by_name('Fred')









