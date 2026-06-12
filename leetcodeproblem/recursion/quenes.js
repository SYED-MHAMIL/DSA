// /**
//  * @param {number} n
//  * @return {string[][]}
//  */
// var solveNQueens = function(n) {
//     let chesboard = Array.from({length: n},()=> new Array(n).fill('.'));
//     let res = []
//     // what is constraints : 
//     // quenes can be one in one column and one row
//     // quenes canot attack  to each other ( you can safe it if one quene is not in diagonal,same row and same column)
    

//     //[['Q','.','.','.']
//     // ['.','.','.','.']
//     // ['.','Q','.','.']
//     // ['.','.','.','.']]

//       // isValid to place
//           function isValid(chesboard,row,col) {
//             // row
//             for (let i = 0; i < col; i++) {
//                if (chesboard[row][i]  == 'Q') {
//                  return  false
//                }
                
//             } 

//             // upper-left digonal
//             for(let r=row,c=col; r>=0 && c>=0; r--,c--){
//                    if(chesboard[r][c] == 'Q') return false
//             }

//              // lower-left digonal
//             for(let r=row,c=col; r<n && c>=0; r++,c--){
//                    if(chesboard[r][c] == 'Q') return false
//             }
//             return true

//           }


//     function board(chesboard,col,res) {
//          if (col == n) {
//              let temp = chesboard.map((row)=> row.join(""));
//              res.push(temp);
            
//          }
    
//           for (let row = 0; row < n; row++) {
//                 if (isValid(chesboard,row,col)) {
//                     console.log("is claide ");
                    
//                      chesboard[row][col] = 'Q'
//                      board(chesboard,col+1,res)
//                      chesboard[row][col] = '.'
//                 }  
//           }  
  
//     }
//      board(chesboard,0,res)
//     return  res
// };


// console.log(solveNQueens(4));








//  placing quen in rows


// /**
//  * @param {number} n
//  * @return {string[][]}
//  */
// var solveNQueens = function(n) {
//     let chesboard = Array.from({length: n},()=> new Array(n).fill('.'));
//     let res = []
//     // what is constraints : 
//     // quenes can be one in one column and one row
//     // quenes canot attack  to each other ( you can safe it if one quene is not in diagonal,same row and same column)
    

//     //[['Q','.','.','.']
//     // ['.','.','.','.']
//     // ['.','Q','.','.']
//     // ['.','.','.','.']]

//       // isValid to place
//         function isValid(chesboard,row,col) {
//             // column
//             for (let i = 0; i < row; i++) {
//                if (chesboard[i][col]  == 'Q') {
//                  return  false
//                }
                
//             } 

//             // upper-left digonal
//             for(let r=row,c=col; r>=0 && c>=0; r--,c--){
//                    if(chesboard[r][c] == 'Q') return false
//             }

//              // lower-left digonal
//             for(let r=row,c=col; r<n && c>=0; r++,c--){
//                    if(chesboard[r][c] == 'Q') return false
//             }
//             return true

//           }


//     function board(chesboard,row,res) {
//          if (row == n) {
//              let temp = chesboard.map((row)=> row.join(""));
//              res.push(temp);
            
//          }
    
//           for (let col = 0; col < n; col++) {
//                 if (isValid(chesboard,row,col)) {
//                     console.log("is claide ");
                    
//                      chesboard[row][col] = 'Q'
//                      board(chesboard,row+1,res)
//                      chesboard[row][col] = '.'
//                 }  
//           }  
  
//     }
//      board(chesboard,0,res)
//     return  res
// };


// console.log(solveNQueens(4));
