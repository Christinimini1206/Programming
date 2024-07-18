/* VARIABLES */
var canvasX = 400;
var canvasY = 400;

var leftEyeX = 158;
var rightEyeX = canvasX - leftEyeX;

var eyeY = 190;
var pupilY = eyeY - 1;

var eyeWidth = 45;
var eyeHeight = 30;

var pupilWidth = 25;
var pupilHeight = 25;


/* SETUP RUNS ONCE */
function setup() {
  //sets the screen size
  createCanvas(canvasX, canvasY); 

  //sets the background color
  background(173, 239, 255); 
}

/* DRAW LOOP REPEATS */
function draw() {
  angleMode(DEGREES);
  rectMode(CENTER);

  /* BACKGROUND SHADOW */
  var moveX = 5;
  var moveY = 5;
  fill(125, 211, 232);
  stroke(125, 211, 232);

  strokeWeight(0);
  rect(200 + moveX, 253 + moveY, 180, 180);
  ellipse(canvasX / 2 + moveX, canvasY / 2 + moveY, 158, 190);
  ellipse(canvasX / 2 + moveX, canvasY / 2 - 30 + moveY, 180, 180);
  rect(110 + moveX, 250 + moveY, 20, 200);
  rect(canvasX - 110 + moveX, 250 + moveY, 20, 200);
  triangle(300 + moveX, 350 + moveY, 280 + moveX, 350 + moveY, 280 + moveX, 360 + moveY);
  triangle(canvasX - 300 + moveX, 350 + moveY, canvasX - 280 + moveX, 350 + moveY, canvasX - 280 + moveX, 360 + moveY);
  strokeWeight(20);
  arc(200 + moveX, 165 + moveY, 180, 180, 180, 360);
  arc(200 + moveX, 155 + moveY, 180, 180, 180, 360);

  
  /* BACK HAIR */
  strokeWeight(0);
  fill(8, 122, 161);
  rect(200, 253, 180, 180);
  fill(128, 138, 194, 191);
  rect(200, 253, 140, 180);
  fill(173, 239, 255);
  ellipse(200, 345, 180, 30);


  /* FACE */
  // Whole Face
  fill(217, 170, 158);
  ellipse(canvasX / 2, canvasY / 2, 170, 190);
  fill(255, 239, 224);
  ellipse(canvasX / 2, canvasY / 2, 158, 190);
  fill(255, 239, 224) ;
  ellipse(canvasX / 2, canvasY / 2 - 30, 180, 180);

  // Blush
  fill(255, 226, 217);
  ellipse(canvasX / 2 - 55, canvasY / 2 + 12, 40, 30);
  ellipse(canvasX / 2 + 55, canvasY / 2 + 12, 40, 30);

  // Eyelash Shadow
  if (mouseIsPressed) {
    strokeWeight(0);
  }
  else {
    strokeWeight(2);
  }
  stroke(217, 170, 158);
  noFill();
  arc(leftEyeX - 14, eyeY - 10, eyeWidth - 8, eyeWidth / 2 - 10, 90, 180);
  arc(rightEyeX + 14, eyeY - 10, eyeWidth - 8, eyeWidth / 2 - 10, 0, 90);

  arc(leftEyeX - 9, eyeY - 20, eyeWidth - 20, eyeWidth / 2 - 5, 90, 180);
  arc(rightEyeX + 9, eyeY - 20, eyeWidth - 20, eyeWidth / 2 - 5, 0, 90);

  // Mole
  strokeWeight(0);
  fill(54, 36, 32);
  ellipse(canvasX / 2 - 60, canvasY / 2 + 8, 3, 3);
  ellipse(217, 266, 2, 2);

  /* EYEBROWS */
  // Brows
  noFill();
  strokeWeight(2);
  stroke(4, 48, 51);
  arc(leftEyeX, eyeY - 25, eyeWidth + 10, 20, 180, 360);
  arc(rightEyeX, eyeY - 25, eyeWidth + 10, 20, 180, 360);

  // Rectangles to cover
  strokeWeight(0);
  fill(255, 239, 224);
  rect(leftEyeX - 30, eyeY - 25, 15, 15);
  rect(leftEyeX + 30, eyeY - 25, 15, 15);

  rect(rightEyeX - 30, eyeY - 25, 15, 15);
  rect(rightEyeX + 30, eyeY - 25, 15, 15);

  
  /* EYES */
  if (mouseIsPressed) {
    // Eyelids
    strokeWeight(5);
    noFill();

    stroke(4, 48, 51);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight, 0, 180);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight - 5, 0, 180);

    arc(rightEyeX, eyeY, eyeWidth, eyeHeight, 0, 180);
    arc(rightEyeX, eyeY, eyeWidth, eyeHeight - 5, 0, 180);

    // Eyelids (Color 2)
    strokeWeight(3);
    stroke(31, 121, 128);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight - 3, 0, 180);
    arc(rightEyeX, eyeY, eyeWidth, eyeHeight - 3, 0, 180);
  }
  else {
    // Outer Eye Part
    fill(217, 170, 158);
    ellipse(leftEyeX - 2, eyeY + 0.5, eyeWidth, eyeHeight);
    ellipse(rightEyeX + 2, eyeY + 0.5, eyeWidth, eyeHeight);
    
    fill('white');
    ellipse(leftEyeX, eyeY, eyeWidth, eyeHeight);
    ellipse(rightEyeX, eyeY, eyeWidth, eyeHeight);
  
    // Shade
    strokeWeight(5);
    noFill();
    stroke(225, 220, 230);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight - 15, 180, 360);
    arc(rightEyeX, eyeY, eyeWidth, eyeHeight - 15, 180, 360);
  
    strokeWeight(0);
    
    // Pupils
    fill("black");
    ellipse(leftEyeX - 3, pupilY, pupilWidth, pupilHeight);
    ellipse(rightEyeX - 5, pupilY, pupilWidth, pupilHeight);
  
    // Pupils (Color Layer 1)
    fill(16, 100, 115);
    ellipse(leftEyeX - 3, pupilY + 5, pupilWidth - 8, pupilHeight - 12);
    ellipse(rightEyeX - 5, pupilY + 5, pupilWidth - 8, pupilHeight - 12);
  
    // Pupils (Color Layer 2)
    fill(82, 134, 217);
    ellipse(leftEyeX - 3, pupilY + 7, pupilWidth - 15, pupilHeight - 17);
    ellipse(rightEyeX - 5, pupilY + 7, pupilWidth - 15, pupilHeight - 17);
  
    // Pupils (Color Layer 3)
    fill(185, 144, 245);
    ellipse(leftEyeX - 3, pupilY, pupilWidth - 20, pupilHeight - 8);
    ellipse(rightEyeX - 5, pupilY, pupilWidth - 20, pupilHeight - 8);
  
    // Pupils (Color Layer 4)
    fill(238, 220, 252);
    ellipse(leftEyeX - 3, pupilY, pupilWidth - 22, pupilHeight - 10);
    ellipse(rightEyeX - 5, pupilY, pupilWidth - 22, pupilHeight - 10);
  
  
    // Eye Highlight 1
    fill(238, 220, 252);
    ellipse(leftEyeX + 4, pupilY + 2, 3, 3);
    ellipse(rightEyeX + 2, pupilY + 2, 3, 3);
  
    // Eye Highlight 2
    fill(238, 220, 252);
    ellipse(leftEyeX, pupilY, 5, 5);
    ellipse(rightEyeX - 2, pupilY, 5, 5);
  
    // Eye Highlight 3
    fill('white');
    ellipse(leftEyeX - 4, pupilY - 6, 12, 12);
    ellipse(rightEyeX - 6, pupilY - 6, 12, 12);

    // Eyelids
    strokeWeight(5);
    noFill();

    stroke(4, 48, 51);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight, 180, 360);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight - 5, 180, 360);

    arc(rightEyeX, eyeY, eyeWidth, eyeHeight, 180, 360);
    arc(rightEyeX, eyeY, eyeWidth, eyeHeight - 5, 180, 360);


    // Eyelash
    stroke(4, 48, 51);
    strokeWeight(2);
    arc(leftEyeX - 12, eyeY - 15, eyeWidth - 8, eyeWidth / 2 - 10, 90, 180);
    arc(rightEyeX + 12, eyeY - 15, eyeWidth - 8, eyeWidth / 2 - 10, 0, 90);

    arc(leftEyeX - 7, eyeY - 25, eyeWidth - 20, eyeWidth / 2 - 5, 90, 180);
    arc(rightEyeX + 7, eyeY - 25, eyeWidth - 20, eyeWidth / 2 - 5, 0, 90);

    // Eyelids (Color 2)
    strokeWeight(3);
    stroke(31, 121, 128);
    arc(leftEyeX, eyeY, eyeWidth, eyeHeight - 3, 180, 360);
    arc(rightEyeX, eyeY, eyeWidth, eyeHeight - 3, 180, 360);
  }

  /* NOSE */
  strokeWeight(3);
  stroke(217, 170, 158);
  arc(190, 203, 15, 20, 0, 80);

  strokeWeight(3);
  line(197, 203, 192, 212);

  stroke(255, 239, 224);
  strokeWeight(2.5);
  arc(190.5, 200, 14, 25, 0, 80);
  // x1, y1, x2, y2

  strokeWeight(0);

  if (mouseIsPressed) {
    // Mouth 
    noFill();
    stroke(245, 137, 118);
    strokeWeight(3);
    arc(200, 243, 50, 20, 0, 180);
    strokeWeight(0);
    fill(255, 239, 224);
    ellipse(200, 240, 60, 20);
  }
  else {
    /* MOUTH */
    // Mouth (Whole)  
    fill(245, 137, 118);
    arc(200, 240, 50, 50, 0, 180);
    arc(200, 240, 50, 8, 180, 360);

    // Teeth
    fill('white');
    arc(200, 240, 40, 10, 0, 180);
    arc(200, 240, 40, 7, 180, 360);

    // Tongue
    fill(255, 181, 168);
    arc(200, 255, 37, 6, 180, 360);
    arc(200, 255, 37, 15, 0, 180);
    arc(200, 257, 33, 15.5, 0, 180);
  }
  
  strokeWeight(0);
  
  /* HAIR */
  // Side hair
  fill(23, 199, 230);
  rect(110, 250, 20, 200);
  rect(canvasX - 110, 250, 20, 200);
  triangle(300, 350, 280, 350, 280, 360);
  triangle(canvasX - 300, 350, canvasX - 280, 350, canvasX - 280, 360);

  // Bang
  fill(23, 199, 230);
  ellipse(200, 160, 100, 10);
  rect(200, 120, 100, 80);
  triangle(140, 160, 110, 160, 155, 80);
  triangle(canvasX - 140, 160, canvasX - 110, 160, canvasX - 155, 80);

  // Top Head Line
  strokeWeight(20);
  stroke(23, 199, 230);
  noFill();
  arc(200, 165, 180, 180, 180, 360);
  arc(200, 155, 180, 180, 180, 360);

  // Shading
  strokeWeight(0);
  fill(27, 169, 209);
  triangle(100, 170, 100, 350, 111, 355);
  triangle(canvasX - 100, 170, canvasX - 100, 350, canvasX - 111, 355);
  triangle(140, 160, 130, 160, 149, 108);
  triangle(canvasX - 140, 160, canvasX - 130, 160, canvasX - 149, 108);

  // Lighting
  strokeWeight(3);
  stroke(57, 219, 247);
  line(120, 160, 120, 358);
  line(canvasX - 120, 160, canvasX - 120, 358);

  strokeWeight(0);
  fill(57, 219, 247);
  rect(200, 120, 90, 35);
  ellipse(200, 135.5, 90, 30);
  
  fill(23, 199, 230);
  ellipse(200, 102.5, 90, 10);

  fill(57, 219, 247);
  quad(135, 90, 147, 98, 128, 138, 112, 120);
  quad(canvasX - 135, 90, canvasX - 147, 98, canvasX - 128, 138, canvasX - 112, 120);

  fill(23, 199, 230);
  arc(200, 90, 140, 40, 0, 180);


  /* TEXT */
  textSize(20);
  fill(12, 145, 168);
  text("Click to see me blink!", 20, 30);
  textSize(16);
  text("\"I sacrifice my sleep for drawing.\" - ???", 110, 386);
}

