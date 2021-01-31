function solution(seoul) {
    const index = seoul.findIndex((element, index, arr) => element === "Kim")
    return `김서방은 ${index}에 있다`
}