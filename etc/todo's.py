# TODO's

# 1
# TODO Fix the issue where the issue where the sentence is left un-generated by the token limit
# TODO Make a connection to a DB that stores user data, somehow keeps it secure (read up on this) (@Ekansh has already done this, need to auth and integrate)
# TODO Optimize storage data speeds (^)
# TODO Make a work around for storing JSON's (Using the DB ^)
# TODO Auth (@EKANSH)

# 2
# TODO Optimize the path-way for using the model, and initializing it (on it)
# TODO Update the pathway, so it's very linear, but also make sure the code is build-upon-able (Done)(6.1)
# TODO try memory management, if time permits (HOW)(6.1)
# TODO Make CuBlas work, find the code that used to make it work (Done)
# TODO Make sure it works only once per initliaisation (on it, 2.1)
# TODO Make it so that multiple people can use it at the same time using only one branch of the AI model (I think this should not even be listed)

# 3
# TODO UX
# TODO Make it so that it's the best model that can be used (Need to find a good sentence transformer)(6.1)
# TODO Find a good prompt for staying on context (I think I found it)

# 4
# TODO Indexing
# TODO Use a good model for the sentence transformers, space and quality wise (3.1)(6.1)
# TODO Make sure the indexing works as intended with a 100% hit ratio (It's going to 60-70% at max)

# 5
# TODO Use cases
# Dashboard: (Contract Insights)
# Commitments to meet (both ways), defaulting against contract, risks, how is the comparitive performance, payment milestones
# Summarization:
# Drafting document, summarize, talk to summary
# AI Query Bot:
# Query to constitution, Dumbing down words via indexing of dictionary

# 6
# References
# https://huggingface.co/docs/diffusers/optimization/fp16#memory-and-speed <-For optimizing the model loading and using

# 7
# ! Json Design
# userName(int(6))
# auth(0/1)
#       TODO [Need to make edge case for this, in case auth fails, there is no check on UN, auth is done by backend]
# cCont(var) [Contains CURRENT context]
# xCont(var) [Contains WHOLE context]
# mode(int) [Each mode has a name and integer assigned to it] (5):
# ?     [
#       1: Talk to constituion / ask questions regarding law
#       2: Summarization
#       3: Talk to summary (Used both 1 and 2, calls a portion of 1)
#       4: Draft Document (Can use/call a portion 2)
#       5: Master mode (God Mode) (Make special username for it, bypass AUTH and backend AUTH)
# ?     ]
