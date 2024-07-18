//Move the catcher with the left and right arrow keys to catch the falling objects. 

/* VARIABLES */
let catcher, fallingObject;
let score = 0;

/* PRELOAD LOADS FILES */
function preload(){
  
}

/* SETUP RUNS ONCE */
function setup() {
  createCanvas(400,400);
  
  //Create catcher 
  catcher = new Sprite(200, 380, 100, 20, "k");
  catcher.color = color(95,158,160);
  
  //Create falling object
  fallingObject = new Sprite(100,0,10);
  fallingObject.color = color(0,128,128);
  fallingObject.vel.y = 5;

}

/* DRAW LOOP REPEATS */
function draw() {
  background(224,224,224);

  // Draw directions to screen
  fill(0);
  textSize(12);
  text("Move the \ncatcher with the \nleft and right \narrow keys to \ncatch the falling \nobjects.", width - 100, 20);

  //If fallingObject reaches bottom, move back to random position at top
  if (fallingObject.y >= height) {
    fallingObject.y = 0;
    fallingObject.x = random(width);
    fallingObject.y = random(1, 5);
    score -= 1;
  }

  // Move catcher
  if (kb.pressing("left")) {
    catcher.vel.x = -5;
  }
  else if (kb.pressing("right")) {
    catcher.vel.x = 5;
  }
  else {
    catcher.vel.x = 0;
  }

  // Stop catcher at edges of screen
  if (catcher.x < 50) {
    catcher.x = 50;
  }
  else if (catcher.x > 350) {
    catcher.x = 350;
  }

  //If fallingObject collides with catcher, move back to random position at top
  if (fallingObject.collides(catcher)) {
    fallingObject.y = 0;
    fallingObject.x = random(width);
    fallingObject.vel.y = random(5, 10);
    fallingObject.direction = "down";
    score += 1;
  }

  fill(0, 128, 128);
  textSize(20);
  text("Score: " + score, 10, 30);

  if (score == 5) {
    win();
  }
}

function win() {
  background(244, 244, 244);
  catcher.pos = {x: 0, y: -200};
  fallingObject.pos = {x: 0, y: -400};
  textAlign(CENTER);
  text("You Won!", width / 2, height / 2);
  textSize(40);
}