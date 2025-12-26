# What the interviewer wants from the testing questions

1. Need to come up with a reasonable amount of test cases
2. Do you understand the bigger picture of the product: Do you understand about the software properly. If working in E-commerce like Amazon it is important to test if the images are being displayed properly and even more important that payments, shipment queue and others work properly
3. Knowing how the different products fit together: Do you know how the software fits together with the bigger ecosystem? If you are developing Google spreadsheets, it is important to test the opening, editing and deleting functionality but also integration with Gmail and others
4. Organization: Do you test in a proper manner or spout things that come in your head. A good candidate will breakdown the parts into categories like Taking photos, image management and settings and so on.
5. Practicality: Can you actually create something testing plans. Need to reasonable for the company to implement

# Testing is under 4 categories

1. Test a real world object like a pen

Before writing out test cases. It is important to ask some questions and understand what is the use of the product and based on their reply we reply with the test cases:

Q: How would you test a paperclip

- Question 1 to ask: Who will use it and why? Will the paperclip be used by teachers or by artists?
- Question 2 to ask: What is the use cases?
- Question 3 to ask: What is the bounds of use? The bounds means constraints. Any environmental issues are we facing? What is the expected lifespan? What is the maximum capacity?
- Question 4 to ask: What are the stress / failure conditions: Ask the interviewer when it is acceptable for the product to fail and what it means. For example, if testing a laundary machine, you might think it should handle atleast 30 clothes but if we load in 30-40 then it is ok for the cloths to be not adequately cleaned. If more than 45, extreme failure is acceptable but that means the machine should not switch on, not something like causing a fire or damage to the cloths
- Question 5: How to perform the testing: Manual testing / Automated testing using a machine. For example, for a chair we can test the "sits / yr" or by using a machine to load and unload weight off it

2. Test a piece of software

- Software testing has 2 aspects to it: Manual vs Automated testing and White Box vs Black box testing

3. Write test for a function

4. Troubleshoot an existing issue
