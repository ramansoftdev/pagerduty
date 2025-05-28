## PagerDuty 

### Description

PagerDuty: Imagine you are creating a PagerDuty clone which should alert employees on an on-call rota whenever an incident arises. The on-call rota consists of Engineers and Managers. 



- If an employee receives an alert for an incident, they should not receive alerts for subsequent incidents until they have resolved their current incident. 
- A Manager should not receive an alert for an incident unless there are no Engineers available



- When an employee starts their on-call shift, they should login with their integer id.
- When an employee logs in, it should return their employees details such as their name and whether they are an Engineer, and add the Employee to the correct group of available on-call employees.
- Once its determined whether an incident should be directed to an Engineer or a Manager, if there are several available, the incident should be directed to the Employee who has been available the longest.

