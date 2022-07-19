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
import repositories.visited_repository as visited_repository

visit_blueprint = Blueprint("visit", __name__)

@visit_blueprint.route('/visited/<id>', methods=["GET"])
def show_visited(id):
    visited = visited_repository.select_by_user_id(id)
    return render_template('visited/visited.html', all_cities=visited)
