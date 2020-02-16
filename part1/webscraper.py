# -*- coding: utf-8 -*-
"""
webscraper.py
Author: Eric Biscocho
Date: 02/05/2019
"""

import requests
from bs4 import BeautifulSoup
import csv

wikiLink = "https://en.wikipedia.org/wiki/"


class Oscars:
    def __init__(self):
        self.bestPictureWiki = wikiLink + "Academy_Award_for_Best_Picture"
        self.bestDirectorWiki = wikiLink + "Academy_Award_for_Best_Director"
        self.bestActorWiki = wikiLink + "Academy_Award_for_Best_Actor"
        self.bestActressWiki = wikiLink + "Academy_Award_for_Best_Actress"
        self.bestActorSuppWiki = wikiLink + "Academy_Award_for_Best_Supporting_Actor"
        self.bestActressSuppWiki = wikiLink + "Academy_Award_for_Best_Supporting_Actress"
        self.bestScreenplayOriginalWiki = wikiLink + "Academy_Award_for_Best_Original_Screenplay"
        self.bestScreenplayAdaptedWiki = wikiLink + "Academy_Award_for_Best_Adapted_Screenplay"

        self.best_picture()
        self.best_director()
        self.best_actor_actress()
        self.best_actor_actress(1)
        self.best_actor_actress(2)
        self.best_actor_actress(3)
        self.best_screenplay()
        self.best_screenplay(False)

    def best_picture(self):
        results = []
        response = requests.get(self.bestPictureWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, tr_tag in enumerate(content.findAll('tr', attrs={'style': 'background:#FAEB86'})):
            if i >= 66:
                for j, td_tag in enumerate(tr_tag.findAll('td')):
                    if j % 2 == 0:
                        title = td_tag.b.text.encode('utf-8', 'replace')
                    elif j % 2 == 1:
                        name = td_tag.b.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year,
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file="./data/oscars/best_picture.csv", cols=['name', 'title', 'year'], results=results)

    def best_director(self):
        results = []
        response = requests.get(self.bestDirectorWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, td_tag in enumerate(content.findAll('td', attrs={'style': 'background:#FAEB86;'})):
            if i >= 134:
                if i % 2 == 0:
                    name = td_tag.b.text.encode('ascii', 'replace')
                else:
                    title = td_tag.b.text.encode('ascii', 'replace')
                    entity = {
                        'name': name,
                        'title': title,
                        'year': year
                    }
                    results.append(entity)
                    year += 1

        self.create_csv(file="./data/oscars/best_director.csv", cols=['name', 'title', 'year'], results=results)

    def best_actor_actress(self, option=0):
        style = "background:#FAEB86;"
        if option == 0:
            response = requests.get(self.bestActorWiki)
            count = 201
            file = "./data/oscars/best_actor.csv"
        elif option == 1:
            response = requests.get(self.bestActressWiki)
            count = 201
            file = "./data/oscars/best_actress.csv"
        elif option == 2:
            response = requests.get(self.bestActorSuppWiki)
            style = "background:#FAEB86"
            count = 174
            file = "./data/oscars/best_actor_supporting.csv"
        else:
            response = requests.get(self.bestActressSuppWiki)
            count = 174
            file = "./data/oscars/best_actress_supporting.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, td_tag in enumerate(content.findAll('td', attrs={'style': style})):
            if i >= count:
                if i % 3 == 0:
                    name = td_tag.a.text.encode('ascii', 'replace')
                elif i % 3 == 2:
                    title = td_tag.a.text.encode('ascii', 'replace')
                    entity = {
                        'name': name,
                        'title': title,
                        'year': year
                    }
                    results.append(entity)
                    year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    def best_screenplay(self, original=True):
        if original:
            response = requests.get(self.bestScreenplayOriginalWiki)
            file = "./data/oscars/best_screenplay_original.csv"
        else:
            response = requests.get(self.bestScreenplayAdaptedWiki)
            file = "./data/oscars/best_screenplay_adapted.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        if original:
            for i, td_tag in enumerate(content.findAll('td', attrs={'style': 'background:#FAEB86'})):
                if i >= 106:
                    if i % 2 == 0:
                        title = td_tag.b.text.encode('ascii', 'replace')
                    elif i % 2 == 1:
                        name = td_tag.b.text.encode('ascii', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1
        else:
            for i, tr_tag in enumerate(content.findAll('tr', attrs={'style': 'background:#FAEB86'})):
                for j, td_tag in enumerate(tr_tag.findAll('td')):
                    if i >= 66:
                        if j % 3 == 0:
                            title = td_tag.b.text.encode('utf-8', 'replace')
                        elif j % 3 == 1:
                            name = td_tag.b.text.encode('utf-8', 'replace')
                            entity = {
                                'name': name,
                                'title': title,
                                'year': year,
                            }
                            results.append(entity)
                            year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    @staticmethod
    def create_csv(file, cols, results):
        """
        Helper function to write list of dicts to csv file.
        """
        try:
            with open(file, 'w') as f:
                w = csv.DictWriter(f, fieldnames=cols)
                w.writeheader()
                for data in results:
                    w.writerow(data)

        except IOError:
            print("I/O error")


class BAFTA:
    def __init__(self):
        self.bestFilmWiki = wikiLink + "BAFTA_Award_for_Best_Film"
        self.bestDirectionWiki = wikiLink + "BAFTA_Award_for_Best_Direction"
        self.bestActorLeadingWiki = wikiLink + "BAFTA_Award_for_Best_Actor_in_a_Leading_Role"
        self.bestActressLeadingWiki = wikiLink + "BAFTA_Award_for_Best_Actress_in_a_Leading_Role"
        self.bestActorSuppWiki = wikiLink + "BAFTA_Award_for_Best_Actor_in_a_Supporting_Role"
        self.bestActressSuppWiki = wikiLink + "BAFTA_Award_for_Best_Actress_in_a_Supporting_Role"
        self.bestScreenplayOriginalWiki = wikiLink + "BAFTA_Award_for_Best_Original_Screenplay"
        self.bestScreenplayAdaptedWiki = wikiLink + "BAFTA_Award_for_Best_Adapted_Screenplay"

        self.best_film()
        self.best_direction()
        self.best_actor_actress()
        self.best_actor_actress(1)
        self.best_actor_actress(2)
        self.best_actor_actress(3)
        self.best_screenplay()
        self.best_screenplay(False)

    def best_film(self):
        results = []
        response = requests.get(self.bestFilmWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, td_tag in enumerate(content.findAll('td', attrs={'style': 'background:#ccc;'})):
            if i >= 111:
                if i % 3 == 0:
                    title = td_tag.b.text.encode('utf-8', 'replace')
                elif i % 3 == 2:
                    name = td_tag.b.text.encode('utf-8', 'replace')
                    entity = {
                        'name': name,
                        'title': title,
                        'year': year
                    }
                    results.append(entity)
                    year += 1

        self.create_csv(file="./data/bafta/best_film.csv", cols=['name', 'title', 'year'], results=results)

    def best_direction(self):
        results = []
        response = requests.get(self.bestDirectionWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, tr_tag in enumerate(content.findAll('tr', attrs={'style': 'background:#B0C4DE;'})):
            if i > 24:
                for j, b_tag in enumerate(tr_tag.findAll('b')):
                    if j % 2 == 0:
                        name = b_tag.text.encode('utf-8', 'replace')
                    elif j % 2 == 1:
                        title = b_tag.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file="./data/bafta/best_direction.csv", cols=['name', 'title', 'year'], results=results)

    def best_actor_actress(self, option=0):
        if option == 0:
            response = requests.get(self.bestActorLeadingWiki)
            count = 68
            file = "./data/bafta/best_actor.csv"
        elif option == 1:
            response = requests.get(self.bestActressLeadingWiki)
            count = 57
            file = "./data/bafta/best_actress.csv"
        elif option == 2:
            response = requests.get(self.bestActorSuppWiki)
            count = 24
            file = "./data/bafta/best_actor_supporting.csv"
        else:
            response = requests.get(self.bestActressSuppWiki)
            count = 24
            file = "./data/bafta/best_actress_supporting.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, tr_tag in enumerate(content.findAll('tr', attrs={'style': 'background:#B0C4DE;'})):
            if i > count:
                for j, b_tag in enumerate(tr_tag.findAll('b')):
                    if j % 3 == 0:
                        name = b_tag.text.encode('utf-8', 'replace')
                    elif j % 3 == 1:
                        title = b_tag.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    def best_screenplay(self, original=True):
        if original:
            response = requests.get(self.bestScreenplayOriginalWiki)
            file = "./data/bafta/best_screenplay_original.csv"
        else:
            response = requests.get(self.bestScreenplayAdaptedWiki)
            file = "./data/bafta/best_screenplay_adapted.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, tr_tag in enumerate(content.findAll('tr', attrs={'style': 'background:#B0C4DE;'})):
            if i > 10:
                for j, b_tag in enumerate(tr_tag.findAll('b')):
                    if j % 3 == 0:
                        title = b_tag.text.encode('utf-8', 'replace')
                    elif j % 3 == 1:
                        name = b_tag.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    @staticmethod
    def create_csv(file, cols, results):
        """
        Helper function to write list of dicts to csv file.
        """
        try:
            with open(file, 'w') as f:
                w = csv.DictWriter(f, fieldnames=cols)
                w.writeheader()
                for data in results:
                    w.writerow(data)

        except IOError:
            print("I/O error")


class Guilds:
    def __init__(self):
        self.motionPictureWiki = wikiLink + "Producers_Guild_of_America_Award_for_Best_Theatrical_Motion_Picture"
        self.featureFilmWiki = wikiLink + "Directors_Guild_of_America_Award_for_Outstanding_Directing_–_Feature_Film"
        self.sagPrefix = "Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_"
        self.bestActorWiki = wikiLink + self.sagPrefix + "Male_Actor_in_a_Leading_Role"
        self.bestActressWiki = wikiLink + self.sagPrefix + "Female_Actor_in_a_Leading_Role"
        self.bestActorSuppWiki = wikiLink + self.sagPrefix + "Male_Actor_in_a_Supporting_Role"
        self.bestActressSuppWiki = wikiLink + self.sagPrefix + "Female_Actor_in_a_Supporting_Role"
        self.bestScreenplayOriginalWiki = wikiLink + "Writers_Guild_of_America_Award_for_Best_Original_Screenplay"
        self.bestScreenplayAdaptedWiki = wikiLink + "Writers_Guild_of_America_Award_for_Best_Adapted_Screenplay"

        self.pga()
        self.dga()
        self.sag()
        self.sag(1)
        self.sag(2)
        self.sag(3)
        self.wga()
        self.wga(False)

    def pga(self):
        results = []
        response = requests.get(self.motionPictureWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, table_tag in enumerate(content.findAll('table', attrs={'class': 'wikitable', 'cellpadding': '5'})):
            for j, td_tag in enumerate(table_tag.findAll(name=['td', 'tr'], attrs={'style': 'background:#FAEB86;'})):
                if (i == 1 and j > 7) or (i > 1):
                    if j % 2 == 0:
                        title = td_tag.b.text.encode('utf-8', 'replace')
                    else:
                        name = td_tag.b.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file="./data/pga/motion_picture.csv", cols=['name', 'title', 'year'], results=results)

    def dga(self):
        results = []
        response = requests.get(self.featureFilmWiki)
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, table_tag in enumerate(content.findAll('table', attrs={'class': 'wikitable', 'cellpadding': '5'})):
            for j, td_tag in enumerate(table_tag.findAll('td', attrs={'style': 'background:#FAEB86;'})):
                if (i == 5 and j > 7) or (i > 5):
                    if j % 2 == 0:
                        name = td_tag.b.text.encode('utf-8', 'replace')
                    else:
                        title = td_tag.b.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file="./data/dga/feature_film.csv", cols=['name', 'title', 'year'], results=results)

    def sag(self, option=0):
        attrs = {'class': 'wikitable', 'cellpadding': '5'}
        if option == 0:
            response = requests.get(self.bestActorWiki)
            file = "./data/sag/best_actor.csv"
        elif option == 1:
            response = requests.get(self.bestActressWiki)
            file = "./data/sag/best_actress.csv"
        elif option == 2:
            response = requests.get(self.bestActorSuppWiki)
            file = "./data/sag/best_actor_supporting.csv"
        else:
            response = requests.get(self.bestActressSuppWiki)
            attrs = {'cellpadding': '4'}
            file = "./data/sag/best_actress_supporting.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for table_tag in content.findAll('table', attrs=attrs):
            for i, td_tag in enumerate(table_tag.findAll('td', attrs={'style': 'background:#FAEB86;'})):
                if i % 3 == 0:
                    name = td_tag.b.text.encode('utf-8', 'replace')
                elif i % 3 == 1:
                    title = td_tag.b.text.encode('utf-8', 'replace')
                    entity = {
                        'name': name,
                        'title': title,
                        'year': year
                    }
                    results.append(entity)
                    year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    def wga(self, original=True):
        if original:
            response = requests.get(self.bestScreenplayOriginalWiki)
            attrs = {'style': 'background:#FAEB86'}
            file = "./data/wga/screenplay_original.csv"
        else:
            response = requests.get(self.bestScreenplayAdaptedWiki)
            attrs = {'style': 'background:#FAEB86;'}
            file = "./data/wga/screenplay_adapted.csv"

        results = []
        content = BeautifulSoup(response.content, 'html.parser')
        year = 1994

        for i, table_tag in enumerate(content.findAll('table', attrs={'class': 'wikitable'})):
            for j, td_tag in enumerate(table_tag.findAll('td', attrs=attrs)):
                if (i == 3 and j > 7) or (i > 3):
                    if j % 2 == 0:
                        title = td_tag.b.text.encode('utf-8', 'replace')
                    else:
                        name = td_tag.b.text.encode('utf-8', 'replace')
                        entity = {
                            'name': name,
                            'title': title,
                            'year': year
                        }
                        results.append(entity)
                        year += 1

        self.create_csv(file=file, cols=['name', 'title', 'year'], results=results)

    @staticmethod
    def create_csv(file, cols, results):
        """
        Helper function to write list of dicts to csv file.
        """
        try:
            with open(file, 'w') as f:
                w = csv.DictWriter(f, fieldnames=cols)
                w.writeheader()
                for data in results:
                    w.writerow(data)

        except IOError:
            print("I/O error")


if __name__ == '__main__':
    oscars = Oscars()
    baftas = BAFTA()
    guilds = Guilds()
