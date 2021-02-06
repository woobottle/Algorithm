function solution(n) {
    var answer = Math.sqrt(n) % 1 == 0 ? Math.sqrt(n) : -1
    if(answer !== -1){
        answer = Math.pow(answer+1,2)
    }
    return answer;
}