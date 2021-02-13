# API Endpoints

1. Login -> Github Oauth Save it on the database
2. GetProfileData -> Get Profile Data
3. GetPreviousResults -> Get Previous Results from the database
4. GetPreviousMatches -> |
    Get Results from the db and see whether the score is more than a specific criteria [50%] and if it is return the results. 
5. GetCurrentRooms -> returns list of rooms

6. CreateRoom -> create a new room 
    /*
        Create a websocket connection with our backend
        Create a new room.
        Show the room name.
    */
7. JoinRandomRoom -> GetCurrentRooms and where number of people is < 2 and then join the room
8. PostAnswers -> GetAnsweredDetails and calculate matching probability and save the details in the results table. return the results.
9. ChatImplementation -> 
    // Websockets implementation of chat.
10. GetUpcomingHackathons -> New and Upcoming Hackathons Listing.

Recommendation for rutuja - 

Fetch API's Javascript on Mozilla Developer Network

[link for fetch api](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
