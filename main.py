import json
from pprint import pprint
import hashlib

counter = 0
URL = 'https://en.wikipedia.org/wiki/'
new_file = 'links_to_countries.txt'
main_file = 'countries.json'


class WikiIterators:

    def __init__(self, country_file):
        with open(country_file, encoding='UTF-8') as file:
            countries_list = json.load(file)
            country_names = (country['name']['common'] for country in countries_list)
            self.iter_country_names = iter(country_names)

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.iter_country_names)
        log = f'For the country {country_name} link - {self.get_link(country_name)}'
        return log

    def get_link(self, country_name: str):
        country_name = country_name.replace(' ', '_')
        country_url = f'{URL}{country_name}'
        return country_url


def hashing(hash_file: str):
    with open(hash_file, encoding='UTF-8') as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    with open(new_file, 'w', encoding='UTF-8') as country_links_file:
        for country_link in WikiIterators(main_file):
            counter += 1
            country_links_file.write(f'{counter} : {country_link}\n')
        counter = 0
    for hash_str in hashing(new_file):
        counter += 1
        print(f" {counter} : {hash_str}")
