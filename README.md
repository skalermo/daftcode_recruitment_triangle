# triangle_tree

## Intro

## Problem

Source [here](https://github.com/daftcode/daftacademy-python_levelup-spring2020/tree/master/rekrutacja)

In a graph like shown below the cheapest path from top to bottom is required to be found.

```plain
    5    
   9 6   
  2 3 5  
 1 3 6 9 
6 7 6 4 2
```

## Solution
The solution is based on A* search algorithm. I think it is optimal for this problem, so I used it.

## Implementation
Currently, there are two implementations: written in Python and Rust, and I also compiled Rust solution to native Python module using [PyO3](https://github.com/PyO3/pyo3). It is not my proudest code (especially Rust code), but it works.

## Usage
To run the script you need to provide it path to file as an input:
```console
$ python solve.py path/to/your/file
```

## Performance
I timed all implementations and placed results (in seconds) in table below.

Problem size | Python | PyO3 | Rust
---|---|---|---
5    | 2.043e-04 | 5.223e-05 | **4.037e-05**
10   | 4.196e-04 | **5.715e-05** | 5.730e-05
50   | 0.021 | 7.473e-04 | **7.372e-04**
100  | 0.185 | 3.729e-03 | **3.547e-03**
500  | 25.3 | 0.289 | **0.282**
1000 | - | 2.33 | **2.3**

As expected Rust and PyO3 are faster than Python implementation.  
As I didn't expect Rust and PyO3 performed almost identically (sometimes PyO3 was a little bit faster).

## Problem generator
I wrote simple script [gen_problem.py](problems/gen_problem.py) to create problems similar to those in the [problems](problems/) folder.
