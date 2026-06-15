# Online Learning — AdaHedge

This project implements and compares the **Hedge algorithm with a fixed learning rate** and the **AdaHedge algorithm** introduced in:

Tim van Erven, Peter D. Grünwald, Wouter M. Koolen, Steven de Rooij (2011), *Adaptive Hedge*.

The setting is **prediction with expert advice**, where the learner combines a finite set of experts and aims to minimize regret with respect to the best expert in hindsight.

---

## Objective

Implement Hedge and AdaHedge, and compare their performance across different types of synthetic loss sequences. In particular, study how performance depends on the difficulty of the sequence.

---

## Experimental setup

Three regimes are considered:

- **Stochastic:** one expert has Bernoulli(0.3), others Bernoulli(0.5)
- **Adversarial:** the best expert changes over time
- **Low-gap:** best expert Bernoulli(0.49), others Bernoulli(0.5)

---

## Evaluation

- Cumulative loss
- Regret over time
- Comparison across different learning rates for Hedge

---

## Expected output

- Regret curves for all settings
- Comparison between Hedge and AdaHedge
- Identification of regimes where AdaHedge improves performance