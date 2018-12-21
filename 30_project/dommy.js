/* Team AK47 
Ryan Aday
SoftDev1 pd<p>
K30 -- Testing JS
2018-12-21 
*/

/* Header Change */
var x = document.getElementById("thelist");
var y = x.getElementsByTagName("li");
var header = document.getElementById("h");

for (i=0; i<y.length; i++){
	let replacement=y[i];
	replacement.addEventListener('mouseover', function(e){
		header.innerHTML=replacement.innerHTML;
	});
}	

/*Remove Main List Fxns */
for (i=0; i<y.length; i++){
	let replacement=y[i];
	console.log(y[i]);
	replacement.addEventListener('click', function(e){
		replacement.remove();
	});
}

/*Adding Elements to Main List*/

var list = document.getElementById("thelist");
var counter=8;

var b=document.getElementById("b");
b.addEventListener('click', function(e){
	var li= document.createElement("li");
	li.appendChild(document.createTextNode("item " + counter));
	counter++;
	list.appendChild(li);

});


/*Making Fibonacci List Elements*/
var fibonacci = (n) => {
    if(n < 2) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
};

var fcounter=0;

var fb=document.getElementById("fb");
var fiblist=document.getElementById("fiblist");

fb.addEventListener('click', function(e){
var li= document.createElement("li");
	li.appendChild(document.createTextNode(fibonacci(fcounter)));
	fcounter++;
	fiblist.appendChild(li);	
	let replacement=li;
	replacement.addEventListener('click', function(e){
		replacement.remove();
	});
	replacement.addEventListener('mouseover', function(e){
		header.innerHTML=replacement.innerHTML;
	});
});

