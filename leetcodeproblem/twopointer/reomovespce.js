// let s =  "        hello    world    "
// remove using trim anas

// let t = s.trim()
// // console.log(t);
// "hello    world"
// // remove the  space
// let newstr = "" 
// function removeSpacebetween(str){
//     for (let i = 0; i < str.length-1; i++) {
//         const element = str[i];
//         const nextelement = str[i+1];
//         if(element == " " && nextelement == " "){
//                 newstr+=""
//         }else{
//           newstr+=element
//         }
        
//     }
//       newstr+=str[str.length-1]
//     return newstr.split(" ").reverse().join(" ")
  
//   }


//  console.log(removeSpacebetween(t))










// +++++++++++++++++++++++++++++++++++++
    // two 
// +++++++++++++++++++++++++==

// let s =  "        hello    world    "
// function removeSpace(str) {
//   let newStr = ""
//   let isFirstwordStart = false
//   let index= str.length -1
//   while(index >0){
//      let element = str[index]
//       if(element != " "){
//           isFirstwordStart =true
//       }
//       if (isFirstwordStart){
//          console.log("d");
         
//            if (element != " ") {
//               let firstidx = index
            
//              while(str[index] != " "){
//                     index-=1
//              }
//              newStr+=str.slice(index+1,firstidx+1)
             
//            }else{
//               while(str[index] == " " && str[index -1] == " "){
//                     index-=1
//              }
//             if((str[index] == " ") && !(str[index -1] == " ")){
//               newStr+=str[index]
//              }
//            }
//            index-=1
//       }else{
//          index-=1
//       }
//   }  
//   // if (str[0] == " ") {
//   //     newStr+=str[0]
//   // }
// return  newStr
// }


// console.log(removeSpace("the sky is blue"));



// function removeSpace(str) {
//     // str = str.split("")
//     let words = []
//     let  current_words = ""
//     for (let i = 0; i < str.length; i++) {
//         const element = str[i];
//         if (element != " ") {
//                current_words+=element
           
//             }else{
                
//             if(current_words != ""){
//                 //   console.log(current_words)
//                       words.push(current_words)
//                       current_words = ""
//                 }            
//             }
            
        

//     }
//             if(current_words != ""){
                   
//                      words.push(current_words)
//                             current_words = ""
//                   }     
       
//    return  words.reverse().join(" ")    
// }

// console.log(removeSpace("hello  world"));



// *******************************************************
//              two pointer
// *******************************************************


// function removeSpace(str) {
//     str = str.split("")
//      let left = 0
//     let right = str.length -1
    
//     while (left < right) {
//         while (str[left] === " ") {
//             str[left] = ""
//             left+=1
//         }
//         while (str[right] === " ") {
//             str[right] = ""
//             right-=1
//         }
//         [str[left],str[right]] =[str[right],str[left]]
//         left+=1
//         right-=1
//     }
//     return str
// }

// console.log(removeSpace("  hello  world   "));

// function removeSpace(str) {
//     str = str.split("")
//      let left = 0
//      let right = str.length
//      let words = []
//     //  s=  "a son "
//     while (left < right) {
//         let current_words = ""
//         while (str[left] != " ") {
//            current_words+= str[left]  
//            left+=1
//         } 
//         if(current_words != ""){
//            words.push(current_words)
//         }
//         left+=1
//     }
// }

// console.log(removeSpace("  hello  world   "));



function removeSpace(str) {
    str = str.split("")
     let left = 0
     let right = str.length -1
     let words = ""
    //  s=  "a son "
    while (left < right) {  
         [str[left],str[right]] =[str[right],str[left]]
        left+=1
        right-=1
        }
    let chr = 0 
    let  lenght= str.length
    while (chr < lenght) {
         let current_words = []
         while(str[chr] != " "){
             current_words.unshift(str[chr])
             chr+=1
         }
         if (current_words != "") {
            words+=` ${join(current_words)}`
            current_words=''
         }   
        chr+=1     
    }
  return words
}

console.log(removeSpace("  hello  world   "));

function join(array) {
    let  str = ""
    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        str+=element
    }
    return str
}