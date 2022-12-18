
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

Exercise in longest common subsequence.

optional arguments:
  -h, --help  show this help message and exit
  -file       provide a path to a file containing hash input.
```

The code is delivered as a zipped folder. Once unzipped it has the following directory structure:

```
.
├── README.md
├── algos
│   ├── __init__.py
│   └── algorithms.py
├── analysis
│   ├── __init__.py
│   ├── metrics.py
│   └── perf_runner.ipynb
├── data
│   └── Input.txt
├── driver.py
└── filehandler
    ├── __init__.py
    └── io.py
```
To run the program change directories to `GMcC-PP03` and execute the file `driver.py` as described. 

```
>> python driver.py -file
```

You will be prompted for a path to the input file. The required input file is provided, named `Input.txt`.

```
Enter file input path: ./data/Input.txt
```

## Supporting Code

There are several modules contained in this submission:

The module `analysis` contains functions for profiling the code, notably `profile` which provides a means of 
instrumenting each LCS algorithm and measuring its performance. 

## Performance

## REFERENCES

 Email to student: gmccoll2@jhu.edu

 
 