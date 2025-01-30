/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const isScramble = (s1, s2) => {
    const len = s1.length;
    if (s1 === s2) return true;

    const memo = new Map();

    const isScrambleHelper = (start1, start2, length) => {
        const key = `${start1}-${start2}-${length}`;
        if (memo.has(key)) return memo.get(key);

        const subS1 = s1.substring(start1, start1 + length);
        const subS2 = s2.substring(start2, start2 + length);

        if (subS1 === subS2) {
            memo.set(key, true);
            return true;
        }

        const count = new Array(26).fill(0);
        for (let i = 0; i < length; i++) {
            count[subS1.charCodeAt(i) - 97]++;
            count[subS2.charCodeAt(i) - 97]--;
        }

        for (let i = 0; i < 26; i++) {
            if (count[i] !== 0) {
                memo.set(key, false);
                return false;
            }
        }

        for (let i = 1; i < length; i++) {
            if (
                (isScrambleHelper(start1, start2, i) && isScrambleHelper(start1 + i, start2 + i, length - i)) ||
                (isScrambleHelper(start1, start2 + length - i, i) && isScrambleHelper(start1 + i, start2, length - i))
            ) {
                memo.set(key, true);
                return true;
            }
        }

        memo.set(key, false);
        return false;
    };

    return isScrambleHelper(0, 0, len);
};