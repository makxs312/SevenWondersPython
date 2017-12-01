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

    def add_manager(self, immutableDictForm):
        context = SevenWondersContext()
        countries = immutableDictForm.getlist("countries[]")
        id = immutableDictForm.get("manager[Id]")
        firstName = immutableDictForm.get("manager[FirstName]")
        lastName = immutableDictForm.get("manager[LastName]")
        dateOfBirth = immutableDictForm.get("manager[DateOfBirth]")
        phoneNumber = immutableDictForm.get("manager[PhoneNumber]")
        email = immutableDictForm.get("manager[Email]")
        password = immutableDictForm.get("manager[Password]")
        countriesList = ",".join(countries)
        context.exec_param_sproc(context.ADD_MANAGER_SPROC,
                                 [("id", id),
                                  ("firstName", firstName),
                                  ("lastName", lastName),
                                  ("dateOfBirth", str(dateOfBirth)),
                                  ("phoneNumber", phoneNumber),
                                  ("email", str(email)),
                                  ("password", str(password)),
                                  ("countriesList", str(countriesList))])
        return