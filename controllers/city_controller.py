from crypt import methods
from inspect import trace
from operator import methodcaller
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.visited_repository as user_repository

city_blueprint = Blueprint("city", __name__)

@city_blueprint.route('/my_cities', methods=["GET"])
def show_cities():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template('city/my_cities.html', all_cities = cities, all_countries = countries)

@city_blueprint.route('/my_cities', methods=['POST'])
def add_city():
    city_name = request.form["city-name"]
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(city_name, country)
    city_repository.save(city)
    return redirect('/my_cities')