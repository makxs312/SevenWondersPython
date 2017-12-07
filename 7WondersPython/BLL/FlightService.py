from DAL.SevenWondersContext import SevenWondersContext
import itertools

class FlightService(object):
    def get_flight_short_info(self, id):
        context = SevenWondersContext()
        result = context.exec_param_sproc(context.GET_FLIGHT_SHORT_INFO_MODEL, [("id", id)])
        return result