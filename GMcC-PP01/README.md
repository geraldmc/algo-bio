
## Requirements

  * Python 3+ is required. No external libraries used.

## Execution & Output

The program is made up of several modules. The user interacts with the file `driver.py`. To learn more, please type the following at the command prompt: 

```
>> python driver.py -h
```

and the following message will be displayed.

```
usage: driver.py [-h] (-file | -create | -test OUTPUT)

Apply Strassen's algorithm. Compare it with a 'brute force' algorithm.

optional arguments:
  -h, --help    show this help message and exit
  -file         a path to a file containing one or more paired matrices.
  -create       the order and an interval range to create a paired matrix.
  -test OUTPUT  direct a matrix to a named output file
```

The code is delivered as a zipped folder. Once unzipped it has the following directory structure:

```
├── GMcC-PP01
│   ├── README.md
│   ├── algorithms
│   │   ├── __init__.py
│   │   ├── bruteforce.py
│   │   └── strassen.py
│   ├── analysis
│   │   ├── __init__.py
│   │   └── perf_runner.ipynb
│   ├── data
│   │   ├── LabStrassenInput.txt
│   │   ├── __init__.py
│   │   └── matrix_maker.py
│   ├── driver.py
│   └── filehandler
│       ├── __init__.py
│       └── io.py
```
To run the program change directories to `GMcC-PP01` and execute the file `driver.py` as described. For purposes of this assignment (to test parsing of input and writing of output) please enter the following at the command prompt:

```
>> python driver.py -file
```

You will be prompted for paths to input and output files. You may direct the resulting output to a specified file or to the console. Choosing `Yes` sends the output to a named file. If you unzip the supplied code then the assignment-provided data file will be available under the directory `./data` as indicated below.

```
Enter input path: ./data/LabStrassenInput.txt
Enter output path: ./foo.txt

Read 3 matrix pairs from file ./data/LabStrassenInput.txt
Print the result[s] to a file? (Yes|No): Yes
Printed 3 matrix pairs/products to file ./foo.txt

[Matrix Input 1]
2
2 1
1 5
6 7
4 3

[Matrix Product 1]
16 17
26 22

etc...
```

If choosing `No` the output will be directed to stdout. 

Note that I have used the naive form of matrix multiplication to handle the input/output part of this exercise. To directly test my implementation of Strassen's algorithm please execute the following steps. From the project root cd into `algorithms` and execute the file `strassen.py`:

```
>> python strassen.py
```
This produces the following output:

```
Using Strassen's:
A*B = [[16, 17], [26, 22]]
Number of Strassen Multiplications: (7)
A*B = [[-1, -4, -2, 13], [7, -6, 2, 6], [11, 5, -1, 1], [-6, 9, -8, 3]]
Number of Strassen Multiplications: (63)
A*B = [[-4, 4, 6, 3, -4, -3, -6, -10], [7, 4, 0, -5, 11, 0, 0, 8], [6, -11, 0, -8, -4, 4, 8, 5], [-4, 11, 7, 1, -6, 1, -4, -3], [-7, 2, -2, 8, 6, -5, -4, 6], [9, -1, 10, -3, 11, 4, 5, 10], [18, 9, 13, 12, 5, 3, 0, -2], [18, -5, -4, -11, -3, 1, 3, 3]]
Number of Strassen Multiplications: (462)
```



## Supporting Code

There are several modules contained in this submission: `algorithms` contains implementations of Strassen's and the standard algorithm; `analysis` contains a Python notebook to render plots of the algorithms' performance (may be run directly to generate the plot); `data` for the input data and for creating new matrices for testing; and `filehandler` for file input and output. 

## Performance

I have tested each algorithm on order sizes that are powers of two. The results are in the following table. This table and a graph of the same results are included in the Analysis section. 

| Order (2^n) | Naive      | Strassen  |
|-------------|------------|-----------|
| 1           | 1          | 0         |
| 2           | 8          | 7         |
| 4           | 64         | 56        |
| 8           | 512        | 399       |
| 16          | 4096       | 2800      |
| 32          | 32,768     | 19,607    |
| 64          | 262,144    | 137,256   |
| 128         | 2,097,152  | 960,799   |
| 256         | 16,777,216 | 6,725,600 |

---

## REFERENCES
Pomerance, Andrew, Edward Ott, Michelle Girvan, and Wolfgang Losert. “The Effect of Network Topology on the Stability of Discrete State Models of Genetic Control.” Proceedings of the National Academy of Sciences of the United States of America 106, no. 20 (May 19, 2009): 8209–14. https://doi.org/10.1073/pnas.0900142106.


 Email to student: gmccoll2@jhu.edu