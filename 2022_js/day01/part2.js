const fs = require('fs');

fs.readFile('2022_js/day01/input.txt', function(err, data) {
  if (err) throw err;

  const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

  let currentCalories = 0;
  const calories = [];

  for (const line of lines) {
    const cal = parseInt(line);

    // console.log("isNaN of " + line + ": " + isNaN(cal));
    if (isNaN(cal)) {
      calories.push(currentCalories);
      currentCalories = 0;
    } else {
      currentCalories += cal;
    }
  }

  // Not optimal!
  calories.sort((a, b) => a - b).reverse();
  const top3Calories = calories[0] + calories[1] + calories[2];
  console.log('Sum of top 3 calories: ' + top3Calories);
});
