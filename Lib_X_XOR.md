# XOR の性質
定義
- a = 0, b = 0 -> xor(a,b)= 0
- a = 1, b = 0 -> xor(a,b)= 1
- a = 0, b = 1 -> xor(a,b)= 1
- a = 1, b = 1 -> xor(a,b)= 0

可換
- a ^ b == b ^ a

結合
- (a ^ b) ^ c == a ^ (b ^ c)

逆元
- a ^ x ^ x == a
- a ^ x == b ^ x  <=> a == b            // ^x を作用させる
- a != b          <=> a ^ x != b ^ x    // ^x を作用させる

通常和との関係
- a ^ b <= a + b        // 桁の繰上りがxorにはない