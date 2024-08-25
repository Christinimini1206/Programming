const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const MongoClient = require('mongodb').MongoClient;

const connectionString = 'mongodb+srv://Venture:Sketch@venturesketch.dgjs2.mongodb.net/venturesketch?retryWrites=true&w=majority';

app.use(bodyParser.urlencoded({extended: true}));
app.listen(3000, function() {
	console.log('listening on 3000')
});

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html')
});

app.get('/artGallery2.html', function(req, res){
  res.sendFile(__dirname + '/artGallery2.html')
});

MongoClient.connect(connectionString, (err, client) => {
  if (err) return console.error(err)
  console.log('Connected to Database')  // Check if it’s connected
  const db = client.db('VentureSketch')
  const quotes = db.collection('images_test')

  app.post('/images', (req, res) => {
    console.log(req.body.image)
    quotes.insertOne(req.body)
      .then(result => {
        console.log(result)
      })
      .catch(error => console.error(error))
  })
})

