import csv
import xmlrpc.client

url = "http://localhost:8014"
db = "test"
user = "bharat.yadav@targetintegration.com"
password = "admin"


common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))

uid = common.authenticate(db, user, password, {})

models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

base = models.execute_kw(db, uid, password, "ir.module.module", "search", [[('name', '=', 'base')]])
print(base)