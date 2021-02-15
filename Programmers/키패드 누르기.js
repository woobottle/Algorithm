function address(number){
    if(number === 0){
        number = 11
    }
    if(number%3 == 0){
     return [(~~(number/3)-1), (number%3 === 0 ? 3 : number%3)]
    }
    else{
     return [(~~(number/3)), (number%3 === 0 ? 3 : number%3)]
    }
}

function solution(numbers, hand) {
    var answer = '';
    let c_l = 10
    let c_r = 12
    let p_p = [0, 0], p_l = [3, 1] , p_r = [3, 3], d_l = 0, d_r = 0
    
    numbers.forEach((e) => {
        if([1,4,7].includes(e)){
            answer += "L"
            c_l = e
        }else if([3,6,9].includes(e)){
            answer += "R"           
            c_r = e
        }else {
            p_p = address(e); p_l = address(c_l); p_r = address(c_r)
            d_l = Math.abs(p_p[0] - p_l[0]) + Math.abs(p_p[1] - p_l[1])
            d_r = Math.abs(p_p[0] - p_r[0]) + Math.abs(p_p[1] - p_r[1])
            
            if(d_l > d_r) {
                answer += "R"
                c_r = e
            }else if(d_l < d_r){
                answer += "L"
                c_l = e
            }else{
                if(hand === "left"){
                  answer += "L"
                  c_l = e
                }else{
                  answer += "R"
                  c_r = e
                }
            }
        }
    })
    return answer;
}