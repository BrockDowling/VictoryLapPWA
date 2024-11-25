from logging import raiseExceptions
import psycopg
from psycopg import connect
# import routes for info 
from app import routes

DBUrl = ("Secret Key")
# Create connection and cursor objects
try:
    conn = psycopg.connect(DBUrl)
    print("Connected to PostgreSQL")
except:
    raise Exception("Cannot connect to PostgreSQL")


cur = conn.cursor()


# current_user_id = api call to get username, get user_id where username = usernmae

data_query = (""" WITH temp as (SELECT weight, weightused, setschosen, repschosen, RANK () OVER (partition by workoutid ORDER BY timelogged DESC) as ranked FROM Users
                LEFT JOIN WorkoutQuestions on workoutquestions.userid = users.userid) select * from temp where ranked = 1 AND UserID = current_user_id""")

cur.execute(data_query)
# need to alter for flask implementation
result_data = cur.fetchall()
print(result_data)
print(type(result_data))
# returns it as multiple entrys for that user
# grabs all users entrys but iterable so can work for one or many

def calc_score(entry):
    total_score = 0.0
    for i in range(len(entry)):
        score = 0
        score = ((entry[i][1] / entry[i][0]) * (entry[i][2] * entry[i][3]))
        total_score += score
    return print("Workout Score for User is:", total_score)

try:
    calc_score(result_data)
    # insert into database user workout score for workout at dateentered 
except:
    raise Exception("Cannot calculate workout score")


conn.commit()
conn.close()
cur.close()
