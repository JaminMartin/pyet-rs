use pyo3::prelude::*;
use rayon::prelude::*;

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

#[pyfunction]
pub fn general_energy_transfer_para(time: Vec<f64>, radial_data: Vec<f64>, amp: f64, cr: f64, rad: f64, offset: f64) -> PyResult<Vec<f64>> {
    let n = radial_data.len() as f64;


    let result = time.par_iter().map(|t| {
        let sum: f64 = radial_data.iter().map(|r| (-t * (cr * r + rad)).exp()).sum();
        amp / n * sum + offset
    }).collect();

    Ok(result)
}



fn doper(number_atons: u32, concen: u32) -> Vec<String> {
    let result = (0..=number_atons).into_par_iter().map(|_| rando(concen)).collect();
    result
}


fn doper_seq(number_atons: u32, concen: u32) -> Vec<String> {
    let result = (0..=number_atons).
    into_iter()
    .map(|_| rando(concen))
    .collect();
    result
}


fn rando(concen: u32) -> String {
   let temp = concen as f64;

   let mut rng = rand::thread_rng();
   let random_number: f64 = rng.gen();
   //println!("{}", temp / 100.00);
   //println!("{}", random_number);
   match random_number < temp / 100.0 {
     true => "dopant".to_string(), 
     false  => "Y".to_string(),
   } 
    
}


#[pymodule]
fn pyet_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(general_energy_transfer, m)?)?;
    m.add_function(wrap_pyfunction!(general_energy_transfer_para, m)?)?;
    Ok(())
}
