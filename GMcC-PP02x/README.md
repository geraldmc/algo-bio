# Programming Project 2 - Fall 2022 (Gerald McCollam)
# EN.605.620.81.FA22 Algorithms for Bioinformatics

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
├── analysis
│   ├── __init__.py
│   └── metrics.py
├── data
│   ├── Extra.txt
│   └── Input.txt
├── driver.py
├── filehandler
│   ├── __init__.py
│   └── io.py
├── hashtables
│   ├── LinearProbing.py
│   ├── QuadraticProbing.py
│   ├── SeparateChaining.py
│   └── __init__py
└── perf.py
```
To run the program change directories to `GMcC-PP02` and execute the file `driver.py` as described. 

```
>> python driver.py -file
```

You will be prompted for a path to the input file. The required input file is provided, renamed as `Input.txt`.

```
Enter file input path: ./data/Input.txt
```

## Supporting Code

There are several modules contained in this submission:

#### `analysis`

The module `analysis` contains functions for profiling the code, notably `plot` which provides a means of 
plotting a histogram for each variation of hashing algorithm and measuring the distribution of hash keys. The module `filehandler` contains functions to handle input and ouput using a number of functions `pre_process`, `divide_chunks`, `print_5iter`, and `print_3iter`. The function `pre_process` loads provided data from file and renders it as a dictionary for the three algorithms. Finally, the `hashtables` module provides three implementations of hashing schemes `LinearProbing.py`, `QuadraticProbing.py` and `SeparateChaining.py`. 


## REFERENCES

 Email to student: gmccoll2@jhu.edu

 
 