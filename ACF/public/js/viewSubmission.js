loadToolbar()

function loadToolbar(){
  var btns = document.querySelectorAll('.collapsible');
  for(var i = 0; i < btns.length; i++){
    var btn = btns[i];
    btn.addEventListener('click', function(){
      var e = this.nextElementSibling;
      if (e.style.display === 'none'){
        e.style.display = 'block';
 /*       var height = 
        document.getElementById("artworks").style.height = "";*/
      }
      else{
        e.style.display = 'none';
      }
    });
  }
}

/*fetch("NPO.json")
  .then(response => 
  {
    console.log(response)
    return response.json()
  })
  .then(response => console.log(response.NPO[0]))
  .catch(error => {console.error()})


  fetch("VSartWorks.jpg")
  .then(response =>{
      console.log(response);
      return response.blob(); 


    })
  .then(response =>{
      console.log(response);
      document.getElementById("chocolate").src=URL.createObjectURL(response);
    }) */

/*var imageArray = new Array();

if (localStorage.getItem("image")){
     imageArray = JSON.parse(localStorage.getItem("image"));
     loadBGImages(imageArray, document.querySelector('#artworks'))
}
else{
  fetch("/json/image.json")
  .then(response => 
  {
    return response.json();
  })
  .then(response => {
    console.log(response)
    localStorage.setItem("image", JSON.stringify(response.image));
    imageArray = response.image;})
  .catch(error => {console.error()})
  loadBGImages(imageArray, document.querySelector('#artworks'))
}

function loadBGImages(urls, div){
  console.log(urls);
  for (var i = 0; i < urls.length; i++){
    
    var imgtag = new Image();
    imgtag.src = urls[i].imageUrl;
    imgtag.classList.add('imgbtn');
    imgtag.title = urls[i].title;
    imgtag.addEventListener('click', function(){

      document.getElementById('artTitle').innerHTML = this.title;
      document.getElementById('biggerImage').src = this.src;

      
    });
    imgtag.addEventListener('dblclick', function() {
      window.open("https://a0eb4cf9-abbe-4ac3-bfbe-9eeb5a97af2f.id.repl.co/2ndPage.html?artistName=Autumn1&imageName=artwork1.jpg", '_blank');
    });
    div.appendChild(imgtag);
  }
}*/

if (localStorage.getItem("image")){
     imageArray = JSON.parse(localStorage.getItem("image"));
     loadArtworks(imageArray, document.querySelector('#artworks'))
}
else{
  fetch("/json/image.json")
  .then(response => 
  {
    return response.json();
  })
  .then(response => {
    console.log(response)
    localStorage.setItem("image", JSON.stringify(response.image));
    imageArray = response.image;})
  .catch(error => {console.error()})
  loadBGImages(imageArray, document.querySelector('#artworks'))
}

function loadArtworks(urls, div){
  for (var i = 0; i < urls.length; i++){
    var titleArtist = new Array;
    titleArtist.title = urls[i].title;
    titleArtist.artist = urls[i].artistName;
    titleArtist.addEventListener('click', function(){
      document.getElementById('artTitle').innerHTML = this.title;
      document.getElementById('biggerImage').style.src = this.src;
      
    });
    titleArtist.addEventListener('dblclick', function() {
      window.open("https://a0eb4cf9-abbe-4ac3-bfbe-9eeb5a97af2f.id.repl.co/2ndPage.html?artistName=Autumn1&imageName=artwork1.jpg", '_blank');
    });
    div.appendChild(imgtag);
  }
}

