const fs = require('fs');

fs.readFile('input.txt', function(err, data) {
    if(err) throw err;

    const lines = data.toString().replace(/\r\n/g,'\n').split('\n');

    let summary = {
        "zeros": {},
        "ones": {}
    }

    // Summarize count of zeros and ones

    for(let line of lines) {
        
        for(let index=0; index < line.length; index++) {
            
            bit = line.charAt(index)
            if (bit == "0") {
                if (!summary.zeros[index]) {
                    summary.zeros[index] = 0;
                }
                summary.zeros[index] += 1;
            }
            else if (bit == "1") {                
                if (!summary.ones[index]) {
                    summary.ones[index] = 0;
                }
                summary.ones[index] += 1;
            }
        }
    }
    console.log("Summary: ", summary)

    // Determine gamma / epsilon
    length = Object.keys(summary.ones).length;  // Should be same length with zeros
    
    let gamma = ""; // most common bit
    let epsilon = ""; // most common bit
    for(let index=0; index < length; index++) {
        if (summary.zeros[index] > summary.ones[index]) {
            gamma += "0";
            epsilon += "1";
        }
        if (summary.zeros[index] < summary.ones[index]) {
            gamma += "1";
            epsilon += "0";
        }
    }
    
    // log binary results
    console.log("Gamma (binary): ", gamma);
    console.log("Epsilon (binary): ", epsilon);

    // log int results
    gamma_int = parseInt(gamma, 2);
    epsilon_int = parseInt(epsilon, 2);
    console.log("Gamma (int): ", gamma_int);
    console.log("Epsilon (int): ", epsilon_int);   
    
    // log power consumption
    console.log("Power Consumption: ", gamma_int * epsilon_int);
});