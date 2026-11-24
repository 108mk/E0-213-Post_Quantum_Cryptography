# Assignments

## A1: Cryptanalysis of RC4

A presentation with Ishan Pandey (February 2023) on why the RC4 stream cipher is broken. It covers RC4's key-scheduling and keystream-generation algorithms, the biases in its keystream and how they give a distinguisher, and the attacks on RC4 in TLS by AlFardan et al. (2013).

| File | What it is |
|---|---|
| [`rc4-cryptanalysis_slides.pdf`](a1_rc4-cryptanalysis/rc4-cryptanalysis_slides.pdf) | Final slides (21 slides) |
| [`rc4-cryptanalysis_slides.pptx`](a1_rc4-cryptanalysis/rc4-cryptanalysis_slides.pptx) | The same slides, editable |
| [`rc4-cryptanalysis_early-draft.pptx`](a1_rc4-cryptanalysis/rc4-cryptanalysis_early-draft.pptx) | An earlier 8-slide draft that spells the algorithms out in text |
| [`rc4_cipher.ipynb`](a1_rc4-cryptanalysis/rc4_cipher.ipynb) | RC4 in Python: key scheduling, keystream generation, encryption and decryption |
| [`rc4_bias_notes.ipynb`](a1_rc4-cryptanalysis/rc4_bias_notes.ipynb) | Working notebook on keystream bias. It is a scratch pad, and some cells do not run on their own |

Background: lecture 3 ([stream ciphers](../lectures/03_stream-ciphers.pdf)) and the [AlFardan et al. slides](../../references/slides/alfardan-et-al-2013_rc4-in-tls.pdf).

Related repository: [108mk/Cryptanlysis_of_RC4](https://github.com/108mk/Cryptanlysis_of_RC4).

## A2: Grover meets Simon

A presentation with Ishan Pandey (April 2023) of the paper *Grover Meets Simon – Quantumly Attacking the FX-construction* by Leander and May. It covers Grover search against block ciphers, Simon's algorithm against the Even–Mansour construction, and how the paper combines the two to break the FX construction at roughly the cost of Grover search on the underlying cipher.

| File | What it is |
|---|---|
| [`grover-meets-simon_slides.pdf`](a2_grover-meets-simon/grover-meets-simon_slides.pdf) | Our slides (25 slides) |
| [`paper-summary_rajiv-sangle.pdf`](a2_grover-meets-simon/paper-summary_rajiv-sangle.pdf) | A written summary of the same paper by Rajiv Sangle |

Papers: [Leander and May (2017)](../../references/papers/leander-may-2017_grover-meets-simon.pdf) and a later feasibility analysis by [Zhu et al. (2023)](../../references/papers/zhu-et-al-2023_feasibility-of-grover-meets-simon.pdf).

## Scribe exercises

[`scribe-exercises_manish-kumar.pdf`](scribe-exercises_manish-kumar.pdf) holds my solutions to exercises that were set during the lectures.

| Lecture | Exercise |
|---|---|
| 12, identification protocols | Combine Diffie–Hellman key agreement with signature-based mutual authentication |
| 16, code-based cryptography I | Build a KEM from McEliece and study its security |
| 17, code-based cryptography II | Extend the "Sloppy Alice" attack to the Niederreiter system |
| 18, lattices: basic concepts | Efficiency of GGH and the sizes of its keys and ciphertext |
| 21, encryption and signature from LWE | Correctness, sizes and cost of Regev's scheme; how the optimised version improves on it and why it is IND-CPA secure |
| 22, secret sharing | Build the monotone circuit for a given access structure |
