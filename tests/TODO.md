# Glossary application presentation test task list

- [x] completed task
- [ ] _**> current task**_
- [ ] planned task

## e2e

### open `/ru/glossary/`
- [x] returns `200`, title "Glossary"
- [x] shows term definition
- [x] shows term explanation
- [ ] shows next term definition
- [ ] shows next term explanation
- [ ] shows term explanation with timeout
- [ ] replace definition and explanation constants with variables

## Request handler unit test
- [x] handler returns presentation card data

## Exercise Service

### API (FastAPI)
- [ ] GET `/presentation/` returns `200` + JSON {definition, explanation}
- [ ] GET `/presentation/` returns `404` for unknown
- [ ] GET `/presentation/` returns `500` on internal error

### UseCase
- [ ] handle() returns presentation card data
- [ ] handle() raises NotFound for unknown