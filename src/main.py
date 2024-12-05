import typer
from db_charge import Queries

app = typer.Typer()

@app.command()
def create_nodes():
    charge = Queries()
    charge.node("Person", {"name": "Alice", "age": 30})
    charge.node("Person", {"name": "Bob", "age": 35})

@app.command()
def create_relation():
    charge = Queries()
    charge.load_relation("Person", "Alice", "Person", "Bob", "FRIEND")

@app.command()
def filter_people():
    charge = Queries()
    nodes = charge.filter_nodes("Person", "age", 30)
    for node in nodes:
        print(node)

@app.command()
def count_people():
    charge = Queries()
    count = charge.count_nodes("Person")
    print(f"Total number of Person nodes: {count}")

@app.command()
def create_index_and_constraint():
    charge = Queries()
    charge.create_index("Person", "name")
    print("Index created on 'name' for Person label.")

    charge.create_constraint("Person", "name")
    print("Unique constraint created on 'name' for Person label.")

@app.command()
def update_alice():
    charge = Queries()
    charge.update_node(
        "Person",
        {"name": "Alice"},
        {"age": 31},
    )

def get_friend_relationships():
    relations = Queries()
    pairs = relations.get_bidirectional_relations("FRIEND")
    for a, b in pairs:
        print(f"{a['name']} <-> {b['name']}")

@app.command()
def delete_relationship():
    charge = Queries()

    # Eliminar relaciones de Alice
    charge.delete_relationship("Person", "Alice", "Person", "Bob", "FRIEND")
    print("Relationship deleted.")

@app.command()
def delete_node():
    charge = Queries()

    # Eliminar nodo Alice
    charge.delete_nodes("Person", {"name": "Alice"})
    print("Alice's node deleted.")




if __name__ == "__main__":
    app()