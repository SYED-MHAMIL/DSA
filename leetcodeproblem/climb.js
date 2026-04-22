var climbStairs = function(n) {
      if(n <=2){
         return n
      }
    let first= 1 , second = 2  ;
    let res = 3 
    for(let i=3; i<=n; i++){
      res=res+2
    }
    return res
};

console.log(climbStairs(4));
