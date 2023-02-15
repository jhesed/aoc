const fs = require('fs');

fs.readFile('2022_js/day02/input.txt', function(err, data) {
  if (err) throw err;

  const POINTS_WON = 6;
  const POINTS_DRAW = 3;

  /*
  Brainstorming:

    Opponent moves
      A - Rock
      B - Paper
      C - Scissors
      ['A', 'B', 'C']

    My moves
      X - Needs to lose
        A - C [2]
        B - A [0]
        C - B [1]
        Therefore, needs to subtract 1 from current index.

      Y - Needs to draw
        Give the same index

      z - Needs to win
        Index + 1
  */

  const OPPONENT_MOVES = ['A', 'B', 'C'];

  const lines = data.toString().replace(/\r\n/g, '\n').split('\n');

  let points = 0;
  for (const line of lines) {
    const values = line.split(' ');
    const opponent = values[0];
    const mine = values[1];

    opponentMoveIndex = OPPONENT_MOVES.indexOf(opponent);

    // TODO: Move this to its own function
    if (mine == 'X') {
      // Needs to lose
      myMoveIndex = opponentMoveIndex - 1;
      if (myMoveIndex < 0) {
        myMoveIndex = 2;
      }
    } else if (mine == 'Y') {
      // Needs to draw
      myMoveIndex = opponentMoveIndex;
    } else if (mine == 'Z') {
      // Needs to win
      myMoveIndex = opponentMoveIndex + 1;
      if (myMoveIndex > 2) {
        myMoveIndex = 0;
      }
    }

    moveDiff = myMoveIndex - opponentMoveIndex;

    // Calculation
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
