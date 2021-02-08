function solution(x, n) {
    return [...Array(n).keys()].map((a) => (a+1) * x)
}