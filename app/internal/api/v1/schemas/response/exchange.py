from pydantic import BaseModel

class CourseResponseItem(BaseModel):
    direction: str
    value: float

class CourseResponse(BaseModel):
    exchanger: str
    courses: list[CourseResponseItem]