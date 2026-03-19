/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    let stack= [];
    let res= ""
    let i = 0
    for(chr of word){
        stack.push(chr)
        if(chr == ch){  
           break
        }
        i++
    }

     if(i == word.length)return word 
          while(stack.length >0){
            res+=stack.pop()
          }
    

    for(let j=i+1; j<word.length; j++){
          let element = word[j]
          res+=element        
    }
       
   return res  
};


console.log(reversePrefix("abcdefd","d"))