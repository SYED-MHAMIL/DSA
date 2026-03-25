function prevSmallernumber(array) {
       let stack = []
       let result =  new Array(array.length).fill(-1)
       for (let index = 0; index < array.length; index++) {
        const element = array[index];
        
        while (stack.length > 0  && stack[stack.length -1]  >= element) {
                 stack.pop()
        }  
        
        if (stack.length > 0  && stack[stack.length -1]  <  element) {
            result[index] = stack[stack.length -1]        
               
        }
        stack.push(element)

       }
       return result
}







function nextSmallernumber(array) {
    let stack = []
    let result =  new Array(array.length).fill(-1)
    for (let index = array.length-1; index >= 0 ; index--) {
        const element = array[index];
        
        while (stack.length > 0  && stack[stack.length -1]  >= element) {
            stack.pop()

            
        }  
        
        if (stack.length > 0  && stack[stack.length -1]  <  element) {
            result[index] = stack[stack.length -1]        
            
        }
        stack.push(element)
        
    }
    return result
}
let n= nextSmallernumber([3,1,2,4])
let p =  prevSmallernumber([3,1,2,4])
console.log(n)
console.log(p);
console.log(((n[0] - 0) *(0- p[0])) * 3 );
