var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  alter: function() {
    alert ('Name is ' + this.name + ','
    + 'Job is ' + this.job + ','
    + 'Age is ' +  this.age);
  }
}

var employee1 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
    console.log(this.name.length);
  }
}

var employee2 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function() {
    console.log (this.name.split(" ",1));
  }
}
