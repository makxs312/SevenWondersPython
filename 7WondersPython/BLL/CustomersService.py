from DAL.SevenWondersContext import SevenWondersContext
import itertools

class CustomersService(object):
    def get_customers(self):
        context = SevenWondersContext()
        customers = context.exec_no_param_sproc(context.GET_CUSTOMERS_SPROC)
        return customers

    def change_customer_status(self, id):
        context = SevenWondersContext()
        context.exec_param_sproc(context.CHANGE_CUSTOMER_STATUS_SPROC, [("id", id)])
        return