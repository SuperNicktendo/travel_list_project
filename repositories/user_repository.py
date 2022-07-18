from db.run_sql import run_sql
from models.user import User
from models.city import City
from models.country import Country
from models.visited import Visit

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user


