import sqlalchemy as db
from sqlalchemy import select, func

# Create engine and connect to the SQLite database
engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()

# Define the Studentt table
Studentt = db.Table('Studentt', metadata,
                    db.Column('Id', db.Integer(), primary_key=True),
                    db.Column('Name', db.String(255), nullable=False),
                    db.Column('Major', db.String(255), default="Math"),
                    db.Column('marks', db.Integer(), default=35)
                    )

# Create the table in the database
metadata.create_all(engine)

# Insert data into the Studentt table
query = db.insert(Studentt)
values_list = [
    {'Id': 2, 'Name': 'mayur', 'Major': "Science", 'marks': 50},
    {'Id': 3, 'Name': 'nisha', 'Major': "Math", 'marks': 60},
    {'Id': 4, 'Name': 'mark', 'Major': "English", 'marks': 70}
]

# Transaction management with error handling
try:
    # Insert the values
    conn.execute(query, values_list)
    conn.commit()  # Commit the transaction

    # Create a query to count the number of students
    count_query = select([func.count()]).select_from(Studentt)

    # Execute the count query
    result = conn.execute(count_query)
    student_count = result.scalar()  # Get the count value

    print(f'Total number of students: {student_count}')

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()  # Ensure the connection is closed

    conn.close()  # Ensure the connection is closed
