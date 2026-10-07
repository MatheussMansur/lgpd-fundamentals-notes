# Module 1 - Understanding LGPD

Lei 13.709/2018. In force since Aug 2020, sanctions only since Aug 2021.
Applies to any processing by a person or company (public or private), not only digital
("inclusive nos meios digitais").

Note from the course: MP 1.317/2025 turned the ANPD into the *Agência* Nacional de Proteção de Dados,
a regulatory agency linked to the Ministry of Justice. It also enforces the ECA Digital (Lei 15.211/2025).

## 1.1 Basic concepts
- **personal data**: any info that can lead to identifying a person: name, address, email, ID, CPF,
  GPS location, IP address...
- **sensitive personal data**: info with a bigger impact if exposed: racial/ethnic origin, religion,
  political opinion, union or religious/philosophical/political membership, health, sex life,
  genetic, biometric
- **processing (tratamento)**: any operation, manual or automated: collect, register, organize, change,
  consult, use, disclose, block, destroy...

### Actors
- **titular**: the person the data is about (child, adult or elderly)
- **controlador**: decides the legal basis, the purpose and how data is processed.
  GDPR calls it "controller"/"responsável"
- **operador**: usually a company that processes data on behalf of the controller.
  The controller can also be the operator. US/EU call it "processor"
- **agentes de tratamento**: controller + operator
- **encarregado (DPO)**: person or company appointed by the controller or the operator.
  Bridge between agents, data subjects and ANPD. Also guides the controller's staff
- **ANPD**: watches, implements and enforces LGPD and applies the sanctions

## 1.2 Data subject rights
The controller has to make these work "with simplicity, speed and quality".
- confirmation that data is processed (art. 18, I)
- access: purpose, how, who the controller is, sharing, responsibilities (arts. 9 and 18, II)
- correction (18, III)
- anonymization, blocking or deletion of unnecessary/excessive data, "right to be forgotten" (18, IV)
- portability to another provider, on express request (18, V)
- know who the data was shared with (18, VII)
- be told you can refuse consent and what happens if you do (18, VIII)
- revoke consent (18, IX)
- object to processing based on other legal bases when the law is broken (18, §2)
- review of decisions made only by automated processing (art. 20)
- petition the controller or the ANPD (18, §1)

A data breach ("violação de dados") isn't only a hack or a leak: any non-compliance counts, even data
that should be available and isn't.

**Pseudonymized vs anonymized**
- pseudonymized: can only be linked back with extra info kept separately by the controller, in a
  safe controlled place -> still personal data
- anonymized: can't identify the person with reasonable technical means available at the time.
  Not personal data, LGPD doesn't apply unless the anonymization is reversed
- the course uses encryption as an example: without the key, considering reasonable means, it counts
  as anonymized

## 1.3 Relations between the actors
How each actor relates to the others (from the course infographic):

| From -> To | What happens |
|---|---|
| titular -> public/private sector | asks for info, update, correction, access; consents or revokes consent (public sector: only in some cases); asks about automated criteria; exercises rights |
| public/private sector -> titular | processes data, authorizes, denies improper third-party access, grants access, explains criteria, informs sharing, corrects, compensates, takes care, assesses impact |
| titular -> ANPD | reports, requests |
| ANPD -> titular | accepts or rejects the request, informs, protects |
| ANPD -> public sector | regulates, asks for info, evaluates practices, applies sanctions, approves procedures, authorizes sensitive processing, recommends, determines, gives guidelines (art. 55-J) |
| public sector -> ANPD | appoints/informs the DPO, looks for best practices, appeals, defends itself, pays fines, follows the rules, informs |

ANPD isn't only about fining. It also writes the national data protection policy guidelines, handles
data subject petitions, educates the public, studies privacy practices and works with PROCONs,
regulatory agencies and consumer associations.

Podcast "LGPD Serpro" with Ulysses Machado: ep. 1 the DPO role, ep. 2 the data subject, ep. 3 consent.
