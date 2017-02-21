Title: The Metropolitan Police and your phone
Date: 2012-05-18 10:08
Author: Paul Bailey
Slug: the-metropolitan-police-and-your-phone

BBC News has published a story (actually posted last night) with the
headline [Met Police to extract suspects' mobile phone data][].

The story is seeing some traction on Twitter this morning, so I thought
I'd dig in a little, and see what I could find.

It appears that the system that the Met have bought is produced by
[Radio Tactics][]. From having a look at their site, my guess is that
they've bought [ACEOS Kiosk][]. Looking at the ["full datasheet"][], the
selling point of the system is pulling data from various electronic
devices, and storing that data securely, with a full audit trail.

Thumbs up to that. If the police want to acquire this data, I want it to
be secure. But what else is it doing? Actually, it's difficult to tell
for sure, without a more comprehensive description. what does seem clear
is that it understands the layout of data internally on lots of devices,
in order to be able to extract (for example) text messages, IM
conversations, and so on. The operator doesn't need to know anything
about the internal implementation of the device to be able to extract
and archive data on the phone.

What is less clear is whether it can bypass hardware encryption on these
devices. My understanding is that all BlackBerry devices, all iOS
devices from iPhone 3GS onwards, and recent Android devices (because of
the fragmentation of this OS, it wasn't quite so clear which ones)
encrypt, in hardware, all their data stored internally.

This means, that without a passcode, data can't be read directly from
the internal storage. That read access would be how the product extracts
information. Nowhere in the description of ACEOS does it detail cracking
encryption like this. If it did, I imagine that would be a big selling
point. Indeed, if this hardware encryption was easily cracked, that
would be a big technology story too.

It seems far more likely to me that this product is about rapidly and
efficiently extracting data that would have previously required a
forensic specialist. I don't think that's a bad thing, and my guess is
that it can't be done without your passcode anyway (you do have one set,
don't you?).

If the police suspect that your phone has been used for criminal
activity, then you'll be obliged to give them the passcode anyway (I
think that not doing so is an offence). Encryption or not, they'll get
onto your phone, if they have reasonable suspicion of criminal activity.

So, onto retention of the data, and that's where the real problem is.
From the original article:

A Met Police spokesman told the BBC that when a suspect was released,
"data received from the handsets is retained and handled in accordance
with other data held by the MPS [Metropolitan Police Service]" -
regardless of whether charges had been brought.

So actually, this isn't a technology story at all. If you refuse to give
the police your passcode, or wilfully delete data from the phone, you've
broken the law anyway. The latest devices have sufficient means to
protect your data from casual extraction. The issue here is about data,
and retention thereof, and we've been down this road with DNA,
fingerprints, any information that the police might want to retain to
make their job easier.

The solution to this particular problem is a change of policy, not a 79p
app that enables you to destroy evidence.

</p>

  [Met Police to extract suspects' mobile phone data]: http://www.bbc.co.uk/news/technology-18102793
  [Radio Tactics]: http://www.radio-tactics.com
  [ACEOS Kiosk]: http://www.radio-tactics.com/products/law/aceso-kiosk
  ["full datasheet"]: http://www.radio-tactics.com/datasheets/rt-ds-ukv7-aceso-1332426274-1334334584.pdf
