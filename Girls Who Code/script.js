//Press a button to choose your path
//See the README file for more information

/* VARIABLES */
let screen = 0;
let materials = [];
let materialLoadedImage = [];

let enter;
let storyScreen;
let skip;
let start;

let mat1;
let mat2;
let mat3;
let mat4;
let mat5;
let mat6;
let mat7;
let reset;
let matEaster;
let container;
let next;
let prev;

let chosen1;
let chosen2;
let chosen3;

let redo;

function preload() {
  // Arrows
  beforeArr = loadImage("Assets/Arrows/Before.png");
  nextArr = loadImage("Assets/Arrows/Next.png");

  // Materials
  material1 = loadImage("Assets/Materials/Material 1.png");
  material2 = loadImage("Assets/Materials/Material 2.png");
  material3 = loadImage("Assets/Materials/Material 3.png");
  material4 = loadImage("Assets/Materials/Material 4.png");
  material5 = loadImage("Assets/Materials/Material 5.png");
  material6 = loadImage("Assets/Materials/Material 6.png");
  material7 = loadImage("Assets/Materials/Material 7.png");

  // Game Play Screen
  beaker = loadImage("Assets/Game Play/beaker.png");
  resetMat = loadImage("Assets/Game Play/Reset.jpg");
}

/* SETUP RUNS ONCE */
function setup() {
  createCanvas(900, 600);
  textAlign(CENTER);
  textSize(60);
  noStroke();

  /* HOME SCREEN */
  background("pink");
  text("Aroma", width / 2, height / 2 - 100);
  enter = new Sprite(width / 2, height / 2 + 100);
  textSize(20);

  /* Create buttons for all screens */
  skip = new Sprite(-200, 100);  // Story Screen
  start = new Sprite(-200, 200);  // Instruction Screen
  // Arrow Buttons
  prev = new Sprite(1100, 0);
  next = new Sprite(1100, 100);
  // Game Play Screen
  container = new Sprite(-200, 300);
  mat1 = new Sprite(-200, 400);
  mat2 = new Sprite(-200, 500);
  mat3 = new Sprite(-200, 600);
  mat4 = new Sprite(-200, 700);
  mat5 = new Sprite(-200, 800);
  mat6 = new Sprite(-200, 900);
  mat7 = new Sprite(-200, 1000);
  reset = new Sprite(-200, 1100);

  chosen1 = new Sprite(-200, 1200);
  chosen2 = new Sprite(-200, 1300);
  chosen3 = new Sprite(-200, 1400);

  // Story Screen
  storyScreen = loadAnimation(
    'Assets/Story/Story1.png',
    'Assets/Story/Story2.png',
    'Assets/Story/Story3.png',
    'Assets/Story/Story4.png',
    'Assets/Story/Story5.png',
    'Assets/Story/Story6.png',
    'Assets/Story/Story7.png',
    'Assets/Story/Story8.png'
  );
  storyScreen.frameDelay = 10;
}

/* DRAW LOOP REPEATS */
function draw() {
  // Display enter button
  enter.width = 100;
  enter.height = 50;
  enter.collider = 'k';
  enter.color = 'plum';
  enter.text = "Start!";
  enter.textSize = 25;

  // Main page
  if (screen == 0) {
    if (enter.mouse.presses()) {
      instruction();
      screen = 1;
    }
  }
  // Instruction Page
  else if (screen == 1) {
    if (start.mouse.presses()) {
      chooseMaterialScreen();
      screen = 2;
    }
  }
  // Choose Materials Page
  else if (screen == 2) {
    if (prev.mouse.presses()) {
      instruction();
      screen = 1;
      materials = [];
    }
    else if (next.mouse.presses() && materials.length == 3) {
      mixMaterialScreen();
      screen = 3;
    }
    else if (reset.mouse.presses()) {
      materials = [];
    }
    else if (mat1.mouse.presses() && materials.includes(1) == false && materials.length < 3) {
      materials.push(1);
    }
    else if (mat2.mouse.presses() && materials.includes(2) == false && materials.length < 3) {
      materials.push(2);
    }
    else if (mat3.mouse.presses() && materials.includes(3) == false && materials.length < 3) {
      materials.push(3);
    }
    else if (mat4.mouse.presses() && materials.includes(4) == false && materials.length < 3) {
      materials.push(4);
    }
    else if (mat5.mouse.presses() && materials.includes(5) == false && materials.length < 3) {
      materials.push(5);
    }
    else if (mat6.mouse.presses() && materials.includes(6) == false && materials.length < 3) {
      materials.push(6);
    }
    else if (mat7.mouse.presses() && materials.includes(7) == false && materials.length < 3) {
      materials.push(7);
    }
    else if (reset.mouse.presses()) {
      materials = [];
    }
  }
  // Mixing Page
  else if (screen == 3) {
    if (prev.mouse.presses()) {
      chooseMaterialScreen();
      screen = 2;
      materials = [];
    }
    else if (next.mouse.presses()) {
      screen = 4;
    }
  }
}

/* FUNCTIONS TO DISPLAY SCREENS */
function story() {
  enter.pos = {x: -200, y: 0}
  background("pink");
  animation(storyScreen, width / 2, height / 2);

  skip.pos = {x: 800, y: 50};
  skip.width = 100;
  skip.height = 50;
  skip.collider = 'k';
  skip.color = 'plum';
  skip.text = "Skip";
  skip.textSize = 25;
}

function instruction() {
  enter.pos = {x: -200, y: 0}
  prev.pos = {x: 1100, y: 0};
  next.pos = {x: 1100, y: 100};
  mat1.pos = {x: -200, y: 400};
  mat2.pos = {x: -200, y: 500};
  mat3.pos = {x: -200, y: 600};
  mat4.pos = {x: -200, y: 700};
  mat5.pos = {x: -200, y: 800};
  mat6.pos = {x: -200, y: 900};
  mat7.pos = {x: -200, y: 1000};
  
  background("lightblue");

  text("Instruction\n\nClick any three materials you want and click \"Done\" after that.\nFeel free to look at recipe book to know what kind of material you need to look for.\nNOTE: There is an easter egg ending! Good luck with finding it :)", width / 2, height / 2 - 200);

  start.pos = {x: width / 2, y: height / 2 + 100};
  start.width = 250;
  start.height = 50;
  start.collider = 'k';
  start.color = 'plum';
  start.text = "Make a Perfume!";
  start.textSize = 20;
}

function chooseMaterialScreen() {
  start.pos = {x: -200, y: 100};
  container.pos = {x: -200, y: 300};
  background("beige");

  textSize(30);
  text("Choose Three Materials", width / 2, 70);

  // Arrows
  prev.pos = {x: 100, y: 50};
  prev.image = beforeArr;
  prev.collider = 'k';
  
  next.pos = {x: 800, y: 50};
  next.image = nextArr;
  next.collider = 'k';

  reset.pos = {x: width / 2 + 315, y: height / 2 - 100};
  reset.image = resetMat;
  reset.collider = 'k';

  // Perfume Materials
  mat1.image = material1;
  mat1.pos = {x: width / 2 - 315, y: height / 2 - 100};
  mat1.collider = 'k';
  
  mat2.image = material2;
  mat2.pos = {x: width / 2 - 105, y: height / 2 - 100};
  mat2.collider = 'k';
  
  mat3.image = material3;
  mat3.pos = {x: width / 2 + 105, y: height / 2 - 100};
  mat3.collider = 'k';

  mat4.image = material4;
  mat4.pos = {x: width / 2 - 315, y: height / 2 + 120};
  mat4.collider = 'k';
  
  mat5.image = material5;
  mat5.pos = {x: width / 2 - 105, y: height / 2 + 120};
  mat5.collider = 'k';
  
  mat6.image = material6;
  mat6.pos = {x: width / 2 + 105, y: height / 2 + 120};
  mat6.collider = 'k';
  
  mat7.image = material7;
  mat7.pos = {x: width / 2 + 315, y: height / 2 + 120};
  mat7.collider = 'k';

}

function mixMaterialScreen() {
  mat1.pos = {x: -200, y: 400};
  mat2.pos = {x: -200, y: 500};
  mat3.pos = {x: -200, y: 600};
  mat4.pos = {x: -200, y: 700};
  mat5.pos = {x: -200, y: 800};
  mat6.pos = {x: -200, y: 900};
  mat7.pos = {x: -200, y: 1000};

  chosen1.pos = {x: width / 2 - 300, y: height / 2 - 100};
  chosen2.pos = {x: width / 2, y: height / 2 - 100};
  chosen3.pos = {x: width / 2 + 300, y: height / 2 - 100};
  background("beige");

  let taken1 = false;
  let taken2 = false;
  let taken3 = false;
  
  container.pos = {x: width / 2, y: height / 2 + 100};
  container.image = beaker;

  if (materials.includes(1)) {
    if (taken1 == false) {
      taken1 = true;
      chosen1.image = material1;
    }
    else if (taken1 == false) {
      taken2 = true;
      chosen2.image = material1;
    }
    else if (taken1 == false) {
      taken3 = true;
      chosen3.image = material1;
    }
  }
  else if (materials.includes(2)) {
    if (taken1 == false) {
      taken1 = true;
      chosen1.image = material2;
    }
    else if (taken1 == false) {
      taken2 = true;
      chosen2.image = material2;
    }
    else if (taken1 == false) {
      taken3 = true;
      chosen3.image = material2;
    }
  }
  else if (materials.includes(3)) {
    if (taken1 == false) {
      taken1 = true;
      chosen1.image = material3;
    }
    else if (taken1 == false) {
      taken2 = true;
      chosen2.image = material3;
    }
    else if (taken1 == false) {
      taken3 = true;
      chosen3.image = material3;
    }
  }
}