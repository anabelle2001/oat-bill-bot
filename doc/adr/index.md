# Architecture knowledge base

Welcome 👋 to the architecture knowledge base of oatbill-bot.
You will find here all the Architecture Decision Records (ADR) of the project.

## Definition and purpose

> An Architectural Decision (AD) is a software design choice that addresses a functional or non-functional requirement that is architecturally significant.
> An Architectural Decision Record (ADR) captures a single AD, such as often done when writing personal notes or meeting minutes; the collection of ADRs created and maintained in a project constitutes its decision log.

An ADR is immutable: only its status can change (i.e., become deprecated or superseded). That way, you can become familiar with the whole project history just by reading its decision log in chronological order.
ADRs are usefull, in part, because:

- They speed up the onboarding of a new team member
- Their use prevents blind acceptance/reversal of a past decision (see [Michael Nygard's famous article on ADRs][1])
- They formalize the decision process of the team

## Usage


In fact, the developers manage this documentation directly with markdown files located next to their code, so it is more convenient for them to keep it up-to-date.
You can browse the ADRs by using the left menu or the search bar.

The typical workflow of an ADR is the following:

![ADR workflow](/l4b-static/adr-workflow.png)

The decision process is entirely collaborative and backed by pull requests.

## More information

- [Log4brains documentation][2]
- [What is an ADR and why should you use them][3]
- [ADR GitHub organization][4]


[1]: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html
[2]: https://github.com/thomvaill/log4brains/tree/master#readme
[3]: https://github.com/thomvaill/log4brains/tree/master#-what-is-an-adr-and-why-should-you-use-them
[4]: https://adr.github.io/