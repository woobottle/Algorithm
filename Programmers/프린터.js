function solution(priorities, location) {
    let sortedPriorities = priorities.slice()
    sortedPriorities.sort().reverse()
    let count = 0
    priorities = priorities.map((value,index) => [value,index])

    while(true){
        let curr = priorities.shift()
        if(curr[0] == sortedPriorities[0]){
            count += 1   
            sortedPriorities.shift()
            if(curr[1] == location) {
                break
            }
        }
        else {
            priorities.push(curr)
        }
    }   
    return count;
}