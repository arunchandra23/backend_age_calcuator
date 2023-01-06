import sqlite3


import sqlite3
conn = sqlite3.connect('AgeCalculator', check_same_thread=False)
conn.execute("""CREATE TABLE IF NOT EXISTS requests
(
    "id" integer PRIMARY KEY AUTOINCREMENT,
    "name" character varying NOT NULL,
    "age" character varying NOT NULL,
    "dateOfBirth" character varying NOT NULL,
    "created_at" character varying NOT NULL
   
) """)
def executeQuery(query):
    conn = sqlite3.connect('AgeCalculator', check_same_thread=False)
    if("INSERT" in query or 'UPDATE' in query ):
        # try:
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()
            return "Updated successfully "
        # except :
        #     conn.close()
        #     return("Something Went Wrong")
    elif('DELETE' in query):
        # try:
            conn.execute(query)
            conn.commit()
            conn.close()
            return("Data Deleted")
        # except:
        #     conn.close()
        #     return("Something Went Wrong")

    else:
        # try:
            print(query)
            cursor=conn.execute(query)
            column_names = [desc[0] for desc in cursor.description]
            data=[]
            for i in cursor:
                a={}
                for b in column_names:
                    a[b]=i[column_names.index(b)]
                data.append(a)
            conn.close()
            return(data)
        # except:
        #     conn.close()
        #     return("Something Went Wrong")