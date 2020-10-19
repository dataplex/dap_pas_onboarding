class ConjurRole:
    def __init__(self, account, resource_type, name, api_key):
        self.__account = account
        self.__resource_type = resource_type
        self.__name = name
        self.__api_key = api_key

    @property
    def account(self):
        return self.__account

    @property
    def name(self): 
        return self.__name

    @property
    def login_name(self):
        if self.__resource_type == "host":
            return 'host/' + self.__name

        return self.__name

    @property
    def api_key(self):
        return self.__api_key