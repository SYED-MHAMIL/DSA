//  given the string returned the "reversed" string where all charactor that are not a letter stay on the same place

// example 1
// input "ab-cd"
// output: dc-ba 



// Example :2 

// input : "a-bC-dEf=ghlj!!"
// output : "j-lh-gfE=dCba!!" 


function isAlpha(chr) {
    return (
         (chr >= "A" && chr <= "Z") ||
         (chr >= "a" && chr <= "z")
    )    
}





function reverseStringBasedOnAlpha(str) {
    str= str.split("")
    let left =  0 
    let right =  str.length -1
    
    while(left  < right){
         while(left < right && !isAlpha(str[left])){ 
             left+=1
         }
         while(left < right && !isAlpha(str[right])){ 
            right-=1
         }
         
         [str[left],str[right]]=[str[right],str[left]]
          left+=1
          right-=1
         

    }
     return str.join("")
}

const reversestring = reverseStringBasedOnAlpha("a-bC-dEf=ghlj!!")

function checktest(str) {
    const  arr = ["dc-ba","j-lh-gfE=dCba!!"]
    return arr.some(chStr => chStr == str)

}

console.log(checktest(reversestring));
