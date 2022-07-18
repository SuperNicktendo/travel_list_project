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

travel_blueprint = Blueprint("travel", __name__)

@travel_blueprint.route('/my_countries', methods=["GET"])
def show_countries():
    countries = country_repository.select_all()
    return render_template('visit/show_countries.html', all_countries = countries)

#ADD COUNTRY:
@travel_blueprint.route('/my_countries', methods=["POST"])
def add_country():
    country_name = request.form['country_id']
    country = Country(country_name)
    country_repository.save(country)
    places = country_repository.select_all()
    return redirect('/my_countries')