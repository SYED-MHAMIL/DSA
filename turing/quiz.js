// class Point {
//   constructor(x, y) {
//     this.x = x;
//     this.y = y;
//   }

//   static displayName = "Point"; // Static property

//   static distance(a, b) { // Static method
//     const dx = a.x - b.x;
//     const dy = a.y - b.y;
//     return Math.hypot(dx, dy);
//   }
// }

// const p1 = new Point(5, 5);
// const p2 = new Point(10, 10);

// // console.log(Point.displayName); // Access static property: "Point"
// // console.log(Point.distance(p1, p2)); // Call static method: 7.0710678118654755

// // The following will result in an error or undefined because static members are not on the instance:
// console.log(p1.displayName); // undefined
// console.log(p1.__proto__); // TypeError or undefined


// let a= 0
// try {
//      if (a == 0) {
//          throw new Error();
         
//      }
// } catch{
//     console.log("error");
    
// }






// let a= 0
// try {
//      if (a == 0) {
//         // 
//          let error = " zeror dont alloow"
//          throw new Error("zero erorr", {cause:error});
         
//     }
// } catch(erorr){
//     console.log(erorr.message, erorr.cause);
    
// }





// *******************************
        //  new question
// *******************************
// const arr = [10, 20, 30, 40];

// const index = arr.findIndex(num => num > 25);

// console.log(index); // 2





// *******************************
        //  new question
// *******************************


// function Dev() {}
// Dev.prototype.language = 'JS';
// const person = new Dev();
// // person.language = 'Python';
// console.log(Dev);


// *******************************
        //  new question
// *******************************

// const a = { x: 1 };
// const b = { x: 1 };
// const c = a;

// console.log(a === b, a === c);




// *******************************
        //  new question
// *******************************

// var x = 10;
// if (true) {
//     var x = 20;
//     console.log(x);
// }
// console.log(x);




// *******************************
        //  new question
// *********************************

// 'use strict';
// function check() {
//     this.value = 5;
// }
// check();



// *******************************
        //  new question
// *********************************


// const a = {};
// const b = { key: 'b' };
// const c = { key: 'c' };

// a[b] = 123;
// a[c] = 456;

// console.log(a[b]);
// console.log(a[c]);


// const numbers = [1, 2, 3];
// numbers[10] = 11;
// console.log(numbers.length);    




// var foo = 1;
// function foo() {}
// console.log(typeof foo);


// a =[1, 2, 3].reduce((acc, curr) => {
//         console.log("s");
        
//   return acc + curr;
// });

// console.log(a);



// const str = "5";
// console.log(str.padStart(4, "0").length);