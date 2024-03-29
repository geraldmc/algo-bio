## Algorithms for Bioinformatics Programming Project 2 - Fall 2022

### Requirements

  * Python 3+ is required. No external libraries used.

### Execution & Output

The program is made up of several modules. The user interacts with the file `driver.py`. To learn more, please type the following at the command prompt: 

```
>> python driver.py -h
```

The following message will be displayed.

```
usage: driver.py [-h] --input INFILE [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --input INFILE   input file containing values to be hashed.
  --output OUTPUT  output file.
```

### Run Assignment Code
To run the program change directories to `GMcC-PP02x` and execute the file `driver.py`. There are two input data files supplied. The first is `./data/Minimum.txt`. This is the required input for the assignment. To run this, please execute the following:

```
>> python driver.py --input ./data/Minimum.txt --output ./data/output.txt
```

A second supplied data file is named `./data/Extra.txt` To run this execute the following:
```
>> python driver.py --input ./data/Extra.txt --output ./data/output.txt
```

The code is delivered as a zipped folder. Once unzipped it has the following directory structure:
```
.
├── LICENSE
├── README.md
├── analysis
│   ├── __init__.py
│   ├── metrics.py
│   └── perf_notebook.ipynb
├── data
│   ├── Extra.txt
│   └── Minimum.txt
├── driver.py
├── filehandler
│   ├── __init__.py
│   └── io.py
├── hashtables
│   ├── LinearProbing.py
│   ├── QuadraticProbing.py
│   ├── SeparateChaining.py
│   ├── __init__py
└── perf.py
```

### Supporting Code

There are several modules contained in the submission:

#### `analysis`
The module `analysis` contains functions for profiling including `metrics.py` and `perf_notebook.ipynb`. The first executes code to recreate the hash key distribution plot and to instrument the hashing functions for timing purposes. The notebook creates the plots that are contained in the report and can be run on Google Colab.

#### `filehandler`
This module contains several functions for inputing data, and printing the resulting output in proper format.

#### `hashtables`
This contains three files `LinearProbing.py`, `QuadraticProbing.py`, and `SeparateChaining.py`.



## REFERENCES

 Email to student: gmccoll2@jhu.edu

 
 