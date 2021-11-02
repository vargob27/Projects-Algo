// Reverse
// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
// array – move values within the array that you are given. As always, do not use built-in array functions such as splice().

function reverseArr(arr) {
    for (i = 0; i < arr.length / 2; i++) {
        let temp = arr[i];
        arr[i] = arr[arr.length - 1 - i];
        arr[arr.length - 1 - i] = temp;
    }
    console.log(arr);
    return arr;
}
var test = [1, 3, 5, 7, 9, 11];
// reverseArr(test);

// Rotate
// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
// change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.
function rotate(arr, offset) {
    if (offset > 0) {
        for (i = 0; i < offset; i++) {
            let temp = arr[arr.length -1];
            for (i2 = arr.length - 2; i2 >= 0; i2--) {
                arr[i2 + 1] = arr[i2];
            }
            arr[0] = temp;
            // console.log(arr);
        }
        return arr;
    } else {
        let convert = offset * -1
        for (i = 0; i < convert; i++) {
            let temp = arr[0];
            for (i2 = 1; i2 < arr.length; i2++) {
                arr[i2-1] = arr[i2];
            }
            arr[arr.length-1] = temp;
            // console.log(arr);
        }
        return arr;
    }
}
var test2 = [1, 3, 5, 7];
console.log(test2);
console.log(rotate(test2, -1));

// Filter Range
// Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.
function filterRange(arr, min, max) {
    for (i = 0; i < arr.length; i++) {
        if (arr[i] < min || arr[i] > max) {
            // arr[i] = null;
            for (i2 = i + 1; i2 < arr.length; i2++) {
                arr[i2 - 1] = arr[i2];
            }
            arr.length--;
            i--;
        }
    }
    return arr;
}
// console.log(filterRange(test2, 3, 5));

// Concat
// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].
function concat(arr1, arr2) {
    // output = [...arr1, ...arr2];
    // return output;
    
    let output = [];
    let counter = 0;
    for (i = 0; i < arr1.length; i++) {
        output[counter] = arr1[i];
        counter++;
    }
    for (i2 = 0; i2<arr2.length; i2++) {
        output[counter] = arr2[i2];
        counter++;
    }
    return output;
}
var con1 = [2,4,6];
var con2 = [69, 420];
console.log(concat(con1, con2));