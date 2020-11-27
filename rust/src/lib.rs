mod tree;
pub mod triangle_solver;

use triangle_solver::solve;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Solves problem. Fast.
#[pyfunction]
pub fn solve_fast(filename: &str) -> PyResult<(u32, Vec<u8>)> {
    Ok(solve(filename))
}

/// A Python module implemented in Rust.
#[pymodule]
pub fn triangle_solver_lib(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve_fast, m)?)?;

    Ok(())
}