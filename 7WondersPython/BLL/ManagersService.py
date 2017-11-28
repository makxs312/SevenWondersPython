from DAL.SevenWondersContext import SevenWondersContext
import itertools

class ManagersService(object):
    def get_managers(self):
        context = SevenWondersContext()
        managers = context.exec_no_param_sproc(context.GET_MANAGERS_SPROC)
        return managers

    def change_manager_status(self, id):
        context = SevenWondersContext()
        context.exec_param_sproc(context.CHANGE_MANAGER_STATUS_SPROC, [("id", id)])
        return