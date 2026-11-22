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
- [ ] > _**`request_handler.handle()` returns friendly message on `204` Service API status**_

## Infrastructure
- [ ] service HTTP client handles request errors
- [ ] server returns `404`
- [x] in-memory term repository returns list of terms
- [x] repository adds terms

## Service API
- [x] GET `/presentation/` returns `200` + JSON {definition, explanation}
- [ ] GET `/presentation/` returns `404` for unknown
- [ ] GET `/presentation/` returns `500` on internal error
- [ ] >> _**GET `/presentation/` returns `204` on `NoItemsForExercise` domain exception**_
- [x] Add DI
- [x] use case gets terms via repository

## Domain
- [x] presentation model returns presentation object-value
- [ ] created random presentation card (fix hardcoded presentation card)
- [x] repository provides terms for presentation card creation