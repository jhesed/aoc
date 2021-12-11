const fs = require('fs');

fs.readFile('2021_js/day01/input.txt', function(err, data) {
    if (err) throw err;

    const lines = data.toString().replace(/\r\n/g, '\n').split('\n');
    const WINDOW_SIZE = 3;

    let line_num = 0;
    let increased = 0;

    let curr_sum = 0;
    let prev_sum = 0;

    for (var index = 0; index < lines.length; index++) {
        for (var i = 0; i < WINDOW_SIZE; i++) {
            if (!lines[index + i]) {
                break;
            }
            curr_sum += parseInt(lines[index + i]);
        }
        if (index > 0 && curr_sum > prev_sum) {
            increased += 1;
        }
        // console.log(prev_sum, curr_sum, increased);
        prev_sum = curr_sum;
        curr_sum = 0;
    }

    console.log("Increased: ", increased);
});
