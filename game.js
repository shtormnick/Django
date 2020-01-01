var playerOne = prompt('Player One: Enter your Name, you will be Blue');
var p1Color = 'rgb(86, 151, 255)';

var playerTwo = prompt('Player Two: Enter your Name, you will be Red');
var p2Color = 'rgb(237, 45, 73)';

var currentPlauer = 1;
var currentName = playerOne;
var currentColor = p1Color;

$('h3').text(playerOne+'it is your turn, please pick a column to drop your blue chip.');
$('.board button').on('click',function() {
  var col =$(this).coloset('td').index();
  var bottomAvail = checkBottom(col);
  changeColor(bottomAvail,col,currentColor);
})
