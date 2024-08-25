/* IMPORTS */
const express = require("express");
const ejs = require("ejs");
const { text } = require("body-parser");

/* INITIALIZING THE APP */
const app = express();

// Rendering the homepage: index
app.get("/", function (req, res) {
  res.render("index");
});

app.get("/eat", function (req, res) {
  res.send("I love pizza and food 🍕");
});

/* TEMPLATE ENGINE */
app.set("view engine", "ejs");

/* LOADING STATIC FILES */
app.use(express.static("public"));
app.use(express.static("views"));

app.get("/pizza", function (req, res) {
  res.send("🍕");
});

app.get("/pizza/:eat", (req, res) => {
  const count = req.params.eat;
  let i = 0,
    text = "";
  while (i < count) {
    text += "🍕";
    i++;
  }
  res.send(text);
});

app.listen(3000, function () {
  console.log("listening on 3000");
});
