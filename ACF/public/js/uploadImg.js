
var form = document.getElementById("form");

form.addEventListener("submit",function(event){
  event.preventDefault();
  var reader = new FileReader();
  var name = document.getElementById("imageFile").files[0].name;
  console.log(name);
  
  reader.readAsDataURL(document.getElementById("imageFile").files[0]);
  
  reader.addEventListener("load", function(){
    localStorage.setItem(name, this.result);


  });


});


});
/*
for(var i =0; i< localStorage.length; i++){ 
  var im = new Image();
  im.src = localStorage.getItem(localStorage.key(i));*/

  $.getJSON("image.json", function (result){
    result.image[0]: name
  });