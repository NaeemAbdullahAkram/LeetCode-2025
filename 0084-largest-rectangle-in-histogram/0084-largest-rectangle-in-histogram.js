/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let n = heights.length;
    var next = new Array(n);
    next = nextSmallerElement(heights, n);
    var prev = new Array(n);
    prev = prevSmallerElement(heights, n);
    var area = 0;
    for(let i=0; i<n; i++){
        var l = heights[i];
        if(next[i] == -1){
            next[i] = n;
        }
        var b = next[i] - prev[i] - 1;
        var newArea = l*b;
        area = Math.max(area, newArea);
    }
    return area;
};

var prevSmallerElement = function(st, n){
    let stack = [];
    stack.push(-1);
    var ans1 = new Array(n);

    for(let i=0; i<n; i++){
        let curr = st[i];
        while(stack[stack.length-1] != -1 && st[stack[stack.length-1]] >= curr){
            stack.pop();
        }
        //ans is top of stack
        ans1[i] = stack[stack.length-1];
        stack.push(i);
    }
    return ans1;
}

var nextSmallerElement = function(st, n){
    let stack = [];
    stack.push(-1);
    var ans = new Array(n);

    for(let i=n-1; i>=0; i--){
        let curr = st[i];
        while(stack[stack.length-1] != -1 && st[stack[stack.length-1]] >= curr){
            stack.pop();
        }
        //ans is top of stack
        ans[i] = stack[stack.length-1];
        stack.push(i);
    }
    return ans;
}