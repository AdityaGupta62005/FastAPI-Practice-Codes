from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city':'Pune', 'state':'Maharashtra', 'pin':'450036'}

address1 = Address(**address_dict)

patient_dict = {'name':'Parth','gender':'Male','age':53, 'address':address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump_json()
# temp = patient1.model_dump()
# temp = patient1.model_dump(include=['name', 'age'])
# temp = patient1.model_dump(exclude=['name', 'age'])
# temp = patient1.model_dump(exclude={'address':['state']})
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))