from dataclasses import dataclass

from pydantic import BaseModel, EmailStr


class CustomerModel(BaseModel):
    name: str
    Email: EmailStr
