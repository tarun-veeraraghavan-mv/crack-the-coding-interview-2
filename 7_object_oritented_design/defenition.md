# How to approach

# Step 1: Handle Ambiguity

- These questions are intentionally vague in nature to test whether you will make assumptions or ask clarifying questions
- When asked use the "six Ws" formula with: "Who, what, when, where, how, why"
- For example, if designed to make a coffee machine. It is important to know if it should be designed for a massive restaurant serving 100 people / hr or used by elderly to produce only black coffee

# Step 2: Define core classes / objects

- Analyze what is the core objects in the system
- For a restaurant, core objects are Guest, Table, Order, Meal, Employee, Server and Host

# Step 3: Analyze relationships

- Having the core objects decided we want to analyze the relationships between them.
- Do we need to inherit from something or any one to one relationships
- Party should have an array of Guests
- Server and Host inherits from the Employee
- One table can have one Party, but each Party can have multiple Tables

BUT MAKE SURE TO CLARIFY THE RELATIONSHIPS WITH THE INTERVIEWER. Sometimes it is okay for one Table to Have multiple Parties. This is where communication is important

# Step 4: Investigate Actions

- With the basic objects and relationships defined, you need to think of the key actions of the object
- For example, a Party walks into the restaurant, Host looks at the reservation and assigns the Party a Table

# Step 5: Design Patterns

- Singleton and Factory are the most common type of OOD patternss
