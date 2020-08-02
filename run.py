#!/usr/bin/env bash
'''
run.py module : things to revise: __raw_data() and __test()
'''

from cells import Cell
from gspreadcycle import GSpreadCycle as gs
from listnode import ListNode, SingleLinkedList
from neo4jdriver import DriverLifecycle, Neo4jDatabase
from myutils import DataFile
from myutils import CleanData 
import cells
import myutils
import gspreadcycle
import pickle
import csv

_author_=["Jennifer Kwon"]
_date_ = "2019"
_email_="kwonjy3@uci.edu"

csv_filename = "netflix_titles.csv"
_pickle_filename = "data_pickle"

uri= "bolt://localhost:7687"
user = "neo4j"
password = "jenniferkwon"


nodes = []
dict_list=[]

def __read(filename):

    '''
    __read(filename): read data from csv file.
    '''

    i = 0
    f=0
    csv_reader = csv.reader(open(csv_filename, 'r'))
    fields = next(csv_reader)
    for row in csv_reader:
        while(f < len(fields)):
            c = Cell(i, fields[0], row[f])
            c.add_data()
            dict_list.append(dict(ID=i, header=fields[f], content=row[f]))
            nodes.append(c)
            f+=1
        f=0    
        i+=1

def __save(filename):

    '''
     __savefilename): saves data from csv file to pickle file.
    '''

    with open(filename, 'wb') as file_object:
        serialized = dict_list
        pickle.dump(serialized, file_object)
        file_object.close()

def __restore(filename):

    '''
    __restore(filename): restores pickle file of into nodes list.
    '''

    with open(filename, 'rb') as file_object:
        raw_data = file_object.read()
    deserialized = pickle.loads(raw_data)
    file_object.close()
    global nodes
    nodes = deserialized

    
def __raw_data():

    '''
    __raw_data(): Analyzes data files for word count and word occurrences.

    Needs revising.
    '''

    df = DataFile("data_file")
    for i in data:
        dictionary = dict(i)
        for key,value in dictionary.items():
            df.write(key + ',' + value + ' | ')
            myutils.word_count(value)

    df.write("\nOccurrences of words\n")
    for word, count in myutils.occurrences.items():
        text = "{0}: {1} \n".format(word, count)
        df.writelines(text)
        
    df.close()

def __clean():

    '''
    __clean(): Cleans list of nodes of symbols to query.
    '''

    cleandata = CleanData()
    cleandata.delete_symbols(nodes)


def __graph(center_node):

    '''
    __graph(): graph visualiztion of csv file in neo4j browser.
    '''

    dr = DriverLifecycle(uri, user, password)
    session = dr.get_session()
    db = Neo4jDatabase()
    db.delete_all_nodes(session)
    db.delete_all_relationships(session)
    
    for i in nodes:
        db.insert_cell(session, i)

    linked_list = SingleLinkedList()

    # DO NOT CHANGE
    count = len(nodes)
    i = 1
    while i <= count:
        for c in nodes:
            if c['ID'] == i: #if c.ID == i: 
                linked_list.append_node(c)
                if c['header'] == center_node: #if c.header == center_node:
                    cellB = c
        index = 0
        while index < linked_list.list_length():
            cellA = linked_list.traverse_list(index, linked_list.list_length())
            #if cellA.header == center_node:
               # continue
            if cellB is not None and cellA is not None:
                db.linkCells(session, cellA, cellA['header'], cellB) #db.linkCells(session, cellA, cellA.header, cellB)
                cellA = None
            index+=1
        linked_list.destroy()
        i+=1
    dr.close()

    
def __test(start_node, end_node):
    """
    __test(start_node, end_node): pass start_node and end_node that will display nodes and relationships.

    Need revising.
    """

    dr = DriverLifecycle(uri, user, password)
    session = dr.get_session()
    db = Neo4jDatabase()
    db.delete_all_nodes(session)
    db.delete_all_relationships(session)
    
    #for i in nodes:
    #    db.insert_cell(session, i)

    linked_list = SingleLinkedList()

    # DO NOT CHANGE
    count = len(nodes)
    i = 1
    while i <= count:
        for n in nodes:
            if n.ID == i:
                linked_list.append_node(n)
        cellA = linked_list.search_list(start_node) 
        cellB = linked_list.search_list(end_node)
        if cellB is not None and cellA is not None:
            db.linkCells(session, cellA, cellA.header, cellB)
        cellA = None
        cellB = None
        linked_list.destroy()
        i+=1

    dr.close()       
            

def main():

    '''
    gspreadcycle.main() is needed to extract data from Google Sheets
    '''
    #gspreadcycle.main() 

    __read(csv_filename)
    __save(_pickle_filename)
    __restore(_pickle_filename)
    __clean()
    '''
    __graph(param): param is the center node in cluster of in neo4j graph
    '''
    __graph("title")


if __name__ == "__main__":
    main()

