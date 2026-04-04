// 1 0 1 0
// 1 1 1 1
// 1 1 1 1






function  maximalRectangle(matrix) {
        if (!matrix.length) return 0;
        let histogramMatrix = []
        let  heights;
        heights=  new Array(matrix[0].length).fill(0) 
        for (let i = 0; i < matrix.length; i++) {
            const element = matrix[i];
            
            
            for (let j = 0; j < element.length; j++) {
                let element1 = element[j];
                
                
                if (element1 === '1') {
                    heights[j] += 1 

                } else {
                    heights[j] = 0 
                }
                
            }
            histogramMatrix.push([...heights])
            
        }
        

        // apply largest hsitogram in restangular 
        
        //  previos smaller 
        function  prevsmallele(array) {
            let stack = []
            let result = new Array(array.length).fill(-1)
            for (let index = 0; index < array.length; index++) {
                const element = array[index];
                while (stack.length  > 0 && array[stack[stack.length -1 ]] >= element) {
                    stack.pop()
                }
                if (stack.length  > 0) {
                    result[index]  = stack[stack.length -1]
                }


                stack.push(index)
                
            }
            return result
        }



        //  next smaller 
        function  nextsmallele(array) {
            let stack = []
            let result = new Array(array.length).fill(array.length)
            for (let index = 0; index < array.length; index++) {
                const element = array[index];
                while (stack.length  > 0 && array[stack[stack.length -1 ] ] >= element) {
                    result[stack[stack.length -1]]  =  index 
                    stack.pop()
                }
        
                stack.push(index)        
            }
            return result
        }


        
        let max = 0;
        
        for (let index = 0; index < histogramMatrix.length; index++) {
            let element =  histogramMatrix[index]
            
                    let pse =  prevsmallele(element)
                    let nse =  nextsmallele(element)
            
            for (let index = 0; index < element.length; index++) {
                let restangle = element[index]  * (nse[index] -  pse[index] - 1)
                
                max = Math.max(restangle,max)      
                
            }

            
        }
        return max

        
    }

console.log(maximalRectangle(
    [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]));



    //  [3,  2, 3, 2]
    // pse: [-1,-1, 1, 1]
// nse: [1  ,4, 3, 4]


// 1-(-1)-1 * 3 =  3
// 4-(-1)-1 * 2 =  20 



// [1,0,1,0,0]
// [2,0,2,1,1]
// [3,1,3,2,2]
// [4,0,0,3,0]


// 
