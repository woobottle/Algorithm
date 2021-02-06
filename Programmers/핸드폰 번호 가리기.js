function solution(phone_number) {
    let phone_number_split = phone_number.split("");
    for(let i = 0, length = phone_number_split.length; i < length - 4; i++){
        phone_number_split[i] = "*"
    }
    return phone_number_split.join("")
}

function solution(phone_number) {
    return phone_number.replace(/\d(?=\d{4})/g, "*")
}