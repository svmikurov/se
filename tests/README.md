# Test list

## Context

Open page with `/ru/glossary/` path returns presentation exercise

## BFF
- [x] returns `200`, title "Glossary"
- [x] The page displays hardcoded definition text
- [x] The page displays hardcoded explanation text
- [ ] shows next term definition
- [ ] shows next term explanation
- [ ] shows term explanation with timeout
- [ ] replace definition and explanation constants with variables
- [x] request handler returns presentation card data

## Presentation service request
- [x] GET `/presentation/` returns `200` + JSON {definition, explanation}
- [ ] GET `/presentation/` returns `404` for unknown
- [ ] GET `/presentation/` returns `500` on internal error

## Presentation service
- [x] `handle()` returns presentation card
- [ ] `handle()` raises `NotFound` for unknown
- [ ] gets presentation card from injected domain dependency

## Domain
- [x] presentation model returns presentation object-value
- [ ] created random presentation card from (fix hardcoded presentation card)