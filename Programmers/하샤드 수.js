function solution(num) {
    var answer = true;
    let sum_num_arr = String(num).split("").reduce((prev, curr) => Number(prev) + Number(curr));
    if(num % sum_num_arr !== 0) {
        answer = false;
    }
    return answer;
}