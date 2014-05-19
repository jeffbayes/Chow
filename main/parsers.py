from locu import MenuItemApiClient
from locu import VenueApiClient
import datetime
import time

### parsers.py
### Locu parser classes go here.

global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Dish:
    def __init__(self,locuResult,searchTime=''):
        self.venue_client = VenueApiClient(KEY)
        self.attrs = {}
        self.searchTime = time.strftime( "%H:%M:%S",searchTime)
        self.searchDay = time.strftime("%A",searchTime)
        self.parse_locu(locuResult)
        
    def get_attr(self, attr):
        if attr in self.attrs:
            return self.attrs[attr]
        else:
            return "Data Not Available"

    def parse_locu(self,locuResult):
        """
        Takes Locu json and creates attributes dictonary.
        """

        self.attrs['name'] = locuResult["name"]
        self.attrs["description"] = locuResult["description"]
        self.attrs["price"] = locuResult["price"]
        self.attrs["venue"] = locuResult["venue"]["name"]
        self.attrs["venue_id"] = locuResult ["venue"]["id"]
        self.attrs["id"] = locuResult["id"]

        details = self.venue_client.get_details(locuResult["venue"]["id"])
        if self.searchDay:
            hours_today = details["objects"][0]["open_hours"][self.searchDay]
            if hours_today:        
                self.attrs["available"] = self.set_avalability(hours_today,self.searchTime)

    def set_avalability(self,hours,time):
        """
        Checks to see if dish is available at a given time. If no arguments is given
        it defaults to the current localtime time. 
        
        args: 
            hours: list  of hours i.e ["11:00:00 - 12:30:00","2:00:00-4:00:00"]
            time: "12:00:00"
        """
        
        for interval in hours:
            interval = interval.replace(' ','').split('-')
            start = interval[0]
            end = interval[1]
            if  start < time < end:
                return True
        return False

    def load_DB_attrs(self):
        """
        load the rating and number of ratings from database.
        """
        pass
        
        
class Venue:
    def __init__(self,locuResult,searchTime=''):
        self.venue_client = VenueApiClient(KEY)
        self.attrs = {}
        self.searchTime = time.strftime( "%H:%M:%S",searchTime)
        self.searchDay = time.strftime("%A",searchTime)
        self.parse_locu(locuResult)

    def get_attr(self,attr):
        if attr in self.attrs:
            return self.attrs[attr]
        else:
            return "Data Not Available"

    def parse_locu(self,locuResult):
        """
        Takes Locu json and creates attributes dictonary.
        """

        self.attrs['name'] = locuResult["name"]
        self.attrs["description"] = locuResult["description"]
        self.attrs["price"] = locuResult["price"]
        self.attrs["venue"] = locuResult["venue"]["name"]
        self.attrs["venue_id"] = locuResult ["venue"]["id"]
        self.attrs["id"] = locuResult["id"]

        details = self.venue_client.get_details(locuResult["venue"]["id"])
        if self.searchDay:
            hours_today = details["objects"][0]["open_hours"][self.searchDay]
            if hours_today:        
                self.attrs["available"] = self.set_avalability(hours_today,self.searchTime)

    def set_avalability(self,hours,time):
        """
        Checks to see if dish is available at a given time. If no arguments is given
        it defaults to the current localtime time. 
        
        args: 
            hours: list  of hours i.e ["11:00:00 - 12:30:00","2:00:00-4:00:00"]
            time: "12:00:00"
        """
        
        for interval in hours:
            interval = interval.replace(' ','').split('-')
            start = interval[0]
            end = interval[1]
            if  start < time < end:
                return True
        return False

    def load_DB_attrs(self):
        """
        load the rating and number of ratings from database.
        """
        pass
