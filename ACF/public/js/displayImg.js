
/*      "date": "August 28",
      "title": "title of artwork",
      "artistName": "name/username of artist",
      "description": "img description",
      "size": "",
      "medium": "digital/traditional",
      "NPO":"npo name",
      "imageData":"fundraiser, donation, etc",
      "event": "",
      "win":"yes/no",
      "imageUrl":"image address",
      "comments":[
        "comment1", "comment2"  */

fetch("/json/image.json")
.then(response => 
{
  console.log(response)
  return response.json()
})
.then(response => 
{

  var rowDiv = document.getElementById('rowParent');

  for( var i = 0; i < response.image.length; i++)
  {

    var vColumn = document.createElement("div");
    vColumn.classList.add("column");

    var imgtag = document.createElement("img");
    imgtag.src = response.image[i].imageUrl; 
     var url  = `https://new-venturesketch-website.venturesketch.repl.co/html/artGallery.html?artistName=${response.image[i].artistName}&imageName=${response.image[i].imageUrl}`;
    imgtag.className= url;
    imgtag.addEventListener('click', function () {

      window.open(this.className);

     // `<a href ="${url}">Click me</a>`
       
    });
    var leftDiv = document.createElement("div");
    leftDiv.classList.add("leftDivUnderPicture");

    var artistName = document.createElement("div");
    artistName.innerHTML = response.image[i].artistName;
    artistName.classList.add("artistName");

    var title = document.createElement("div");
    title.innerHTML = response.image[i].title;
    title.classList.add("title");


   var rightDiv = document.createElement("div");
    rightDiv.classList.add("rightDivUnderPicture");

    var cButton = document.createElement("button");
    cButton.innerHTML = "comment";
    cButton.classList.add("commentButton");
    cButton.addEventListener('click', function () {
            window.open("/html/artGallery2.html");

    });

    leftDiv.append(artistName, title);
    rightDiv.append(cButton);
    vColumn.append(imgtag,leftDiv , rightDiv);
    rowDiv.append(vColumn);


  }

})
.catch(error => {console.error()})


  

