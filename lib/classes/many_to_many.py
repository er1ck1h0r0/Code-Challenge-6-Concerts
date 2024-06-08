class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value)>0:
            self._name=value
        else:
            raise ValueError ("The name must not be an empty string")
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self,value):
        if isinstance(value,str) and len(value)>0:
            self._hometown=value
        else:
            raise ValueError("The hometown must not be an empty string")

    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self._name = name
        self._city = city
    
    @property
    def venue_name(self):
        return self._name
    
    @venue_name.setter
    def venue_name(self,value):
        if isinstance(value,str) and len(value) >0:
            self._name=value
        else:
            raise ValueError("Venue name must not be an empty string")
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self,value):
        if isinstance(value,str) and len(value)>0:
            self._city=value
        else:
            raise ValueError("City name must not be an empty string")

    def concerts(self):
        pass

    def bands(self):
        pass
