# Whatsapp-mass-messaging-Python
A python code which uses web automation to send mass whatsapp messages to people without having to save the phone numbers which are provided in csv file.
## Versions availaible
<ul>
<li><strong>1.0.0</strong> - The message_text, no_of_message, mobile_no_list variables where they have their usual meaning are hardcoded or ecplicitly defined in the code. 
<li><strong>1.1.0</strong> - The code is modified so the number of mobile numbers are extracted from the csv file "test_numbers.csv".
  <br>
  To extract the numbers use the code:
  <br>
  <code>
  with open('test_numbers.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
      for row in csv.reader(csvfile, delimiter=';')]
  # get mobile no from csv file
  </code>
  </li>
<li>
  <strong>1.2.0</strong> - The code is modified so the number of mobile numbers are extracted from the csv file "test_numbers.csv" and message is too extraccted from a text file.
  The code can take the message in all different languages, for demonstration I have named the file "hindi_message.txt".
  <br> For extracting the text use code:
  <br>
  <code>
  with open('hindi_message.txt') as hindi_file:
    for text in hindi_file:
        message_text+=text
  </coode>
  </li>
</ul>
