from web_app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String

          

class Appointment(db.Model):

    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    patient_id = Column(Integer)
    appointment_date = Column(String(30), default = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

#staff can be doctor or receptionist
class Staff(db.Model):

    __tablename__ = "staffs"

    staff_id = Column(Integer, primary_key=True)
    staff_name = Column(String(30))
    staff_contactno = Column(String(30))
    staff_address = Column(String(200))


class Patients(db.Model):

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    patient_name = Column(String(30))
    patient_contactno = Column(String(30))
    patient_address = Column(String(200))
    
    
class User(db.Model):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_type = Column(String(20)) #user type can be doctor or  receptionist
    password = Column(String(200)) 
    










    










