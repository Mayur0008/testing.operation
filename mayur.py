
from sqlalchemy import MetaData
metadata_obj = MetaData()
from sqlalchemy import Table, Column, Integer, String

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False),
)
employees = Table(
    "employees",
    metadata_obj,
    Column("employee_id", Integer, primary_key=True),
    Column("employee_name", String(60), nullable=False),
    Column("employee_dept", Integer, ForeignKey("departments.department_id")),
)
for t in metadata_obj.sorted_tables
    print(t.name)

