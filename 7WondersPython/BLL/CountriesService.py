from DAL.SevenWondersContext import SevenWondersContext
import itertools

class CountriesService(object):
    def get_countries(self):
        context = SevenWondersContext()
        countries = context.exec_no_param_sproc(context.GET_COUNTRIES_SPROC)
        return countries

    def get_country(self, id):
        context = SevenWondersContext()
        country = context.exec_param_sproc(context.GET_COUNTRY_SPROC, [("id", id)])
        return country

    def add_country(self, country):
        context = SevenWondersContext()        
        id= country.get("id");
        name = country.get("name");
        context.exec_param_sproc(context.ADD_COUNTRY_SPROC, [("id", id), ("name", name)])
        return

    def is_name_valid(self, country):
        context = SevenWondersContext()
        id = country.get("id");
        name = country.get("name");
        isValid = context.exec_param_sproc(context.IS_COUNTRY_NAME_VALID, [("id", id), ("name", name)])
        return isValid;

    def delete_country(self, id):
        context = SevenWondersContext()
        context.exec_param_sproc(context.DELETE_COUNTRY_SPROC, [("id", id)])
        return