import pypyodbc
pypyodbc.lowercase = False

class SevenWondersContext(object):
    GET_MANAGERS_SPROC = "[dbo].[GetManagers]"
    GET_CUSTOMERS_SPROC = "[dbo].[GetCustomers]"
    GET_MANAGER_SPROC = "[dbo].[GetManager]"
    CHANGE_MANAGER_STATUS_SPROC = "[dbo].[ChangeManagerStatus]"
    CHANGE_CUSTOMER_STATUS_SPROC = "[dbo].[ChangeCustomerStatus]"
    EDIT_MANAGER_SPROC = "[dbo].[EditManager]"
    ADD_MANAGER_SPROC = "[dbo].[AddManager]"
    GET_COUNTRIES_FOR_MANAGER_SPROC = "[dbo].[GetCountriesForManager]"

    GET_COUNTRIES_SPROC = "[dbo].[GetCountries]"
    DELETE_COUNTRY_SPROC = "[dbo].[DeleteCountry]"
    GET_COUNTRY_SPROC = "[dbo].[GetCountry]"
    ADD_COUNTRY_SPROC = "[dbo].[AddCountry]"
    IS_COUNTRY_NAME_VALID = "[dbo].[IsCountryNameValid]"

    GET_CITIES_SPROC = "[dbo].[GetCities]"
    DELETE_CITY_SPROC = "[dbo].[DeleteCity]"
    GET_CITY_SPROC = "[dbo].[GetCity]"
    ADD_CITY_SPROC = "[dbo].[AddCity]"
    IS_CITY_NAME_VALID = "[dbo].[IsCityNameValid]"

    GET_TOURS_PAGE_MODEL = "[dbo].[GetToursPageModel]"
    GET_FLIGHT_SHORT_INFO_MODEL = "[dbo].[GetFlightShortInfoModel]"

    SEPARATOR = ","

    def exec_no_param_sproc(self, sproc_name):
        return self.__exec_sproc(sproc_name)

    def exec_param_sproc(self, sproc_name, params):
        return self.__exec_sproc(sproc_name, params)

    def __connect(self):
        connection = pypyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=(localdb)\MSSQLLocalDB;Database=SevenWonders;Trusted_Connection=Yes;')
        return connection.cursor()

    def __construct_command(self, sproc_name, params = None):
        sql_command = "exec " + sproc_name
        if params:
            param_strings = []
            for param in params:
                if isinstance(param[1], str):
                    param_strings.append("@" + param[0] + " = N'" + str(param[1]) + "'")
                elif param[1] is None:
                    continue
                else:
                    param_strings.append("@" + param[0] + " = " + str(param[1]))
            sql_command += self.SEPARATOR.join(param_strings)
        return sql_command

    def __read_results(self, cursor):
        query_results = []
        if cursor.description:
            columns = [column[0] for column in cursor.description]
            query_row = cursor.fetchone()
            while query_row:
                query_results.append(dict(zip(columns, query_row)))
                query_row = cursor.fetchone()
        return query_results

    def __disconnect(self, cursor):
        connection = cursor.connection
        connection.commit()
        connection.close()

    def __exec_sproc(self, sproc_name, params=None):
        cursor = self.__connect()
        sql_command = self.__construct_command(sproc_name, params)
        cursor.execute(sql_command)
        query_results = self.__read_results(cursor)
        self.__disconnect(cursor)
        return query_results