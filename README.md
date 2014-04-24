Possible Names:

Die Clickbait, Die! // Upworthless

The basic idea:

Installed on your browser (Chrome to start) as an extension, the extension would have
a preinstalled library of clickbait sites, which can be editable by the user. The
library would certainly start with Upworthy, but could include other clickbait sites
like ThinkProgress, TheBlaze, or whatever else the user does not want to give pageviews.
Thus, when the user is directed to that site, either by typing it directly into their browser
or by clicking a link (e.g. Facebook share), the extension works its magic! If this user is the
first visitor to this webpage, it would scrape the page then store the data... somewhere. (This 
is a technical issue we'll have to address, depending on how we want to display the data.) 
After the data is stored that first time, we then access it in one of two methods.

Tanner's Method: [I honestly don't totally understand, so if you could give me an ELI5 here it'd
be pretty sweet. I gave you contributor abilities.]

Jeff's Method: I only have like three minutes to write this, so here's the short version. We take
the title, body text, and whatever video might be in there, and display it on a very mimimalistic
web page. The first thing that came to mind was fatpita.com, in that vein of minimalism... but less
intrusive with the Facebook sharing. We want you to enjoy your content without the constant badgering
to share the content with everyone and your sister. We want the site to be attractive without any level
of intrusiveness. The only problem that comes to mind with this is storing the data for all of these web
pages. A few thoughts on that: we could cap a table at ~100-500 (whatever is realistic) pages stored at
once, and then the least recently accessed page could be dropped from our database - basically caching.
This wouldn't be a coverall for all pageviews to Upworthy/etc., but could put a serious dent in what
they are getting.
