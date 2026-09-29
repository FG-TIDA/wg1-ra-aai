
.. _chapter-building-blocks:

Standards' Existing Building Blocks
===================================

.. note::

   This chapter surveys the standards that can serve as building blocks for
   AI-agent remote attestation, and records where each of them stops with
   respect to the decision a relying party has to make. It is offered as
   material for discussion, not as a settled position. The survey is written
   to be readable without the reader having to consult each source: what is
   cited is what the cited work provides, and what it does not.

IETF Landscape and Mapping to Agent RA
--------------------------------------

**RATS architecture.** The IETF Remote ATtestation procedureS architecture
provides the reference model for this area: it separates the roles of
attester, verifier, relying party, and endorsement, and it distinguishes the
evidence a system produces from the appraisal performed on it. This separation
is the reason the present document can speak of a consumer-side gap at all —
the architecture anticipates a relying party, but it does not specify the
party's obligations.

Where it stops for agent RA: the architecture defines the roles and the
information flows between them. It does not say what a relying party must
require of an appraisal before acting, nor what the correct behaviour is when
a required input to that appraisal is missing. This is the gap chapter 02
states and chapter 03 breaks down.

**Entity Attestation Token.** The Entity Attestation Token defines a claim
container together with a set of registered claims. It solves the question of
how attestation results are carried, and it is deliberately agnostic about
which claims a given consumer needs.

Where it stops for agent RA: a container that can carry a claim does not
establish that the claim was present, checked, and found acceptable. The
consumer-side question — which claims are mandatory for a stated action, and
what an absent claim means — is outside the scope of the token definition.

**Transparency and freshness.** Certificate Transparency and the broader
family of append-only logs supply the property that a record, once made, can
be shown to have existed and to be unaltered. This is the mechanism that makes
an appraisal reproducible by a third party who was not present at the
decision.

Where it stops for agent RA: availability of a log says nothing about which
appraisals are required to be logged, what the log entry must contain for the
appraisal to be recomputable, or for how long the entry must remain
retrievable.

TCG Landscape and Mapping to Agent RA
-------------------------------------

**Roots of measurement.** The Trusted Computing Group's work supplies the
hardware-backed root of measurement on which most deployed attestation chains
rest, together with layered approaches that build a device identity out of
successively measured components.

Where it stops for agent RA: the measured object is a component identity. For
an agent, the behaviour-determining surface is wider than the measured
artefacts — configuration, retrieved context, and exercised state are not
components with stable identities. Extending measurement to that surface is an
open problem, not a solved one, and it is one of the reasons the consumer-side
requirement has to be stated in terms of evidence boundaries rather than in
terms of full coverage.

**Reference integrity.** Reference-integrity mechanisms supply the mapping
from a measurement to a statement of what a measurement is supposed to be,
which is the input an appraisal needs in order to return anything other than a
bare digest.

Where it stops for agent RA: the reference set describes what the producer
intended to ship. It does not describe which differences from that reference
are tolerable for a stated action, and tolerability is a property of the
decision being made, not of the measurement.

Other bodies whose work bounds this area
----------------------------------------

The blocks above are not the only relevant ones, and the boundaries between
them matter for the same reason.

- **Credential and identifier frameworks** (W3C Verifiable Credentials, the
  X.509 family, national identity-code specifications) define how an
  identifier or a claim is encoded and presented. They are the layer below
  this document's subject: encoding a claim is not the same as verifying that
  the claim was checked.
- **Control-objective frameworks** (sectoral and cross-sectoral risk
  management guidance) state what an organisation should govern. They supply
  the objectives an appraisal serves without defining an evidence format a
  third party could recompute.
- **Conformity regimes** (product-safety and market-access instruments in
  different jurisdictions) state what must be demonstrated before an artefact
  may be placed on a market. They are a source of consumer-side requirements,
  not a specification of the verifying party's checks.
- **Telecommunication identity and trust work** supplies interoperable
  identity and trust frameworks of long standing, together with the regulatory
  habit of stating requirements so that they survive across adopting
  jurisdictions.

Mapping summary
---------------

The table records, for each block, what it contributes and where it stops for
the decision this document is concerned with.

.. list-table::
    :header-rows: 1
    :widths: 26 34 40

    * - Building block
      - What it provides
      - Where it stops for agent RA
    * - RATS architecture
      - Roles, evidence/appraisal separation, information flow
      - Relying-party obligations left unspecified
    * - Entity Attestation Token
      - Claim container and registered claims
      - Which claims are mandatory for an action; meaning of absence
    * - Transparency logs
      - Existence and integrity of a record
      - What must be logged for an appraisal to be recomputable
    * - Roots of measurement
      - Hardware-backed chain to a component identity
      - Measurement of a behaviour-determining surface wider than components
    * - Reference integrity
      - Measurement-to-intent mapping
      - Which deviations are tolerable for a stated action
    * - Credential frameworks
      - Encoding and presentation of identifiers and claims
      - Verification obligations (a layer above encoding)
    * - Control-objective frameworks
      - Governance objectives to be served
      - An evidence format a third party can recompute
    * - Conformity regimes
      - What must be demonstrated before market access
      - The checks a verifier must perform, stated individually

Design implication
------------------

Read as a set, the blocks cover the generation and carriage of evidence well,
and leave the consumption of it thinly specified. Two consequences follow, and
they shape the requirements in the remaining chapters.

First, the work is **composition rather than invention**. Each block already
provides something the decision needs; the gap is at the boundaries between
them, where one block's output is another's assumed input and no document
states who checks the join.

Second, the composition should be arranged so that a **neutral core** is kept
separate from **declared local layers**. A block whose scope is defined by one
regime's instrument cannot be reused as-is by a party operating under another,
whereas a neutral core with a declared profile can be instantiated per sector
and per jurisdiction without being rewritten. This is the basis on which the
cross-jurisdiction question in chapter 03 is posed.

Where a mechanism is cited in this document, the citation is expected to
resolve to a stable, independently retrievable target rather than to a working
draft or an ephemeral reference; the reference list records this expectation
and invites reviewers to flag entries that do not meet it.
