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


let a= 0
try {
     if (a == 0) {
         throw new Error();
         
     }
} catch{
    console.log("error");
    
}