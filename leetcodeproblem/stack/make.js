class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
}
/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val)
    if(this.minStack.length >  0){
       if(this.minStack[this.minStack.length -1] >= val ){
          this.minStack.push(val)
       }
    }else{
       this.minStack.push(val)
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if(this.stack.length > 0){
        let param = this.stack.pop()
        if (this.minStack.length > 0 && this.minStack[this.minStack.length -1] == param) {
              this.minStack.pop()  
        } 
    }
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if(this.stack.length > 0){
    return this.stack[this.stack.length -1]
    }
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    
    return  this.minStack[this.minStack.length -1]
};


//   Your MinStack object will be instantiated and called as such:
 var obj = new MinStack()
  obj.push(3)
  obj.push(1)
  obj.push(0)
  obj.pop()
  obj.pop()
  var param_3 = obj.top()
  var param_4 = obj.getMin()
 console.log(param_4)
