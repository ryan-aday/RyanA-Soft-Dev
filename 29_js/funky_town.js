/* Team AK47 
Ryan Aday
SoftDev1 pd<p>
K29 -- Testing JS
2018-12-20 
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


/*Adding EventListeners
You need to create a var that looks for a specific object in the html file
that carries a specific id.  You can then add a listener to the variable to
check for a type of input done to that object.  WARNING-- the second constraint
in the parens must be a function; hence, the code below.
*/

var factButt=document.getElementById("fact")
factButt.addEventListener("click", fa);


var fibButt=document.getElementById("fib")
fibButt.addEventListener("click", fi);


var gButt=document.getElementById("g")
gButt.addEventListener("click", gc);

var randButt=document.getElementById("rand")
randButt.addEventListener("click", ra);

/*Functions
Can call upon vars.  alert() shoots a textbox telling you the 
return of a function/string you place in the parens
*/

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
