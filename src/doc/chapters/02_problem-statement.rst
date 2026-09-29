
.. _chapter-problem-statement:

Problem Statement
=================

.. note::

   This chapter states the problem the document addresses. It is written from
   the position of the party that has to **act on** an attestation — the
   relying party — because that is where the consequences of an unattested or
   partially attested action are realised. The text is offered as material for
   discussion, not as a settled position.

Security and Privacy Vulnerabilities of AI Agents and Agentic Networks
----------------------------------------------------------------------

An AI agent differs from the software artefacts that current remote
attestation practice was built around in three ways that are directly relevant
to what an attestation can establish.

**The behaviour-determining surface is larger than the code.** What an agent
does is determined jointly by model artefacts, code, configuration, retrieved
context, and the state actually exercised at the moment of action. Two
executions of the same signed artefact can behave differently. An attestation
that covers only the artefact therefore leaves the behaviour-determining
surface partly unattested.

**Agents compose other agents.** In agentic networks, an action at one node may
have been delegated through several others. Trust in the outcome depends on the
integrity of the delegation path, yet the evidence presented at the point of
action is often evidence about the final node only. Where the chain is not
carried, a consumer cannot distinguish "this agent was authorised" from "some
agent upstream of this one was authorised at some earlier time".

**Verification itself has a privacy cost.** Evidence that makes an action
auditable tends also to disclose the principal, the agent, the relationship
between them, the scope of delegated authority, and the fact of service use.
The stronger the evidence required, the more is disclosed to whoever collects
it. This creates a tension between auditability and disclosure that is not
resolved by adding more evidence.

The vulnerabilities that follow are not primarily failures of cryptography.
They are failures at the seam between the party producing evidence and the
party consuming it:

- **Producer-side completeness is not consumer-side sufficiency.** A
  well-formed, correctly signed attestation may still omit the one claim a
  given decision requires.
- **Default-permissive behaviour on missing evidence.** Where no requirement
  fixes the outcome of an incomplete check, the common implementation default
  is to proceed, so the absence of evidence is silently equivalent to a pass.
- **Unreproducible acceptance decisions.** Because each attestation family
  implies its own acceptance procedure, two parties can accept the same
  evidence for incompatible reasons, and neither can demonstrate why.

Core Problem
------------

The core problem is an **asymmetry between the production and the consumption
of agent evidence**.

The existing building blocks for remote attestation — hardware roots of trust
and device quotes, trusted-execution reports, signed manifests, transparency
logs — specify in detail how evidence is **generated** and what makes it
well-formed. They do not specify what a relying party must **check** when it
receives that evidence, nor what the correct outcome is when a required check
cannot be carried out.

The consequence is specific and observable:

   Evidence is accepted because nothing in the profile requires anyone to
   establish that the verification step examined anything at all.

This failure mode is not hypothetical. It takes recognisable shapes: a check
that is skipped for an environment that does not support it; a check that is
short-circuited once an earlier step fails; a check evaluated against an empty
set of inputs and reported as passed; a verification routine that returns
success because it could not construct the failing case. In each of these the
reported outcome is "verified".

Gap
---

The gap between what current remote attestation provides and what AI agents
require is therefore a **profile gap, not a capability gap**. The primitives
needed to bind an attestation to an action, to give it a validity window, and
to make it re-verifiable offline by a third party already exist and are in
general use. What is missing is an agreed statement of:

- **what a relying party must check**, expressed as individually evaluable
  checks rather than as a single verdict;
- **what the outcome must be** when a required check is missing, inconclusive,
  or cannot be performed — that is, whether the required behaviour for a given
  failure class is to deny or to permit;
- **how "the check did not run" is distinguished from "the check ran and
  passed"**, so that the two cannot be reported identically;
- **how freshness is expressed**, so that evidence valid for one action is not
  silently reused for another;
- **which identifier level** a given decision depends on — the agent type, the
  agent instance, or the authority under which the instance acted.

This document does not attempt to supply that profile. It records, per
chapter, where the gap is and what would have to be fixed for the building
blocks to be usable at a decision point.
