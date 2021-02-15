// function solution(N, stages) {
//     let sta_len = stages.length
//     let check = new Array(N+1).fill(0)
//     let arr = new Array(N)
//     let ans = []
    
//     Array(N).fill(1).map((e, i) => arr[i] = [0, sta_len, 0, i+1])
//     stages.sort()
    
//     let standard = 0
//     stages.forEach((e,i) => {
//         if(e <= N){
//             standard += 1
//             arr[e-1][0] += 1
//             arr[e-1][1] = sta_len - standard
//         }
//         else{
//             arr[N-1][1] = sta_len - standard
//         }
//     })
    
//     arr.forEach((e,i) => {
//         arr[i][2] = arr[i][0] / (arr[i][0] + arr[i][1])
//     })
    
//     arr.sort(function(a,b) {
//         if(b[2] > a[2]){
//             return 1;
//         }
//         else if(b[2] < a[2]){
//             return -1;
//         }
//         else{
//            return a[3] - b[3]
//         }
//     })
    
//     arr.forEach((e,i) => ans.push(e[3]))
//     console.log(arr)
//     return ans;
// }
function solution(N, stages) {
    var answer = [];
    let temp = Array(N).fill(0);
    let temp2 = Array(N)
    Array(N).fill(0).map((e,i) => temp2[i] = [0, i])
    
    stages.forEach((e) => {
        if(e <= N) {
            temp[e-1] += 1
        }
    })
    
    let standard = stages.length
    temp.forEach((e, i) => {
        temp2[i][0] = isNaN(e / standard) ? 0 : e / standard
        standard -= e
    })
    
    temp2.sort(function(a,b) {
        if(a[0] > b[0]) {
            return -1
        }
        else if(a[0] < b[0]) {
            return 1
        }
        else{
            return a[1] - b[1]
        }
    })
    
    return temp2.map(e => { return e[1] + 1 }) 
}