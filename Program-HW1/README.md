
## Requirements

  * Python 3+ (any version of Python 2 will fail).

## Execution & Output

The program is made up of several modules. The user need only interact the file `driver.py` To learn more, please type: 

```
python driver.py -h
```

the following usage message will be displayed.

```
usage: driver.py [-h] (-file | -create | -test OUTPUT)

Apply Strassen's algorithm. Compare it with a 'brute force' algorithm.

optional arguments:
  -h, --help    show this help message and exit
  -file         provide a path to a file containing one or more paired matrices. (<- choose this one!)
  -create       provide the order and an interval range to create a new paired matrix.
  -test OUTPUT  direct a matrix to a named output file
```

For purposes of the assignment (to test proper parsing of input and writing of output) one should type:

```
python driver.py -file
```

You will be prompted for a path to an input file and to an output file. You will be given a choice to write to that file or to the console. Output to a file (part of the assignment's requirement) will look like the following:

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

will be generated.

---

REFERENCES
Pomerance, Andrew, Edward Ott, Michelle Girvan, and Wolfgang Losert. “The Effect of Network Topology on the Stability of Discrete State Models of Genetic Control.” Proceedings of the National Academy of Sciences of the United States of America 106, no. 20 (May 19, 2009): 8209–14. https://doi.org/10.1073/pnas.0900142106.


 Email to student: 
© 2022 Gerald McCollam