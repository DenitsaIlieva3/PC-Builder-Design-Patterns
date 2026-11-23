
from models.computer import Computer


class OfficePC(Computer):

    def get_description(self):
        return "Office PC - Computer for everyday office tasks"

    def get_price(self):
        return 650.00

    def get_performance(self):
        return 50


class GamingPC(Computer):

    def get_description(self):
        return "Gaming PC - Computer for gaming and demanding applications"

    def get_price(self):
        return 1200.00

    def get_performance(self):
        return 85


class ServerPC(Computer):

    def get_description(self):
        return "Server PC - Computer for data storage and server applications"

    def get_price(self):
        return 1800.00

    def get_performance(self):
        return 100
