import os
from neo4j import GraphDatabase

class Queries:
    def __init__(self):
        self.driver = GraphDatabase.driver(os.environ.get('neo_url'), auth=(os.environ.get('neo_user'), os.environ.get('neo_password')))

    def node(self, label, properties):
        query = f"""
        CREATE (n:{label} {{ {', '.join(f'{k}: ${k}' for k in properties.keys())} }})
        RETURN n
        """
        with self.driver.session() as session:
            result = session.run(query, **properties)
            return result.single()["n"]
    
    def load_relation(self, label1, property1, label2, property2, relationship_type):
        query = f"""
        MATCH (a:{label1} {{name: $name1}})
        MATCH (b:{label2} {{name: $name2}})
        CREATE (a)-[r:{relationship_type}]->(b)
        RETURN r
        """
        with self.driver.session() as session:
            result = session.run(query, name1=property1, name2=property2)
            return result.single()["r"]
    
    def update_node(self, label, properties, updates):
        query = f"""
        MATCH (n:{label} {{name: $name}})
        SET n.age = $new_age
        RETURN n
        """
        with self.driver.session() as session:
            result = session.run(query, name=properties["name"], new_age=updates["age"])
            return result.single()["n"]
    
    
    def filter_nodes(self, label, property, value):
        query = f"""
        MATCH (n:{label})
        WHERE n.{property} > $value
        RETURN n
        """
        with self.driver.session() as session:
            result = session.run(query, value=value)
            return [record["n"] for record in result]
    
    def count_nodes(self, label):
        query = f"""
        MATCH (n:{label})
        RETURN COUNT(n)
        """
        with self.driver.session() as session:
            result = session.run(query)
            return result.single()[0]
    
    def create_index(self, label, property):
        query = f"""
        CREATE INDEX FOR (n:{label}) ON (n.{property})
        """
        with self.driver.session() as session:
            session.run(query)
    
    def create_constraint(self, label, property):
        query = f"""
        CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE
        """
        with self.driver.session() as session:
            session.run(query)
    
    def get_bidirectional_relations(self, relationship_type):
        query = f"""
        MATCH (a:Person)-[r:{relationship_type}]-(b:Person)
        RETURN a, b
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [(record["a"], record["b"]) for record in result]
    
    def delete_relationship(self, label1, property1, label2, property2, relationship_type):
        query = f"""
        MATCH (a:{label1} {{name: $name1}})-[r:{relationship_type}]-(b:{label2} {{name: $name2}})
        DELETE r
        """
        with self.driver.session() as session:
            session.run(query, name1=property1, name2=property2)
    
    def delete_nodes(self, label, properties):
        query = f"""
        MATCH (n:{label} {{name: $name}})
        DELETE n
        """
        with self.driver.session() as session:
            session.run(query, name=properties["name"])