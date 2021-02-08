function solution(arr1, arr2) {
    var answer = arr1.map((item, idx, array) => {
        return arr1[idx].map((item2, idx2, array) => { return item2 + arr2[idx][idx2] })
    })
    return answer;
}

return arr1.map((a, i) => a.map((b,j) => b + arr2[i][j]))