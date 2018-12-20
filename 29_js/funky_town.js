/* Team AK47 

*/

var fact = (n) => {
    if(n == 0) {
        return 1
    }
    return n * fact(n - 1);
}

var fibonacci = (n) => {
    if(n < 2) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

var gcd = (a, b) =>{
    if (!b) {
        return a;
    }
    return gcd(b, a % b);
}

var students=["James", "Audrey", "TD", "DANK MEMER"]

var randomStudent = () =>{
    return students[Math.floor(Math.random()*students.length)]; 
}

var factButt=document.getElementById("fact")
factButt.addEventListener("click", fa);


var fibButt=document.getElementById("fib")
fibButt.addEventListener("click", fi);


var gButt=document.getElementById("g")
gButt.addEventListener("click", gc);

var randButt=document.getElementById("rand")
randButt.addEventListener("click", ra);

function fa(){
	console.log(fact(20));
	alert(fact(20))
}

function fi(){
	console.log(fibonacci(20));
	alert(fibonacci(20));
}

function gc(){
	console.log(gcd(20, 10));
	alert(gcd(20,10));
}

function ra(){
	console.log(randomStudent());
	alert(randomStudent());
}

    /* console.log() */
/* document.getElementById(<ID>) 
	document.getElementsByTagName

	.addEventListener(<EVENT>, <FUNCTION>)


var hh = document.getElementById("b");
hh.addEventListener('click', fxnName)
*/