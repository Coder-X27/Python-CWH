import re

str = """
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com (may go to user.name@example.com inbox depending on mail server)
x@example.com (one-letter local-part)
example-indeed@strange-example.com
admin@mailserver1 (local domain name with no TLD, although ICANN highly discourages dotless email addresses[10])
example@s.example (see the List of Internet top-level domains)
" "@example.org (space between the quotes)
"john..doe"@example.org (quoted double dot)
mailhost!username@example.org (bangified host route used for uucp mailers)
user%example.com@example.org (% escaped mail route to user@example.com via example.org)

Invalid email addresses
Abc.example.com (no @ character)
A@b@c@example.com (only one @ is allowed outside quotation marks)
a"b(c)d,e:f;g<h>i[j\k]l@example.com (none of the special characters in this local-part are allowed outside quotation marks)
just"not"right@example.com (quoted strings must be dot separated or the only element making up the local-part)
this is"not\allowed@example.com (spaces, quotes, and backslashes may only exist when within quoted strings and preceded by a backslash)
this\ still\"not\\allowed@example.com (even if escaped (preceded by a backslash), spaces, quotes, and backslashes must still be contained by quotes)
1234567890123456789012345678901234567890123456789012345678901234+x@example.com (local-part is longer than 64 characters)
i_like_underscore@but_its_not_allow_in_this_part.example.com (Underscore is not allowed in domain part)
Common local-part semantics
According to RFC 5321 2.3.11 Mailbox and Address, "...the local-part MUST be interpreted and assigned semantics only by the host specified in the domain of the address." This means that no assumptions can be made about the meaning of the local-part of another mail server. It is entirely up to the configuration of the mail server.

Local-part normalization
Interpretation of the local part of an email address is dependent on the conventions and policies implemented in the mail server. For example, case sensitivity may distinguish mailboxes differing only in capitalization of characters of the local-part, although this is not very common.[11] Gmail ignores all dots in the local-part of a @gmail.com address for the purposes of determining account identity.[12]

Subaddressing
Some mail services support a tag included in the local-part, such that the address is an alias to a prefix of the local part. For example, the address joeuser+tag@example.com denotes the same delivery address as joeuser@example.com. RFC 5233,[13] refers to this convention as sub-addressing, but it is also known as plus addressing, tagged addressing or mail extensions.

Addresses of this form, using various separators between the base name and the tag, are supported by several email services, including Andrew Project (plus),[14] Runbox (plus), Gmail (plus),[15] Rackspace (plus), Yahoo! Mail Plus (hyphen),[16] Apple's iCloud (plus), Outlook.com (plus),[17] ProtonMail (plus),[18] Fastmail (plus and Subdomain Addressing),[19] postale.io (plus),[20] Pobox (plus),[21] MeMail (plus),[22] MMDF (equals), Qmail and Courier Mail Server (hyphen).[23][24] Postfix and Exim allow configuring an arbitrary separator from the legal character set.[25][26]

The text of the tag may be used to apply filtering,[23] or to create single-use, or disposable email addresses.[27]

In practice, the form validation of some web sites may reject characters such as "+" in an email address – treating them, incorrectly, as invalid characters. This can lead to an incorrect user receiving an e-mail if the "+" is silently stripped by a website without any warning or error messages. For example, an email intended for the user-entered email address foo+bar@example.com could be incorrectly sent to foobar@example.com. In other cases a poor user experience can occur if some parts of a site, such as a user registration page, allow the "+" character whilst other parts, such as a page for unsubscribing from a site's mailing list, do not.

Validation and verification

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed. (July 2019) (Learn how and when to remove this template message)
Email addresses are often requested as input to website as validation of user existence. Other validation methods are available, such as cell phone number validation, postal mail validation, and fax validation.

An email address is generally recognized as having two parts joined with an at-sign (@), although technical specification detailed in RFC 822 and subsequent RFCs are more extensive.[28]

Syntactically correct, verified email addresses do not guarantee that an email box exists. Thus many mail servers use incorrectly other techniques and check the mailbox existence against relevant systems such as the Domain Name System for the domain or using callback verification to check if the mailbox exists. Callback verification is an imperfect solution, as it may be disabled to avoid a directory harvest attack.

Several validation techniques may be utilized to validate an user email address. For example,[29]

Verification links: Email address validation is often accomplished for account creation on websites by sending an email to the user-provided email address with a special temporary hyperlink. On receipt, the user opens the link, immediately activating the account. Email addresses are also useful as means of delivering messages from a website, e.g., user messages, user actions, to the email inbox.
Formal and informal standards: RFC 3696 provides specific advice for validating Internet identifiers, including email addresses. Some websites instead attempt to evaluate the validity of email addresses through arbitrary standards, such as by rejecting addresses containing valid characters, such as + and /, or enforcing arbitrary length limitations. Email address internationalization provides for a much larger range of characters than many current validation algorithms allow, such as all Unicode characters above U+0080, encoded as UTF-8.
Algorithmic tools: Large websites, bulk mailers and spammers require efficient tools to validate email addresses. Such tools depend upon heuristic algorithms and statistical models.[30]
Sender reputation: An email sender's reputation may used to attempt to verify whether the sender is trustworthy or a potential spammer. Factors that may be incorporated into an assessment of sender reputation include the quality of past contact with or content provided by, and engagement levels of, the sender's IP address or email address.
Browser-based verification: HTML5 forms implemented in many browsers allow email address validation to be handled by the browser.[31]
Some companies offer services to validate an email address, often using an application programming interface, but there is no guarantee that it will provide accurate results.

Internationalization
The IETF conducts a technical and standards working group devoted to internationalization issues of email addresses, entitled Email Address Internationalization (EAI, also known as IMA, Internationalized Mail Address).[32] This group produced RFC 6530, 6531, 6532 and 6533, and continues to work on additional EAI-related RFCs.

The IETF's EAI Working group published RFC 6530 "Overview and Framework for Internationalized Email", which enabled non-ASCII characters to be used in both the local-parts and domain of an email address. RFC 6530 provides for email based on the UTF-8 encoding, which permits the full repertoire of Unicode. RFC 6531 provides a mechanism for SMTP servers to negotiate transmission of the SMTPUTF8 content.

The basic EAI concepts involve exchanging mail in UTF-8. Though the original proposal included a downgrading mechanism for legacy systems, this has now been dropped.[33] The local servers are responsible for the local-part of the address, whereas the domain would be restricted by the rules of internationalized domain names, though still transmitted in UTF-8. The mail server is also responsible for any mapping mechanism between the IMA form and any ASCII alias.

EAI enables users to have a localized address in a native language script or character set, as well as an ASCII form for communicating with legacy systems or for script-independent use. Applications that recognize internationalized domain names and mail addresses must have facilities to convert these representations.

Significant demand for such addresses is expected in China, Japan, Russia, and other markets that have large user bases in a non-Latin-based writing system.

For example, in addition to the .in top-level domain, the government of India in 2011[34] got approval for ".bharat", (from Bharat Ga?arajya), written in seven different scripts[35][36] for use by Gujrati, Marathi, Bangali, Tamil, Telugu, Punjabi and Urdu speakers. Indian company XgenPlus.com claims to be the world's first EAI mailbox provider,[37] and the Government of Rajasthan now supplies a free email account on domain ????????.???? for every citizen of the state.[38] A leading media house Rajasthan Patrika launched their IDN domain ???????.???? with contactable email.

Internationalization examples
The example addresses below would not be handled by RFC 5322 based servers, but are permitted by RFC 6530. Servers compliant with this will be able to handle these:

Latin alphabet with diacritics: Pelé@example.com
Greek alphabet: d???µ?@pa??de??µa.d???µ?
Traditional Chinese characters: ??@??.??
Japanese characters: ???@??.??
Cyrillic characters: ???????@?-??????????.??
Devanagari characters: ??????@???????.????
"""

email=re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]",str)
for items in email:
    print(items)