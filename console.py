import pdb
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country1 = Country("Japan")
country_repository.save(country1)
country2 = Country("Italy")
country_repository.save(country2)
country3 = Country("France")
country_repository.save(country3)
country4 = Country("Spain")
country_repository.save(country4)

city1 = City("Tokyo", country1)
city_repository.save(city1)
city2 = City("Venice", country2)
city_repository.save(city2)
city3 =City("Rome", country2)
city_repository.save(city3)
city4 = City("Paris", country3)
city_repository.save(city4)
city5 = City("Barcelona", country4)
city_repository.save(city5)



pdb.set_trace()