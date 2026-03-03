//  take every susutring and and see is it palendrom or not;
// is palendrom func

// function is_palendrom(text,i,j){
//     // text = 'a'
//     const strt =i
//     const end =  j  
//     let left= strt 
//     let right= end
//     while (left <= right){
//         if(text[left] != text[right]){
//            return  false
//         }
//         left+=1
//         right-=1

//     }
//     return true
// }


// function  longestPalendrom(s) {
//     // remove slicing  and got o(n2)
//     let longest_palen=s[0];
//     for(let i=0;  i<s.length; i++ ){
//         for (let j = i; j < s.length; j++){            
//             //  console.log(substr);
              
//              if(is_palendrom(text,i,j)){
                
//                  if(longest_palen.length < substr.length ){
//                      longest_palen = substr

//                  }
//              }
            
//         }
//     }
//     return longest_palen
// }

// console.log(longestPalendrom("abcbbc"));








// function is_palendrom(text,i,j){
//     // text = 'a'
//     const strt =i
//     const end =  j  
//     let left= strt 
//     let right= end
//     while (left <= right){
//         if(text[left] != text[right]){
//            return  false
//         }
//         left+=1
//         right-=1

//     }
//     return true
// }


// function  longestPalendrom(s) {
//     let start_palendrom=0
//     let end_palendrom  =0 
//     for(let i=0;  i<s.length; i++ ){
//         for (let j = i; j < s.length; j++){            
              
//              if(is_palendrom(s,i,j)){
                
                 
//                  if((end_palendrom - start_palendrom +1) <= (j-i +1) ){
//                      start_palendrom= i
//                      end_palendrom=  j
//                  }
//              }
            
//         }
//     }
//     return s.slice(start_palendrom,end_palendrom+1)
// }

// console.log(longestPalendrom("abaab"));
// 3 pointer --
// left,mid,right








function  longestPalendrom(s){
      let left;
      let  right;
      let start_palendrom=0;
      let end_palendrom=0;
      
      // aabba 
      for (let i = 0; i < s.length; i++) {
        // for even
        left=i
        right=i + 1
        while(left >=0 && right <= s.length && s[left] == s[right]){
            if((end_palendrom-start_palendrom+1) < (right-left + 1)){
                start_palendrom=left
                end_palendrom = right                       
            }  
            left-=1
            right+=1
        }

        // for odd
        left=i-1
        right=i + 1
        while(left >=0 && right <= s.length && s[left] == s[right]){
            if((end_palendrom-start_palendrom+1) < (right-left + 1)){
                start_palendrom=left
                end_palendrom = right                       
            }  
            left-=1
            right+=1
        }


        
      }
   return   s.slice(start_palendrom,end_palendrom+1)
}


console.log(longestPalendrom("aaabbaaa"));
