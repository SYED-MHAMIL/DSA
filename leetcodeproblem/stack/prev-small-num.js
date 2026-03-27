// function prevSmallernumber(array) {
//     // 3,1,2,4
//        let stack = []
//        let result =  new Array(array.length).fill(-1)
//        for (let index = 0; index < array.length; index++) {
//         const element = array[index];
        
//         while (stack.length > 0  && array[stack[stack.length -1]]  > element) {
//                  stack.pop()
//         }  
        
//         if (stack.length > 0  && array[stack[stack.length -1]]  <=  element) {
//             result[index] = array[stack[stack.length -1]]         
               
//         }
//         stack.push(index)
    
//        }
//        return result
// }


// “Remove all bigger elements on the left, so the top of the stack becomes the nearest smaller.”
 function prevSmallernumber(array) {
    let stack = [] 
    // 3,1,2,4
    let result = new Array(array.length).fill(-1)
    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        while (stack.length > 0 &&  array[stack[stack.length -1]] > element) {
                stack.pop()
        }
        if(stack.length>0 && array[stack[stack.length -1]] < element){
               result[index] =  array[stack[stack.length -1]]
        }
         
               
          stack.push(index)

    }
    return result
 }






// function nextSmallernumber(array) {
//     let stack = []
//     let result =new Array(array.length).fill(4)
//     for (let index = 0;  index < array.length ; index++) {
//         const element = array[index];
        
//         while (stack.length > 0  && array[stack[stack.length -1]]  > element) {
//             result[stack[stack.length -1]] = element        
//             stack.pop()       
//         }  
        
//         stack.push(index)
        
//     }
//     return result
// }


// every one waiting next smaller element so every time when i will have smaller ones i will give them instantly and remove to the waiting 

// “Keep a stack of unresolved elements, and whenever a smaller number appears, resolve all bigger ones waiting before it.”


function nextSmallernumber(array) {
    // arr = [1,4, 5, 2, 10, 8]
    let stack= []
    let result =new Array(array.length).fill(4)

    for (let index = 0; index < array.length; index++) {
        const element = array[index];

         while (stack.length > 0 && array[stack[stack.length -1]] > element) {
                   result[stack[stack.length -1]] =    element
                   stack.pop() 
         }


         stack.push(index)
        
    }
return  result
}


let array =  [1,1]
let n= nextSmallernumber(array)
let p =  prevSmallernumber(array)
console.log("nse ",n,`for this [${array}]`)
console.log("pse",p,`for this  [${array}]`);
// console.log(((n[1] - 1) *(1- p[1])) * 1);
