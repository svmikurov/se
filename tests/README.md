# Test list

## Context

Glossary term study presentation page shows presentation card  
http://127.0.0.1:8200/ru/glossary/presentation/

## WEB BFF
- [x] returns `200`, title "Glossary"
- [x] The page displays hardcoded definition text
- [x] The page displays hardcoded explanation text
- [ ] shows next term definition
- [ ] shows next term explanation
- [ ] shows term explanation with timeout
- [ ] replace definition and explanation constants with variables
- [x] request handler returns presentation card data
- [x] `request_handler.handle()` returns presentation card
- [ ] `request_handler.handle()` raises `NotFound` for unknown
- [x] gets presentation card from injected domain dependency

## Infrastructure
- [ ] service HTTP client handles request errors
- [ ] server returns `404`
- [x] in-memory term repository returns list of terms
- [ ] >>> _**repository adds terms**_

## Service API
- [x] GET `/presentation/` returns `200` + JSON {definition, explanation}
- [ ] GET `/presentation/` returns `404` for unknown
- [ ] GET `/presentation/` returns `500` on internal error
- [x] Add DI
- [ ] _**use case gets terms via repository**_

## Domain
- [x] presentation model returns presentation object-value
- [ ] created random presentation card (fix hardcoded presentation card)
- [ ] _**glossary repository provides terms for presentation card creation**_