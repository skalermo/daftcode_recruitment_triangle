# triangle_tree

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
For heuristic I just calculated distance from current node to bottom row multipled by 1 (minimal cost).

## Implementation
Currently, there are two implementations: written in Python and Rust, and I also compiled Rust solution to native Python module using [PyO3](https://github.com/PyO3/pyo3). It is not my proudest code (especially Rust code), but it works.

## Usage
Keep in mind that this project was made and meant to be run on Linux.

### Python (PyO3)
For plain Python usage Python3 is required.  
If you want to use compiled with PyO3 `triangle_solver_lib` you are going to need Python 3.6 or higher (I used 3.8.6).

```console
$ python main.py file/to/solve
```

If you want to use `triangle_solver_lib` add `-r` flag:
```console
$ python main.py file/to/solve -r
```

### Rust

To run binary just type
```console
$ ./rust_solver file/to/solve
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
But I didn't expect Rust and PyO3 performed almost identically (sometimes PyO3 was a little bit faster).

## Problem generator
I wrote simple script [gen_problem.py](problems/gen_problem.py) to create problems similar to those in the [problems](problems/) folder.
