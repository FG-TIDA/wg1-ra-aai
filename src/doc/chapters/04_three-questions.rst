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

**A worked, publicly checkable example.** In the course of other work on
evidence packages for automated systems, an evidence construction was built in
which a package is sealed with an evidence root, anchored to a public
transparency log (Sigstore Rekor [1]_, entry ``logIndex 2883389783``), and
archived with a persistent software identifier (Software Heritage SWHID [2]_).
A relying party can (a) re-compute the package digest, (b) look up the
transparency-log entry, and (c) confirm the archive anchor — all
without contacting the producer. A reference implementation is released under a
persistent DOI (https://doi.org/10.5281/zenodo.22821834), with the archive
digest published alongside it, so that a third party can confirm the artefact
was not altered after release. The released material includes a fixture set of
eight packages — one clean baseline and seven mutations, all within one
documented threat-model class — each carrying an expected per-check outcome
that is machine-compared against a hand-derived expectation matrix, so the
table cannot drift silently; and a second implementation of the verifier,
written from the specification rather than from the reference code, whose
verdicts agree with the reference on every fixture. A demonstration run
exercises both an accept path and a tamper-detection path.

The artefact describes itself as a proposal rather than a formal standard, and
scopes its results accordingly: a PASS means that no violation was found within
the observed evidence boundary, not that trustworthiness is asserted in
general. This is worth stating because the boundary is part of what is offered —
a verifier-side artefact that does not state the limits of its own verdict is
itself an instance of the problem this chapter examines.

This is offered not as a proposed mechanism for this chapter but as evidence
that the three properties above are achievable with existing, general-purpose
building blocks.

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
cannot be specified before the failure modes are enumerated. In the work cited
above, such a record has been started: it lists failures that occurred in
practice together with their root cause and the change that addressed them, in
a deliberately plain format, so that others can extend it with their own cases.

Two entries in that record were found by the test corpus rather than by
review: a migration whose target carried a duplicate identifier was collapsed
before comparison and still reported "no injections", and an empty migration
scored PASS on all four preservation checks. Both are corrected in the
development version that follows the one released under the DOI above; the
record of them is kept in the project's change log. They are offered as
concrete instances of the class — the check ran, and it reported success while
checking nothing.

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

This aligns attestation with a **gate** semantics: the question at each
trigger is not "is the agent trustworthy in general" but "may *this* action
proceed *now*". The consequence is that an attestation is only
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

.. [1] Sigstore Rekor — public transparency log for software artefacts.
   Overview: https://docs.sigstore.dev/logging/overview/
.. [2] Software Heritage persistent identifiers (SWHID), specified in
   ISO/IEC 18670. https://docs.softwareheritage.org/
