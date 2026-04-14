=== Sentiment Classifier ===
  [raw response]: ```json
{"results": [{"text": "I love how quickly the invoices are processed!", "sentiment": "positi
  POSITIVE: I love how quickly the invoices are processed!
  NEGATIVE: This audit is taking forever and nothing is organized.
  NEUTRAL: The quarterly report has been submitted.

=== GL Account Classifier ===
  [raw response]: ```json
{"results": [{"transaction": "Monthly Adobe Acrobat subscription $54.99", "category": "Softw
  Software        → Monthly Adobe Acrobat subscription $54.99
  Revenue         → Client invoice payment received $12,500
  Office Supplies → Office printer paper and toner $87.00
  Travel          → Flight to Chicago for client meeting $430

=== Invoice Priority Classifier ===
  [raw response]: ```json
{"results": [{"invoice": "Vendor overdue notice - 90 days past due, $45,000", "priority": "H
  High     → Vendor overdue notice - 90 days past due, $45,000
  Medium   → New vendor first invoice, net 30 terms, $1,200
  High     → IRS penalty notice - response required within 10 days