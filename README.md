# Whatsapp-mass-messaging-Python

![GitHub followers](https://img.shields.io/github/followers/Rishit-dagli?label=Follow&style=social)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FRishit-dagli%2Fpopup_box)](https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/Rishit-dagli/Whatsapp-mass-messaging-Python/)
![Twitter Follow](https://img.shields.io/twitter/follow/rishit_dagli?label=Follow&style=social)

A python code which uses web automation to send mass whatsapp messages to people without having to save the phone numbers which are provided in csv file.
## Versions availaible

* **1.0.0** - The message_text, no_of_message, mobile_no_list variables where they have their usual meaning are hardcoded or ecplicitly defined in the code. 
* **1.1.0** - The code is modified so the number of mobile numbers are extracted from the csv file "test_numbers.csv".
* **1.2.0** - The code is modified so the number of mobile numbers are extracted from the csv file "test_numbers.csv" and message is too extraccted from a text file.
  The code can take the message in all different languages, for demonstration I have named the file "hindi_message.txt".

To extract the numbers use the code:

```
with open('test_numbers.csv', 'r') as csvfile:
  moblie_no_list = [int(row[0])
    for row in csv.reader(csvfile, delimiter=';')]
# get mobile no from csv file
```

For extracting the text use code:

```py
with open('hindi_message.txt') as hindi_file:
  for text in hindi_file:
      message_text+=text
```
