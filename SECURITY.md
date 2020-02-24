# Security Analysis

Describe the security considerations you will take when building your app in this file. This should
include both a threat assessment and a planned defense strategy.

- Injection
    - Threat Assement: One aspect we could be vulnerable to is injection attacks. Since we pull data as "notification" packets,
        and then store them in our database, this could lead to vulnerabilities.
        Injection attacks could occur from Piazza Posts, Blackboard assignments, or even the users
        themselves since eventually we aim to allow users to add their own notifications.
    - Planned Defense Strategy: We will follow the OWASP recommendations for injections.
        When reading in notifications, we will have to make sure to santize and validate the data
        before storing it to the server.


