
.. _chapter-references:

References
==========

.. note::

   References are listed below in the format used by the template. Entries
   marked *normative* are required to implement the mechanisms discussed in
   this document; entries marked *informative* are cited for context. Where a
   cited work has been superseded or has advanced in status since this document
   was drafted, the current citation is given so that readers resolve to the
   published text.

Normative references
--------------------

[RATS-Architecture]
    IETF RFC 9334, *Remote ATtestation procedureS (RATS) Architecture*,
    H. Birkholz, D. Thaler, M. Richardson, N. Smith, January 2023.

    https://datatracker.ietf.org/doc/html/rfc9334

[EAT]
    IETF RFC 9711, *The Entity Attestation Token (EAT)*, L. Lundblade,
    G. Mandyam, J. O'Donoghue, C. Wallace, April 2025.

    https://datatracker.ietf.org/doc/html/rfc9711

[TCG]
    Trusted Computing Group, *specifications*.

    https://trustedcomputinggroup.org/

Informative references
----------------------

[CT-v2]
    IETF RFC 9162, *Certificate Transparency Version 2.0*, B. Laurie,
    E. Messeri, R. Stradling, December 2021.

    https://datatracker.ietf.org/doc/html/rfc9162

[VC-DATA-MODEL]
    W3C, *Verifiable Credentials Data Model*, W3C Recommendation.

    https://www.w3.org/TR/vc-data-model/

Note on resolution and persistence
----------------------------------

Two properties are worth recording for this chapter, because they affect
whether a citation remains checkable over the life of the document.

First, the reference to Entity Attestation Token above cites the published RFC
rather than the earlier draft. The draft identifier had been used in the
chapter skeleton; the published identifier is given here so that the citation
does not decay. This is consistent with the correction proposed separately in
this repository.

Second, where this document cites a specific claim about a mechanism, the
citation should resolve to a **stable, independently retrievable** target — a
published RFC, a standing specification, or a persistent identifier. Citations
that resolve only to a working draft, an ephemeral URL, or a timestamping
assertion of disputed validity do not satisfy this requirement and should not
be relied on as evidence. Reviewers are asked to flag any citation in this
document that does not meet this condition.
