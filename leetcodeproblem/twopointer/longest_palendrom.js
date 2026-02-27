

//  take every susutring and and see is it palendrom or not;
// is palendrom func

function is_palendrom(text){
    
    if(text[0] !== text[text.length-1]){
          return  false
    }
   
    if(text.length <= 1){
    return  true
    }
    return is_palendrom(text.slice(1,text.length -1))
}


function  longestPalendrom(s) {
    // remove slicing  and got o(n2)
    let longest_palen=s[0];
    for(let i=0;  i<s.length; i++ ){
        for (let j = i; j < s.length; j++){            
             const substr = s.slice(i,j+1)
            //  console.log(substr);
              
             if(is_palendrom(substr)){
                
                 if(longest_palen.length < substr.length ){
                     longest_palen = substr

                 }
             }
            
        }
    }
    return longest_palen
}

console.log(longestPalendrom("aba"));
