
# Requirements

  * Python 3+

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.


# Sample Execution & Output

If run without command line arguments, using

```
python driver.py -h
```

the following usage message will be displayed.

```
Apply Strassen's algorithm. Compare with brute force algorithm.

positional arguments:
  input file path:  a path to a file containing matrices.

optional arguments:
  -h, --help        show this help message and exit
```

If run using

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