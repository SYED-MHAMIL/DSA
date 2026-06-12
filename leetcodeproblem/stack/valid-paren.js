/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    let open  = {
        ")" :"(",
         "}" : "{",
         "]": "["
    } 
    for(c of s){
        if(open[c]){
            
            if(open[c] == stack[stack.length -1]){
                stack.pop()      
            }else{
                return false
            }
        }else{
            stack.push(c)
        }

    }
    return stack.length == 0  
};


console.log(isValid("()[]{}"

));
