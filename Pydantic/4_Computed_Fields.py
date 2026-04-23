from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float #Kg
    height: float #Mtr
    married:bool
    alergies:List[str]
    contact_details: Dict[str, str]  

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.height)
    print('BMI',patient.bmi)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    print("Patient data inserted successfully!")


patient_info = {'name':'Anurag', 'age':89,'email':'abc@gmail.com','linkedin_url':'http://linkedin.com', 'weight':45.36, 'height' : 1.72, 'married':'False', 'alergies':['Nimonia', 'Rabies'], 'contact_details': {'phone':'7720820568', 'emergency':'7720820563'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)