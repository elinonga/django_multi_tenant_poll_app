# Introduction to multi tenant applications

## What are multi tenant apps?
Multi tenant applications allow you to serve multiple customers with one install of the application. 
Each customer has their data completely isolated in such an architecture. Each customer is called a tenant.

## The structure of the code
In the shared code above, I have taken a single tenant application and re-architect it to be a multi tenant application. 
You will use a slightly modified Django polls app as our base.

## The various approached to multi tenancy
- Shared database with shared schema
- Shared database with isolated schema
- Isolated database with a shared app server
- Completely isolated tenants using Docker

## Shared database with shared schema
A single database keeps every tenant’s data. A ForeignKey in the tables identifies the tenant.

## Shared database with isolated schema
A single database keeps every tenant’s data. Each tenant’s data is in a separate schema within the single database. 
The schema identifies the tenant and data tabled do no have a FK to the tenant.

## Isolated database with a shared app server
Every tenant’s data is in a separate database. The database identifies the tenant.

## Completely isolated tenants using Docker
A new set of docker containers are launched for each tenant. Every tenant’s data is in a separate database (which may or may not be running in container). A set of containers identifies the tenant.
