Input Validation Example
========================

As everyone should know, you never trust the data that the client sends to your server. I threw together this simple flask site for a simple demo of a server which blindly trusts the client when performing stock trades. The user view page uses javascript to make sure the user doesn't enter any invalid values for buy/sell numbers, but the server does no checks. Can you get $1,000,000 from it?
