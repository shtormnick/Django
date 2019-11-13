function sleebIn(weekday, vocation) {
  return (!weekday || vocation);
}
function monkeyTrouble(aSmile, bSmile) {
  return (aSmile && bSmile) || (!aSmile && !bSmile);
}
function stringTimes(str, n) {
  var returnStr='';
  var i = 0;
  while (i<n) {
    returnStr += str;
    i++
  }
  return returnStr;
}
function lukySum(a, b, c){
  if (a===13){
    return 0;
  }
  if (b === 13){
    return a;
  }
  if (c === 13){
    return a+b;
  }
  return a+b+c;
}
function caught_speeding(speed, is_birthday){
  var nTiket = 0;
  var sTiket = 1;
  var bTiket = 2;
  if (speed <= 60){
    return nTiket;
  }
  if (speed > 60 && speed <=80){
    return sTiket;
  }
  if (is_birthday){
    return speed -= 5;
  }
  return bTiket;
}
