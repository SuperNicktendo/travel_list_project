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

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route('/user', methods=["GET"])
def show_users():
    user = user_repository.select_all()
    return render_template('user/user.html', all_users = user)
