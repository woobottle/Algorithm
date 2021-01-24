https://programmers.co.kr/learn/courses/30/lessons/64061

인형을 뽑고 바구니에 넣을때 이전과 같은게 있으면 그 인형을 터뜨림
터진 인형의 개수를 구하는 문제

function solution(board, moves) {
    let answer = 0;
    let baskets = [];
    let boardSize = board.length
    moves.forEach(element => {
        for(let i = 0; i < boardSize; i++){
            if(board[i][element-1] !== 0){
                if(baskets[baskets.length - 1] == board[i][element-1]){
                  answer += 2
                  baskets.pop()
                }else{
                  baskets.push(board[i][element-1])
                }
                board[i][element-1] = 0
                break
            }
        }
    });

    return answer;
}