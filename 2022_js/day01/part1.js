const fs = require('fs');

fs.readFile('2022_js/day01/input.txt', function(err, data) {
  if (err) throw err;

  const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

  let maxCalories = 0;
  let currentCalories = 0;

  for (const line of lines) {
    const cal = parseInt(line);

    // console.log("isNaN of " + line + ": " + isNaN(cal))
    if (isNaN(cal)) {
      if (currentCalories > maxCalories) {
        maxCalories = currentCalories;
      }
      currentCalories = 0;
      // console.log("max: " + maxCalories)
    } else {
      currentCalories += cal;
    }
  }

  console.log('Max Calories: ' + maxCalories);
});
