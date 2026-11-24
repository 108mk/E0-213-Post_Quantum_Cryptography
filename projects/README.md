# Projects

Small implementations that go with the lectures. They use toy parameters and are for learning only.

## `lattice/` (SageMath)

| File | Goes with | What it does |
|---|---|---|
| [`euclid.sage`](lattice/euclid.sage) | Lecture 19 | Euclid's algorithm, the extended algorithm and modular inverse, printing every step. Also Euclid for polynomials |
| [`ggh.sage`](lattice/ggh.sage) | Lecture 18 | GGH encryption: a nearly orthogonal private basis, a skewed public basis (measured by Hadamard ratio), and decryption by rounding |
| [`ntru.sage`](lattice/ntru.sage) | Lecture 19 | NTRUEncrypt: key generation, encryption and decryption |
| [`kyber.sage`](lattice/kyber.sage) | Lecture 21 | Kyber-style encryption from module LWE over $\mathbb{Z}_q[x]/(x^n+1)$ |
| [`ggh_analysis.ipynb`](lattice/ggh_analysis.ipynb), [`kyber.ipynb`](lattice/kyber.ipynb) | | Notebook versions of `ggh.sage` and `kyber.sage` |

### Running

Install SageMath by following its [installation guide](https://doc.sagemath.org/html/en/installation/index.html). `kyber.sage` also needs `tqdm`, which you can add with `sage -pip install tqdm`.

Run these from `projects/lattice/`:

```bash
sage ntru.sage
```

This runs ten encrypt-and-decrypt checks with n = 743, q = 2048 and prints `True` for each.

```bash
sage -c 'load("ggh.sage"); print(test_correctness(5, 100, 3)); print(test_security(5, 100, 3))'
```

The arguments are the dimension, the size of the private basis entries and the bound on the error. `test_correctness` checks that decryption with the private basis recovers the message. `test_security` checks that decryption with the public basis does not.

```bash
sage -c 'load("kyber.sage"); print(test_percentage(200))'
```

This counts how many of 200 random messages decrypt correctly. With the toy parameters q = 17, n = 4 only about 60% do, because the noise is large compared with q. Calling `set_vals(7681, 256)` first switches to parameters where decryption succeeds.

```bash
sage -c 'load("euclid.sage"); print(mod_inv(7, 40))'
```

The scripts were last checked in November 2026 with passagemath 10.8, a pip-installable distribution of SageMath. The two notebooks were saved with a plain Python kernel, so switch the kernel to SageMath before running them.

## `hash-based-signatures/` (Python 3)

Tanja Lange's snippets that build one-time signatures from a hash function in small steps. They go with lectures 9 and 10 and need only the standard library. The source is listed in [`references/README.md`](../references/README.md).

| File | What it signs |
|---|---|
| [`signempty.py`](hash-based-signatures/signempty.py) | The empty message. The signature is a hash preimage of the public key |
| [`signbit.py`](hash-based-signatures/signbit.py) | One bit, using two `signempty` key pairs |
| [`sign4bits.py`](hash-based-signatures/sign4bits.py) | Four bits, using four `signbit` key pairs |
| [`lamport.py`](hash-based-signatures/lamport.py) | An integer message, by signing each bit of its SHA3-256 hash (Lamport's scheme) |
| [`weak_winternitz.py`](hash-based-signatures/weak_winternitz.py) | A value from 0 to 15 with a single hash chain. Deliberately insecure: a signature on m gives a signature on any larger value |
| [`slow_winternitz.py`](hash-based-signatures/slow_winternitz.py) | The fix: a second chain signs 16 − m, so the message cannot be pushed up without breaking the other chain |

Run this from `projects/hash-based-signatures/`:

```python
import lamport

pk, sk = lamport.keypair()
signed = lamport.sign(2023, sk)
print(lamport.open(signed, pk))   # 2023
```
