from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married:bool
    alergies:List[str]
    contact_details: Dict[str, str]  
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    print("Patient data inserted successfully!")


patient_info = {'name':'Anurag', 'age':89,'email':'abc@gmail.com','linkedin_url':'http://linkedin.com', 'weight':45.36, 'married':'False', 'alergies':['Nimonia', 'Rabies'], 'contact_details': {'phone':'7720820568', 'emergency':'7720820563'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)