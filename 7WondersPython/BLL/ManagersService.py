from DAL.SevenWondersContext import SevenWondersContext
import itertools

class ManagersService(object):
    def get_managers(self):
        context = SevenWondersContext()
        managers = context.exec_no_param_sproc(context.GET_MANAGERS_SPROC)
        return managers

    def get_countries(self):
        context = SevenWondersContext()
        countries = context.exec_no_param_sproc(context.GET_COUNTRIES_SPROC)
        return countries

    def get_manager(self, id):
        context = SevenWondersContext()
        manager = context.exec_param_sproc(context.GET_MANAGER_SPROC, [("id", id)])
        return manager

    def change_manager_status(self, id):
        context = SevenWondersContext()
        context.exec_param_sproc(context.CHANGE_MANAGER_STATUS_SPROC, [("id", id)])
        return