// /**
//  * @param {number[][]} matrix
//  * @param {number} target
//  * @return {boolean}
//  */
// var searchMatrix = function(matrix, target) {
//    let m =  matrix.length
//    let n =  matrix[0].length   
   
//    let left =  0 
//    let right =  (n * m ) -1  

//    while(left <= right){
//     // 
//      let mid = Math.floor((left + right) /2) 
//      let row = Math.floor(mid / n)  
//      let col = mid % n
     
//      if(matrix[row][col]  == target){
//                return true
//      }else if (matrix[row][col] < target) {
//             left= mid+ 1 
//      }else{
//         right= mid- 1
//      }

//    }
//   return  false
// };

// console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3));






/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let m= matrix[0].length -1 ; 
    let n = matrix.length -1 ; 
    let row = 0
    while (row<=n  || m>=0) {
         if(matrix[row][m] == target){
             return true
         }else if(matrix[n][m] > target){
               m--
         }else{
              row++
         }
    }
    return false

   
};

console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3));
