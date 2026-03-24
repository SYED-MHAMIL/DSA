// Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

// Example 1:

// Input: s = "bcabc"
// Output: "abc"
// Example 2:

// Input: s = "cbacdcbc"
// Output: "acdb"
 

// Constraints:

// 1 <= s.length <= 104
// s consists of lowercase English letters.








// +++++++++++++++++++++++++++++++++++++++++++++++++++++++
//           way to solve
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++



// #1
// if i just solve by the incereasing order so see what happenns

// Input: s = "bcabc"
// Output: "abc"

// ans :  in first #1 example  we see the  'b' so i'll put in to satck and then see 'c' so again put  and when i come into  i'll see that 'a' is greather both so we should remove it and put all reamaining beavuse those order is incerasing

// let's move on second

// Input: s = "cbacdcbc"
// Output: "acdb"
// ans : if i do exactly what i did in the first example so the ans is Output: "abc" so that is wrong why beacuse we need to include every letter in once time but we deleted (we lose) how can i come up with solution  

// here is idea 
// ************
// incerasing order + freequency ()
// ************

// if i do wih frequency so the answer is "acdbc" we are getting wrong  tooo because we are not which element i have included

// here is idea 
// ************
// incerasing order + freequency () + visited (means i have visit this element before)
// ************
    


