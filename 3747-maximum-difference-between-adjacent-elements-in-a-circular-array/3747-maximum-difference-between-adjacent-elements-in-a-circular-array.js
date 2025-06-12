/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function(nums) {
    let maxDiff = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        // Calculate absolute difference between nums[i] and next element, wrapping with modulo
        let diff = Math.abs(nums[i] - nums[(i + 1) % n]);
        if (diff > maxDiff) {
            maxDiff = diff;
        }
    }
    return maxDiff;
};