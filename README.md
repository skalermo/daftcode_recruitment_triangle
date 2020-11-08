# daftcode_recruitment_triangle

## Problem

In a graph like shown below the cheapest path from top to bottom is required to be found.

```plain
    5    
   9 6   
  2 3 5  
 1 3 6 9 
6 7 6 4 2
```

## Solution
The solution is based on A* search algorithm.  
Implementation can be found in source file [PathTree.py](PathTree.py) in function [find_best_path](https://github.com/skalermo/daftcode_recruitment_triangle/blob/59ca7eed1a27fec3f4183a46184667864741271e/PathTree.py#L26).

## Usage
To run the script you need to provide it path to file as an input:
```console
$ python solve.py path/to/your/file
```

## Problem generator
I wrote simple script [gen_problem.py](problems/gen_problem.py) to create problems similar to those in the [problems](problems/) folder.
