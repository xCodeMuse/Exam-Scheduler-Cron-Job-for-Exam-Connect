
from tracemalloc import Snapshot
import firebase_admin
from firebase_admin import credentials, firestore


from datetime import date, datetime


cred = credentials.Certificate("/Inueron/firebase-python/firebaseConfig.json")
firebase_admin.initialize_app(cred)

curr_time = datetime.now().strftime("%Y-%m-%d %H:%M")

db = firestore.client()

collRef = db.collection("tests")
results = collRef.where(
    "exam_date_time", ">=", datetime.now().strftime("%Y-%m-%d")).get()


for i in results:
    doc = collRef.document(i.id)
    d = i.to_dict()
    if(d['exam_date_time'][:-7] == curr_time):
        print(d['exam_date_time'][:-8])
        doc.update({"isActive": True})
    doc.update({"key_unlock_cost":'999'})
  
    
