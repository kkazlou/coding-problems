# Kill K-th Bit

*Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.*

In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number `n` the `k-th` bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the `k-th` bit of `n` back to `0`.

Example

* For `n = 37` and `k = 3`, the output should be `solution(n, k) = 33`.

37<sub>10</sub> = 100**1**01<sub>2</sub> ~> 100**0**01<sub>2</sub> = 33<sub>10</sub>.

* For `n = 37` and `k = 4`, the output should be `solution(n, k) = 37`.

The `4-th` bit is `0` already (looks like the Mad Coder forgot to encrypt this number), so the answer is still `37`.