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