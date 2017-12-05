from DAL.SevenWondersContext import SevenWondersContext
import itertools

class CitiesService(object):
    def get_cities(self):
        context = SevenWondersContext()
        cities = context.exec_no_param_sproc(context.GET_CITIES_SPROC)
        return cities
  
    def delete_city(self, id):
        print(id)
        context = SevenWondersContext()
        context.exec_param_sproc(context.DELETE_CITY_SPROC, [("id", id)])
        return

    def get_city(self, id):
        context = SevenWondersContext()
        city = context.exec_param_sproc(context.GET_CITY_SPROC, [("id", id)])
        return city[0]

    def add_city(self, city):
        context = SevenWondersContext()        
        id= city.get("Id");
        name = str(city.get("Name"));
        countryId = city.get("CountryId");
        context.exec_param_sproc(context.ADD_CITY_SPROC, [("id", id), ("name", name), ("countryId", countryId)])
        return

    def is_name_valid(self, city):
        context = SevenWondersContext()
        id = city.get("id");
        name = str(city.get("name"));
        countryId = city.get("countryId");
        isValid = context.exec_param_sproc(context.IS_CITY_NAME_VALID, [("id", id), ("name", name), ("countryId", countryId)])
        return isValid;


