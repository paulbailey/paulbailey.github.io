Title: What do IP addresses tell us anyway?
Date: 2012-05-09 09:18
Author: Paul Bailey
Slug: what-do-ip-addresses-tell-us-anyway

Yesterday I saw some misinformation being distributed about IP
addresses. It was in the context of a rather petty disgreement about
someone's identity on Twitter, but it did make me think that this is an
area that plenty of people don't really understand.

With that in mind, here's a brief run-down of what an IP address is,
what it says about you, and what it doesn't. I'm by no means a
networking expert, but I am an IT professional and hope that I have a
decent enough grasp of the topic to explain things correctly. Please
feel free to correct me if I make any mistakes.

One of these addresses (IPv4 specifically, which is the type of address
that is still commonly used across the internet) is formed of four
numbers, from 0 to 255, separated by dots. Every device connected to a
network will have at least one of these addresses.

The more observant amongst you will have spotted a flaw in the system.
If the addresses take the format 192.168.0.34, then we only have
4,228,250,625 possible addresses. That might seem like a lot, but when
you think of every phone, tablet, laptop, and computer in the world, not
to mention TVs, DVD players and others, it's not very many at all.

That's wny we have the concept of **private** and **public** IP
addresses. There are ranges of addresses that are designated as
"private", which can be reused on internal networks (like your wi-fi
network at home). The most common range used is 192.168.X.X

If you just had a private IP address though, you would never be able to
connect to anything on the internet, just to other devices on your home
network. This is where your broadband router comes in. It does the
clever trick of translating your private IP address into a public one.

Your ISP (that's BT, or Virgin Media for example) assigns a public IP
address to your router, which then shares it with all the devices
connected to your network. This is why an IP address isn't quite enough
to identify someone online. The public address could be shared between
several people. To someone outside your own home network, they would
never know who in the house is connected.

The situation becomes even more confused because of the way ISPs tend to
distribute these public IP addresses to their customers' routers. These
addresses tend to be 'dynamic', which means that a particular public IP
address isn't tied to a particular account, let alone a particular
internet user. What's my IP address today might be yours tomorrow. 

Don't be fooled though. My IP address is assigned 'dynamically' by my
ISP, but it has only changed once in the last three months, when I
upgraded my connection speed. In that time, the router was rebooted
several times, and it always ended up with the same address.

Even if your ISP does change IP addresses more frequently, it isn't
happening second by second. If you think about it, the IP address is
where a web server sends its pages to, where an mail server sends its
e-mails to. If that address is constantly changing, then things would
fail to arrive, and need to be re-sent, all the time.

Even this dynamic changing doesn't hide you from law enforcement,
obviously. ISPs keep records of which IP address is assigned to which
customer at what time. It's this record-keeping that probably means
public IP addresses change less than they might. Some ISPs also offer
static public IP addresses, which are useful for users that want to be
able to connect to their home network remotely.

Still, you do have a degree of anonymity from people hosting servers,
who don't have a warrant to get your account information. All they can
really derive from your IP address is your (rough) geographic location
(the accuracy of this varies wildly), and probably who your ISP is. If
you're connecting through a work computer, they probably have a decent
idea of the company you work for, but this depends on how large the
company is, and whether they have their own public IP addresses.

It's also worth noting that public IP addresses aren't shared across ISP
customers. If they were, a web server wouldn't know whether to send the
BBC Sport homepage to you, or your neighbour. A public IP address is
unique to the router in your home, at a given point in time.

In summary, your IP address isn't some Prisoner-esque number that
identifies you to all and sundry, but neither is it an unidentifable
detail that gives nothing away about you.

It could, for example, be used to corrolate two online identities as the
same person (or at least on the same private network). That would be a
fair assumption if the IP addresses logged were the same, and there
wasn't a lot of time between the requests logged.

 
