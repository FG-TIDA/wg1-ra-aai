
.. _chapter-three-questions:

Three Fundamental Questions
===========================

.. note::

   This chapter is structured around three questions: *what* should be
   attested for an AI agent, *how* an attestation should be produced and
   consumed, and *when* it should be produced. The text below frames each
   question from the position of the party that must **act on** an
   attestation — the relying party — because the consumption side is where
   agent attestation currently has the least shared vocabulary. The
   contributions below are offered as material for discussion, not as
   settled positions.

What to Attest?
---------------

An attestation is only useful if the party receiving it can determine what
claim it is entitled to draw from it. For AI agents, the candidate objects of
attestation are not mutually exclusive, and they are not equivalent in
strength:

- **The agent type or deployment.** Which agent implementation, build, or
  deployment is this — independent of any particular execution.

- **Code and configuration.** The instructions and settings that determine
  what the agent can do, and under which limits.

- **Model and weights.** The model artefact actually loaded, where the agent
  is model-driven.

- **Runtime state actually exercised.** The state, context and reachable
  tool surface at the moment of the action, which may differ from the state
  at load.

- **Behaviour observed during operation.** What the agent actually did, as
  distinct from what it is capable of doing.

- **The authored policy set.** The identity and version of the rules the
  agent's actions are evaluated against, and the authority under which those
  rules were authored. Behaviour is only meaningful against a reference, so the
  reference is itself a candidate object of attestation. It changes
  independently of code, model and runtime state; the timing side of that
  independence is the *At policy change* trigger in *When to Attest?* below.

The difficulty is that these objects have different lifetimes and different
verification costs, and a single attestation cannot carry all of them at
equal strength. The distinction that matters at the point of reliance is
between a **static claim** ("this artefact is what it says it is") and an
**instance claim** ("*this* execution, with *this* state, acted under *this*
authority"). For agents whose behaviour is probabilistic, a static claim
alone does not support a consequential decision.

One way to answer it is to separate three things that are often
conflated in a single identifier: the identifier of the agent *type*, the
identifier of the *instance*, and the statement of *authority* under which the
instance acted. Regimes in other regulated domains separate a type-level
identifier from an instance- or production-level identifier for exactly this
reason, and the separation is what allows a consumer to cache the first and
must re-check the second.

A **conformance verdict** is a behavioural form of the instance claim: the
result of evaluating one specific action against the authored policy set. It
is a claim by the engine that issued it, so it should carry the identity of
that engine. Carrying the issuer is necessary for the verdict to stand as an
instance claim, but it is not sufficient on its own. A verdict should also be
**re-derivable** by the relying party from the evidence package. If only the
issuing engine can recompute the verdict, the claim rests on a producer-side
computation that the *Offline re-verifiability* requirement in *How to
Attest?* rules out.

A verdict is more usable when it is drawn from a small closed vocabulary than
when it is free text, because a closed set can be compared across
heterogeneous evidence. One such set is the vocabulary stated in the themes
discussion on intent-based security policies (issue 6) — *permit*,
*remediate*, *block*, *escalate*, *indeterminate*. Which terms a particular
profile adopts is a matter for that profile; what matters here is that the
terms are fixed and shared, rather than chosen by each producer.

One distinction is worth keeping: a verifier's *no-assertion* result is
evidence-side, while an *indeterminate* verdict is action-side. The two
should not be read as the same state.

How to Attest?
--------------

For agentic AI, the binding constraint is **not the generation of an
attestation but its consumption**. An attestation produced by any mechanism
(a hardware quote, a trusted-execution report, a signed manifest) still has to
be *accepted* by a relying party that did not run the attestation itself.
Three properties must be established at the point of consumption, and each is
independently failable:

1. **Binding** — the evidence is bound to *this* agent instance, for *this*
   action, and not merely to a binary, an image, or a logical identity. Where
   behaviour is probabilistic, binding to a static artefact is insufficient;
   the evidence must reference the runtime state actually exercised.

2. **Freshness** — the evidence is not a replay. A valid attestation from an
   earlier session must not be accepted for a later action. This requires an
   explicit, verifiable notion of *when* the evidence was produced relative to
   the action (see *When to Attest?* below).

3. **Offline re-verifiability** — the relying party can re-derive the verdict
   from the evidence package alone, without requiring the producer's
   infrastructure to be online, and without having to trust a verdict that
   only the producer is able to compute.

**How the three can be met together.** They are not in tension with one
another, and a single construction can carry all of them. Such a construction
moves away from one opaque attestation and towards a *verifiable evidence
package*: the evidence supporting an action is sealed under a digest, the
digest is published to a public transparency log so that its existence at a
given point in time can be checked by anyone, and the package is archived
under a persistent identifier so that its contents can be confirmed unmodified
after release. A relying party can then re-compute the package digest, look up
the log entry, and confirm the archive anchor — all of it offline, without
contacting the producer, and without having to trust a verdict that only the
producer is able to compute.

A construction of this kind is a proposal rather than a formal standard, and it
should scope its results accordingly: a pass means that no violation was found
within the observed evidence boundary, not that trustworthiness is asserted in
general. That scoping is part of the contribution. A verifier-side artefact
that does not state the limits of its own verdict is itself an instance of the
problem this chapter examines.

The shape is described here not as a mechanism proposed for adoption in this
chapter, but to record that the three properties above are jointly achievable
using existing, general-purpose building blocks.

**A minimal verifier-side checklist (proposed, for discussion).** For evidence
claiming to support a consequential agent action, a relying party should be
able to answer, from the package alone:

- Does the evidence bind to the specific agent instance *and* the specific
  action?
- Is the freshness window explicit, and is the evidence inside it?
- Can the verdict be re-derived without contacting the producer?
- If verification of any of the above cannot be completed, is the default
  outcome to **deny** the action rather than to allow it?

The last point is where current practice appears weakest. "The check silently
passed because nothing was actually checked" is a recurring failure mode in
automated verification generally, and — to the best of the author's knowledge —
it is not yet enumerated for agent attestation. A catalogue of such cases —
verification steps that report success while checking nothing — would be a
modest but concrete contribution to this chapter, because failure semantics
cannot be specified before the failure modes are enumerated. Entries in such a
catalogue are worth recording in plain form: what happened, the root cause, and
the change that addressed it, so that others can extend the record with their
own cases.

Two instances are worth naming, because both were found by running a test
corpus rather than by review. In the first, a comparison silently collapsed two
distinct items into one before comparing them, and the check reported that
nothing had been altered. In the second, a conformance check scored a pass on
an empty input, because every assertion it made was vacuously true. Both belong
to the same class: the check ran, and it reported success while checking
nothing.

When to Attest?
---------------

Attestation timing for agents should be driven by **the moments at which the
authority boundary changes**, not by a fixed schedule. For a long-lived agent,
"attest at load" is insufficient: the agent's relevant state — its context,
its delegated authority, its reachable tools — changes during operation.

The trigger set can be expressed as *events*, each producing a fresh,
bound attestation:

- **At grant** — when authority is first conferred on the agent.
- **At (re)delegation** — when the agent hands a sub-task, and its authority,
  to another agent.
- **At consequential action** — immediately before an action that is
  irreversible or that crosses an organisational boundary.
- **At policy change** — when the rules the agent is subject to are
  themselves updated.

This aligns attestation with a **decision-point** semantics: the question at
each trigger is not "is the agent trustworthy in general" but "may *this*
action proceed *now*". The consequence is that an attestation is only
meaningful **relative to a decision point**, and a verifier should be able to
state which decision point it is satisfied about. Two consequences follow.
First, an attestation whose decision point cannot be named is not usable.
Second, the *default* behaviour when a required attestation is missing must be
stated per decision point, because silence is currently interpreted
inconsistently.

Research Gaps
-------------

- **Consumption-side requirements are unstandardised.** Existing attestation
  building blocks specify how evidence is *produced*; they do not specify what
  a *relying party* must check. A profile that fixes the verifier's
  obligations — and the default outcome when those obligations cannot be
  met — is missing.

- **Failure semantics are undefined.** Profiles should state, for each failure
  class, whether the required behaviour on failure is to deny or to allow, and
  how a "check did not run" outcome is distinguished from "check ran and
  passed".

- **Freshness and replay for continuously operating agents.** There is no
  widely adopted vocabulary for expressing "this evidence is valid for *this*
  action and no other" in an agent context.

- **Binding to instance state.** Research on binding evidence to the state
  actually exercised by a probabilistic system remains thin, relative to work
  on binding evidence to static artefacts.

Standardization Gaps
--------------------

- **No common verifier-side checklist.** Each attestation family implies its
  own acceptance procedure, so a relying party facing heterogeneous evidence
  has no shared minimum to apply.

- **No agreed treatment of "absence of evidence".** Whether a missing
  attestation blocks an action, permits it, or raises an exception is
  currently a local decision.

- **No layered identifier convention for agents.** Where a distinction between
  type-level and instance-level identification is needed, it is not yet
  expressed as a convention that a relying party can depend on. This chapter
  does not propose such a convention; it records its absence as a gap.

- **Timing triggers are not standardised.** "At load" versus "per action"
  versus "continuously" is treated as an implementation choice, so two
  conforming implementations can produce evidence that is not mutually
  comparable at a decision point.
