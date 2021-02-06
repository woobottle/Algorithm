function solution(n) {
    var answer = [] 
    String(n).split("").reverse().forEach(element => answer.push(Number(element)))
    return answer;
}