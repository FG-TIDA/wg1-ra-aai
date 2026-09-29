
.. _chapter-core-challenges:

RA Core Challenges
==================

.. note::

   This chapter describes the core challenges of remote attestation for AI
   agents. The challenges are stated at the level at which they block
   convergence — that is, where reasonable implementers currently have no
   shared answer — rather than as a catalogue of technical obstacles. They are
   deliberately expressed independently of any particular cryptographic
   mechanism.

C1. The attested object is not a single thing
---------------------------------------------

For conventional software, "attest this" has a reasonably stable referent: an
artefact, a build, a running image. For an agent the candidate objects are
several, they have different lifetimes, and they cannot all be covered at equal
strength by one attestation:

- the agent **type** or deployment (stable across executions);
- the **code and configuration** that bound what it can do;
- the **model artefact** actually loaded, where the agent is model-driven;
- the **runtime state** actually exercised (which may differ from load state);
- **behaviour observed** during the action (what it did, as distinct from what
  it was able to do).

The difficulty is not that these are hard to attest individually. It
is that a profile written for one of them does not compose with a profile
written for another, and a relying party facing a mixed set has no basis for
deciding what the combination establishes.

C2. Probabilistic behaviour does not support static claims
----------------------------------------------------------

Attestation practice is built on the claim "this artefact is what it says it
is". For a system whose behaviour is probabilistic, that claim is necessary but
insufficient for a consequential decision: it constrains what the system *could*
do, not what *this* execution is about to do. The distinction that matters at
the point of reliance is between the **type claim** and the **instance claim**,
and current profiles do not consistently separate them.

C3. The consumption side has no shared vocabulary
-------------------------------------------------

The producer side has a settled vocabulary (roots of trust, endorsement,
appraisal, evidence, attestation results). The consumer side does not. There is
no agreement on what a relying party's minimum check set is, so each
deployment re-derives it, and evidence from two conforming implementations is
not mutually comparable at a decision point.

C4. The outcome of a failed or absent check is undefined
--------------------------------------------------------

Profiles generally specify what happens when verification succeeds. They
generally do not specify the required behaviour when a check is skipped,
defaults, short-circuits, errors out, or evaluates an empty set. Where the
default is left to the implementation, it is commonly to proceed. A profile
cannot state "on failure class X, behaviour must be Y" until the failure
classes have been enumerated, and that enumeration is currently incomplete.

C5. Delegation chains are carried asymmetrically
------------------------------------------------

When agents act through other agents, the authority under which the final
action occurred is a property of the chain, not of the final node. Evidence
tends to be presented by, and about, the final node. The challenge is to define
what has to be carried forward at each hop — and what has to remain verifiable
at the end — without requiring every intermediate party to disclose more than
its role in the chain.

C6. Freshness and replay have no agent-level expression
-------------------------------------------------------

There is no widely adopted vocabulary for expressing "this evidence is valid
for this action and no other". Continuous operation makes the problem sharper
than in one-shot attestation: evidence that was correct at one decision point
remains well-formed at the next, and nothing in its form distinguishes the two
uses.

C7. Auditability and disclosure pull in opposite directions
-----------------------------------------------------------

Evidence sufficient to audit an action is usually evidence sufficient to
profile the principal, the agent, and their relationship. Strengthening the
evidence improves accountability and worsens disclosure. Resolving this
requires formats that let a consumer establish a required property without
receiving the underlying values — a property that most current evidence
structures do not carry.

C8. Heterogeneous evidence has no common minimum
------------------------------------------------

Different attestation families imply different acceptance procedures, different
failure semantics, and different assumptions about the verifier's environment.
A relying party that must accept evidence from several families has no common
floor to apply, so its acceptance decision is a local, undocumented engineering
choice rather than a conformance question.

Relationship between the challenges
-----------------------------------

C3, C4, and C8 are properties of the **profile layer** and are, in principle,
addressable by agreement rather than by new mechanism. C1, C2, C5, and C6
require vocabulary that does not yet exist. C7 constrains what any of the
others may require, because every additional checkable claim is also an
additional disclosure. A profile that addresses C3/C4/C8 without regard to C7
would resolve the consumer-side gap by increasing the privacy cost, which
trades one problem for another.
