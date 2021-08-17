# Unit Test Coverage #

## coverage python tool ##
We will be measuring our unit test coverage with a python tool, called coverage.  This will present us with a table containing each file in the test case, and a percentage of the statements from that file covered by the test case.  Info on what to do with this information coming soon.

## How to use it ##
First you'll need to install the tool by going into the terminal of your IDE and entering the command

`pip install coverage`

Then, while in the root directory of your repository, simply run your unit tests with the command to measure the coverage.

`coverage run -m unittest tests/test_<filename>.py`

To run multiple test files, you can use

`coverage run -m unittest discover`

and view the report with

`coverage report -m`

which should produce an output that looks similar to the following
```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
my_program.py                20      4    80%   33-35, 39
my_other_module.py           56      6    89%   17-23
-------------------------------------------------------
TOTAL                        76     10    87%
```

Further documentation on the coverage tool and other options can be found [here](https://coverage.readthedocs.io/en/coverage-5.5/ "Coverage Documentation").  Keep in mind that we are using unittest for our test cases, so use that option whenever applicable.