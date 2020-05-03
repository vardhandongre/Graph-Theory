var cities = [];
var totalCities = 5;

var order = [];

var recordDistance;
var bestPath;
var totalPermutations;
var count = 0;


function setup() {
	createCanvas(500, 600);
	for (var i=0; i<totalCities; i++){
		var v = createVector(random(width),random(height/2));
		cities[i] = v;
		order[i] = i;


	}

	var d = Citydistance(cities, order);
	recordDistance = d;
	bestPath = order.slice();

	totalPermutations = factorial(totalCities);
	console.log(totalPermutations);

}

function draw() {
	background(0);
	//frameRate(5);
	fill(255);
	for (var i=0; i<cities.length; i++){
		ellipse(cities[i].x, cities[i].y,8,8)
}



stroke(255, 0, 255);
strokeWeight(4);
noFill();
beginShape();
for (var i = 0; i < order.length; i++) {
	var n = bestPath[i]
	vertex(cities[n].x, cities[n].y);

}
endShape();

translate(0, height/2);
stroke(255);
strokeWeight(1);
noFill();
beginShape();
for (var i = 0; i < order.length; i++) {
	var n = order[i]
	vertex(cities[n].x, cities[n].y);

}
endShape();




var d = Citydistance(cities, order);
if (d < recordDistance) {
	recordDistance = d;
	bestPath = order.slice()
	console.log(recordDistance);
}

textSize(24);
// var s = "";
// for (var i=0; i<order.length; i++) {

// 	s += order[i];
// }

fill(255);
var percent = 100* (count/totalPermutations);
text(nf(percent, 0, 3) + "% completed", 20, height / 2 - 50);


nextOrder();

}

function swap(a, i, j){
	var temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}

function Citydistance(points, order){
	var sum = 0;
	for(var i =0; i < order.length-1; i++){
		var cityAIndex = order[i]
		var cityA = points[cityAIndex]
		var cityBIndex = order[i+1]
		var cityB = points[cityBIndex]
		var d = dist(cityA.x, cityA.y, cityB.x, cityB.y);
		sum += d;
	}
	return sum;

}



function factorial(n) {
	if (n == 1) {
		return 1;
	} else {
		return n*factorial(n-1);
	}
}







// This is the lexical order algorithm

function nextOrder() {

	count++;

	var largestI = -1;
	for (i=0; i<order.length-1;i++) {
		if (order[i] < order[i+1]) {
			largestI = i;
		}

	}

	if (largestI == -1) {
		noLoop();
		console.log("Finished");
	}

	var largestJ = -1;
	for (j = 0; j < order.length; j++) {
		if (order[largestI] < order[j]) {
			largestJ = j;
		}
	}

	swap(order, largestI, largestJ);

	var endArray = order.splice(largestI+1);

	endArray.reverse();
	order = order.concat(endArray);


}

	
