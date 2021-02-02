function solution(n) {
    var answer = 0;
    for(let i = 1, end = ~~Math.sqrt(n); i<=end; i++){
        if(n%i === 0){
            answer += i
            if(i !== n/i){
             answer += (n/i)   
            }
        }
    }
    return answer;
}