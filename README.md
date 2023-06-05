# Maximal substring of matching characters    
Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring. "Well-formed" in this instance means that each pair of parentheses match up to form an expression that can be evaluated, e.g.    
    
Example input: `(())()()))`    
 Well-formed substring: `(())()()`    
 Input will be a string of parentheses, output should be the integer length of the maximal well-formed substring.     
    
    
### Creating your solution    
 Your method should be as shown in the `solutions/maximal_substring_example.py`, named `solution` and accepting one string positional argument. Once complete, place your solution file in the `solutions/maximal_substring` folder, with the filename <something>_maximal_substring.py, e.g. `ichux_maximal_substring.py`.

**Do not** modify any code outside of that in your solutions file.  
  
### Running the tests  
  
You'll want to first install the requirements; navigate to the code directory and run (preferably in a virtualenv),  
  
`pip install -r requirements.txt`  
  
Now, from within the directory, run the `./test_runner.py` script.

## Scoring
A successful solution must of course first pass the test cases, the execution of which is profiled using the `pytest-profiling` plugin. If a solution passes the tests, it will be profiled standalone using `cProfile`. The score for a successful solution is the sum of the `pytest` profiler time and the `cProfile` profile time.

