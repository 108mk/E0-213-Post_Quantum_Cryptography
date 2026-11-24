# Notes

A topic-by-topic knowledge base for post-quantum cryptography, meant for looking a concept up quickly.

It starts as a map from each family of schemes to the course material that covers it. Notes written after the course go in one folder per family, next to this file.

## Topic map

Numbers in the Lectures and Scribes columns link to the lecture slides and to the scribe for that lecture.

| Topic | Lectures | Scribes | Code and assignments | Papers and talks |
|---|---|---|---|---|
| Symmetric-key cryptography | [2](../course/lectures/02_symmetric-encryption-basics.pdf), [3](../course/lectures/03_stream-ciphers.pdf), [4](../course/lectures/04_block-ciphers-des.pdf), [5](../course/lectures/05_block-ciphers-aes-and-modes.pdf), [6](../course/lectures/06_hash-functions.pdf), [7](../course/lectures/07_message-authentication-codes.pdf) | | [A1: RC4 cryptanalysis](../course/assignments/a1_rc4-cryptanalysis) | [AlFardan et al. 2013](../references/slides/alfardan-et-al-2013_rc4-in-tls.pdf) |
| Quantum attacks on symmetric schemes | [1](../course/lectures/01_introduction.pdf), [6](../course/lectures/06_hash-functions.pdf), [7](../course/lectures/07_message-authentication-codes.pdf) | | [A2: Grover meets Simon](../course/assignments/a2_grover-meets-simon) | [Leander and May 2017](../references/papers/leander-may-2017_grover-meets-simon.pdf), [Zhu et al. 2023](../references/papers/zhu-et-al-2023_feasibility-of-grover-meets-simon.pdf) |
| Public-key foundations, identification, Fiat–Shamir | [8](../course/lectures/08_public-key-basics-and-key-establishment.pdf), [12](../course/lectures/12_identification-protocols.pdf), [13](../course/lectures/13_identification-to-signature.pdf) | | [Scribe exercises](../course/assignments/scribe-exercises_manish-kumar.pdf) | |
| Hash-based signatures | [9](../course/lectures/09_signatures-from-hash-functions.pdf), [10](../course/lectures/10_one-time-signatures.pdf), [11](../course/lectures/11_hash-based-many-time-signatures.pdf) | | [`hash-based-signatures/`](../projects/hash-based-signatures), [class test problem 1](../course/exams/class-test-1_problem-1.jpeg) | |
| Multivariate cryptography | [14](../course/lectures/14_mq-identification-and-signature.pdf), [15](../course/lectures/15_mq-signatures.pdf) | [14](../course/scribes/14_mq-identification-and-signature_manish-kumar/scribe.pdf), [15](../course/scribes/15_mq-signatures_eleena-gupta.pdf) | [Class test problem 2](../course/exams/class-test-1_problem-2.jpeg) | [Sakumoto et al. 2011](../references/papers/sakumoto-shirai-hiwatari-2011_mq-identification-schemes.pdf), [Chen et al. 2016](../references/papers/chen-et-al-2016_5-pass-mq-identification-to-signatures.pdf), [MQDSS talk 2019](../references/slides/chen-et-al-2019_mqdss-nist-round-2.pdf) |
| Code-based cryptography | [16](../course/lectures/16_code-based-crypto-1.pdf), [17](../course/lectures/17_code-based-crypto-2.pdf) | [16](../course/scribes/16_code-based-crypto-1_ishan-pandey.pdf), [17](../course/scribes/17_code-based-crypto-2_aman-tyagi.pdf) | [Scribe exercises](../course/assignments/scribe-exercises_manish-kumar.pdf) | Lange's slides, parts [I](../references/slides/lange_code-based-crypto-1_mceliece.pdf), [II](../references/slides/lange_code-based-crypto-2_niederreiter.pdf), [III](../references/slides/lange_code-based-crypto-3_goppa-codes.pdf), [V](../references/slides/lange_code-based-crypto-5_information-set-decoding.pdf), [VI](../references/slides/lange_code-based-crypto-6_quantum-isd.pdf) |
| Lattice-based cryptography | [18](../course/lectures/18_lattices-basic-concepts.pdf), [19](../course/lectures/19_lattices-ntru.pdf), [20](../course/lectures/20_lattices-lwe.pdf), [21](../course/lectures/21_encryption-and-signatures-from-lwe.pdf) | [18](../course/scribes/18_lattices-basic-concepts_prasanth-kumar-a-s.pdf), [20](../course/scribes/20_lattices-lwe_swapnoneel-sarkar.pdf) | [`lattice/`](../projects/lattice), [scribe exercises](../course/assignments/scribe-exercises_manish-kumar.pdf) | |
| Secret sharing | [22](../course/lectures/22_secret-sharing.pdf) | | [Scribe exercises](../course/assignments/scribe-exercises_manish-kumar.pdf) | |
| Isogeny-based cryptography | Not covered in the course | | | |

## Adding a note

1. Write one note per concept or scheme, and keep it short enough to reread in a few minutes.
2. Put it in a folder named after its family, for example `notes/lattice/regev-encryption.md`. Create the folder when the first note needs it.
3. Start from [`_template.md`](_template.md), so every note answers the same questions in the same order.
4. Write maths in LaTeX between `$…$` or `$$…$$`. GitHub renders it in Markdown.
5. Link back to the lecture, scribe, code and paper the note draws on, and add the note to the topic map above.

## Gaps worth filling first

- **Standardisation status.** The course ended in April 2023. Since then NIST has published [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) (ML-KEM), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) (ML-DSA) and [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) (SLH-DSA) in August 2024, selected HQC in March 2025, and is running a separate process for [additional signature schemes](https://csrc.nist.gov/projects/pqc-dig-sig).
- **What became of the schemes in the lectures.** One status note each for MQDSS, UOV, Rainbow, McEliece, NTRU and the LWE-based schemes.
- **Isogeny-based cryptography,** which the course did not cover.
- **A size cheat sheet** comparing key, ciphertext and signature sizes across families.
