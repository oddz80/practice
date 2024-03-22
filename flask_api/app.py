from flask import Flask, render_template, request
from bson import ObjectId
from bson.json_util import dumps,loads
from flask_pymongo import PyMongo
from bson.json_util import dumps,loads
app = Flask(__name__)


username = "user"
password = "secret"
app.config["MONGO_URI"] = "mongodb://%s:%s@localhost/foracs?authSource=admin" % (username, password)
mongo = PyMongo(app)

@app.route("/",methods=["GET"])
def index():
    return "hello"


@app.route("/one-employee/<post_id>", methods=["GET"])
def get_one_by_ObjId(post_id: str):
    # Convert from string to ObjectId:
    document = mongo.db.employees.find_one({"_id": ObjectId(post_id)})
    print(document)
    return dumps(document)





@app.route("/all-employees", methods=["GET"])
def get_all():
    # Convert from string to ObjectId:
    document = mongo.db.employees.find()
    employees =[]
    for employee in document:
        employees.append(employee)
    return dumps(employees)

@app.route("/create-employee",methods=["POST"])
def insert_one():
    data = request.data
    print(data)
    post_id = mongo.db.employees.insert_one(loads(data)).inserted_id
    print(f"Employee with id : {post_id} inserted to db")
    return dumps({"id":post_id})

@app.route("/one-employee-by-name/<name>", methods=["GET", "POST"])
def find_one_by_name(name: str):
    one = mongo.db.employees.find_one({"name": name})
    return dumps(one)
    








if __name__ == "__main__":
    app.run(host="0.0.0", debug=True, port=5000)