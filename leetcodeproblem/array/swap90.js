// Naive bse brute forse 

 var rotate = function(matrix) {
    let n = matrix.length
    let res =[]
    for (let i = 0; i < n; i++) {
     let arr =  []
     for(let j = i; j < n; j++){
        arr.push(matrix[i][j])
     }  
     res.push(arr)
        
    }
    return  matrix
 }









// var rotate = function(matrix) {
//     // matrix[i][j] = matrix[j][i]
//     let n = matrix.length
//     let m = matrix[0].length
//     for(let i=0;  i<n; i++){
//       for(let j=0; j<m; j++){
//                 //  [ matrix[i][j],matrix[j][i] ]=[ matrix[j][i],matrix[i][j] ]
//                                  [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
                                 
                                 
//             //   row[0][1],col[1][0]
//             //   row[0][2]=3,col[2][0]
//       };
//       console.log(matrix);
      
//     }

//     for(let i=0;  i<n; i++){
//          matrix[i].reverse()
//     //   for(let j=0; i<m; j++){
//     //              [matrix[i][j],matrix[j][i]]=[matrix[j][i],matrix[i][j]]

//     //   };
//     }
//     // return matrix
// };

console.log(rotate([[1,2,3],[4,5,6],[7,8,9]]));
