from dateutil import parser
from datetime import *
from math import sqrt
import json


import requests

requests.get('https://sh-mockapi.azurewebsites.net/api/ticketprice?eventId={eventId}')

class City:
    def __init__(self, Name: str, xCor: int, yCor: int):
        self.Name = Name
        self.xCor = xCor
        self.yCor = yCor
'''
/*-------------------------------------
        Coordinates are roughly to scale with miles in the USA

           2000 +----------------------+  
                |                      |  
                |                      |  
             Y  |                      |  
                |                      |  
                |                      |  
                |                      |  
                |                      |  
             0  +----------------------+  
                0          X          4000

        ---------------------------------------*/
'''

cityMap : dict[str, City]= {
        'New York': City('New York', 3572, 1455),
        'Los Angeles': City('Los Angeles', 462, 975),
        'Boston': City('Boston', 3778, 1566),
        'Chicago': City('Chicago', 2608, 1525),
        'San Francisco': City('San Francisco', 183, 1233),
        'Washington': City('Washington', 3358, 1320)
    }

class MarketingEngine():
    def __init__(self, events):
        self.events = events
    
    def SendCustomerNotifications(self, customer):
        if customer is None:
            raise Exception("Invalid customer")
        print("Hi dear customer: ", customer.Name)
        
        for event in self.events:
            if event.City == customer.City:
                print("We'd like recommend you the event %s on date %s" %(event.Name, event.EventDate))

    
    def SendBirthdayEventNotification(self, customer):
        closest_birthday_event, lowest_date_diff = (None, None)
        birth_date = datetime(datetime.now().year, customer.BirthDate.month, customer.BirthDate.day)

        if (datetime.now() - birth_date).days > 0:
            birth_date = datetime(datetime.now().year + 1, customer.BirthDate.month, customer.BirthDate.day)
        
        for event in self.events:
            if lowest_date_diff is None or abs(event.EventDate - birth_date) < lowest_date_diff:
                lowest_date_diff = abs(event.EventDate - birth_date)
                closest_birthday_event = event
        
        print("We have an event around your birthday! Check out: %s, city: %s, date: %s" %(closest_birthday_event.Name, closest_birthday_event.City, closest_birthday_event.EventDate))


    def ComputeNearestEvents(self, customer, k=5, should_print=True):
        (x1, y1) = (cityMap[customer.City].xCor, cityMap[customer.City].yCor)
        distance_to_events = []


        for event in self.events:
            (x2, y2) = (cityMap[event.City].xCor, cityMap[event.City].yCor)
            dist = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
            distance_to_events.append((dist, event))

        distance_to_events.sort(key=lambda elem: elem[0])  # Time: O(n log n)
        distance_to_events = distance_to_events[:k]

        if should_print:
            for (dist, event) in distance_to_events:
                print("These are the nearest events to you (name, city, date): ", event.Name, event.City, event.EventDate)
        
        return distance_to_events


    def ComputePricesForNearestPerMiles(self, customer, miles_limit):
        all_events_li = self.ComputeNearestEvents(customer, k=len(self.events), should_print=False)
        events_li = [(dist, event) for (dist, event) in all_events_li if sqrt(dist) <= miles_limit]
        output = []

        for (dist, event) in events_li:
            try:
                response = requests.get('https://sh-mockapi.azurewebsites.net/api/ticketprice?eventId=' + str(event.Id)).content
                response = json.loads(response)
                print(response)
                output.append((float(response["Price"]), event))
            except:
                print("API Request failed")
        
        output.sort(key=lambda elem: elem[0])  # Time: O(n log n)
        for (price, event) in output:
                print("These are the events (price asc) near you (price, name, city, date): ", price, event.Name, event.City, event.EventDate)

        return output



class Event :
    def __init__(self, Id, Name, City, EventDate) :
        self.Id = Id
        self.Name = Name
        self.City = City 
        self.EventDate = EventDate
        

class Customer :
    def __init__(self, Id, Name, City, BirthDate) :
        self.Id = Id
        self.Name = Name
        self.City = City
        self.BirthDate = BirthDate

def main():
    events: list[Event] = [
        Event(1, "Phantom of the Opera", "New York", parser.parse('2023-12-23')),
        Event(2, "Metallica", "Los Angeles", parser.parse('2023-12-02')),
        Event(3, "Metallica", "New York", parser.parse('2023-12-06')),
        Event(4, "Metallica", "Boston", parser.parse('2023-10-23')),
        Event(5, "LadyGaGa", "New York", parser.parse('2023-09-20')),
        Event(6, "LadyGaGa", "Boston", parser.parse('2023-08-01')),
        Event(7, "LadyGaGa", "Chicago", parser.parse('2023-07-04')),
        Event(8, "LadyGaGa", "San Francisco", parser.parse('2023-07-07')),
        Event(9, "LadyGaGa", "Washington", parser.parse('2023-05-22')),
        Event(10, "Metallica", "Chicago", parser.parse('2023-01-01')),
        Event(11, "Phantom of the Opera", "San Francisco", parser.parse('2023-07-04')),
        Event(12, "Phantom of the Opera", "Chicago",parser.parse('2024-05-15'))
    ]

    customer: Customer = Customer(Id = 1, Name ="John", City = "New York", BirthDate = parser.parse('1995-05-10'))

    engine: MarketingEngine = MarketingEngine(events)

    engine.SendCustomerNotifications(customer)
    engine.SendBirthdayEventNotification(customer)
    engine.ComputeNearestEvents(customer)
    engine.ComputePricesForNearestPerMiles(customer, 200)
    engine.ComputePricesForNearestPerMiles(customer, 10000)


if __name__ == '__main__':
    main()
