from DAL.SevenWondersContext import SevenWondersContext
import itertools

class FlightsService(object):
    def get_flights(self, pageIndex, pageSize):
        context = SevenWondersContext()
        managers = context.exec_param_sproc(context.GET_FLIGHTS_SPROC, [("pageIndex", pageIndex), ("pageSize", pageSize)])
        return managers

    def get_schedule(self, id):
        context = SevenWondersContext()
        schedule = context.exec_param_sproc(context.GET_SCHEDULE_SPROC, [("id", id)])
        return schedule