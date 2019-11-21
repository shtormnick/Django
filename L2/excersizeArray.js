var roster = [];
function addNew() {
  var name = prompt("Add name");
  roster.push(name);
}
function remove() {
  var name = prompt("Remove name");
  var index = roster.indexOf(name);
 if( index > -1){
   roster.splice(index, 1);
 }
 console.log(roster);
}
function display() {
  for(var i = 0;i<roster.length;i++){
  console.log(roster[i])
}
}
