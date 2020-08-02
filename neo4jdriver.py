#!/usr/bin/env bash
"""
neo4jdriver module: has class DriverLifecycle with functions to open Neo4j Desktop browser on Mac,
                    and class Neo4jDatabase  with query functions.
"""

from neo4j import GraphDatabase
from gspreadcycle import GSpreadCycle as gs

_author_=["Jennifer Kwon", "Anne Wang", "Mauricio Lomeli"]
_date_ = "9/3/2019"
_credits_ = ["Rebecca Zhuo", "Smruti Vidwans"]
_email_="kwonjy3@uci.edu"
_status_="Prototype V 0.0.2"

uri = "bolt://localhost:7687"
user = "neo4j"
password = "jenniferkwon"

class DriverLifecycle:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="jenniferkwon"):
        self.driver = None
        self.session = None

        import os
        os.system("cd")
        #os.system("cd ~/Downloads/neo4j-community-3.5.9")
       # os.system("cd ~/Applications/neo4j-community-3.5.9")
        #os.system("./bin/neo4j")
        #os.system("open http://localhost:7474/db/data")

        import subprocess
        import platform
        
        if platform.system() == "Darwin":
            #app = "Neo4j Desktop"
            #subprocess.call(["/usr/bin/open", "-W", "-n", "-a" "/Applications/Neo4j Desktop.app"])
            print("pass neo4j desktop")
        elif platform.system() == "Windows":
            print("open neo4j desktop manually")
        elif platform.system() =="Linux":
            print("open neo4j desktop manually")

        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=(user, password))
        self.session = self.driver.session()
            
    def close(self):
        self.driver.close()

    def get_driver(self):
        return self.driver

    def get_session(self):
        return self.session 

class Neo4jDatabase:
    
    def __init__(self):
        pass

    def delete_all_nodes(self, session):
        """
        delete_all_nodes(self, session): method deletes all nodes in current session on neo4j.
        """
        return session.run("MATCH (n) DETACH DELETE(n)")

    def delete_all_relationships(self, session):
        """
        delete_all_relationships(self, session): method deletes all relationships in current session from neo4j.
        """
        return session.run("MATCH ()-[r]-() DELETE r")

    def insert_str(self, session, text):
        pass
    
    def insert_cell(self, session, data):
        """
        insert_cell(self, session, data: Cell): method creates new node if it does not exist.
        """
        
        import cells
        #query = 'MATCH (n: cell {{ID: {0}, header: "{1}", content: "{2}" }}) RETURN n'.format(data.ID, data.header, data.content)
        #is_match = session.run(query)

        #if (is_match.peek() == None):
        if isinstance(data, dict):
            query = 'CREATE (n: cell {{ID: {0}, header: "{1}", content: "{2}" }}) RETURN n'.format(data['ID'], data['header'], data['content'] )
        elif isinstance(data, cells.Cell):
            query = 'CREATE (n: cell {{ID: {0}, header: "{1}", content: "{2}" }}) RETURN n'.format(data.ID, data.header, data.content )

        return session.run(query)  

    def insert_dict(self, session,data): #insert updated dictionary, match cell with content and header
        """
        insert_dict(self, session,data): method inserts dictionary into neo4j data
        """
        pass
    
    def linkStr(self, strA, link_message, strB):
        pass

    def linkCells(self, session, cellA, link_message, cellB):
        """
        linkCells(self, session, cellA, link_message, cellB): method links cellA and cellB in neo4j graph.
        Must have the option of merging cells with same header and content, or option of unique nodes.
        """
        import cells
        #query = 'MATCH (n: cell {{header: "{1}", content: "{2}" }}) RETURN n'.format(data.ID, data.header, data.content)
        #is_match = session.run(query)

        #if (is_match.peek() == None):
        '''    
        query = 'MATCH (a: cell) WHERE a.ID = {0} AND a.header = "{1}" AND a.content = "{2}"\n'\
                'MATCH (b: cell) WHERE b.ID = {3} AND b.header = "{4}" AND b.content = "{5}"\n'\
                'MERGE (a)-[r:`{6}`]->(b)'.format(cellA.ID, cellA.header, cellA.content ,cellB.ID, cellB.header, cellB.content, link_message) 
        ''' 
        query = 'MATCH (a: cell) WHERE a.ID = {0} AND a.header = "{1}" AND a.content = "{2}"\n'\
                'MATCH (b: cell) WHERE b.ID = {3} AND b.header = "{4}" AND b.content = "{5}"\n'\
                'MERGE (a)-[r:`{6}`]->(b)'.format(cellA['ID'], cellA['header'], cellA['content'] ,cellB['ID'], cellB['header'], cellB['content'], link_message)                                                           
        return session.run(query)

            
            



            
                
