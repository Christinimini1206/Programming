const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const MongoClient = require('mongodb').MongoClient;

const connectionString = 'mongodb+srv://Venture:Sketch@venturesketch.dgjs2.mongodb.net/venturesketch?retryWrites=true&w=majority';

// var artistArray = new Array();
// var NPOArray = new Array();

var clickK1 = 0
var clickK2 = 0
var clickK3 = 0
var clickK4 = 0
var clickK5 = 0
var clickK6 = 0

var clickL1 = 0
var clickL2 = 0
var clickL3 = 0

var clickP1 = 0
var clickP2 = 0
var clickP3 = 0
var clickP4 = 0

// var newArtist = new Object();
var words = new Array();
var level = '';
var prefer = new Array();

/* $.getJSON("/json/artist.json", function(result){
  artistArray = result.artist;
  console.log(artistArray);
}); */

/*
fetch("/json/artist.json")
  .then(response => 
  {
    console.log(response)
    return response.json()
  })
  .then(response => {
    console.log(response.artist[0])
    artistArray = response.artist;
  })
  .catch(error => {console.error()})

fetch("/json/npo.json")
  .then(response => 
  {
    console.log(response)
    return response.json()
  })
  .then(response => {
    console.log(response.NPO[0])
    NPOArray = response.NPO;
  })
  .catch(error => {console.error()})
*/

app.use(bodyParser.urlencoded({extended: true}));
app.listen(3000, function() {
	console.log('listening on 3000')
});
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html')
});

function clickJoin(){
  alert('asdf');
  var choice = document.getElementById("role").value;
  if (choice == "artist"){
    window.location.href = "/html/artistSU.html";
    MongoClient.connect(connectionString, (err, client) => {
      if (err) return console.error(err)
      console.log('Connected to Database')  // Check if it’s connected
      const db = client.db('VentureSketch')
      const quotes = db.collection('Artists_test')

      app.post('/userInfo', (req, res) => {
        quotes.insertOne(req.body)
          .then(result => {
            console.log(result)
          })
          .catch(error => console.error(error))
      })
    })
    // location.replace("https://Artist-Sign-Up-Page.christinel1206.repl.co")
    /*
    newArtist.firstName = document.getElementById("fname").value;
    newArtist.lastName = document.getElementById("lname").value;
    newArtist.email = document.getElementById("email").value;
    newArtist.password = document.getElementById("pword").value;
     //artistArray.push(newArtist);
    localStorage.setItem('temp', JSON.stringify(newArtist));
    */

    // localStorage.setItem('artist', JSON.stringify(artistArray));
    // console.log(localStorage.getItem('artist'));
  }

  else if (choice == "NPO"){
    window.location.href = "/html/npoSU.html";
    MongoClient.connect(connectionString, (err, client) => {
      if (err) return console.error(err)
      console.log('Connected to Database')  // Check if it’s connected
      const db = client.db('VentureSketch')
      const quotes = db.collection('NPO')

      app.post('/userInfo', (req, res) => {
        quotes.insertOne(req.body)
          .then(result => {
            console.log(result)
          })
          .catch(error => console.error(error))
      })
    })
    /*
    var newNPO = new Object();
    newNPO.firstName = document.getElementById("fname").value;
    newNPO.lastName = document.getElementById("lname").value;
    newNPO.email = document.getElementById("email").value;
    newNPO.password = document.getElementById("pword").value;
    localStorage.setItem('tempNPO', JSON.stringify(newNPO));
    */
    // newNPO.companyName = document.getElementById("").value;
    // newNPO.companyDesc = document.getElementById("").value;
        // localStorage.setItem('NPO', JSON.stringify(NPOArray));
    console.log(localStorage.getItem('NPO'));
  }

  else {
    alert("Please fill out the form.");
  }
}


// Key 1
function key1() {
  // console.log(localStorage)
  // var lst = localStorage.getItem("artist");
  clickK1++;
  if (clickK1 % 2 == 1) {
    document.getElementById("k1").style.backgroundColor = "#001BA8";
    words.push('aesthetic');
    console.log(words);
  }
  else if (clickK1 % 2 == 0) {
    $(document).ready(function(){
      $("#k1").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('aesthetic');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}

// Key 2
function key2() {
  clickK2++;
  if (clickK1 % 2 == 1) {
    document.getElementById("k2").style.backgroundColor = "#001BA8";
    words.push('anime');
    console.log(words);
  }
  else if (clickK2 % 2 == 0) {
    $(document).ready(function(){
      $("#k2").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('anime');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}

// Key 3
function key3() {
  clickK3++;
  if (clickK3 % 2 == 1) {
    document.getElementById("k3").style.backgroundColor = "#001BA8";
    words.push('fineArt');
    console.log(words);
  }
  else if (clickK3 % 2 == 0) {
    $(document).ready(function(){
      $("#k3").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('fineArt');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}

// Key 4
function key4() {
  clickK4++;
  if (clickK4 % 2 == 1) {
    document.getElementById("k4").style.backgroundColor = "#001BA8";
    words.push('popArt');
    console.log(words);
  }
  else if (clickK4 % 2 == 0) {
    $(document).ready(function(){
      $("#k4").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('popArt');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}

// Key 5
function key5() {
  clickK5++;
  if (clickK5 % 2 == 1) {
    document.getElementById("k5").style.backgroundColor = "#001BA8";
    words.push('vibrant');
    console.log(words);
  }
  else if (clickK5 % 2 == 0) {
    $(document).ready(function(){
      $("#k5").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('vibrant');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}

// Key 6
function key6() {
  clickK6++;
  if (clickK6 % 2 == 1) {
    document.getElementById("k6").style.backgroundColor = "#001BA8";
    words.push('others');
    console.log(words);
  }
  else if (clickK6 % 2 == 0) {
    $(document).ready(function(){
      $("#k6").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('others');
        words.splice(indexN, 1)
        console.log(words);
      });
    });
  }
}


// Level 1
function level1() {
  clickL1++;
  if (clickL1 % 2 == 1) {
    document.getElementById("l1").style.backgroundColor = "#001BA8";
    level = 'beginner';
  }
  else if (clickL1 % 2 == 0) {
    $(document).ready(function(){
      $("#l1").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        level = '';
      });
    });
  }
}

// Level 2
function level2() {
  clickL2++;
  if (clickL2 % 2 == 1) {
    document.getElementById("l2").style.backgroundColor = "#001BA8";
    level = 'intermediate';
  }
  else if (clickL2 % 2 == 0) {
    $(document).ready(function(){
      $("#l2").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        level = '';
      });
    });
  }
}

// Level 3
function level3() {
  clickL3++;
  if (clickL3 % 2 == 1) {
    document.getElementById("l3").style.backgroundColor = "#001BA8";
    level = 'professional';
  }
  else if (clickL3 % 2 == 0) {
    $(document).ready(function(){
      $("#l3").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        level = '';
      });
    });
  }
}


// Preference 1
function prefer1() {
  clickP1++;
  if (clickP1 % 2 == 1) {
    document.getElementById("p1").style.backgroundColor = "#001BA8";
    prefer.push('poster');
  }
  else if (clickP1 % 2 == 0) {
    $(document).ready(function(){
      $("#p1").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('poster');
        prefer.splice(indexN, 1)
        console.log(prefer);
      });
    });
  }
}

// Preference 2
function prefer2() {
  clickP2++;
  if (clickP2 % 2 == 1) {
    document.getElementById("p2").style.backgroundColor = "#001BA8";
    prefer.push('cards');
  }
  else if (clickP2 % 2 == 0) {
    $(document).ready(function(){
      $("#p2").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('cards');
        prefer.splice(indexN, 1)
        console.log(prefer);
      });
    });
  }
}

// Preference 3
function prefer3() {
  clickP3++;
  if (clickP3 % 2 == 1) {
    document.getElementById("p3").style.backgroundColor = "#001BA8";
    prefer.push('logos');
  }
  else if (clickP3 % 2 == 0) {
    $(document).ready(function(){
      $("#p3").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('logos');
        prefer.splice(indexN, 1)
        console.log(prefer);
      });
    });
  }
}

// Preference 4
function prefer4() {
  clickP4++;
  if (clickP4 % 2 == 1) {
    document.getElementById("p4").style.backgroundColor = "#001BA8";
    prefer.push('others');
  }
  else if (clickP4 % 2 == 0) {
    $(document).ready(function(){
      $("#p4").hover(function(){
        $(this).css("background-color", "#001BA8");
        }, function(){
        $(this).css("background-color", "#FFFFFF");
        var indexN = words.indexOf('others');
        prefer.splice(indexN, 1)
        console.log(prefer);
      });
    });
  }
}


function clickJoinArt(){
  var temp = JSON.parse(localStorage.getItem('temp'));
  temp.keywords = words;
  temp.level = level;
  temp.preference = prefer;
  artistArray.push(temp);
  localStorage.setItem('artist', JSON.stringify(artistArray));
  window.location.href = "/html/verify.html";
}

function clickJoinNPO() {
  var tempNPO = JSON.parse(localStorage.getItem('tempNPO'));
  tempNPO.compName = document.getElementById("compName").value;
  tempNPO.compDesc = document.getElementById("compDesc").value;
  NPOArray.push(tempNPO);
  localStorage.setItem('NPO', JSON.stringify(NPOArray));
  window.location.href = "/html/verify.html";
}

function connectMongoDB() {
  
}