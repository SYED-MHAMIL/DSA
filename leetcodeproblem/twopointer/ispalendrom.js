


// class Solution {
//    isPalindrome = function(s) {
//     let left =0
//     let right = s.length -1 
//     // madam
//     while(left <= right){
//        let isLeft = false
//        let isRight = false
//        if(s[left] in words 
//        || s[left] in nums){
//            isLeft = true
//        }
       
//        if(s[right] in words 
//        || s[right] in nums){
//            isRight = true
//        }

       
//        if(isRight && isLeft){
//           left+=1
//           right-=1 
//        }else if(!isRight && !isLeft){
//         return false
//        }else{
//         if(isRight){
//            left+=1
//         }else{
//             right-=1
//         }
        

//        }


//     }
    
    
//     return true
// }  
//  isAlnum(c){
//      return (
//         c >= "A"
//      )
//  }

// }

// const pla =new isPalindrome("ass")
// pla.isPalindrome()



/**
 * @param {string} s
 * @return {boolean}
 */

function isAlNum(chr){
    return (
        chr >= "A" && chr <= "Z" ||
        chr >= "a" && chr <= "z" ||
        chr >= "0" && chr <= "9"
    )
}
var isPalindrome = function(s) {
    let left =0
    let right = s.length -1 
    // ;Madam abc madam;
    // "s"
    while(left <right){
        if(s.length == 1){
              return true
        }
        while(left < right && !isAlNum(s[left])){
          left+=1
        }
        
        while(left < right && !isAlNum(s[right])){    
          right-=1
        }
        console.log({"left": left,"right" : right});
        if(s[left].toLowerCase() == s[right].toLowerCase()){
             left+=1
             right-=1
        }else{
            return false
        }
    }
    
    
    return true
};


console.log(isPalindrome(".,"));
