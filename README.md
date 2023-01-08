# Welcome to MoodBoost API!

## Documentation

MoodBoost API is a REST API that allows you to easily fetch jokes and motivational quotes to brighten your day and boost your mood!

**Current release intakes GET requests only :zany_face:**

### Instructions

Press this link for [MoodBoost API](https://moodboostapi.pythonanywhere.com) or send GET requests to <https://moodboostapi.pythonanywhere.com>.

### Endpoints

Responses are returned in JSON format.

* (Default) GET https://moodboostapi.pythonanywhere.com/

    * Returns random message of motivation/humor

    * Sample output:

    * ![placeholder](https://github.com/kjung4706/MoodBoost-API/placeholder.png)

* GET https://moodboostapi.pythonanywhere.com/type=joke

    * Returns random joke
    ```
    {
       "id": 5,
      "message": "What do you call a snake that's 3.14 meters long? A pi-thon!",
      "type": "joke"
   }
    ```

* GET https://moodboostapi.pythonanywhere.com/type=motivate

    * Returns random motivational message
    ```
    {
       "id": 15,
       "message": "You have the power to create the life you desire.",
       "type": "motivate"
   }
    ```

* GET https://moodboostapi.pythonanywhere.com/id=<id>

    * Returns random message based on id


### Authentication

No authentication is required to use MoodBoost API.

### Tech Stack

* Python

* Flask

* SQLAlchemy

* marshmallow

* Postman

* PythonAnywhere

**Developed by Emily Pham and Kyle Jung**
