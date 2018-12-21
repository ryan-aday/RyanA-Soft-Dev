var thelist= document.getElementById("thelist");

var list0= document.getElementById("list0");
var list1= document.getElementById("list1");
var list2= document.getElementById("list2");
var list3= document.getElementById("list3");
var list4= document.getElementById("list4");
var list5= document.getElementById("list5");
var list6= document.getElementById("list6");
var list7= document.getElementById("list7");

var header = document.getElementById("h");
var mainListC=8;

/* Header Change */
  mainList = thelist.getElementsByTagName('li');
  console.log(mainList);


/*Remove Main List Fxns */
list0.addEventListener('click', function(e){
	list0.remove();
});

list1.addEventListener('click', function(e){
	list1.remove();
});

list2.addEventListener('click', function(e){
	list2.remove();
});

list3.addEventListener('click', function(e){
	list3.remove();
});

list4.addEventListener('click', function(e){
	list4.remove();
});

list5.addEventListener('click', function(e){
	list5.remove();
});

list6.addEventListener('click', function(e){
	list6.remove();
});

list7.addEventListener('click', function(e){
	list7.remove();
});


/*Adding Elements to Main List*/

var list = document.getElementById("thelist");


var counter=8;
var b=document.getElementById("b");

b.addEventListener('click', function(e){
	var li= document.createElement("li");
	li.setAttribute("id", "list8");
	li.appendChild(document.createTextNode("item New"));
	list.appendChild(li);	
});


/*Making Fibonacci List Elements*/
var fibonacci = (n) => {
    if(n < 2) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
};

var counter=0;

var fb=document.getElementById("fb");
var fiblist=document.getElementById("fiblist");

fb.addEventListener('click', function(e){
var li= document.createElement("li");
	li.appendChild(document.createTextNode(fibonacci(counter)));
	counter++;
	fiblist.appendChild(li);	
});

