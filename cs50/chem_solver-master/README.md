# Chem Solver
#### Video Demo:  <https://youtu.be/xDutyvMWi3E>
#### Description:
Solves chem reactions equations and balances/simplified
has a responsive navbar and footer with a drop down menu for account settings
app,py is the main file for the backend and solver has helper functions like formatting the data and the actual algorithm that solves the reactions
has some css mainly for layout
the main page uses css grid for the layout
there are 4 html files
index.html is the page for the home page it has a script tag at the end that waits for the user to enter the rection into the form then sends a fetch request to the back end
layout.html is the template page that has the header with links to style sheets
took about 5 days to make
took awhile to to decide on a design for that page
i ended up going for a simple clean light design that doesn't overwhelm the user
i wanted to add a login system but decided against it because i thought about the UX and didn't want to bog the user down with having to sign in
took awhile to get the layout working well i started with just trying to space things out with padding and margin but this proved very difficult so i moved to css flex which also was not right for my application so i eventually came to css grid and i'm glad i did i had to lay it out on the whiteboard first but after that it was very easy

future plans to add a sqlite database for auto charges so the user does not have to enter them in as well as to store other facts about the elements





more types of reactions like replacement and riding the limiting reactions
i also wanted to change the UI to instead have a plus button where were the user will be able add more elements or ions or combinations of elements
future plans to add css grid periodic table that's interactive when you hover over the elements more info will be shown
similar i want to add a table for polyatomic ions
i also want to add general quiz for reaction the table and polyatomic ions
i do also want to login page for "pro mem"
optional login page with logout page
account page where using can edit their account settings
lightmode/dark mode switch for better UI/UX

long term
long term I want to make this like photo math for chem with photo section that can solve all types of problems and even word to element converter with roman numerals
for the photo part i will need to add some image reaction for handwriting


this will evidently turn into a iphone and android app
i want to use the existing html and css for the code and not have to rewrite the code in another language




