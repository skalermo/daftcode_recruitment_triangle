use std::env;
use std::time::Instant;

extern crate triangle_solver_lib;
use triangle_solver_lib::triangle_solver::solve;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} path/to/file", args[0]);
        return;
    }

    let start = Instant::now();
    let (cost, path) = solve(args[1].as_str());
    let elapsed = start.elapsed();
    println!("Elapsed: {:?}", elapsed);
}
