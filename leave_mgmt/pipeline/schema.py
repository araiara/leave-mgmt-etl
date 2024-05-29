import typing as ty
from datetime import date, datetime

from pydantic import BaseModel


class LeaveEventSchema(BaseModel):
    id: int
    userId: int
    empId: str
    designationId: int
    designationName: str
    firstName: str
    middleName: ty.Optional[str]
    lastName: str
    email: str
    departmentDescription: str
    startDate: date
    endDate: date
    leaveDays: int
    reason: str
    status: str
    leaveTypeId: int
    leaveTypeName: str
    defaultDays: int
    transferableDays: int
    fiscalId: int
    fiscalStartDate: datetime
    fiscalEndDate: datetime
    fiscalIsCurrent: bool
    createdAt: datetime
    updatedAt: datetime
