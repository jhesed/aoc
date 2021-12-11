const fs = require('fs');

fs.readFile('2021_js/day02/input.txt', function(err, data) {
    if (err) throw err;

    const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

    let line_num = 0;
    let increased = 0;

    horizontal = 0;
    depth = 0;
    aim = 0;
    for (let line of lines) {

        let line_data = line.split(/\s/);
        let command = line_data[0];
        let value = parseInt(line_data[1]);

        if (command == "forward") {
            horizontal += value;
            depth += aim * value;
        } else if (command == "up") {
            aim -= value;
            // depth -= value;
        } else if (command == "down") {
            aim += value;
            // depth += value;
        }
        console.log(line_data, horizontal, depth, aim);
    }

    console.log(horizontal, depth, aim, horizontal * depth);
});
