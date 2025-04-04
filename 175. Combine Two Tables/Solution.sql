select firstName, lastName, city, state from Person left outer join address on Person.personId = Address.personId
