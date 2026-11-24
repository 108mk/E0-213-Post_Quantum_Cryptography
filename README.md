# E0 213: Quantum-Safe Cryptography

Course material, assignments and working notes from **E0 213 Quantum-Safe Cryptography**, taught by Dr. Sanjit Chatterjee and Dr. Tapas Pandit at the Indian Institute of Science, Bengaluru, in January–April 2023.

The course is a first introduction to cryptography that is expected to stay secure against an adversary with a quantum computer. It starts with symmetric-key primitives and then covers hash-based, multivariate, code-based and lattice-based public-key schemes.

No prior cryptography is assumed. The lectures do assume undergraduate algorithms, linear algebra, probability, number theory and abstract algebra, and the basic ideas of quantum computing.

## What is where

| Folder | Contents |
|---|---|
| [`course/lectures/`](course/lectures) | The instructors' slides, one PDF per lecture (22 decks) |
| [`course/scribes/`](course/scribes) | Typeset lecture notes written by students, numbered by the lecture they cover |
| [`course/assignments/`](course/assignments) | Two paper presentations and solutions to exercises set in the lectures |
| [`course/exams/`](course/exams) | Class test 1 |
| [`projects/`](projects) | Code: lattice schemes in SageMath, hash-based signatures in Python |
| [`references/`](references) | Reading list with links to the books, plus the papers and external slides used in the course |
| [`notes/`](notes) | Topic-by-topic knowledge base. It starts as a map of the material above and grows beyond the course |

My grade transcript for the M.Tech programme is in [`course/transcript_manish-kumar.pdf`](course/transcript_manish-kumar.pdf).

## Where to start

- **New to cryptography:** read lectures 1–8 in order. They build the symmetric-key and public-key basics that the rest of the course relies on.
- **Here for one family of schemes:** open the [topic map](notes/README.md), which lists the lectures, scribes, code and papers for each family.
- **Studying a single lecture:** read the slides, then the scribe if there is one, then run the matching code in [`projects/`](projects).

## Lectures

| # | Date (2023) | Slides | What it covers | Scribe |
|---|---|---|---|---|
| 1 | 09 Jan | [Introduction](course/lectures/01_introduction.pdf) | Why quantum computers threaten deployed cryptography, post-quantum candidates, standardisation, course outline | |
| 2 | — | [Symmetric-key encryption: basic ideas](course/lectures/02_symmetric-encryption-basics.pdf) | Classical ciphers, adversary models, semantic security, perfect secrecy and the one-time pad | |
| 3 | 16 Jan | [Stream ciphers](course/lectures/03_stream-ciphers.pdf) | Pseudo-random bit generators, RC4, WEP as a case study | |
| 4 | 18 Jan | [Block ciphers I](course/lectures/04_block-ciphers-des.pdf) | Feistel networks, DES, meet-in-the-middle attack, Triple-DES | |
| 5 | 23 Jan | [Block ciphers II](course/lectures/05_block-ciphers-aes-and-modes.pdf) | Substitution-permutation networks, AES, CBC and CTR modes | |
| 6 | 25 Jan | [Hash functions](course/lectures/06_hash-functions.pdf) | Security notions, generic attacks, the quantum setting, iterated constructions | |
| 7 | 30 Jan | [Message authentication codes](course/lectures/07_message-authentication-codes.pdf) | CBC-MAC, CMAC, NMAC and HMAC, authenticated encryption, quantum security of symmetric-key cryptography | |
| 8 | — | [Public-key cryptography: basic notions and key establishment](course/lectures/08_public-key-basics-and-key-establishment.pdf) | Key distribution, Merkle puzzles, Diffie–Hellman key agreement and its hardness assumptions | |
| 9 | 06 Feb | [Signatures from hash functions: basic concepts](course/lectures/09_signatures-from-hash-functions.pdf) | Signature definitions and EUF-CMA security, RSA and hashed RSA, first one-time signatures | |
| 10 | 08 Feb | [One-time signatures](course/lectures/10_one-time-signatures.pdf) | One-time signatures for arbitrary messages, security reduction, Winternitz | |
| 11 | 13 Feb | [Hash-based many-time signatures](course/lectures/11_hash-based-many-time-signatures.pdf) | Merkle trees, the Merkle signature scheme, XMSS, stateless signing | |
| 12 | 20 Feb | [Identification protocols](course/lectures/12_identification-protocols.pdf) | Challenge-response, mutual authentication, signature-based identification | |
| 13 | 22 Feb | [Identification to signature](course/lectures/13_identification-to-signature.pdf) | Proofs of knowledge, zero-knowledge, Schnorr identification and Schnorr signature | |
| 14 | 27 Feb | [Identification and signature from the MQ problem](course/lectures/14_mq-identification-and-signature.pdf) | The MQ problem, the Sakumoto–Shirai–Hiwatari identification scheme, Fiat–Shamir, MQDSS | [Manish Kumar](course/scribes/14_mq-identification-and-signature_manish-kumar/scribe.pdf) |
| 15 | 01 Mar | [Multivariate quadratic signatures](course/lectures/15_mq-signatures.pdf) | Isomorphism of polynomials, Oil and Vinegar, UOV, Rainbow | [Eleena Gupta](course/scribes/15_mq-signatures_eleena-gupta.pdf) |
| 16 | 08 Mar | [Code-based cryptography I](course/lectures/16_code-based-crypto-1.pdf) | Linear codes, syndrome decoding, McEliece, Niederreiter | [Ishan Pandey](course/scribes/16_code-based-crypto-1_ishan-pandey.pdf) |
| 17 | 20 Mar | [Code-based cryptography II](course/lectures/17_code-based-crypto-2.pdf) | Information-set decoding, attacks on textbook McEliece, key sizes | [Aman Tyagi](course/scribes/17_code-based-crypto-2_aman-tyagi.pdf) |
| 18 | 27 Mar | [Lattices: basic concepts](course/lectures/18_lattices-basic-concepts.pdf) | Bases, determinant, successive minima, hard lattice problems, GGH encryption and signature | [Prasanth Kumar A S](course/scribes/18_lattices-basic-concepts_prasanth-kumar-a-s.pdf) |
| 19 | 29 Mar | [Lattices: NTRU](course/lectures/19_lattices-ntru.pdf) | Polynomial rings, NTRUEncrypt, attacks, NTRU as a lattice problem | |
| 20 | 03 Apr | [Lattices: LWE](course/lectures/20_lattices-lwe.pdf) | Learning with errors, decision LWE, hardness, SIS, relation to SVP | [Swapnoneel Sarkar](course/scribes/20_lattices-lwe_swapnoneel-sarkar.pdf) |
| 21 | 05 Apr | [Encryption and signature from LWE](course/lectures/21_encryption-and-signatures-from-lwe.pdf) | Regev's encryption, IND-CPA proof, optimised Regev, signature from a Σ-protocol | |
| 22 | 10 Apr | [Secret sharing](course/lectures/22_secret-sharing.pdf) | Shamir's threshold scheme, general access structures, threshold cryptography | |

Lectures 2 and 8 have no date on their title slides.

## Assignments

- **A1, Cryptanalysis of RC4** (with Ishan Pandey): why the RC4 stream cipher is broken. Slides and notebooks are in [`course/assignments/a1_rc4-cryptanalysis/`](course/assignments/a1_rc4-cryptanalysis).
- **A2, Grover meets Simon** (with Ishan Pandey): a presentation of Leander and May's quantum attack on the FX construction. Slides are in [`course/assignments/a2_grover-meets-simon/`](course/assignments/a2_grover-meets-simon).
- **Scribe exercises:** my solutions to exercises set in six of the lectures, in [`scribe-exercises_manish-kumar.pdf`](course/assignments/scribe-exercises_manish-kumar.pdf).

[`course/assignments/README.md`](course/assignments/README.md) describes each one.

## Conventions

- File and folder names are lowercase, hyphenated and free of spaces.
- Lectures and scribes carry the lecture number as a prefix, so `16_…` in `scribes/` goes with `16_…` in `lectures/`.
- Papers and external slides are named `author-year_short-title.pdf`.
- Books are linked from [`references/README.md`](references/README.md), not stored here.

## Licence and credits

This repository mixes my own work with material that belongs to other people, so no single licence covers everything in it.

- **My own writing** is licensed under [CC BY 4.0](LICENSE): the lecture-14 scribe and its LaTeX source, the scribe exercises, the notes and the README files. You may reuse and adapt it as long as you give credit.
- **Code I write on my own** is licensed under the [MIT licence](LICENSE-CODE). At present all the code here is joint or third-party work, listed below.
- **Joint work** is shared with my co-authors' agreement and is not covered by the two licences above: the A1 and A2 slides and the RC4 notebooks, written with Ishan Pandey, and the Sage scripts in `projects/lattice/`, which we wrote together in class during the lattice lectures.
- **Course material** by Dr. Sanjit Chatterjee and Dr. Tapas Pandit (the lecture slides and the class test) is shared with the instructors' permission and remains theirs.
- **Classmates' work** is shared with each author's consent and remains theirs: the scribes by Eleena Gupta, Ishan Pandey, Aman Tyagi, Prasanth Kumar A S and Swapnoneel Sarkar, and the paper summary by Rajiv Sangle.
- **Third-party material** remains the property of its authors and publishers: Tanja Lange's slides and code, and the published papers and conference slides in `references/`. Sources are listed in [`references/README.md`](references/README.md).
