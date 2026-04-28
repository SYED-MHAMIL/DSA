/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    if(n == 1){
        return true
    }
    const l =n.toString().length
    let numbers =n
    let sum =0 
    for(let i=0; i<l; i++){
          sum+= numbers%10
          numbers=Math.floor(numbers/10)          
    }
    isHappy(sum)
}; 