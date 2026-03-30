//  what i learned thi and what i forgot first i do don t that is what was generater question
//  then i asked chatgpt 





// var StockSpanner=  function() {
//      this.stack=  []       
// };

// /** 
//  * @param {number} price
//  * @return {number}
//  */
// StockSpanner.prototype.next = function(price) {
//     let span= 1 
//     while(this.stack.length>0 &&  this.stack[this.stack.length -1][0]  <= price){
//             span+=this.stack.pop()[1]
//     }
//     this.stack.push([price,span])
//     return span
        
// };

// /** 
//  * Your StockSpanner object will be instantiated and called as such:
//  * var obj = new StockSpanner()
//  * var param_1 = obj.next(price)
//  */









// +++++++++++++++++++
// Problem:
// Keep track of all prices and return how many consecutive prices are smaller or equal than the current one (from curr price to previous one), only looking one by one.
// ++++++++++++++++++


// example:  
//  in:  [ 100, 70 , 40, 60 ,90 ,30 ]
//  out: [ 1 ,  1  , 1 , 2  , 5 ,  1 ]



// const Array  =   [ 100, 70 , 40, 60 ,90 ,30 ]
// function  ConsecutivePriveSEcurrent() {
//       this.stack  =  [] 
// }

// ConsecutivePriveSEcurrent.prototype.next = function(price) {
//         let count = 1 
         
//         while (this.stack.length > 0 && this.stack[this.stack.length -1 ] <= price) {
//                 this.stack.pop()
//                 count+=1
//         }
  
//         this.stack.push(price)
//         return count 
// }

// const consecutivePrice = new ConsecutivePriveSEcurrent()
// console.log(consecutivePrice.next())  //return somthing



// TODO 

// +++++++++++++++++++++++++++++++++++
//   🔹 Problem: “Remove Smaller Numbers”
// Description:

// You get a list of numbers one by one.

// Keep a stack of numbers.
// For each new number, remove all numbers smaller than it from the stack.
// Return the current state of the stack.

// This is simpler because we just return the stack instead of calculating spans.
// +++++++++++++++++++++++++++++++++++

function StackCleaner() {
     this.stack = []
}

StackCleaner.prototype.add = function (num) {
    while (this.stack.length > 0 &&  this.stack[this.stack.length -1]  < num) {
        this.stack.pop()
    }
    this.stack.push(num)
    return this.stack   

}

let cleaner =new StackCleaner()
console.log(cleaner.add(2)) //
console.log(cleaner.add(1)) //
console.log(cleaner.add(5)) //

