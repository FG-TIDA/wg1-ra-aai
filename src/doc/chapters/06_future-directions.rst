
.. _chapter-future-directions:

Future Directions
=================

.. note::

   This chapter outlines directions the group may wish to pursue: recommended
   next steps, candidate work items, and the areas where new vocabulary is
   needed before standardisation is possible. Items are ordered by how much
   prior agreement they require, from least to most.

D1. A consumption-side profile (lowest dependency)
--------------------------------------------------

The gap identified in the preceding chapters is a profile gap. A companion
profile that fixes, per decision point, what a relying party must check and
what the outcome must be when a required check cannot be completed is
achievable with mechanisms already in use. It requires no new cryptography, and
it can be drafted against existing building blocks. This is the highest-value
next step and the one with the fewest open dependencies.

D2. An enumerated set of failure classes
----------------------------------------

A profile cannot state required behaviour per failure class until the classes
are named. An enumerated, reproducible set of failure modes — including the
cases in which a check reports success while having examined nothing — is a
prerequisite for D1 rather than a parallel activity. This set is best assembled
by collecting cases that independent implementations can reproduce, so that the
enumeration is grounded in observed behaviour rather than in taxonomy.

D3. A layered identifier convention
-----------------------------------

The distinction between agent type, agent instance, and the authority under
which an instance acted recurs in every chapter above. A convention that lets a
relying party cache the first and re-check the second, and that says which one
a given decision depends on, would remove a recurring source of ambiguity. This
chapter does not propose such a convention; it records the need for one.

D4. Shared vocabulary for freshness and scope
---------------------------------------------

Express "this evidence is valid for this action and no other" in a way that is
checkable by the consumer and independent of the production mechanism. A shared
vocabulary here would make evidence from different families comparable at a
decision point, which C8 currently prevents.

D5. Evidence formats that support selective disclosure
------------------------------------------------------

Formats in which a consumer can establish a required property without receiving
the underlying values, so that additional auditability does not impose
proportional additional disclosure. Without progress here, each new checkable
claim carries a privacy cost, which limits how far D1 can go.

D6. Offline re-verifiability as a design objective
--------------------------------------------------

Where evidence is anchored to public, independent infrastructure — a
transparency log entry, a persistent archive identifier — a third party can
re-derive the expected result without contacting the producer. Treating
independent re-verifiability as an objective, rather than as a side effect,
makes it possible to state conformance in terms that a party outside the
deployment can check.

D7. A worked reference profile, applied to one instance of the problem
----------------------------------------------------------------------

The abstract questions above become concrete when applied to a single domain
with an existing obligation to justify decisions. A reference profile
instantiated against one such domain — stating, for that case, which claims are
required, which failure classes apply, and what the default outcome is — would
give the group something falsifiable to converge on and would expose
inconsistencies that abstract discussion does not.

Suggested next steps
--------------------

1. Assemble the failure-class enumeration (D2) as a prerequisite input, with
   reproducible cases contributed by more than one participant.
2. Draft the consumption-side profile (D1) against existing building blocks,
   stating explicitly which failure classes it covers and which remain open.
3. Record, rather than resolve, the vocabulary gaps (D3, D4) as a list of
   terms for which no shared definition yet exists.
4. Identify, for D5 and D6, which existing mechanisms already satisfy the
   requirement and which do not, so that future work targets the remainder.
