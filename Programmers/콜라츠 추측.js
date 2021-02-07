function solution(num) {
    var count = 0;
    while(count < 500) {
        if(num === 1){
            break;
        }
        if(num % 2 === 0){
            num /= 2;
        } else {
            num = (num * 3) + 1;
        }
        count++;
    }
    if(count === 500) {
        count = -1;
    }
    return count;
}