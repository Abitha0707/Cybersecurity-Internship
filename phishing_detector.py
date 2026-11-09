def check_email(sender, subject, message):

    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "click here",
        "free gift",
        "bank details"
    ]

    score = 0

    email_content = (subject + " " + message).lower()

    for word in suspicious_words:
        if word in email_content:
            score += 1

    if "@" not in sender:
        score += 1

    print("\n----- Email Security Report -----")

    print("Sender:", sender)
    print("Subject:", subject)
    print("Risk Indicators:", score)

    if score >= 2:
        print("Result: Suspicious Email")
    else:
        print("Result: No obvious suspicious indicators")


sender = input("Enter sender email: ")
subject = input("Enter email subject: ")
message = input("Enter email message: ")

check_email(sender, subject, message)
