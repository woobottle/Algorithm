function solution(s) {
    let sArray = s.split(" ");
    sArray.forEach((element, index, array) => {
        let elArray = element.split("");
        elArray.forEach((el, el_ind, el_arr) => {
            // 대문자로
            if(el_ind % 2 === 0){
                if(el.charCodeAt(0) >= 97){
                    elArray[el_ind] = String.fromCharCode(el.charCodeAt(0) - 32);   
                }
            }
            // 소문자로
            else{
                if(el.charCodeAt(0) >= 65 && el.charCodeAt(0) <= 90){
                    elArray[el_ind] = String.fromCharCode(el.charCodeAt(0) + 32);       
                }
            }
        })
        sArray[index] = elArray.join("");
    })
    return sArray.join(" ");
}