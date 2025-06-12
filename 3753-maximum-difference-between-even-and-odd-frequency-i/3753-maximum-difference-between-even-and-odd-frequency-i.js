/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function(s) {
    const freq = {};
    for (let ch of s) {
        freq[ch] = (freq[ch] || 0) + 1;
    }

    let maxOdd = -Infinity;
    let minEven = Infinity;

    for (let char in freq) {
        const count = freq[char];
        if (count % 2 === 1) {
            maxOdd = Math.max(maxOdd, count);
        } else {
            minEven = Math.min(minEven, count);
        }
    }

    return maxOdd - minEven;
};
