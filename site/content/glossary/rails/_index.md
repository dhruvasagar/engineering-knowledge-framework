+++
title = "Rails Glossary"
description = "Ruby on Rails terminology used throughout the Engineering Knowledge Framework"
+++


# Purpose

This glossary defines Ruby on Rails terminology used throughout the
Engineering Knowledge Framework.

Rails-specific terms defined here are authoritative across the
repository. Foundational engineering terms are defined in the
[Engineering Glossary](..*engineering*README*).

# Glossary

## ActiveRecord

| Property | Value |
| --- | --- |
| Definition | The ORM (Object-Relational Mapping) layer in Rails that |
|  | maps database tables to Ruby objects and provides |
|  | query, persistence and validation capabilities. |
| Context | ActiveRecord is the default model layer in Rails. It |
|  | implements the Active Record pattern where a class |
|  | wraps a database table. |
| Related | [[#migration][Migration]], [[#model][Model]] |
| References | [Rails Engineering Handbook](..*..*handbooks*rails*README*) |

## Concern

| Property | Value |
| --- | --- |
| Definition | A module used to extract shared behaviour from models or |
|  | controllers, typically placed in `app*models*concerns*` |
|  | or `app*controllers*concerns*`. |
| Context | Concerns are Rails' mechanism for sharing behaviour via |
|  | modules. Use them for cross-cutting concerns, but prefer |
|  | service objects for complex business logic. |
| Related | [[#service-object][Service Object]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Controller

| Property | Value |
| --- | --- |
| Definition | The component in MVC that handles incoming HTTP requests, |
|  | invokes business logic and renders responses. |
| Context | Controllers should be thin. Business logic belongs in |
|  | models, service objects or other domain classes. |
| Related | [[#model][Model]], [[#view][View]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Form Object

| Property | Value |
| --- | --- |
| Definition | A plain Ruby object that encapsulates form validation |
|  | and data processing for forms that do not map directly |
|  | to a single model. |
| Context | Form objects are used when a form collects data for |
|  | multiple models or has validation logic that does not |
|  | belong to any single model. |
| Related | [[#service-object][Service Object]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Migration

| Property | Value |
| --- | --- |
| Definition | A Ruby class that describes a change to the database |
|  | schema, allowing incremental, version-controlled schema |
|  | evolution. |
| Context | Migrations are the Rails way to manage database schema |
|  | changes. Each migration should change one logical thing |
|  | and be reversible. |
| Related | [[#activerecord][ActiveRecord]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Model

| Property | Value |
| --- | --- |
| Definition | The component in MVC that represents business data and |
|  | logic. In Rails, models typically inherit from |
|  | ActiveRecord::Base. |
| Context | Models encapsulate domain logic, validations, |
|  | associations and queries. Keep them focused on |
|  | a single responsibility. |
| Related | [[#activerecord][ActiveRecord]], [[#controller][Controller]], [[#view][View]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

**Presenter

| Property | Value |
| --- | --- |
| Definition | An object that encapsulates presentation logic, |
|  | extracting it from views into a testable class. |
| Context | Presenters wrap model objects with view-specific methods. |
|  | They keep views clean and make presentation logic |
|  | testable without slow feature specs. |
| Related | [[#view][View]], [[#service-object][Service Object]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Query Object

| Property | Value |
| --- | --- |
| Definition | A plain Ruby object that encapsulates a complex database |
|  | query, extracting it from the model into a separate |
|  | class. |
| Context | Query objects keep models clean when queries become |
|  | complex. They are named after the query they perform. |
| Related | [[#activerecord][ActiveRecord]], [[#service-object][Service Object]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## Service Object

| Property | Value |
| --- | --- |
| Definition | A plain Ruby object that encapsulates a single |
|  | business operation, typically with one public method. |
| Context | Service objects are the primary pattern for extracting |
|  | complex operations from controllers and models. They |
|  | are easy to test and can be reused across entry points. |
| Related | [[#form-object][Form Object]], [[#query-object][Query Object]], [[#concern][Concern]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

## View

| Property | Value |
| --- | --- |
| Definition | The component in MVC responsible for rendering the user |
|  | interface, typically using ERB or other template |
|  | languages. |
| Context | Views should contain minimal logic. Presentation logic |
|  | belongs in presenters, decorators or helpers. |
| Related | [[#controller][Controller]], [[#model][Model]], [[#presenter][Presenter]] |
| References | [Rails Engineering Handbook](../..*handbooks*rails*README*) |

# Related Documents

- [Rails Engineering Handbook](../..*handbooks*rails*README*)
- [Engineering Glossary](..*engineering*README*)
- [Architecture Glossary](..*architecture*README*)
- [Style Guide](../..*STYLE_GUIDE*)
- [Glossary Overview](..*README*)
