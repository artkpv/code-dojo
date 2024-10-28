# [1545. Find Kth Bit in Nth Binary String][link] (Medium)

[link]: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

Given two positive integers `n` and `k`, the binary string `Sₙ` is formed as follows:

- `S₁ = "0"`
- `Sᵢ = Sᵢ ₋ ₁ + "1" + reverse(invert(Sᵢ ₋ ₁))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and
`invert(x)` inverts all the bits in `x` ( `0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

- `S₁ = "0"`
- `S₂ = "011"`
- `S₃ = "0111001"`
- `S₄ = "011100110110001"`

Return the `kᵗʰ`bitin `Sₙ`. It is guaranteed that `k` is valid for the given `n`.

**Example 1:**

```
Input: n = 3, k = 1
Output: "0"
Explanation: S₃ is "0111001".
The 1ˢᵗ bit is "0".
```

**Example 2:**

```
Input: n = 4, k = 11
Output: "1"
Explanation: S₄ is "011100110110001".
The 11ᵗʰ bit is "1".
```

**Constraints:**

- `1 <= n <= 20`
- `1 <= k <= 2ⁿ - 1`
