import os
import json


class Country:

    def __init__(self, name):
        self.name = name
        self.states = self.get_states()
        self.cities = self.get_cities()
 

    def __repr__(self):
        return str(self.__dict__)    


    def get_data(self):
        data_file = os.path.dirname(os.path.abspath(__file__)) + f'/{self.name}'.lower() + '.json'
        with open(data_file, 'r') as data:
            return json.load(data)
 
    
    def get_states(self):
        ''' Shows all states in given country.
        INPUT: A JSON Formatted File from https://simplemaps.com/data/de-cities.
        OUTPUT: Returns a list of states.  
        '''
        dt_list = self.get_data()
        states = []
        for index in range(len(dt_list)):
            state = dt_list[index]['admin']
            if state not in states:
                states.append(dt_list[index]['admin'])

        return states


    def get_cities(self):
        ''' Shows all cities in given country.
        INPUT: A JSON Formatted File from https://simplemaps.com/data/de-cities.
        OUTPUT: Returns a list of cities.  
        '''
        dt_list = self.get_data()
        cities = []
        for index in range(len(dt_list)):
            city = dt_list[index]['city'] 
            cities.append(city)

        return cities


    def get_states_and_cities(self):
        ''' A Dictionary with country, state and city info
        OUTPUT: A dictionary
        '''

        # create a dictionary with states in country
        info = {}
        for state in self.states:
            info[state] = []        

        # add cities to keys in dictionary
        dt_list = self.get_data()
        for city in dt_list:
            info.get(city['admin']).append(city['city'])

        return info


if __name__ == "__main__":

    # ----------------------------------- #
    # Tests

    new_country = Country('Germany')

    # print('<Cities and States in Germany>')
    # for key in new_country.__dict__:
    #     print('// ------------------------------------------ //')
    #     print(key, '=>', new_country.__dict__[key])

    print(new_country.get_states_and_cities())




