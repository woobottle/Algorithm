function solution(s, n) {
    var answer = '';
    s.split("").forEach(element => {
        let charNum = element.charCodeAt(0);
        if(charNum >= 97 && charNum <= 122){
            charNum = ((charNum + n - 97) % 26) + 97
        }else if(charNum >= 65 && charNum <= 90){
            charNum = ((charNum + n - 65) % 26) + 65
        }
        answer += String.fromCharCode(charNum)
    })
    return answer;
}