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

    def is_name_valid(self, id, name):
        context = SevenWondersContext()
        valid = context.exec_param_sproc(context.IS_NAME_VALID_SPROC, [("id", id), ("name", name)])
        return valid

    def delete_country(self, id):
        context = SevenWondersContext()
        context.exec_param_sproc(context.DELETE_COUNTRY_SPROC, [("id", id)])
        return