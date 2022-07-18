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
import repositories.wishlist_repository as wishlist_repository


wishlist_blueprint = Blueprint("wishlist", __name__)

@wishlist_blueprint.route('/wishlist')
def bucket_list():
    places = wishlist_repository.select_all()
    return render_template('wishlist/wishlist.html', all_travel = places)

# @wishlist_blueprint.route('/new_location', methods=['GET'])
# def new_location():
#     countries = country_repository.select_all()
#     return render_template('visit/new_location.html', all_countries=countries)

# #ADD COUNTRY:
# @travel_blueprint.route('/my_countries', methods=["POST"])
# def add_country():
#     country_name = request.form['country_id']
#     country = Country(country_name)
#     country_repository.save(country)
#     places = country_repository.select_all()
#     return redirect('/my_countries')

# #ADD CITY


# #DELETE FROM LIST
# @travel_blueprint.route('/list/<id>/delete', methods=['POST'])
# def delete_location(id):
#     city_repository.delete(id)
#     return redirect('/list')

# #EDIT 
# @travel_blueprint.route('/<id>/edit', methods=["GET"])
# def edit_location(id):
#     city = city_repository.select(id)
#     country = country_repository.select_all()
#     return render_template('wishlist/edit.html', city = city, all_countries = country)

# # UPDATE
# @travel_blueprint.route('/<id>/edit', methods=["POST"])
# def update_list(id):
#     city_name = request.form["city-name"]
#     country_id = request.form["country_id"]
#     country = country_repository.select(country_id)
#     city = City(city_name, country)
#     city_repository.update(city)
#     return redirect('/list')    

# UPDATE VISITED


