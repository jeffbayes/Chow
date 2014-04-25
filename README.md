Possible Names:

Die Clickbait, Die! // Upworthless


#The basic idea:

Installed on your browser (Chrome to start) as an extension, the extension would have
a preinstalled library of clickbait sites, which can be editable by the user. The
library would certainly start with Upworthy, but could include other clickbait sites
like ThinkProgress, TheBlaze, or whatever else the user does not want to give pageviews.
Thus, when the user is directed to that site, either by typing it directly into their browser
or by clicking a link (e.g. Facebook share), the extension works its magic! If this user is the
first visitor to this webpage, it would scrape the page then store the data... somewhere. (This 
is a technical issue we'll have to address, depending on how we want to display the data.) 
After the data is stored that first time, we then access it in one of two methods.

#Tanner's Method

We merely scrape the page to find the data of the orginal content and then pair the url for the orignal content with the clickbait content. 


Example: 
This is the upworthy url: https://www.upworthy.com/when-a-family-of-8-kids-turns-on-their-mother-for-money-see-what-her-granddaughter-does?c=reccon1


This is the orginal content url: https://vimeo.com/92570042


We can obtain the orginal content url by finding Upworthy's anchor tag with the text "Orginal" or the just take it from the iframe since it's embeded. The latter will be a better general solution as you're going to always need an iframe for 
embeded videos.




So when the user requests a url that is in DCD's domain blacklist it checks to see if that specifc url is already matched with an OC link.
if True:
    DCD sends opens the OC link instead: http://ntt.cc/2008/01/21/5-ways-to-redirect-url-with-javascript.html
else:
   DCD tries to scrape that webpage for OC and store a clickbait url:OC url pair


**Database Example:**


clickbait url | OC url
------------- | -------------
https://www.upworthy.com/5-minutes-of-what-the-media-actually-does-to-women-8?c=reccon1  | https://www.youtube.com/watch?v=jWKXit_3rpQ
https://www.upworthy.com/move-over-barbie-youre-obsolete  |https://www.youtube.com/watch?v=y-AtZfNU3zw


###Reasons I like this approach:

1. We can store a lot of pages with very little data required.
2. We're no better than the clickbaiters if we just rehost OC.


###Stuff that it wont't cover:
+ Text articles, if they wrote it it's OC and they earned the pageviews even if the article sucks.
However if they're just rehosting another article I'm sure we can address this
+ gifs/pics these are usually a lot harder to find direct link to the OC.


###Risks
+ Upworthy could try to counter us with url obfusication. But this means 2 things
    ..+ Our extension is succseful enough for them to take notice
    ..+they'd get filterd out by Facebooks spam filters thier biggest revenue source





#Jeff's Method: 
I only have like three minutes to write this, so here's the short version. We take
the title, body text, and whatever video might be in there, and display it on a very mimimalistic
web page. The first thing that came to mind was fatpita.com, in that vein of minimalism... but less
intrusive with the Facebook sharing. We want you to enjoy your content without the constant badgering
to share the content with everyone and your sister. We want the site to be attractive without any level
of intrusiveness. The only problem that comes to mind with this is storing the data for all of these web
pages. A few thoughts on that: we could cap a table at ~100-500 (whatever is realistic) pages stored at
once, and then the least recently accessed page could be dropped from our database - basically caching.
This wouldn't be a coverall for all pageviews to Upworthy/etc., but could put a serious dent in what
they are getting.
