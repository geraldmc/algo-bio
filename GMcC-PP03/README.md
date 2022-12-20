# Programming Project 3 - Fall 2022 (Gerald McCollam)
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

You will be prompted for a path to the input file. The required input file is provided, renamed as `Input.txt`.

```
Enter file input path: ./data/Input.txt
```

## Supporting Code

There are several modules contained in this submission:

The module `analysis` contains functions for profiling the code, notably `profile` which provides a means of 
instrumenting each LCS algorithm and measuring its performance. The module also contains functions for randomly generating DNA strings 
of varying length. Finally, it includes an *.ipynb notebook for re-creating the plots included in the accompanying report. 

The module `filehandler` contains the function `pre_process` which loads provided data from file and renders it as a dictionary for the three algorithms.  

Finally, the `algorithms` module provides three implementations of the longest common subsequence problem. `LCS1` is a recursive solution; `LCS2` and `LCS3` are dynamic programming solutions. 

## Performance:

Following is a performance plot of the three algorithms: LCS1 (recursive), LCS2 and LCS3 (DP/iterative).

![alt text](perf_compare.png "Performance plot")


## Output
#### Following is output from a sample run at the command line.

Enter file input path: ./data/input.txt

NOTE: The recursive LCS1 function runs very slowly on sequences longer than
18 characters. It is run on generated test data specific to it, not on the 
provided test data (for time considerations).

Running LCS2 on provided data...

	LCS of length 20 found in 0.002 seconds.
	LCS of length 19 found in 0.002 seconds.
	LCS of length 11 found in 0.001 seconds.
	LCS of length 20 found in 0.001 seconds.
	LCS of length 12 found in 0.001 seconds.
	LCS of length 13 found in 0.001 seconds.

Running LCS3 on provided data...

	LCS of length 20 found in 0.001 seconds.
	LCS of length 19 found in 0.001 seconds.
	LCS of length 11 found in 0.000 seconds.
	LCS of length 20 found in 0.001 seconds.
	LCS of length 12 found in 0.000 seconds.
	LCS of length 13 found in 0.000 seconds.

------------------------generated---------------------------

Running LCS1 on generated data...

	LCS of length C found in 0.000 seconds.
	LCS of length G found in 0.001 seconds.
	LCS of length A found in 0.001 seconds.
	LCS of length G found in 0.001 seconds.
	LCS of length G found in 0.001 seconds.

Running LCS2 on generated data...

	LCS of length 1777 found in 2.708 seconds.
	LCS of length 1950 found in 3.292 seconds.
	LCS of length 2134 found in 4.004 seconds.
	LCS of length 2324 found in 4.782 seconds.

Running LCS3 on generated data...

	LCS of length 1780 found in 1.626 seconds.
	LCS of length 1956 found in 2.018 seconds.
	LCS of length 2131 found in 2.393 seconds.
	LCS of length 2332 found in 2.806 seconds.

--------------------------fin-------------------------------
## Contact:

 Email to student: gmccoll2@jhu.edu

 
 