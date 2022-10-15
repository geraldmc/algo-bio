
## Requirements

  * Python 3+ is required. No external libraries used.

## Execution & Output

The program is made up of several modules. The user interacts with the file `driver.py`. To learn more, please type the following at the command prompt: 

```
>> python driver.py -h
```

and the following message will be displayed.

```
>> python driver.py -h

usage: driver.py [-h] -file

Exercise in hashing.

optional arguments:
  -h, --help  show this help message and exit
  -file       provide a path to a file containing hash input.
```

The code is delivered as a zipped folder. Once unzipped it has the following directory structure:

```
.
├── LICENSE
├── README.md
├── data
│   └── Input.txt
├── driver.py
├── filehandler
│   ├── __init__.py
│   └── io.py
├── hashtables
│   ├── __init__.py
│   └── hash.py
├── pytest.ini
└── tests
    └── test_hashtables.py
```
To run the program change directories to `GMcC-PP02` and execute the file `driver.py` as described. 

```
>> python driver.py -f
```

You will be prompted for a path to the input file.

```
Enter file input path: ./data/Input.txt
```

## Tests
This program supports unit testing with `PyTest`. To run the unit tests execute the following: PyTest must be installed to run tests..

```
>> python -m pytest ./tests
```

## Supporting Code

There are several modules contained in this submission:

## Performance

## REFERENCES

 Email to student: gmccoll2@jhu.edu