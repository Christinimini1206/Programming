var imageArray = new Array();

if(localStorage.getItem("image")){
 	imageArray = JSON.parse(localStorage.getItem("image"));
}
else{
  fetch("/json/image.json").then(response => 
  {
    console.log(response)
    return response.json()
  })
  .then(response => {console.log(response.image[0])
    localStorage.setItem("image", JSON.stringify(response.image));
    imageArray = response.image;})
  .catch(error => {console.error()})
}

//document.images[i]src.addEventListener("click", MakeMove, false)
/*Name: Artwork1.Jpg
Artist: Go Van Kampen
Date Submitted: 6/13/2021
About: Anime, Cartoon
Event: Poster: Fundraiser In SJSU
Npo: Acf,
Win?: Yes*/
function showArtist()
{

  const queryString = document.location.search;

  const urlParams = new URLSearchParams(queryString);

  console.log(queryString);

  const artistUsername = urlParams.get('artistName');
  const imageName = urlParams.get('imageName')

  var index = imageName.match(/(\d+)/);

  //console.log(index);
  
 //alert(artistUsername);   
 //alert(imageName);     
  
  // const artistUsername = "Lian Wang";
  // const imageName = "/pictures/1.png";
   document.getElementById('imageURL').src = imageName;

  
  document.getElementById('artist').innerHTML = imageArray[index[0]].artistName;
  document.getElementById('title').innerHTML = imageArray[index[0]].title;

  console.log(imageArray);

  //alert("we are at 2ndpage");
 // var artistUsername = "Autumn1";
  //var imageName= "artwork1.jpg";
  //$.getJSON("NPO.json", function(result){
  //console.log(result);
  //console.log(result.NPO);
  //console.log(result.NPO[0]);

  //Below is code for the grid of related images

  //int count = 0;
  // for ( var i = 0; i < imageArray.length; i++)
  // {
  //   if(imageArray[i].artistName == artistUsername || imageArray[i].event == imageName)
  //   {
  //     console.log(imageArray[i].artistName);
  //     console.log(imageArray[i].imageUrl);
        
  //       // create new div here
  //     //resource for creating element: https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement
  //     newDiv = document.createElement('div');
  //     newImg = document.createElement('img');
  //     newDiv.appendChild(newImg);

  //    currentDiv = document.getElementById('bottom');
  //     document.body.insertBefore(newDiv, currentDiv);

  //     //document.getElementById("title").innerHTML = imageArray[i].title;
  //     //document.getElementById("artist").innerHTML = imageArray[i].artistName;
  //     newImg.src = imageArray[i].imageUrl;
  //     //newImg.style.width = 10%;
  //   }
  // }
}


/*<section id= "top">
      <div class= "imgDisplay"></div>
      <div class= "imgInfo">
        <p>Title</p>
        <div id= "title"></div>
        <p>Artist</p>
        <div id= "artist"></div>
        <p>Image Information</p>
        <div id= "imageInfo"></div>
      </div>
    </section>
    <section id= "bottom">
    </section>*/


/*$.getJSON("artist.json", function(result){
  console.log(result.artist[0].works[0].name);
  localStorage.setItem('artist', JSON.stringify(result.artist));
  //console.log(localStorage.getItem('artist'));

  var artistArray = "";
  artistArray = localStorage.getItem('artist');
  //console.log(artistArray);

  //artistArray.push(newArtist);



});*/

