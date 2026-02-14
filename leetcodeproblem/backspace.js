//  /**
// #  * @param {string} s
// #  * @param {string} t
// #  * @return {boolean}
// #  */
var backspaceCompare = function(s, t) {

 // s ="a#c"
 // t ="b"

    if(s.length !== s.length){
        return false
    }
    let s_arr= []
    let t_arr= []
    let sele = -1
    let tele = -1
    let count_s_space = 0 
    let count_t_space = 0 
    for(let i=s.length -1; i >= 0; i--){
       if(s[i] != '#'){
          while(count_s_space > 0){
               count_s_space-=1
                continue
          }
          s_arr[sele] = s[i]
          sele-=1
       }else{
          count_s_space+=1
       }

    }
     
   for(let i=t.length -1; i >= 0 ; i--){
          console.log("heelo ");
       if(t[i] != '#'){
          while(count_t_space > 0){
               count_t_space-=1
                continue
          }
          t_arr[tele] = t[i]
          console.log(t_arr[tele]);
          
          tele-=1
       }else{
          count_t_space+=1
       }

    }

    console.log(t_arr);
    
    return t_arr.join("")  == s_arr.join("")
  
};



console.log(backspaceCompare(s = "a#c", t = "b"));
