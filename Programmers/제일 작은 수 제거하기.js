function solution(arr) {
    let minValue = Math.min(...arr)
    var answer = arr.filter(element => element !== minValue);
    if(answer.length === 0){
        answer = [-1]
    }
    return answer;
}