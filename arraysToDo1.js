// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

function pushFront(arr, num) {
    let outputArr = [num, ...arr];
    return outputArr;
}
// Pop Front
// Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().
var arr1 = [1,3,5,7];
function popFront(arr) {
    let output = arr[0];
    [x, ...arr] = arr;
    console.log(arr);
    return output;
}
console.log(popFront(arr1));
// Insert At
// Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. 
// You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).
function insertAt(arr, index, val) {
    for (i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    console.log(arr);
    arr[index] = val;
    return arr;
}
console.log(insertAt(arr1, 1, 99));
