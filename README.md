# A2-Group2

# Our very own chatbot - Harvie The MovieBot

Harvie, the conversational chatbot, specializes in talking about film - movies, tv shows and celebrities. The main goal is for it to be able to handle a conversation of at least 30 turns and be able to deal with any possible input.

For now, most of the conversation is based on a series of questions being asked by the user and the bot responding back with answers from an array. We also allowed the bot to be able to ask questions to the reader.

## How to run the bot/install it
For now, we have not compiled the code to be run as an exectuble program. It currently works using a gui

You can clone this remote repository into your own local machine and then run it by either opening `app.py` (or `code app.py a command line once you navigate to the local repository).You must then compiling/running the file using an IDE or using the command `python app` in the terminal.

Note: You will need to have Python installed on your local machine, we recommend having a version *no earlier* than **v 3.9.10**

## Code breakdown:
### Chatbot
for now the chatbot is a simple class that saves that creates an object with a name as its only attribute to identify our chatbot.

### App
contains the Gui implementation of the bot

### getResponse
takes the user's input (as lowercase) and tries to identify a similar string as in a dictionary of possible questions. If it matches a key, the coressponding value (the pre-written answer to the question) is returned. If not, a key error is returned and handled. the use

### questions
this class stores a list of questions, and our bot will randomly pick one and output it to terminal when the user inputs "ask me a question".


### Nerstanza and POStrack
An api we used to find out if the user is typing in past tense or present tense

### NLTK
An api we used to detect synonyms of the words, the bot should be able to understand a word if its a synonym of a word it currently knows

## Chatbot in action

The chatbot is able to take user input and give back answers. However each word does not have to be the exact same as the key in the dictionary to give back the right response.

![image](https://user-images.githubusercontent.com/45835101/159102731-bc2e84cb-25c3-4745-bf22-87a919e66763.png)


It does manage to answer the same question regardless of the casing.

![image](https://user-images.githubusercontent.com/45835101/159102897-e7f26b04-b109-4d82-8b6c-6080bf55aed6.png)


If there is an unexpected input, it is able to return a default message.

![image](https://user-images.githubusercontent.com/45835101/159102914-9e01609d-7b8d-44db-8de0-fe1a93d18812.png)

Once done all the user has to type is `exit` for chatbot to terminate.

![image](https://user-images.githubusercontent.com/45835101/159102958-bdc379f5-b278-4882-baa5-808fb2f690fc.png)

## A3 Features
Handling lack of question mark for questions

Provides more topics like sports and movies

Handling short form requests

Recognizing works of art (use of NER)

Recognizing synonyms, using these to make calculated responses/guess what the user is trying to say

More error handling to guide user input

Ability to ask the user questions, and respond positively or negatively based on simple key words.

## Individual Project section Features
### Getting song recommendations from spotify using the Spotify Api.
To use the song recommendation tool, you ask the the bot any thing that has "song" in it like "Recommend me a song!" , "What song should i listen to?" etc. It does not have to exactly the same sentence, it just needs to have "song" in the input.
Then the bot then recommends a song to the user along with the artist name.
After the bot prints out the song, Spotify mode has been deactivated to activate it you have to repeat the steps again i.e ask it a question that has "song" in it. 

![image](https://user-images.githubusercontent.com/45835101/162301238-734a6e77-3868-4c19-b396-043df3cda7b9.png)

### Getting the latest topic or tweet from anyone of your choice using the twitter Api.
To get the latest tweet from your favorite celebrity, you ask the bot any input that has "twitter" in it like "What is the latest tweet on twitter", " What is happening on Twitter?" etc. It does not have to be exactly the same sentence, the user input just needs to contain "twitter" in it.
After activating Twitter mode, the bot would ask for the twitter handle of the person you want to get their latest tweet, after you enter the twitter handle, the bot should print out their latest tweet.
After the bot prints out their latest tweet, twitter mode has been deactivated to activate it you have to repeat the steps again i.e ask it a question that has "twitter" in it. 

![image](https://user-images.githubusercontent.com/45835101/162304444-b9109ed3-6175-4f25-a000-1e64ceadb9a8.png)




## Looking ahead
We would love to include the following features to our bot:
- More abilities other than just answering questions such as:
    - quizing the user on movies, tv shows,etc and displaying correct answers at end as a score (trivia mode)
    - being able to give the iMDb synopsis and ratings for a movie using an API
- deploying the bot on a website or as an executable program
- potentially changing the architecture of the software so that the bot is not rule based but instead more intelligent and capable of using NLP to interpret the user's input and give the same response to many similarly worded queries.
