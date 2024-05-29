from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Integer, String

from leave_mgmt.models.partial_columns import NotNullColumn

Base = declarative_base()


class Designations(Base):
    __tablename__ = "designations"
    __table_args__ = {"schema": "std"}

    id = NotNullColumn(Integer, primary_key=True)
    name = NotNullColumn(String(length=255))


class Departments(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "std"}

    id = NotNullColumn(Integer, primary_key=True, autoincrement=True)
    name = NotNullColumn(String(length=255), unique=True)


class Employees(Base):
    __tablename__ = "employees"
    __table_args__ = {"schema": "std"}

    user_id = NotNullColumn(Integer, primary_key=True)
    emp_id = NotNullColumn(Integer, unique=True)
    full_name = NotNullColumn(String(length=255))
    email = NotNullColumn(String(length=255), unique=True)
    department_id = NotNullColumn(Integer, ForeignKey("std.departments.id"))
    designation_id = NotNullColumn(Integer, ForeignKey("std.designations.id"))


class LeaveTypes(Base):
    __tablename__ = "leave_types"
    __table_args__ = {"schema": "std"}

    id = NotNullColumn(Integer, primary_key=True)
    name = NotNullColumn(String(length=255))
    default_days = NotNullColumn(Integer)
    transferable_days = NotNullColumn(Integer)


class FiscalYears(Base):
    __tablename__ = "fiscal_years"
    __table_args__ = {"schema": "std"}

    id = NotNullColumn(Integer, primary_key=True)
    start_date = NotNullColumn(DateTime)
    end_date = NotNullColumn(DateTime)
    is_current = NotNullColumn(Boolean)


class Leaves(Base):
    __tablename__ = "leaves"
    __table_args__ = {"schema": "std"}

    id = NotNullColumn(Integer, primary_key=True)
    employee_id = NotNullColumn(Integer, ForeignKey("std.employees.user_id", ondelete="CASCADE"))
    start_date = NotNullColumn(Date)
    end_date = NotNullColumn(Date)
    leave_days = NotNullColumn(Integer)
    reason = NotNullColumn(String)
    status = NotNullColumn(String(length=255))
    leave_type_id = NotNullColumn(Integer, ForeignKey("std.leave_types.id"))
    fiscal_id = NotNullColumn(Integer, ForeignKey("std.fiscal_years.id"))
    created_at = NotNullColumn(DateTime)
    updated_at = NotNullColumn(DateTime)


class FlatFile(Base):
    __tablename__ = "flatfile"

    id = Column(String, primary_key=True)
    userId = Column(String)
    empId = Column(String)
    designationId = Column(String)
    designationName = Column(String)
    firstName = Column(String)
    middleName = Column(String)
    lastName = Column(String)
    email = Column(String)
    departmentDescription = Column(String)
    startDate = Column(String)
    endDate = Column(String)
    leaveDays = Column(String)
    reason = Column(String)
    status = Column(String)
    leaveTypeId = Column(String)
    leaveTypeName = Column(String)
    defaultDays = Column(String)
    transferableDays = Column(String)
    fiscalId = Column(String)
    fiscalStartDate = Column(String)
    fiscalEndDate = Column(String)
    fiscalIsCurrent = Column(String)
    createdAt = Column(String)
    updatedAt = Column(String)


class DimDesignations(Base):
    __tablename__ = "dim_designations"
    __table_args__ = {"schema": "dwh"}

    id = NotNullColumn(Integer, primary_key=True)
    name = NotNullColumn(String(length=255))


class DimDepartments(Base):
    __tablename__ = "dim_departments"
    __table_args__ = {"schema": "dwh"}

    id = NotNullColumn(Integer, primary_key=True, autoincrement=True)
    name = NotNullColumn(String(length=255), unique=True)


class DimEmployees(Base):
    __tablename__ = "dim_employees"
    __table_args__ = {"schema": "dwh"}

    user_id = NotNullColumn(Integer, primary_key=True)
    emp_id = NotNullColumn(Integer, unique=True)
    full_name = NotNullColumn(String(length=255))
    email = NotNullColumn(String(length=255), unique=True)


class DimLeaveTypes(Base):
    __tablename__ = "dim_leave_types"
    __table_args__ = {"schema": "dwh"}

    id = NotNullColumn(Integer, primary_key=True)
    name = NotNullColumn(String(length=255))
    default_days = NotNullColumn(Integer)
    transferable_days = NotNullColumn(Integer)


class DimFiscalYears(Base):
    __tablename__ = "dim_fiscal_years"
    __table_args__ = {"schema": "dwh"}

    id = NotNullColumn(Integer, primary_key=True)
    start_date = NotNullColumn(DateTime)
    end_date = NotNullColumn(DateTime)
    is_current = NotNullColumn(Boolean)


class FactLeaves(Base):
    __tablename__ = "fact_leaves"
    __table_args__ = {"schema": "dwh"}

    id = NotNullColumn(Integer, primary_key=True)
    employee_id = NotNullColumn(Integer, ForeignKey("dwh.dim_employees.user_id", ondelete="CASCADE"))
    start_date = NotNullColumn(Date)
    end_date = NotNullColumn(Date)
    leave_days = NotNullColumn(Integer)
    reason = NotNullColumn(String)
    status = NotNullColumn(String(length=255))
    leave_type_id = NotNullColumn(Integer, ForeignKey("dwh.dim_leave_types.id"))
    fiscal_id = NotNullColumn(Integer, ForeignKey("dwh.dim_fiscal_years.id"))
    department_id = NotNullColumn(Integer, ForeignKey("dwh.dim_departments.id"))
    designation_id = NotNullColumn(Integer, ForeignKey("dwh.dim_designations.id"))
    created_at = NotNullColumn(DateTime)
    updated_at = NotNullColumn(DateTime)


__all__ = [
    "Base",
    "Designations",
    "Employees",
    "LeaveTypes",
    "FiscalYears",
    "Leaves",
    "FlatFile",
    "DimDesignations",
    "DimEmployees",
    "DimLeaveTypes",
    "DimFiscalYears",
    "FactLeaves",
]
