== TODO ==

* Logoff / Shutdown actions
* Fork the process or launch a thread to send the email
* Collect the report text/date from the UI (and save it), before
  preparing the email
* Create a visual tooltip that the email is being sent
* Create a error widget (pop-up?) to display errors to the user
* Capture and treat errors sending the email:
    * smtplib errors
    * date parsing errors
    * empty content errors (?)
