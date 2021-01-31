function solution(s) {
    var answer = true;
    if(s.length === 4 || s.length === 6){
        for(const el of s.split("")){
            if(isNaN(el/1)){
                answer = false;
                break;
            }
            else{
                continue;
            }
        }
    }
    else {
        answer = false;
    }                      
    return answer;
}

