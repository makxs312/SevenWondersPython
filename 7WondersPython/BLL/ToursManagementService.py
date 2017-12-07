from DAL.SevenWondersContext import SevenWondersContext
import itertools

class ToursManagementService(object):
    def get_tours_for_manager(self, id):
        context = SevenWondersContext()
        result = context.exec_param_sproc(context.GET_TOURS_PAGE_MODEL, [("id", id)])
        return result