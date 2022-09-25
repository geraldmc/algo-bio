
## Requirements

  * Python 3+ is required. No external libraries used.

## Execution & Output

The program is made up of several modules. The user need only interact with the file `driver.py`. To learn more, please type the following at the command prompt: 

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

The code is delivered in a zipped file. Once unzipped it will have the following directory structure:

```
├── Program-HW1
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
To run the program please execute `cd Program-HW1` and execute the file named `driver.py` as described previously. For purposes of this assignment (to test parsing of input and writing of output) please enter the following at the command prompt:

```
>> python driver.py -file
```

You will be prompted for paths to input and output files. You may direct the resulting output to a specified file or to the console. Choosing `Yes` will send the output to a named file. If you unzip the supplied code (gmccollam_code.zip) the data file as specified in the assignment will be available under the directory `./data` as indicated below.

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

If choosing `No` the output will be directed to stdout. There are other options available for testing but this is the intended use for grading purposes.

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