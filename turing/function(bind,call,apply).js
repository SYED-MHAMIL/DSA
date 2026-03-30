// bind


// const module = {
//   x: 42,
//   getX() {
//     return this.x;
//   },
// };

// const unboundGetX = module.getX;
// console.log(unboundGetX()); // The function gets invoked at the global scope
// // Expected output: undefined

// const boundGetX = unboundGetX.bind(module);
// console.log(boundGetX());
// // Expected output: 42


"use strict"; // prevent `this` from being boxed into the wrapper object

// function log(...args) {
//   console.log(this, ...args);
// }
// const boundLog = log.bind("this value", 1, 2);
// const boundLog2 = boundLog.bind("new this value", 3, 4);
// boundLog2(5, 6); // "this value", 1, 2, 3, 4, 5, 6


// let array = [{"name" : "ali"}] 
// array[-1] = {"name" : "zain"}


// function  s() {
//     for (let index = 0; index < this.length; index++) {
//         const element = this[index];
        
        
//         console.log(element.name);
        
//     }
// }

// let  t= s.bind(array)
// t()
