uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
from matplotlib import pyplot
#1.connect to mlab server
from pymongo import MongoClient
client=MongoClient(uri)

#2.get a database
db= client.get_database()

#3. get  a CONNECTION
customer=db["customers"]
event_count = 0
wom_count = 0 
ads_count =0 

for refence in customer.find():
    if refence['ref'] == "events":
        event_count += 1
    elif refence['ref'] == "wom":
        wom_count += 1
    elif refence['ref'] == 'ads':
        ads_count +=1


ref_counts = [event_count, wom_count, ads_count]
ref_names = ["events", "wom", "ads"]
pyplot.pie(ref_counts, labels = ref_names, autopct = "%.1f%%",shadow = True)

pyplot.show()

ref_count = []