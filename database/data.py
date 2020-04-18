import os
from flask import abort
import json

class Country:

    def __init__(self, name):
        self.name = name
        self.states = self.get_states()
        self.cities = self.get_cities()

    def __repr__(self):
        return str(self.__dict__)    

    def data_path(self):
        return os.getcwd() + '/' + f'{self.name}'.lower() + '.json'

    def get_states(self):
        ''' Shows all states in given country.
        INPUT: A JSON Formatted File from https://simplemaps.com/data/de-cities.
        OUTPUT: Returns a list of states.  
        '''
        # open data path and extract states
        with open(self.data_path(), 'r') as data:
            all_cities = json.load(data)
            states = []
            for index in range(len(all_cities)):
                state = all_cities[index]['admin']
                if state not in states:
                    states.append(all_cities[index]['admin'])

        return states


    def get_cities(self):
        ''' Shows all cities in given country.
        INPUT: A JSON Formatted File from https://simplemaps.com/data/de-cities.
        OUTPUT: Returns a list of cities.  
        '''
        with open(self.data_path(), 'r') as data:
            all_cities = json.load(data)
            cities = []
            for index in range(len(all_cities)):
                city = all_cities[index]['city'] 
                cities.append(city)

        return cities


    def show_info(self):
        ''' A Dictionary with country, state and city info
        OUTPUT: A dictionary
        '''
        info = {}
        for state in self.states:
            info[state] = []        

        return info


if __name__ == "__main__":

    # ----------------------------------- #
    # Tests

    new_country = Country('Germany')
    # print(new_country.__dict__.keys())

    print('<Cities and States in Germany>')
    for key in new_country.__dict__:
        print('// ------------------------------------------ //')
        print(key, '=>', new_country.__dict__[key])

    # print(new_country.show_info())



