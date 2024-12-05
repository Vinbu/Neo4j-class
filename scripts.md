# NEO4J SCRIPTS
Below are the commands to follow in python for the correct orden operation of the examples.
## 1. Create node and Relation
Create nodes Alice and Bob:
```bash
python3 main.py create-nodes
```
Create the FRIEND relationship between Alice and Bob:
```bash
python3 main.py create-relation
```
## 2. Upload
Filter people over 30 years old
```bash
python3 main.py filter-people
```
## 3. Count
Counts nodes of type Person
```bash
python3 main.py count-people
```
## 4. Create index and constraint
```bash
python3 main.py create-index-and-constraint
```
## 5. Update
Update Alice's age
```bash
python3 main.py update-alice
```
## 6. Bidirectional relationships
Gets bidirectional relationships of type FRIEND
```bash
python3 main.py get-friend-relationships
```
## 7. Delete relationship
Delete the FRIEND relationship
```bash
python3 main.py delete-relationship
```
## 8. Delete node
Delete Alice's node
```bash
python3 main.py delete-node
```
