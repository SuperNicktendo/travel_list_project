from db.run_sql import run_sql
from models.visited import Visit
from models.city import City
from models.country import Country
from models.user import User
from models.wishlist import Wishlist

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.visited_repository as visited_repository
import repositories.user_repository as user_repository

def save(wishlist):
    sql = "INSERT INTO wishlist (city_id, user_id) VALUES (%s, %s) RETURNING *"
    values = [wishlist.city.id, wishlist.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    wishlist.id = id
    return wishlist

def select_all():
    wishlist =[]
    sql = "SELECT * FROM wishlist"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        user = user_repository.select(row['user_id'])
        wishlist = Wishlist(city, user, row['id'])
        wishlist.append(wishlist)
    return wishlist