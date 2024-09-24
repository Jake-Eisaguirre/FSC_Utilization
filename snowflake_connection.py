
# This script utlizes microsoft single log in to connect to the `ENTERPRISE` database in Snowflake
# and sets the search_path to the `CREW_ANALYTICS` Schema. A sample of how to query the database is
# provided below. 



# pip install `snowflake-connector-python` and `pandas` if not already installed

import snowflake.connector as sf
import pandas as pd
import getpass


# Connect to `ENTERPRISE` Database

try:
    # Prompt for email
    email = input("Enter your email: ")

    # Establish Snowflake connection
    con = sf.connect(
        user=email,
        account="hawaiianair.west-us-2.azure",
        warehouse="DATA_LAKE_READER",
        database="ENTERPRISE",
        authenticator="externalbrowser"
    )
    
    print("Database Connected!")
    

except sf.errors.DatabaseError as e:
    print("Unable to connect to Database.")


# Set search_path to `CREW_ANALYTICS` Schema
cursor = con.cursor()
cursor.execute("USE SCHEMA CREW_ANALYTICS")


# Sample of CT_DEADHEAD table in CREW_ANALYTICS schema in ENTERPRISE Database
query = """
    SELECT *
    FROM CT_DEADHEAD
    LIMIT 10;
"""
# Create cursor for query    
deadhead_cursor = cursor.execute(query)

# Fetch all rows from the query result
deadhead_list = deadhead_cursor.fetchall()

# Get column names from cursor description
columns = [desc[0] for desc in deadhead_cursor.description]

# Convert to dataframe 
deadhead_df = pd.DataFrame(deadhead_list, columns=columns)

# Print the DataFrame
print(deadhead_df)

# Close cursor and database connection if done with quries
cursor.close()
con.close()


