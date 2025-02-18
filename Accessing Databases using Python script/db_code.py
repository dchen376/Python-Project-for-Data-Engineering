import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

#Python scripting: Create and Load the table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
# Reading the CSV file
file_path = '/home/project/Accessing Databases using Python script/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)
# Loading the data to a table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')


#Python Scripting: Running basic queries on data
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#  create the dataframe of the new data.
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

conn.close()