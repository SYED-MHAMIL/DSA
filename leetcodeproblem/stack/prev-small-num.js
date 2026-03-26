function prevSmallernumber(array) {
    // 3,1,2,4
       let stack = []
       let result =  new Array(array.length).fill(-1)
       for (let index = 0; index < array.length; index++) {
        const element = array[index];
        
        while (stack.length > 0  && array[stack[stack.length -1]]  >= element) {
                 stack.pop()
        }  
        
        if (stack.length > 0  && array[stack[stack.length -1]]  <  element) {
            result[index] = array[stack[stack.length -1]]         
               
        }
        stack.push(index)

       }
       return result
}







function nextSmallernumber(array) {
    let stack = []
    let result =new Array(array.length).fill(4)
    for (let index = 0;  index < array.length ; index++) {
        const element = array[index];
        
        while (stack.length > 0  && array[stack[stack.length -1]]  > element) {
            result[stack[stack.length -1]] = element        
            stack.pop()       
        }  
        
        stack.push(index)
        
    }
    return result
}
let n= nextSmallernumber([3,1,2,4])
let p =  prevSmallernumber([3,1,2,4])
console.log(n)
console.log(p);
console.log(((n[1] - 1) *(1- p[1])) * 1);
