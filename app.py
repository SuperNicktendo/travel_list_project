from flask import Flask, render_template

from controllers.wishlist_controller import wishlist_blueprint
from controllers.city_controller import city_blueprint
from controllers.country_controller import country_blueprint
from controllers.user_controller import user_blueprint
from controllers.visited_controller import visit_blueprint

app = Flask(__name__)

app.register_blueprint(wishlist_blueprint)
app.register_blueprint(city_blueprint)
app.register_blueprint(country_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(visit_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)