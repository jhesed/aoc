const fs = require('fs');

fs.readFile('2021_js/day03/input.txt', function(err, data) {
  if (err) throw err;

  const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

  const summary = {
    'zeros': {},
    'ones': {},
  };

  // Summarize count of zeros and ones

  for (const line of lines) {
    for (let index = 0; index < line.length; index++) {
      bit = line.charAt(index);
      if (bit == '0') {
        if (!summary.zeros[index]) {
          summary.zeros[index] = 0;
        }
        summary.zeros[index] += 1;
      } else if (bit == '1') {
        if (!summary.ones[index]) {
          summary.ones[index] = 0;
        }
        summary.ones[index] += 1;
      }
    }
  }

  let [gamma, epsilon] = calculate_gamma_epsilon(summary);

  console.log('Summary: ', summary);

  // log binary results
  console.log('Gamma (binary): ', gamma);
  console.log('Epsilon (binary): ', epsilon);

  // log int results
  gamma_int = parseInt(gamma, 2);
  epsilon_int = parseInt(epsilon, 2);
  console.log('Gamma (int): ', gamma_int);
  console.log('Epsilon (int): ', epsilon_int);

  // log power consumption
  console.log('Power Consumption: ', gamma_int * epsilon_int);


  // ----------------------------------------------- part 2

  // We'll remove non-compliant rating as we loop
  oxygen_summary = {
    ...summary,
  };
  oxygen_rating = [...lines];
  co2_summary = {
    ...summary,
  };
  co2_rating = [...lines];

  for (let l = 0; l < lines.length; l++) {
    line = lines[l];
    for (let index = 0; index < line.length; index++) {
      bit = line.charAt(index);

      g = gamma.charAt(index);
      if (bit != g) {
        if (g == 'G' && bit == 1) {
          continue;
        }
        if (bit == ' 0') {
          oxygen_summary.zeros[index] -= 1;
        }
        if (bit == ' 1') {
          oxygen_summary.ones[index] -= 1;
        }

        delete oxygen_rating[l];
        [gamma, __epsilon] = calculate_gamma_epsilon(oxygen_summary);

        console.log(index, 'New gamma', gamma.charAt(index + 1));
      }


      if (bit != epsilon.charAt(index)) {
        delete co2_rating[l];
        co2_summary.zeros[index] -= 1;
        [__gamma, epsilon] = calculate_gamma_epsilon(co2_summary);
      }
    }
  }

  console.log('oxygen_rating: ', oxygen_rating);
  console.log('co2_rating: ', co2_rating);
});


function calculate_gamma_epsilon(summary) {
  // Determine gamma / epsilon
  length = Object.keys(summary.ones).length; // Should be same length with zeros

  let gamma = ''; // most common bit
  let epsilon = ''; // most common bit
  for (let index = 0; index < length; index++) {
    if (summary.zeros[index] > summary.ones[index]) {
      gamma += '0';
      epsilon += '1';
    }
    if (summary.zeros[index] < summary.ones[index]) {
      gamma += '1';
      epsilon += '0';
    }
    // Quick hack for problem 2.lols
    if (summary.zeros[index] == summary.ones[index]) {
      gamma += 'G';
      epsilon += 'E';
    }
  }
  // console.log("Gamma: ", gamma);
  // console.log("Epsilon: ", epsilon);
  return [gamma, epsilon];
}
