#Chowahua
All ideas come with a cute animal drawing as the website mascot (even a cute Godzilla)!

###Expected Subsets
####L0: Bare Minimum Requirements
Search page, displaying resaurants in Eugene [internal filter]<br/>
Brought to dynamically generated table of Restaurants in Eugene</br>
Click on restaurant, brought to new URL (chowahua.com/restaurant_id)<br/>
Locu integration for Restaurant IDs<br/>
ADMINISTRATIVELY add menu items, as a one-to-many relationship with Restaurant ID<br/>
Average rating for dish, as one-to-one relationship with menu items (or integrated w/ menu items)<br/>
Number of ratings, overall rating stored in the rating (+1 and +rating for average rating)<br/>
Expected URLs
*chowahua.com
*chowahua.com/restaurant_id
*chowahua.com/restaurant_id/name_of_dish
####L1: Prettifying alla dis'

###Informal Use Cases
####Restaurants: chowahua.com/NameOfRestaurant. 
Each restaurant will be listed with its specific, detailed menu. Possible options on the main restaurant page would be displaying its highest rated dish, or "Most Hearty" or other "Most XXXXX." It could also display some metric rating the restaurant as a whole. We could either average all dish ratings together, or average the top five dishes at a restaurant (indicating both quality and variety). Users could also comment and rate the general experience of the restaurant, not pertaining to the food they recieved (e.g. atmosphere, service, etc). 

####Dishes: chowahua.com/NameOfRestaurant/NameOfDish
SIMPLE RATING: Rate the dish on a scale from 1-4(or 5) stars. The user can then either submit as is, or go more in depth with their reviews. Going deeper, we can have a "Heartiness" meter, "Spiciness" meter, a scale between "Bold" or "Mild" (in regards to the flavors used), and of course a comments section.

####User Accounts - NIXED
This could be a slippery slope. I think it would be easiest to gain traction if user accounts were not required, but a user account could access much more in terms of a feature set. Editing past reviews, a "trusted reviewer," and other things could be part of creating a user account.


