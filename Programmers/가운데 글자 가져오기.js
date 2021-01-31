function solution(s) {
    var answer = '';
    let str = s.split("");
    let str_len = s.length;

    if(str_len % 2 === 0){
        answer = str.splice(str_len/2-1, 2).join("")
    }
    else {
        answer = s[~~(str_len/2)]
    }

    return answer;
}