# WheresMyField

When entering a new research field, how do you know which search terms to use to find the right literature? How do you understand who the key researchers are in your new field? Which journals does the field currently publish in?

The long way round to find this out is through months of literature searching and meetings. Whilst learning is fun, a substantial amount of time, effort and resource that goes into starting a new research project could be reallocated from 'understanding the field' However, there is a quicker way: journal article metadata, plus some magic

are the key search terms to use, who are the top authors in the field, and which journals are popular for that research topic. This knowledge base is often developed over months of literature research. However, this knowledge could be more quickly synthesised using the available metadata of the scholarly literature.

You can currently search the metadata of the scholarly literature through proprietary services, such as Web of Science. However, with this metadata available through APIs, we can hand the power of this database

Arcas uses a common language to access structured metadata from multiple journals via API calls. Using Arcas, we have built a database of scholarly literature metadata. The power of being able to access this metadata lies in how we use the data.

'Where's my field?' is a web app for researchers to search for a keyword term and understand the surrounding research field in terms of: other keywords that are commonly published with the search term, authors who are publishing in the field, and the journals in which they are publishing. This overview of a field is the knowledge that is commonly acquired through several months of literature searching and work in a field. Presenting this overview in a simple visualisation breaks down the barrier of entry to a new field, and guides deeper research efforts.



Sustainability journey:

* Web development:

  * Make it deployable on Azure or AWS, i.e. server agnostic


Ultimately, the power of exploring the literature via the availble metadata rests on the depth of the data available. Future work could call in metadata from various aggregator services and original sources, such as Europe PubMedCentral (biomedical literature), grants data, UK data discovery service, Jisc Sherpa/Romeo, ORCiD, ...
