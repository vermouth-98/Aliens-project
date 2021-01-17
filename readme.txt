In Alien Invasion, the player controls a ship that appears at the bottom center of the screen.
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
The player shoots and destroys the aliens, If the player shoots all the aliens, a new feet appear
that moves faster than the previous fleet.
If any alien hits the player's ship of reaches the bottom of the screen, the player loses a ship.
If the player loses three ships, the game.

1. create display screen
2. setting background color and screen caption
3. Creating a Setting Class
4. Add the Ship Image
5. Creating the Ship Class
        When you’re centering a game element, work with the center, centerx, or
    centery attributes of a rect. When you’re working at an edge of the screen,
    work with the top, bottom, left, or right attributes. When you’re adjusting
    the horizontal or vertical placement of the rect, you can just use the x and
    y attributes, which are the x- and y-coordinates of its top-left corner. These
    attributes spare you from having to do calculations that game developers
    formerly had to do manually, and you’ll find you’ll use them often.
6. draw Ship to screen
7. Refactoring main files
8. Piloting the Ship
    a. responding to a Keypass
    b. allowing continuos movement
    c. moving both left and right
    d. Adjusting the Ship's Speed
9 limiting the ship's range 
10. Refactoring check_events()
11. shooting bullets
12. Create Alien
13. create fleet alien
14. Moving aliens
15. Shooting aliens
16 repopulating the fleet
17. Ending the game
18. REsponding to Alien_ship collisions
    Notice that we never make more than one ship; we make only one ship instance for the
whole game and recenter it whenever the ship has been hit. The statistic ships_left
will tell us when the player has run out of ships.
19. Aliens that reaches the bottom of the screen
20. Adding the play Buttom
21. deactivating the play Button
        One issue with our Play button is that the button region on the screen will
    continue to respond to clicks even when the Play button isn’t visible. Click
    the Play button area by accident once a game has begun and the game will
    restart!
22. hiding the mouse cursor
23. leveling up 
24. modifying the speed settings
25. Score
26. high score
17. level
18. Display number of ship