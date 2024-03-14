from pydantic import BaseModel

class CourseRequest(BaseModel):
    symbols: str | None = None