
# Requirements

  * Python 3+

# Sample Execution & Output

To understand how this all works, please first type: 

```
python driver.py -h
```

the following usage message will be displayed.

```
usage: driver.py [-h] (-file | -create | -test OUTPUT)

Apply Strassen's algorithm. Compare it with a 'brute force' algorithm.

optional arguments:
  -h, --help    show this help message and exit
  -file         provide a path to a file containing one or more paired matrices.
  -create       provide the order and an interval range to create a new paired matrix.
  -test OUTPUT  direct a matrix to a named output file
```

If run using:

```
python driver.py './data/LabStrassenInput.txt'
```

output *similar* to

```
    foo bar
    bar foo
    foo bar
```

will be generated.

---

REFERENCES
Pomerance, Andrew, Edward Ott, Michelle Girvan, and Wolfgang Losert. “The Effect of Network Topology on the Stability of Discrete State Models of Genetic Control.” Proceedings of the National Academy of Sciences of the United States of America 106, no. 20 (May 19, 2009): 8209–14. https://doi.org/10.1073/pnas.0900142106.


 Email to student: 
© 2022 Gerald McCollam