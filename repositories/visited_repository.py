from db.run_sql import run_sql
from models.visited import Visit
from models.city import City
from models.country import Country
from models.user import User
from models.wishlist import Wishlist

def save(visit):
    sql = "INSERT INTO visited (city, user) VALUES (%s) RETURNING *"
    values = [visit.city.id, visit.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id
    return visit
