
# this is my conclusion and theory based on Locust Performance Testing


• Assuming 50 simultaneous users:

◦ What are 95th percentile of the response time for the different operations (add, subtract…)?

Answer:
add:62
subtract:51
multiply:49
divide:170


◦ What is the throughput? That is, how many requests/second is performed with this user
load?

Answer:
the aggregated result of the Response Per Second (RPS) was 6.9 when there where 150 users on the application simultaneously and 1 got added in each 2 to 4 seconds. 


• How many simultaneous users can the application handle and still reliably provide responses?

Answer: 
the application could only hold and provide solid performance for 150 user, because the 95%ile is on 8.9ms, but if you change the infrastructure and add more servers using Amazon Web Services' (AWS) ec2 instances and a load balancer and binding the ec2 instances to an auto scaling group (including preferred running ec2 instances and lowest amount and highest amount) you will for sure have a better performance in the application.


• What is the maximum throughput the Calculator application can achieve and still reliably
provide responses?

Answer:
when i test it in 8 to 12min the reliable throughput i can confidently say that i get is ~8 r/s.



additional questions from the customer:

1. Sometimes the response time when performing the add operation seemed to be slower than
usual. It didn’t seem to be related to the number of simultaneous users, but no other clues were
given. Can you figure out under what circumstances the problem may occur?

Answer:
apart from input output (I/O) network delay, when i tested positice integers it reposned with a normal 95%ile but when i tried with the same integers but negativ the 95%ile was almost quadrupled. 



2. The application seemed to crash from time to time. When it happened the application had to be
restarted and then everything went back to normal. Can you reproduce the problem and inform
the developers what seems to cause the problem? What part of the application is triggering the
problem?

Answer:
divide is the only function that saves it in the memory, leading into a crash of memory usage.

Solution:
As I mentioned before a solution to this issue could be to buy a couple of servers and to include them in the company's data canter and for the purpose of disasters or flexibility, you can rent servers from AWS in combination with the on-premises infrastructure, this is called a 'hybrid cloud' and is used by many companies around the world, reliable performance at any speed of load otherwise you can host all your servers on AWS uing EC2 insatnces in an auto scaling group for distrebuted load in performance. More suitable for this scenario could be to add this in Lambda to trigger an automation to store the divide executions in an S3 bucket for simple storage.

- OBS: this is something i would discuss thoroughly with the customers/stakeholders in a real-world scenario.




