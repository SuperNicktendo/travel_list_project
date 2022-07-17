from crypt import methods
from inspect import trace
from operator import methodcaller
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

travel_blueprint = Blueprint("travel", __name__)

@travel_blueprint.route('/list')
def bucket_list():
    places = city_repository.select_all()
    return render_template('visit/list.html', all_travel = places)

@travel_blueprint.route('/new_location', methods=['GET'])
def new_location():
    return render_template('visit/new_location.html')

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

#ADD CITY
@travel_blueprint.route('/list', methods=['POST'])
def add_cty():
    city_name = request.form["city-name"]
    country_name = request.form['country-name']
    country = country_repository[country_name]
    city = City(city_name, country)
    city_repository.save(city)
    return redirect('/list')


#DELETE FROM LIST
@travel_blueprint.route('/list/<id>/delete', methods=['POST'])
def delete_location(id):
    country_repository.delete(id)
    return redirect('/list')


