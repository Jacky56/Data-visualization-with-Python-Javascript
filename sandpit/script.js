var data = [3, 7, 2, 9, 1, 11];
var sum = 0;
data.forEach(function(d){
	sum += d;
});

console.log('Sum = ' + sum);



var times2 = function(x){
	return x*2;
}

console.log(times2(3));