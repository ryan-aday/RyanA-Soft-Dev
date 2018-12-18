function fact(n) {
    if(n == 0) {
        return 1
    }
    return n * fact(n - 1);
}

function fibonacci(n) {
    if(n == 0) {
        return 0
    }
    return n + fibonacci(n - 1);
}

function gcd(a, b){
    if ( ! b) {
        return a;
    }
    return gcd(b, a % b);
}

var students=["James", "Audrey", "TD", "DANK MEMER"]

function randomStudent(){
    return students[Math.floor(Math.random()*students.length)]; 
}