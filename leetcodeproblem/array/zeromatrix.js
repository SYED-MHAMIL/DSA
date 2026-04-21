// Input: matrix=[
// [1,1,1],
// [1,0,1],
// [1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]
// Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

// Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
// Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
// Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
 


// function zeroMatrix(array) {
//     //  rows
//       let n= array.length
      
//     // colums 
//       let m = array[0].length 
      
//       for (let i = 0; i <n; i++) {
//          for (let j = 0; j <  m; j++) {
//             const element = array[i][j];
//             if (element == 0) {
               
//                 // make all respective row zero 
//                  for (let col = 0; col < n; col++) {
//                     const element = array[col][j];
//                     if (element != 0) {
//                         array[col][j]= -1
//                     }                    
//                  }
                 
//                 //  make all colums zero
//                  for (let row = 0; row <  m; row++) {
//                     const element = array[i][row];
//                     if (element != 0) {
//                         array[i][row]= -1
//                     }
                    
//                  }


//             }
//          }
//       }

//     //   second part
//       for (let i = 0; i < n; i++) {
//         for (let j = 0; j < m; j++) {
//             const element = array[i][j];
//             if (element == -1) {
//                 array[i][j]=0
//             }
            
//         }
        
//       }
       
//       return array
// }

// console.log(zeroMatrix(matrix=[[1,1,1],[1,0,1],[1,1,1]]));







// function zeroMatrix(array) {
//     //  rows
      
//      let rows =  new Array(array.length).fill(false)
//     let columns = new Array(array.length).fill(false)

//       let n= array.length
      
//     // colums 
//       let m = array[0].length 
      
//       for (let i = 0; i <n; i++) {
//          for (let j = 0; j <  m; j++) {
//             const element = array[i][j];
//             if (element == 0) {
//                  rows[i] = true
//                  columns[j] = true
            
//             }
//          }
//       }

//     //   second part
//       for (let i = 0; i < n; i++) {
//         for (let j = 0; j < m; j++) {
//             // const element = array[i][j];
//             if (rows[i] || columns[j]) {
//                 array[i][j]=0
//             }
            
//         }
        
//       }
       
//       return array
// }

// console.log(zeroMatrix(matrix=[[1,1,1],[1,0,1],[1,1,1]]));





// function  zeroMatrix(array) {
//    let n = array.length
//    let m= array[0].length
   
//    let firstcolZero = false
//    let firstrowZero = false
   
// //   check zero in first row
//    for (let i = 0; i < n; i++) {
//     const element = array[i][0];
//      if (element  == 0) {
//          firstrowZero =true
//          break
//      }
//    }

// //   check zero in first column
//    for (let i = 0; i < m; i++) {
//     const element = array[0][i];
//      if (element  == 0) {
//          firstcolZero =true
//          break
//      }
//    }


// // first  row/colums as an marker
// for (let i = 1; i < n; i++) {
//       for (let j = 1; j < m; j++) {
//         const element = array[i][j];
//         if (element  == 0) {
            
//               array[0][j] =0
//               array[i][0] =0
//             }
        
//       }
//    }

// // based on marker make cells to zero 

// for (let i = 1; i < n; i++) {
//       for (let j = 1; j < m; j++) {
//         // if cell col OR cell row was zero 
//           if (array[0][j] == 0 || array[i][0] == 0) {
              
//             array[i][j] = 0 
            
//             }
        
//       }
//    }

// // if firstrowZero 
// if (firstrowZero) {
//      for (let i = 0; i < n; i++) {
//         array[i][0] = 0
        
        
//      }
// }

// if (firstcolZero) {
//      for (let i = 0; i < m; i++) {
//         array[0][i] = 0
        
        
//      }
// }


// return array

// }

// console.log(zeroMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]));
