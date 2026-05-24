// function greet(){

//     console.log("hello")
//     greet()
// }


// function main(){
//     greet()
// }

// main()

// so that function calling itself again and agian there is not limit defined  where it should be stop so i will give you the error 

let cnt=1

// le
function counter(n){
    if (n > 2) {
        return 1
    }
    console.log(n)  
    n++
    counter(n)
}
// counter(cnt);

// how its working ? 
// 1. we are calling counter function with cnt value which is 1
// it will call itself with the curr value of n which is 2
// e.g :  
//  function counter(2){
//     if (2 > 2) {
//         return 1
//     }   
//     console.log(2)
//     n++
//     counter(n)
// }

// 2. now it will call itself with the curr value of n which is 3
// e.g :
//  function counter(3){
//     if (3 > 2) {
//         return;
//     }   
//  all below code will not execute because of return statement
//     console.log(3)
//     n++
//     counter(n)
// }



//  PROBLEM : 1. print name 5 times definatly using recursion

cnt =1
function printName(name){
    if (cnt  > 5) {
        return ;
    }
    console.log(name + cnt);
    cnt++
    printName(name)
}
// printName("mohamil")



// Print linearly 1 to n 

function printN(n) {
  if(cnt > n){
   return ;
  }
  console.log(cnt);
  cnt++
  printN(n)
}

// printN(1000)


// print N to 1 
function printNtoOne(n) {
  if(n < 1){
   return;
  }
  console.log(n);
  n--
  printNtoOne(n)
}
// printNtoOne(5)  




//  print linearly from 1  to N (but by  backtracking also called as head recursion);


function printNBacktracking(n) {
    if(n < 1){
     return;
    }
    

    printNBacktracking(n-1);
    console.log(n);
}

// printNBacktracking(3)

// let's see how its working
// 1. we are calling printNBacktracking function with n value which is 3
// e.g :
// function printNBacktracking(3) {
//     if(3 < 1){
//      return;
//     }
//     printNBacktracking(2);
//     console.log(3);
// }

// 2. now it will call itself with the curr value of n which is 2
// e.g :
// function printNBacktracking(2) {
//     if(2 < 1){
//      return;
//     }
//     printNBacktracking(1);
//     console.log(2);
// }

// 3. now it will call itself with the curr value of n which is 1
// e.g :
// function printNBacktracking(1) {
//     if(1 < 1){
//      return;
//     }
//     printNBacktracking(0);
//     console.log(1);
// }

// 4. now it will call itself with the curr value of n which is 0
// e.g :
// function printNBacktracking(0) {
//     if(0 < 1){
//      return;
//     }

//   ALERT :the rest of the code will not execute because of return statement
//     printNBacktracking(-1);
//     console.log(0);
// }










// Reverse a string using recursion by using backtracking
// pan
let reverseStr = '';
function  reverseString(str,idx) {
    if(str.length == idx){
      return ''
    }
    reverseString(str,idx + 1)
    reverseStr+=  str[idx]
     console.log(reverseStr);
     
}

// reverseString('pan',0)



// +++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ========   Example 1 : Sum of Natural Numbers (n=3)    =========
// ++++++++++++++++++++++++++++++++++++++++++++++++++++
// lets n=3
function  sum(n) {
    // base condition 
        if (n == 1) {
             return 1 
        }
    
    
    return n + sum(n-1) 
}

console.log(sum(3))

// sum(3) -> sum(2) -> sum(1)
// 3 <------- 2 <------- 1


//  3 + sum(2) => 3+3 => 6
//  2 + sum(1) => 2+1 => 3