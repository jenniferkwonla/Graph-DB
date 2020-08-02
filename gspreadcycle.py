#!/usr/bin/env bash
"""
gspreadcycle module: has class GSpreadCycle with functions open, extract,
                    write_to_pickle, write_to_csv, read_from_csv and
                    properties header, data.
"""

from cells import Cell
import cells
from myutils import CleanData as cd
import copy
import csv
import gspread
import pickle
from oauth2client.service_account import ServiceAccountCredentials

_author_=["Jennifer Kwon", "Anne Wang", "Mauricio Lomeli"]
_date_ = "9/3/2019"
_credits_ = ["Rebecca Zhuo", "Smruti Vidwans"]
_email_="kwonjy3@uci.edu"
_status_="Prototype V 0.0.2"

json_keyfile_name = "Neo4j-Proj-1-7a1bf17c5f75.json"
spreadsheet_name = "TVShows"
worksheet_name = "Sheet1"
csv_filename = "TVShows_Holidays.csv"
_pickle_filename = "pickle_tv"     

class GSpreadCycle:

    def __init__(self):
        self.cells_values = None
        self.cells_class = None
        self.headers = None
        self.data_list = []  
        self.headers_list =[]
        self.cells_to_graph = [] #list of dictionaries

    def open(self,json_keyfile_name, spreadsheet_name, worksheet_name):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_name,scope)
        gs = gspread.authorize(creds)
        spreadsheet = gs.open(spreadsheet_name)
        self.worksheet = spreadsheet.worksheet(worksheet_name)

    def extract(self):
        self.cells_values = self.worksheet.get_all_records()
        self.cells_values = cd.delete_symbols(self, self.cells_values)
        print(type(self.cells_values))
        self.headers = self.cells_values[0].keys()
        cells_to_graph = copy.deepcopy(self.cells_values)
        self.cells_to_graph = cd.remove_empty_cell(self, cells_to_graph)

        count = len(self.cells_to_graph)
        i = 1
        while i <= count:
            for dictionary in self.cells_to_graph:
                print(dictionary)
                for key, value in dictionary.items():
                    c = Cell(i, key, value)
                    c.add_data()
                i+=1
        cells.Cell.save_data_to_file(_pickle_filename)

    def save_data_to_file(self, filename):

        with open(filename, 'wb') as file_object:
            serialized = self.cells_to_graph
            pickle.dump(serialized, file_object)
            file_object.close()
        
    def write_to_csv(self, csv_filename):
        with open(csv_filename, 'w') as f:
            writer = csv.DictWriter(f, self.headers)
            writer.writeheader()
            writer.writerows(self.cells_values)

    def read_from_csv(self, csv_filename):  
        with open(csv_filename) as f2:
            csv_reader = csv.DictReader(f2)
            self.data_list = list(csv_reader)
            self.headers_list = csv_reader.fieldnames
        
    @property
    def data(self):
        return self.data_list

    @data.setter
    def data(self, other_data_list):
        if isinstance(other_data, list):
            self.data_list.clear()
            self.data_list = other_data_list

    @property
    def headers(self):
        return self.headers_list
    
    @headers.setter
    def headers(self, other_headers_list):
        #self.headers.clear()
        self.headers_list = other_headers_list

    def __str__(self):
        return "data_list is too long to print"

def main():
    gc = GSpreadCycle()
    gc.open(json_keyfile_name, spreadsheet_name, worksheet_name)
    gc.extract()
    gc.write_to_csv(csv_filename)
    gc.read_from_csv(csv_filename)
    print("gspreadcycle.py run is complete")

if __name__ == "__main__":
    main()
