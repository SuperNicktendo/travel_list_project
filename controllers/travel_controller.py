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
    countries = country_repository.select_all()
    return render_template('visit/new_location.html', all_countries=countries)

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
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(city_name, country)
    city_repository.save(city)
    return redirect('/list')

#DELETE FROM LIST
@travel_blueprint.route('/list/<id>/delete', methods=['POST'])
def delete_location(id):
    city_repository.delete(id)
    return redirect('/list')

#DELETE COUNTRY

#EDIT 
@travel_blueprint.route('/<id>/edit', methods=["GET"])
def edit_location(id):
    city = city_repository.select(id)
    country = country_repository.select_all()
    return render_template('visit/edit.html', city = city, all_countries = country)

#UPDATE
@travel_blueprint.route('/<id>/edit', methods=["POST"])
def update_list(id):
    city_name = request.form("city-name")
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(city_name, country)
    city_repository.update(city)
    return redirect('/list')


#HAS VISITED 


