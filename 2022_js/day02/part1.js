const fs = require('fs');

fs.readFile('2022_js/day02/input.txt', function(err, data) {
  if (err) throw err;

  const POINTS_WON = 6;
  const POINTS_DRAW = 3;

  // Rock = A, X
  // Paper = B, Y
  // Scissors = C, Z
  // const LEGEND = ['ROCK', 'PAPER', 'SCISSORS']

  /*
    Brain Exercise

    Format:
      MyMoveIndex
      MyOpponentIndex
      Result

    ROCK = 0
    PAPER = 1
    0-1 == -1  (lost)

    ROCK = 0
    SCI = 2
    0-2 = -2 (win)

    ROCK = 0
    ROCK = 0
    0-0 = 0 (draw)

    PAPER = 1
    ROCK = 0
    1-0 = 1 (win)

    PAPER = 1
    SCISSORS = 2
    1-2 = -1 (lost)

    PAPER-PAPER = 0 (draw)

    SCI = 2
    ROCK = 0
    2-0 = 0 (lost)

    SCI = 2
    PAPER = 1
    2-1 = 1 (win)
  */

  const OPPONENT_MOVES = ['A', 'B', 'C'];
  const MY_MOVES = ['X', 'Y', 'Z'];

  const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

  let points = 0;
  for (const line of lines) {
    const values = line.split(' ');
    const opponent = values[0];
    const mine = values[1];

    opponentMoveIndex = OPPONENT_MOVES.indexOf(opponent);
    myMoveIndex = MY_MOVES.indexOf(mine);
    moveDiff = myMoveIndex - opponentMoveIndex;

    if (opponentMoveIndex == myMoveIndex) {
      // draw
      points += POINTS_DRAW;
    } else if (moveDiff == 1 || moveDiff == -2) {
      // win
      points += POINTS_WON;
    }
    points += myMoveIndex + 1; // refer to spec
  }
  console.log('Points: ' + points);
});
