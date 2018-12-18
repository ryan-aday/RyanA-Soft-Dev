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


