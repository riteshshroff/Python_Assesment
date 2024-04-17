
Whats app UAT BOT FLOW :
-----------------------------

1. user query :Complaint - 
	>>>> First "LANG_DETECT_SERVICE" (For language) 
        >>>> Before request function call (for execution)
        >>>> Then we are calling Api "ELLEBOT API" (understand the query or master question) 
        >>>> Helpers function call to check the VOC flag
2. Output : Register mobile no. -
	>>>> enter your register mob. no.
        >>>> For authentication Nucleus Dedupe Api call validate with otp.
        >>>> Check the agent chat timing and pass the standard message.
3. Output : 
        >>>> Please stay connected while we connect you to an agent. This could take a few minutes.


Whats app MASTER BOT FLOW:
------------------------------
1. user query :Complaint - 
	>>>> First"LANG_DETECT_SERVICE" (For language) 
        >>>> Then we are calling Api "ELLEBOT API" (understand the query or master question) 
        >>>> Helpers function call to check the VOC flag
	>>>> Process Tree response after first request	
2. Output : Please enter the policy number for which you want to raise a complaint.
	>>>> User will enter the policy no.
	>>>> Call the chat history
	>>>> Postgres_post Api for storing data
        >>>> Request data for GetChat api: With session id







