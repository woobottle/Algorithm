// 2월이 29일 까지 있음

function solution(a, b) {
    var answer = '';
    var day_count = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    var day_name = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    // 1/1 은 금요일
    let total_day = b
    for(let i = 0; i < a-1; i++){
        total_day += day_count[i]
    }
    answer = day_name[(total_day-1)%7]
    return answer;
}


function getDayName(a,b){
    var arr = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    var date = new Date(`2016-${a}-${b}`);
    var day = date.getDay()
    return arr[day];
}