function solution(new_id) {
    var answer = new_id;
    answer = answer.toLowerCase()
        .replace(/[^a-z0-9\-\_\.]/g, "")
        .replace(/\.{2,}/g, ".")
        .replace(/^\.|\.$/g, "")
    if(answer.length == 0){
        answer = "a"
    }
    answer = answer.substring(0,15)     
        .replace(/\.$/, "")
    if(answer.length <= 2){
        let last_word = answer.charAt(answer.length - 1)
        Array(3-answer.length).fill(1).map(()=> {
            answer += last_word
        })
    }
    
    return answer;
}

function solution(new_id) {
    const answer = new_id
        .toLowerCase() // 1
        .replace(/[^\w-_.]/g, '') // 2
        .replace(/\.+/g, '.') // 3
        .replace(/^\.|\.$/g, '') // 4
        .replace(/^$/, 'a') // 5
        .slice(0, 15).replace(/\.$/, ''); // 6
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}
