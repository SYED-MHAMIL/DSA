// 



/**
 * @param {number[]} heights
 * @return {number}
 */
      function previosSmallerElement(array){
            let stack = []
            let res =  new Array(array.length).fill(-1);
            for(let i=0; i < array.length; i++){
               //    
               let element = array[i]
               while(stack.length > 0 && array[stack[stack.length - 1]] >= element)
               { 
                    
                    stack.pop()
               }
               if(stack.length  > 0 ){
                    res[i] = stack[stack.length -1]
               }

                
               stack.push(i)
            }
            return res
      }
      
      function nextSmallerElement(array){
            let stack = []
            let res =  new Array(array.length).fill(array.length);
            
            
            for(let i=0; i< array.length; i++){
               //    
               let element = array[i]
               while(stack.length > 0 && array[stack[stack.length - 1]] >= element)
               {
                    res[stack[stack.length - 1]] = i
                    stack.pop()
               }
               stack.push(i)
            }
            return res
      }
var largestRectangleArea = function(heights) {
      let pse = previosSmallerElement(heights)
      let nse = nextSmallerElement(heights)
      console.log('pse',pse);
      console.log('nse',nse);
      
      let res= 0
      for(let i=0; i< heights.length; i++){
          let result = heights[i]*(nse[i] - pse[i] - 1) 
          res=Math.max(res,result)
      }
      return res

};  


console.log(largestRectangleArea([2,1,5,6,2,3]));
