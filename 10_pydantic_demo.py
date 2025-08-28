from pydantic import BaseModel,Field
from typing import Optional

class Student(BaseModel):
    name:str
    branch:str='AIDS'#default
    age:Optional[int]=None#optional
    cgpa:float=Field(gt=0,lt=10,default=5)#conditional

new_student={'name':'nitish'}

student=Student(**new_student)


print(type(student))
student_dict=dict(student)
print(student_dict['age'])
student_json=student.model_dump_json()