# Shorty - Summarise Anything
**Shorty** is a tool to shorten the obscure terms and conditions of services, that would aid customers in making informed choices about the service they’re choosing, before they check that that wolf-in-sheep's-clothing checkbox. Along the way, I realised that **Shorty** can be used for shortening all sorts of text – blogs, books, terms & conditions, research papers, basically, anything that needs to be summarised.
## What inspired me?
The other day I was signing up for a service, and I realised that I had clicked on that “We accept your terms and conditions” checkbox, so many times, and I mean, so many times, without ever bothering to read the terms and conditions, because they are just so darn long. That’s when inspiration struck me; what if there was a tool that could give me a concise summary of whatever was written on that godforsaken page? That’s how **Shorty** came into being. 
## What it does?
**Shorty** is a tool to shorten the obscure terms and conditions of services, that would aid customers in making informed choices about the service they’re choosing, before they check that that wolf-in-sheep's-clothing checkbox. However, **Shorty** can be used for summarising any large body of text, be it blog articles, lecture notes, terms & conditions.
## What’s under the hood?
The heart of **Shorty** is an extractive text summariser, powered by the amazing BERT language representation model, and a play on BERT aptly known as BERTSUM. The exact details can be found in this research [paper]( https://arxiv.org/ftp/arxiv/papers/1906/1906.04165.pdf). A visual representation: ![A visual representation of BERTSUM](https://storage.googleapis.com/groundai-web-prod/media/users/user_10882/project_347721/images/x1.png) In essence, we extract a single vector for each sentence, and pass it through a couple of text-summarisation layers, which score each sentence based on its importance, and accumulate the most important sentences to provide to the user. As for the frontend, the user is presented with a text box, where the user can paste any text, and within a few seconds, the user is provided with the summary.
The entire app is based on the [Google Cloud App Engine](https://cloud.google.com/appengine). I use a python3.9 runtime to power the application, along with Flask as a web framework, to create the API which accepts the text, and provides the user with a summary.
## Challenges that I ran into
Except BERT, everything was new for me. While I have been studying and reading research papers in the field of Natural Language Processing for a long time, I had never written a web-app in Flask. In fact, I didn’t know how to use Flask in the first place. I have had some experience writing web apps using Laravel, and still, that didn’t help me with Flask. 
Then came the Google Cloud App Engine, for which, I literally signed up when the hackathon started. Fortunately, the guide to using the app engine was pretty helpful, and helped me set it up, not before running into some roadblocks, of course. It took me hours before I could run a successful deploy operation, because, apparently, you can’t upload very large files from the deploy operation and I was trying to upload a large BERT model, so I had to ultimately use a base BERT model.
## Accomplishments that I’m proud of
All the steps involved in realising this project. I discovered Flask and the Google App Engine, and am now actively considering moving my existing projects to the app engine, because of the scalability and reliability it offers. I am particularly proud that I could bridge the frontend, and the backend, and obtain the summary of whatever text the user has provided.
## What's next for Shorty - Summarise Anything
We could incorporate abstractive text summarisation into Shorty, wherein we generate language based on the context provided. While abstractive text summarisation is yet to become mainstream, I believe that it could really help summaries be more coherent and readable. Or, we could go for a hybrid approach, generating summaries by amalgamating the two approaches.
