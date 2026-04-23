from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'Pune', 'state':'Maharashtra', 'pin':'450036'}

address1 = Address(**address_dict)

patient_dict = {'name':'Parth','gender':'Male','age':53, 'address':address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)



# Better Organization of related data(eg. vitals, address, )
# Reusability: Use Vitals in multiple models(eg. Patient, MedicalRecord )
# Readability: Easier for developer and API consumers to understand
# Validation: Nested models are validated automatically-no extra work needed