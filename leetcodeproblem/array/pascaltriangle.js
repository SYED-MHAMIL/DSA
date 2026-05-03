/**
 * @param {number} numRows
 * @return {number[][]}
 */
// var generate = function(numRows) {
//     // in every time 
//         // loop start form 1
//         let res = []
//      

//         [1]
//        [1,1]
//       [1,2,1]
//      [1,3,3,1]
//     [1,4,6,4,1]
//   [1,5,10,10,5,1]
 
// we are repeatin the formula of getting nCr for each col 



//         for(let i=0; i<numRows; i++){
             
//              let arr= []
//              if (i == 0) {
//                  res.push([1])
//                  continue  
//              }
//              arr.push(1)
//              for(let j=1; j<i; j++){            
//                 arr.push(res[i-1][j-1]  +  res[i-1][j])
//             }
//              arr.push(1)
             
//              res.push(arr)
//         }
//         return res
// };

// console.log(generate(5));




// interviewr ask  about tell me about each row sum
// // second problem to solve
// // needed trinagle sum 
// function pascalTriangleachrowsum(nth) {
//      let arr= [] 
//     for (let index = 0; index < nth; index++) {
//         const element = 2**index
//         arr.push(element)
//     }
//     return arr
// }

// console.log(pascalTriangleachrowsum(3));



// nCr formula(where you need to combination)
// nCr formula : 
//    nCR  =n! / r! (n-r)!
//
// for example : 
    //  7C2 =  7x6(5x4x3x2x1)/(2x1)(5x4x3x2x1)
    //  res =7/1 => 7
    //  res= res * (6)/2 => 21  

// 
//  
// 
// 
// 
//  n=row , r=col
function nCr(n,r) {
      let res = 1
      n=n-1
      r=r-1 
    //   3C2 = 3x2x1 /2(1)
    for (let  i = 0;  i < r;  i++) {
         res = res * (n-i)
         res=  res /  (i+1)
    }
    return res 

}

    console.log("ncr",nCr(4,3));
    




    // PRINT ANY ROW OF PAASCAL TRI-ANGLE 
    //  PROBLEM
    // 
//         [1]
//        [1,1]
//       [1,2,1]
//      [1,3,3,1]
//     [1,4,6,4,1]
//   [1,5,10,10,5,1]
 
// we are repeatin the formula of getting nCr for each col

//   function PrintRow(N) {
//     for (let index = 1; index <= N; index++){
//           const row = N
//           const col = index
//           console.log(nCr(row,col));
//     }
//     // time complexity of that  O(N * r)
//   }

//   console.log(PrintRow(4));
  

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// EFFIVIENT WAY  CAN I REDUCE THE REPEATING WORK


//   function PrintRowEfficient(N) {
//     let ans = 1
//     console.log(ans)
    
//     for (let index = 1; index < N; index++){
//         ans= ans *(N-index)/index
//         console.log(ans)
//     }
//     // time complexity of that  O(N * r)
//   }

//   console.log(PrintRowEfficient(4));




function PrintPascalTriangle(N) {
     function PrintRowEfficient(N) {
    
    let arr=  []
    let ans = 1
    arr.push(ans)
    
    for (let index = 1; index < N; index++){
        ans= ans *(N-index)/index
        arr.push(ans)
    }
    return arr
    // time complexity of that  O(N * r)
  }
     let arr= []

    // print eact row 
    
    for (let  i =1;  i <= N;  i++) {
         arr.push(PrintRowEfficient(i))  
    }
    return  arr



//    time  completi = o(n)
//    and space compexity  =  O(1)
}

// console.log(PrintPascalTriangle(5));



// var generate = function(numRows) {
//     let res = [ ]
//     for(let i=0; i<numRows; i++){
//         let arr= new Array(i+1).fill(1);
//         for(let j=1; j<arr.length -1; j++){
//             if(i>j){
//                 console.log(res);
                
//                 arr[j] = res[i-1][j-1] + res[i-1][j] 
//             }
//         }
//         arr.push(arr)
//     }
//     return res
// };

// console.log(generate(5));


var generate = function(numRows) {
    let res = [] 
    for(let i=0; i<numRows; i++){
        let arr= new Array(i+1).fill(1)
        for(let j=1;j <arr.length -1; j++){
               if(i > j){
                  arr[j]= res[i-1][j-1]  + res[i-1][j+1]
               }
        }
        res.push(arr)
    }
    return res
};