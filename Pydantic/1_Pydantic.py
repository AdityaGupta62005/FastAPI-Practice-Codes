from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50, title='Name of the Patient', description='Enter the name of the patient in less than 50 chars.', examples=['Nitish', 'Suresh'])]  #FIELD allows custom Data Validation
    age: int = Field(gt=15, lt=90)
    email: EmailStr
    linkedin_url: AnyUrl
    weight:Annotated[ float, Field(gt=5, strict=True)] #STRICT uses to prevent automatic type conversion
    married:Annotated[bool, Field(default=None, description='Is the patient married or not' )]                       #Sets meta data using annotated and field
    alergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]                   #It will stay optional not required to fill
    contact_details: Dict[str, str]                #Performs double check key & val to be str

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    print("Patient data inserted successfully!")


patient_info = {'name':'Anurag', 'age':30,'email':'abc@gmail.com','linkedin_url':'http://linkedin.com', 'weight':45.36, 'married':'False', 'alergies':['Nimonia', 'Rabies'], 'contact_details': {'phone':'7720820568'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)