function solution(arr, divisor) {
    let temp = arr.filter(element => element % divisor === 0).sort(function(a,b){
        return a - b;
    })
    if(temp.length === 0){
        temp.push(-1)
    }
    
    return temp;
}