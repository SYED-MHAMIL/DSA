function  reverseArray(arr,start, end) {

    if(start>= end){
        // console.log(arr)
    return ;
    }
    reverseArray(arr,start+1,end-1)
    console.log({start,end});
    
    [arr[start],arr[end]]=[arr[end],arr[start]]
    return arr
};
let array =  [1,2,3,4,5,6]
// console.log(reverseArray(array,0,array.length -1) 
// )

//  how its working ? 
// 1. we are calling reverseArray function with arr value which is [1,2,3], start value which is 0 and end value which is 2
// e.g :
// function  reverseArray([1,2,3],0,2) {       
//     if(0 >= 2){
//         console.log(arr)
//     return ;
//     }
//      [arr[0],arr[2]]=[arr[2],arr[0]]
//      reverseArray(arr,1,1)
// };

// 2. now it will call itself with the curr value of arr which is [3,2,1], start value which is 1 and end value which is 1
// e.g :
// function  reverseArray([3,2,1],1,1) {
//     if(1 >= 1){
//         console.log(arr)
//     return ;
//     }
//      [arr[1],arr[1]]=[arr[1],arr[1]]
//      reverseArray(arr,2,0)
// };

// 3. now it will call itself with the curr value of arr which is [3,2,1], start value which is 2 and end value which is 0
// e.g :
// function  reverseArray([3,2,1],2,0) {
//     if(2 >= 0){
//         console.log(arr)
//     return ;
//     }
  

// done it ...





function isAlpha(ch) {
    return (
        (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')
    )
}




 //  check if the string is palindrome or not
function isPale(str,start,end) {
    if (start >= end) {
        return true
    }
    if (!isAlpha(str[start])) {
        return isPale(str,start+1,end)
    }

    if (!isAlpha(str[end])) {
        return isPale(str,start,end-1)
    }
    

    if (str[start].toLowerCase() !== str[end].toLowerCase()) {
        
        return false
    }
    return isPale(str,start+1,end-1)    
    }
let str = "@3MADAM;?////"
let is = isPale(str,0,str.length -1)
// console.log({is});

// if (is) {
//     console.log('YES ! its palendrom');
    
// }else{
//     console.log('NO its not palendrom');

// }














// fibonacci numbres


function fibonacciN(n) {
    if (n <= 1) {
        return n;
    }
    let last=  fibonacciN(n-2) 
    let slast =fibonacciN(n-1);
    return  last+slast
    
}
console.log(fibonacciN(3));
// 0+1+2
