use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
pub fn general_energy_transfer(time: Vec<f64>, radial_data: Vec<f64>, amp: f64, cr: f64, rad: f64, offset: f64) -> PyResult<Vec<f64>> {
    let n = radial_data.len() as f64;

    let mut result = Vec::with_capacity(time.len());

    for t in &time {
        let mut sum = 0.0;
        for r in &radial_data {
            sum += (-t * (cr * r + rad)).exp();
        }
        result.push(amp / n * sum + offset);
    }

    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyet_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(general_energy_transfer, m)?)?;
    Ok(())
}
