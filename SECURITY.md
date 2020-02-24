# Security Analysis

The main concerns of our app is that people could gain access to the grading information
of other students, or gain login information (which they could potentially use to compromise the user
in other websites).

- Injection
    - Threat Assessment: One aspect we could be vulnerable to is injection attacks. Since we pull data as "notification" packets,
        and then store them in our database, this could lead to vulnerabilities.
        Injection attacks could occur from Piazza Posts, Blackboard assignments, or even the users
        themselves since eventually we aim to allow users to add their own notifications.
    - Planned Defense Strategy: We will follow the OWASP recommendations for injections.
        When reading in notifications, we will have to make sure to santize and validate the data
        before storing it to the server.

- Cross-Site Scripting XSS
    - Threat Assessment: Our notifications will be displayed as is on the webpage. If someone managed to inject
        some malicious Javascript/HTML Code, whcih then got rendered in our display, this could be harmful. 
        Another aspect of our app would be to attempt to render previews of some relevant data for our notifications.
        The preview could possible run malicious code stored in the external files that we are trying to preview.
    - Planned Defense Strategy: We will follow the OWASP recommendations for XSS.
        As with Injection, we will need to sanitize incoming data, escaping untrusted HTTP data requests as needed.
        We may also make some files unrenderable, the way Blackboard does not allow certain files to be previewed.
        We can also look into learning React JS as it avoids XSS by design.

- Broken Authentication
    - Threat Assessment: The password could be extracted from the database. If someone managed to access our database 
        and inject some malicious code that allowd them to exploit the password and get access to it. 
        This would be harmful because many people tend to reuse the same passwords for other applications 
        or they might have personal information in the password itself.
    - Planned Defense Strategy: To combat this threat, we will follow the OWASP recommendation 
        for Broken Authentication. We will make sure to store passwords in an encrypted format.
        We will also limit the number of login attempts to make sure that the user cannot use this application to brute-force logins.

