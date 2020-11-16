# AirBnB clone - The console

The first part of the AirBnB clone project, in which we implemented the console we use for data management (creating, saving, loading and updating objects) in a JSON file using serialization/deserialization.

## The Console

The console is an command line interpreter that works both interactively and non-interactively mode.

Is used to manage objects:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object 

## Usage

To use the console in interactive mode:

```
$ ./console.py
(hbnb) 
```
or to use the non-interactive mode:
```
$ echo "command" | ./console.py
```
## Commands
* `all`     -	Prints all string representation of all instances based or not on the class name.
```
all [Class]
Class.all()
Class.count()
```
```
(hbnb) all
[City] (deb614d7-7c8b-4bfa-b214-24b1673e7ac3) {'id': 'deb614d7-7c8b-4bfa-b214-24b1673e7ac3', 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 31, 893392), 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 31, 893345)}
(hbnb) City.all()
[City] (deb614d7-7c8b-4bfa-b214-24b1673e7ac3) {'id': 'deb614d7-7c8b-4bfa-b214-24b1673e7ac3', 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 31, 893392), 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 31, 893345)}
((hbnb) City.count()
1
(hbnb)) 
```
* `create`  -	Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
```
create <Class>
```
```
(hbnb) create Place
8c108520-00c3-4033-bdcf-cf3c18b95022
(hbnb) 
```
* `count`  -	Prints the number of instances of the given Class.
```
<Class>.count()
```
```
(hbnb) Amenity.count()
1
(hbnb)  
```
* `destroy` -	Deletes an instance based on the class name and id.
```
destroy <Class> <id>
<Class>.destroy(<id>)
```
```
(hbnb) destroy City deb614d7-7c8b-4bfa-b214-24b1673e7ac3
(hbnb) Place.destroy(8c108520-00c3-4033-bdcf-cf3c18b95022)
```
* `EOF` -	Quit the console with an End of File (ctrl + D).
```
EOF
```
* `help`    -	List available commands with "help" or detailed help with.
```
 help [cmd]
```
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  list  quit  show  update

((hbnb) help create
Create a new instance of a Airbnb Class.

        Usage: create <Class>
        
(hbnb)
```
* `list `   -     List available Classes.
```
list
```
```
(hbnb) list
Place City State Review User BaseModel Amenity
(hbnb) 
```
* `quit`    -	Quit command to exit the program.
```
quit
```
* `show`    -	Print the string representation of an instance based on the class name an id.
```
show <Class> <id>
Class.show(<id>)
```
```
(hbnb) show Amenity c618bbed-6930-48c7-ae24-8124b518467c
[Amenity] (c618bbed-6930-48c7-ae24-8124b518467c) {'updated_at': datetime.datetime(2020, 7, 9, 13, 37, 40, 471585), 'created_at': datetime.datetime(2020, 7, 9, 13, 37, 40, 471529), 'id': 'c618bbed-6930-48c7-ae24-8124b518467c'}
(hbnb) Amenity.show (c618bbed-6930-48c7-ae24-8124b518467c)
[Amenity] (c618bbed-6930-48c7-ae24-8124b518467c) {'updated_at': datetime.datetime(2020, 7, 9, 13, 37, 40, 471585), 'created_at': datetime.datetime(2020, 7, 9, 13, 37, 40, 471529), 'id': 'c618bbed-6930-48c7-ae24-8124b518467c'}
(hbnb) 
```
* `update`  -	Updates an instance based on the class name and id by adding or updating attribute
```
update <Class> <id> <attribute name> "<attribute value>"
<Class>.update(<id>, <attribute name>, <attribute value>)
<Class>.update(<id>, <dictionary representation>)
```
```
(hbnb) update City 18a264ff-3dd1-4866-a25d-c1abd1894ebd name: Joe  
(hbnb) City.update(18a264ff-3dd1-4866-a25d-c1abd1894ebd, name, Jhon)

```
## Authors
[Manuel Torres V.](manueltorresvesga@gmail.com)

[Santiago Mendieta](1494@holbertonschool.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)
