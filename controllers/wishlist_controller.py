from crypt import methods
from inspect import trace
from operator import methodcaller
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
from models.visited import Visit
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.visited_repository as visited_repository
import repositories.wishlist_repository as wishlist_repository


wishlist_blueprint = Blueprint("wishlist", __name__)

@wishlist_blueprint.route('/wishlist/<id>')
def show_wishlist(id):
    cities = wishlist_repository.select_by_user_id(id)
    return render_template('wishlist/wishlist.html', all_travel = cities)

@wishlist_blueprint.route('/wishlist/visited/add/<id>', methods=["GET"])
def add_to_visited(id, user_id=1):
    city = city_repository.select(id)
    user = user_repository.select(user_id)
    visited = Visit(city, user)
    visited_repository.save(visited)
    wishlist_repository.delete_by_city_and_user(id, user_id)
    return redirect(f'/visited/{user_id}')

# #DELETE FROM LIST
@wishlist_blueprint.route('/wishlist/<id>/delete', methods=['POST', 'GET'])
def delete_location(id, user_id =1):
    wishlist_repository.delete_by_city_and_user(id, user_id)
    return redirect(f'/wishlist/{user_id}')

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