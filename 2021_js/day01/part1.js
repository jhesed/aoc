const fs = require('fs');

fs.readFile('2021_js/day01/input.txt', function(err, data) {
    if (err) throw err;

    const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

    let line_num = 0;
    let increased = 0;

    for (let line of lines) {
        if (line_num > 0) {
            // console.log(parseInt(lines[line_num-1]), parseInt(line), parseInt(lines[line_num-1]) > parseInt(line))
            if (parseInt(lines[line_num - 1]) < parseInt(line)) {
                increased += 1;
            }
        }
        line_num += 1;
    }
    console.log("Increased: ", increased);
});
