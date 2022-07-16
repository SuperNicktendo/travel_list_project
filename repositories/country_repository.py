from db.run_sql import run_sql
from models.country import Country
from models.city import City
import repositories.city_repository as city_repository


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country