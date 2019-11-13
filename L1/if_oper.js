var hot = false
var temp = 100

if (temp>80){
  console.log("Hot Outside");
}else {
  console.log("Its not very hot today");
}

var hot1 = false
var temp1 = 50

if (temp1>90) {
  console.log("Hot Outside");
} else if (temp1<=80 && temp1>=50) {
  console.log("Avarege temp Outside");
}else if (temp1<50 && temp1>=32) {
  console.log("Its pretty coll outside");
} else {
  console.log("Its is very coold outside");
}
