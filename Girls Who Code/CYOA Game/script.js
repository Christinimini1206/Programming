//Press a button to choose your path
//See the README file for more information

/* VARIABLES */
let enterButton;
let instButton;
let a1Button;
let a2Button;
let b1Button;
let b2Button;
let screen = 0;
let font;

function preload() {
  font = loadFont('assets/motley-forces/Motley Forces.ttf');
  instrCharacter = loadImage("assets/Images/InstructionCharacter.png")
}

/* SETUP RUNS ONCE */
function setup() {
  createCanvas(600, 400);
  textAlign(CENTER);
  noStroke();

  textFont(font);

  textSize(44);
  // Set up the home screen
  background("pink");
  text("Make a Magic Potion\nwith Me!", width / 2, height / 2 - 80);

  textSize(25);
  
  // Create buttons for all screens
  enterButton = new Sprite(width / 2, height / 2 + 100);
  instButton = new Sprite(-100, -100);
  redoButton = new Sprite(-800, -800)
  
  a1Button = new Sprite(-200, -200);
  a2Button = new Sprite(-300, -300);
  
  b1Button = new Sprite(-400, -400);
  b2Button = new Sprite(-500, -500);
  
  c1Button = new Sprite(-600, -600);
  c2Button = new Sprite(-700, -700);
  
  d1Button = new Sprite(-900, -900);
  d2Button = new Sprite(-1000, -1000);
  
  e1Button = new Sprite(-200, 0);
  e2Button = new Sprite(-1000, -100);

  f1Button = new Sprite(-1000, -200);
  f2Button = new Sprite(-1000, -300);
}

/* DRAW LOOP REPEATS */
function draw() {
  // Display enter button
  enterButton.width = 100;
  enterButton.height = 50;
  enterButton.collider = 'k';
  enterButton.color = 'plum';
  enterButton.text = "Start!";

  // Check enter button
  // Main Page
  if (enterButton.mouse.presses()) {
    showScreenInstruction();
    screen = 0.5;
  }

  // Instructions Page
  if (instButton.mouse.presses()) {
    showScreen1();
    screen = 1;
  }

  /* GAME */
  if (screen == 1) {
    if (a1Button.mouse.presses()) {
      showScreen2();
      screen = 2;
    }
    else if (a2Button.mouse.presses()) {
      showScreen5();
      screen = 5;
    }
  }
  else if (screen == 2) {
    if (b1Button.mouse.presses()) {
      showScreen3();
      screen = 3
    }
    else if (b2Button.mouse.presses()) {
      showScreen4();
      screen = 4;
    }
  }
  else if (screen == 3) {
    if (c1Button.mouse.presses()) {
      showScreen6();
      screen = 6;
    }
    else if (c2Button.mouse.presses()) {
      showScreen7();
      screen = 7;
    }
  }
  else if (screen == 4) {
    if (d1Button.mouse.presses()) {
      showScreen8();
      screen = 8;
    }
    else if (d2Button.mouse.presses()) {
      showScreen6();
      screen = 6;
    }
  }
  else if (screen == 5) {
    if (e1Button.mouse.presses()) {
      showScreen9();
      screen = 9;
    }
    else if (e2Button.mouse.presses()) {
      showScreen6();
      screen = 6;
    }
  }
  else if (screen == 6) {
    if (redoButton.mouse.presses()) {
      showScreenInstruction();
      redoButton.pos = {x: -800, y: -800};
      screen = 0.5;
    }
  }
  else if (screen == 9) {
    if (f1Button.mouse.presses()) {
      showScreen10();
      screen = 10;
    }
    else if (f2Button.mouse.presses()) {
      showScreen8();
      screen = 8;
    }
  }
}

/* FUNCTIONS TO DISPLAY SCREENS */
// Instruction/Story Screen
function showScreenInstruction() {
  background(249, 255, 196);
  textSize(20);
  textAlign(LEFT);
  text("Sabrina is experiencing some \ndifficulties with her school work. \nShe got an assignment to make \na potion, which she will present \nin the class, but she accidentally \ndipped her recipe book in water, \nwhich erased all the instructions! \nThe assignment is due tomorrow, \nand she needs your help! Help her \ncreate the best potion and get \nan A+ on this assignment!", 30, height / 2 - 125);
  enterButton.pos = {x: -100, y: -100};
  image(instrCharacter, 360, 110, 220, 220);

  textAlign(CENTER);
  instButton.pos = {x: width / 4 * 3 + 75, y: 70}
  instButton.width = 80;
  instButton.height = 30;
  instButton.collider = 'k';
  instButton.color = 'plum';
  instButton.text = "Help!";
  instButton.textSize = 20;
}

// Underground water vs. Molten Uranus ice
function showScreen1() {
  
  instButton.pos = {x: -200, y: -200};
  
  background('paleturquoise');
  // text("Welcome to screen 1. Make your first choice.", width / 2, height / 2 - 100);
  // Sabrina: We first need the solvent for our potion! Here's the recipe for you!

  // Add A1 button
  a1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  a1Button.width = 230;
  a1Button.height = 50;
  a1Button.collider = 'k';
  a1Button.color = 'plum';
  a1Button.text = "Underground Water";
  a1Button.textSize = 20;
  // Sabrina: 

  // Add A2 button
  a2Button.pos = {x: width / 2 + 160, y: height / 2 + 100}
  a2Button.width = 230;
  a2Button.height = 50;
  a2Button.collider = 'k';
  a2Button.color = 'plum';
  a2Button.text = "Molten Uranus Ice";
  a2Button.textSize = 20;
}

// Underground water -> Brown sugar vs. Salt
function showScreen2() {
  background('palegreen');
  // text("Welcome to screen 2. Make your second choice.", width / 2, height / 2 - 100);
  a1Button.pos = {x: -200, y: -200};
  a2Button.pos = {x: -300, y: -300};

  b1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  b1Button.width = 150;
  b1Button.height = 50;
  b1Button.collider = 'k';
  b1Button.color = 'plum';
  b1Button.text = "brown sugar";
  b1Button.textSize = 20;

  b2Button.pos = {x: width / 2 + 160, y: height / 2 + 100};
  b2Button.width = 80;
  b2Button.height = 50;
  b2Button.collider = 'k';
  b2Button.color = 'plum';
  b2Button.text = "salt";
  b2Button.textSize = 20;
}

// Underground water -> Brown sugar -> Oak tree branch vs. Blackthorn tree branch
function showScreen3() {
  background('lavender');
  // text("You hit an end point at Screen 3.", width / 2, height / 2 - 100);
  b1Button.pos = {x: -400, y: -400};
  b2Button.pos = {x: -500, y: -500};

  c1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  c1Button.width = 180;
  c1Button.height = 50;
  c1Button.collider = 'k';
  c1Button.color = 'plum';
  c1Button.text = "oak tree branch";
  c1Button.textSize = 20;

  c2Button.pos = {x: width / 2 + 160, y: height / 2 + 100};
  c2Button.width = 250;
  c2Button.height = 50;
  c2Button.collider = 'k';
  c2Button.color = 'plum';
  c2Button.text = "blackthorn tree branch";
  c2Button.textSize = 20;
}

// Underground water -> Salt -> Squid ink vs. Apple moss
function showScreen4() {
  background('plum');
  // text("You hit an end point at Screen 4.", width / 2, height / 2 - 100);
  b1Button.pos = {x: -100, y: -100};
  b2Button.pos = {x: -150, y: -150};

  d1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  d1Button.width = 180;
  d1Button.height = 50;
  d1Button.collider = 'k';
  d1Button.color = 'white';
  d1Button.text = "squid ink";
  d1Button.textSize = 20;

  d2Button.pos = {x: width / 2 + 160, y: height / 2 + 100};
  d2Button.width = 180;
  d2Button.height = 50;
  d2Button.collider = 'k';
  d2Button.color = 'white';
  d2Button.text = "apple moss";
  d2Button.textSize = 20;
}

// Molten Uranus ice -> Diamond powder vs. Iron ore
function showScreen5() {
  background("lightgreen");
  // text("You hit an end point at Screen 5.", width / 2, height / 2 - 100);
  a1Button.pos = { x: -200, y: -200 };
  a2Button.pos = { x: -50, y: -50 };

  e1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  e1Button.width = 180;
  e1Button.height = 50;
  e1Button.collider = 'k';
  e1Button.color = 'plum';
  e1Button.text = "diamond powder";
  e1Button.textSize = 20;

  e2Button.pos = {x: width / 2 + 160, y: height / 2 + 100};
  e2Button.width = 180;
  e2Button.height = 50;
  e2Button.collider = 'k';
  e2Button.color = 'plum';
  e2Button.text = "iron ore";
  e2Button.textSize = 20;
}

// Underground water -> Brown sugar -> Oak tree branch (Result: FAIL)
// Underground water -> Salt -> Apple moss (Result: FAIL)
// Molten Uranus ice -> Iron ore
function showScreen6() {
  background("gray");
  text("I don't think that was the right material...", width / 2, 100);  
  redoButton.pos = {x: width / 2, y: height / 2 + 100};
  redoButton.width = 230;
  redoButton.height = 50;
  redoButton.collider = 'k';
  redoButton.color = 'plum';
  redoButton.text = "Make a New Potion";
  redoButton.textSize = 20;

  c1Button.pos = {x: -600, y: -600};
  c2Button.pos = {x: -700, y: -700};

  d1Button.pos = {x: -800, y: -800};
  d2Button.pos = {x: -900, y: -900};

  e1Button.pos = {x: -200, y: 0}
  e2Button.pos = {x: -1000, y: -100};
}

// Underground water -> Brown sugar -> Blackthorn tree branch (Result: SUCCESS)
function showScreen7() {
  c1Button.pos = {x: -600, y: -600};
  c2Button.pos = {x: -700, y: -700};

  background("lightblue");
  text("Successful!", width / 2, 100)
}

// Underground water -> Salt -> Squid ink (Result: SUCCESS?)
function showScreen8() {
  d1Button.pos = {x: -800, y: -800};
  d2Button.pos = {x: -900, y: -900};

  f1Button.pos = {x: -1000, y: -200};
  f2Button.pos = {x: -1000, y: -300};

  background("lightblue");
  text("Successful?", width / 2, 100);
}

// Molten Uranus ice -> Diamond powder -> Crow's feather vs. Siren's scale 
function showScreen9() {
  e1Button.pos = {x: -200, y: 0};
  e2Button.pos = {x: -1000, y: -100};
  
  f1Button.pos = {x: width / 2 - 160, y: height / 2 + 100};
  f1Button.width = 180;
  f1Button.height = 50;
  f1Button.collider = 'k';
  f1Button.color = 'plum';
  f1Button.text = "crow's feather";
  f1Button.textSize = 20;

  f2Button.pos = {x: width / 2 + 160, y: height / 2 + 100};
  f2Button.width = 180;
  f2Button.height = 50;
  f2Button.collider = 'k';
  f2Button.color = 'plum';
  f2Button.text = "siren's scale";
  f2Button.textSize = 20;
}

// Molten Uranus ice -> Diamond powder -> Crow's feather (Result: SUCCESS - BEST)
function showScreen10() {
  f1Button.pos = {x: -1000, y: -200};
  f2Button.pos = {x: -1000, y: -300};

  background("lightblue");
  text("Successful!", width / 2, 100)
}