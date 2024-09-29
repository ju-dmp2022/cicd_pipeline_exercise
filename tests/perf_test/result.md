
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
the aggregated result of the Response Per Second (RPS) was 2.79 when there where 50 users on the application simultaneously and 1 got added in each 2 to 4 seconds. 


• How many simultaneous users can the application handle and still reliably provide responses?

Answer: 
the application could only hold and provide solid performance for 2 user, because the 95%ile drastically went up to 4-5ms by that amount of users, but if you change the infrastructure and add more servers using Amazon Web Services' (AWS) ec2 instances and a load balancer and binding the ec2 instances to an auto scaling group (including preferred running ec2 instances and lowest amount and highest amount) you will for sure have a better performance in the application.


• What is the maximum throughput the Calculator application can achieve and still reliably
provide responses?

Answer:
the point when the 95%ile is at 5ms the RPS is at 1 r/s,
and this is the point when it starts providing unreliable data because of the load of users. Although it can still provide data... 



additional questions from the customer:

1. Sometimes the response time when performing the add operation seemed to be slower than
usual. It didn’t seem to be related to the number of simultaneous users, but no other clues were
given. Can you figure out under what circumstances the problem may occur?

Answer:
apart from input output (I/O) network delay, I believe it is partly because I have a payload inside my for loop in my add task which the interpreter will read each time in the for loop so twice and that can take some micro seconds which is why I experience a delay in that regard even though it runs twice as many times as the other tasks. 

Example 1: when I run the test in its current state which the for loop in the add task I receive 0.6ms in RPS on the add row, but 0.4 on the subtract column.

Example 2:when I run the same task without the for loop in the add task, all tasks have the same RPS (a couple of nano seconds difference, worst case scenario maybe one half a micro second difference between the tasks).


2. The application seemed to crash from time to time. When it happened the application had to be
restarted and then everything went back to normal. Can you reproduce the problem and inform
the developers what seems to cause the problem? What part of the application is triggering the
problem?

Answer:
after multiple tests my conclusion is that this occurs when the start amount of users are at a very high load and the adding users per second is also at a high level or rather extreme level of performance, and this is actually fully described in the log section of Locust. 
As I mentioned before a solution to this issue could be to buy a couple of servers and to include them in the company's data canter and for the purpose of disasters or flexibility, you can rent servers from AWS in combination with the on-premises infrastructure, this is called a 'hybrid cloud' and is used by many companies around the world, reliable performance at any speed of load.

- OBS: this is something i would discuss thoroughly with the customers/stakeholders in a real-world scenario.




