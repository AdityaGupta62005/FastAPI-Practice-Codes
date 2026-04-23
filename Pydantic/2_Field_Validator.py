from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    married: bool
    alergies: List[str]
    contact_details: Dict[str, str]   

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]       

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')   
        return value  

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    #FIELD VALIDATOR can be operated in two modes the default one is AFTER where the value is provided after type coersion and in BEFORE mode the value which will get is before type coersion
    
    @field_validator('age', mode= 'before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age not valid')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    # print(patient.email)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.alergies)
    # print(patient.contact_details)
    print("Patient data inserted successfully!")


patient_info = {'name':'Anurag', 'age':30,'email':'abc@hdfc.com','linkedin_url':'http://linkedin.com', 'weight':45.36, 'married':'False', 'alergies':['Nimonia', 'Rabies'], 'contact_details': {'phone':'7720820568'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)