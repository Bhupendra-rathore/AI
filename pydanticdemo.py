from pydantic import BaseModel, Field
from typing import List, Optional

class Student(BaseModel):
    name: str 
    age: Optional[int] = None
     
    cgpa: float = Field( ge=0.0, le=10.0,default=5.0)  # CGPA must be between 0.0 and 10.0
    branch: str='cse'

new_student={'name':'john','age':21,'cgpa':8.5,'branch':'ece'}
student =Student(**new_student)

print(type(student))
student_dict=dict(student)
print(student_dict['age'])
student_json=student.model_dump_json()
print(student_json)