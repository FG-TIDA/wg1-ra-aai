
.. _chapter-landscape:

RA Landscape: Industry Analysis
===============================

.. note::

   This chapter surveys the remote attestation (RA) landscape as it relates to
   AI agents. It is offered as material for discussion, not as a settled
   position. Claims are separated into those that hold across sectors and
   jurisdictions and those that are specific to an anchor instance, so that the
   general reading can be checked independently of the example.

Reading the landscape along three axes
--------------------------------------

A survey of this area is only useful if the reader can see which part of a
claim is general and which part is local. Three axes make that separation
checkable:

- **Actor axis** — who produces evidence, who consumes it, and who operates the
  infrastructure both depend on.
- **Sector axis** — in which domain the consequential action takes place, and
  what that domain's regulatory regime requires of the party acting on it.
- **Jurisdiction axis** — under which regime the appraisal of that evidence is
  performed, and which regime recognises the result.

The same technical mechanism can sit at different points on each axis. The
axes are introduced here so that the chapters that follow can state a
requirement in general form and then note where it is anchored.

Market & Actors Map
-------------------

Three groups are distinguishable, and they are not symmetric in maturity.

**Evidence producers.** Platform and silicon vendors, agent runtimes, model
serving stacks, and orchestration layers. This group is well represented in
existing work: the mechanisms for producing a well-formed attestation — a
hardware root of trust, a device or workload quote, a signed manifest — are
specified in detail and implemented at scale for non-agent software.

**Evidence consumers.** The relying parties that must decide whether to accept
an agent's evidence before acting on it: regulated enterprises, workflow
orchestrators acting on behalf of them, auditors, and supervisory bodies. This
group is thinner in the standards record. Its obligations are typically implied
by a compliance regime rather than expressed as a verification profile.

**Infrastructure actors.** Providers of trust anchors, transparency logs,
archival services, and time-stamping. These make third-party re-verification
possible; whether a given appraisal can be recomputed without trusting the
producer depends on which of them is in the path.

The asymmetry worth recording is between the first and second groups. Producer
side evidence has converged on interoperable formats; consumer-side acceptance
criteria have not, and where they are written down at all they tend to be
organisation-local.

RA Ecosystem
------------

Existing deployments of remote attestation follow a recognisable shape: a root
of trust at the device or platform layer, a chain of measurements that carries
that root up to a workload, and an appraisal step performed by whoever is about
to rely on the workload. The pattern is well established for static machine
identities and long-lived services.

Two properties of that pattern change when the attested entity is an agent.
First, the behaviour-determining surface extends beyond the measured artefacts
into configuration, retrieved context, and the state actually exercised at the
moment of action; a measurement chain that terminates at the artefact therefore
covers only part of what determines behaviour. Second, an agent commonly acts
as a delegate of a principal, and may itself delegate further; the appraisal
question is then not only "what is this entity" but "under which authority is
it acting, and does that authority reach this action".

Neither property is a failure of the existing primitives. Both fall at the
seam between the party that generates evidence and the party that consumes it.

Deployment contexts across sectors
----------------------------------

The requirement to act on agent evidence appears in sectors that share little
else. Grouped by the kind of decision being made rather than by industry label:

- **Regulated product and process domains** — healthcare and medical devices,
  pharmaceuticals, food safety. Consequential actions are gated by a regime
  that specifies what must be recorded and retained; a wrong acceptance can
  propagate into a regulated artefact.
- **Financial and payments** — authorisation, settlement, and reporting flows
  where an irreversible transfer or filing follows directly from an appraisal.
- **Energy and utilities** — operational control actions where the
  consequences of an accepted-but-invalid command are physical.
- **Transport and automotive** — safety-relevant actuation, and the
  type-approval and in-service regimes that surround it.
- **Public administration and cross-border services** — benefit, identity, and
  entitlement decisions that are later audited by a different body than the one
  that made them.
- **Enterprise IT and software supply chains** — build, deploy, and change
  gates, where the regime is contractual or sectoral rather than statutory.

What these contexts have in common is a point at which an appraisal feeds an
**action whose effects cannot be recalled** — a release into a regulated
process, a transfer, a command, a filing. What differs is where the obligation
on the verifying party comes from, how long the evidence must remain
re-verifiable, and who is entitled to challenge the decision afterwards.

That combination — a common decision shape with divergent local obligations —
is the reason the chapter keeps the general claim separate from its anchor
instance. A requirement stated only for a single sector is not transferable;
one stated in general form can be instantiated per sector by a profile.

Jurisdictional variation
------------------------

The jurisdiction axis is orthogonal to the sector axis, and the two are often
conflated. A sector requirement may be set at one level and recognised at
another. Three patterns recur, and it is useful to name them without attaching
them to any particular instrument:

- **Requirement set and enforced in the same jurisdiction** — the simplest
  case; the verification obligation and the recognising authority coincide.
- **Requirement set locally, evidence consumed across a boundary** — a
  supplier verifies at the point of production in one regime, while the party
  relying on the result sits in another. The question becomes whether the
  local verdict is reusable, re-interpretable, or has to be repeated.
- **Requirement set regionally, implemented nationally** — a common framework
  is adopted into different national instruments, so that an appraisal
  sufficient for one adopting country is not automatically sufficient for
  another.

These patterns point to a design constraint rather than a defect to be
resolved once: the verifiable core of a mechanism is best kept neutral with
respect to any single regime, with regime-specific obligations added as a
declared layer. Where a document embeds one regime's requirements into the
mechanism itself, reuse across the other two patterns becomes harder.

What the landscape does not yet contain
---------------------------------------

Measured against the three axes, the record is uneven.

- On the **actor axis**, producer-side work is mature and consumer-side work
  is under-specified; the obligations of the verifying party are rarely
  expressed as checks a reader could evaluate one by one.
- On the **sector axis**, deployments exist but the cross-sector common shape
  is not written down, so each sector re-derives its requirements in isolation.
- On the **jurisdiction axis**, the question of when a verdict obtained under
  one regime can be relied on under another is raised in several places but
  not answered in a form a verifier could apply.

The chapters that follow state where the gaps are and what would have to be
fixed for the existing building blocks to be usable at a decision point. This
chapter does not propose a mechanism; it records the shape of the field against
which the requirements in the following chapters should be read.
