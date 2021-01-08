# license key generator
Simple License Key Generator written in Python 3.8

You are allowed to use this project in any way, without limits
You don't have to credit me, but I would appreciate it if you did.

## How to use


    from licensekeygenerator import LicenseKey
    key = LicenseKey()
    keyValue = key.generateKey()
    print(keyValue)

This code will create a default license key.

But you can also create a custimised one. The LicenseKey() class takes 3 arguments

- pAmount : The amount of parts the license key will have. Eg: XX-XX-XX has 3 parts
- pLength : The length of parts the license key will have. Eg: XX-XX-XX has a part length of 2
- divider : The divider of parts the license key will have. Eg XX-XX-XX has a divider of "-"

Example of custom usage:

    from licensekeygenerator import LicenseKey
    key = LicenseKey(3,6,"--")
    keyValue = key.generateKey()
    print(keyValue)

This will print something like:

    XXX--XXX--XXX--XXX--XXX--XXX


If you have any questions, email zyapimstudios@gmail.com or my discord at zyapguy#0320