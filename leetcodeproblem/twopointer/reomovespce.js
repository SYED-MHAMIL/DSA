let s =  "        hello    world    "
// remove using trim anas

let t = s.trim()
// console.log(t);
"hello    world"
// remove the  space
let newstr = "" 
function removeSpacebetween(str){
    for (let i = 0; i < str.length-2; i++) {
        const element = str[i];
        const nextelement = str[i+1];
        if(element == " " && nextelement == " "){
                newstr+=""
        }else{
          newstr+=element
        }
        
    }
      newstr+=str[str.length-1]
    return newstr     
}

 console.log(removeSpacebetween(t))
