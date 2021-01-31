function solution(a, b) {
    var answer = 0;
    let start = (a <= b) ? a : b
    let end = (a <= b) ? b : a
    for(let i =start; i<=end; i++){
        answer += i
    }

    return answer;
}