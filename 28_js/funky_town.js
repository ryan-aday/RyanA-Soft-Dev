/* Team AK47 

*/

var factorial = (n) => {
    if(n == 0) {
        return 1
    }
    return n * fact(n - 1);
}

var fibonnaci = (n) => {
    if(n == 0) {
        return 0
    }
    if(n == 1)
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