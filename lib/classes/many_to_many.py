class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Band name must not be an empty string")
        self._name = value
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Hometown of the band must not be an empty string')
        if hasattr(self, '_hometown'):
            raise AttributeError('The hometown is immutable')
        self._hometown = value

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        self._concerts.append(new_concert)
        venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all_concerts= []
    
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("The date must bot be an emppty string")
        self._date = value
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("Concert venue must be of type Venue")
        self._venue = value

    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise ValueError("Concert band must be of type Band")
        self._band = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("The venue name must not be an empty string")
        self._name = value
         
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("The city name must not be an empty string")
        self._city = value

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise ValueError("Only Concert instances can be added")
        self._concerts.append(concert)

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self]

    def bands(self):
        return  list({concert.band for concert in self.concerts()})
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None
