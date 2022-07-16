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

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = Country(result['name'], result['id'])
    return country

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)





