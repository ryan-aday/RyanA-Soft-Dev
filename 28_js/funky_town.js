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
    var t = b;
    b = a % b;
    a = t;
    return a;
}


