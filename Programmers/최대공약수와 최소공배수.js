function gcd(a,b){
    if(b === 0){
        return a;
    }
    else {
        return gcd(b, a%b);
    }
}

function solution(n, m) {
    let gcdNum = gcd(n,m)
    return [gcdNum, n*m/gcdNum]
}