from db.run_sql import run_sql
from models.visited import Visit
from models.city import City
from models.country import Country
from models.user import User
from models.wishlist import Wishlist
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository

def save(visit):
    sql = "INSERT INTO visited (city_id, user_id) VALUES (%s, %s) RETURNING *"
    values = [visit.city.id, visit.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id
    return visit

def select_all():
    visits = []
    sql = "SELECT * FROM visited"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        user = user_repository.select(row['user_id'])
        visit = Visit(city, user, row['id'])
        visits.append(visit)
    return visits

def select_by_user_id(user_id):
    has_visited =[]
    sql = "SELECT * FROM visited WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)
    user = user_repository.select(user_id)
    for result in results:
        city = city_repository.select(result['city_id'])
        visited = Visit(city, user, result['id'])
        has_visited.append(visited)
    return has_visited
