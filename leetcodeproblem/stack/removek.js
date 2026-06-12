/**
z * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {

      let stack = []
         let count = 0 
      for(n of num){
         while(stack.length > 0 && stack[stack.length-1 ]> n && k >count){
             stack.pop()
             count++
         }              
         stack.push(n)
      while (count < k) {
        stack.pop()
             count++
      }
      
       
      let result = stack.join("").replace(/^0+/, "");

      return result === "" ? "0" : result;
};
}
console.log(removeKdigits(num = "33526221184202197273", k = 19))
