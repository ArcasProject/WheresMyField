# WheresMyField

## The concept

When entering a new research field, how do you know which search terms to use to find the right literature? How do you understand who the key researchers are in your new field? Which journals does the field currently publish in?

The long way round to find this out is through months of literature searching and meetings. Whilst learning is fun, a substantial amount of time, effort and resource that goes into starting a new research project could be reallocated from 'understanding the field' to 'starting the research'.

Discovering the metadata of research more efficiently is possible. Journal articles are accompanied by freely available structured metadata: journal name, author names, title, abstract. Several services offer entry points to this data, as a means of finding research articles, such as PudMed for the biomedical literature, and understanding the research network, such as Web of Science, Microsoft Academic and Yewno Discover. However, there is no free and open service that empowers researchers from any discipline to quickly understand their research field.

Arcas uses a common language to access structured metadata from multiple journals via API calls. Using Arcas, we have built a database of scholarly literature metadata, from some initial keywords. The power of being able to access this metadata lies in how we use the data. For this hack, we have created a web app to explore the Arcas database.

## The tool

'Where's my field?' is a web app for researchers to search for a keyword term and understand the surrounding research field in terms of: other keywords that are commonly published with the search term, authors who are publishing in the field, and the journals in which they are publishing. This overview of a field is the knowledge that is commonly acquired through several months of literature searching and work experience within a field. Presenting this overview in a simple visualisation breaks down the barrier of entry to a new field, saves time, and guides deeper research efforts.

## Future ideas

By building this web app with a modular architecture, we hope that future developers could enhance the features available and add additional features. For example:
* Similar keywords:
 * Strengthen your search by easily including additional keywords of interest and excluding irrelevant results
* Author network:
 * Disambiguate the top author list using ORCiD IDs
 * Present a network map of co-authors to understand key nodes
* Journals published in:
 * Incorporate journal policies from SHERPA/RoMEO
* Influential articles:
 * Include list of most influential articles in a field, by citation count or other metric
 * Incorporate Unpaywall to provide easy access to an open-access version of the article, and integrate the Open Access Button to allow researchers to request an archivable copy of the article where no open-access version is already available
* What's trending?
 * Incorporate a filter by publication date to enable users to distinguish recent versus historic data
* Export / share results:
 * Enable users to save, download, and share their search results, as a collection resource for the community

Ultimately, the power of exploring the literature via the availble metadata rests on the depth of the data available. The web app has been designed to operate agnostic of database, which would allow future development to call in data from various existing aggregator services and original sources, such as Europe PubMedCentral (biomedical literature), grants data, UK data discovery service, Jisc Sherpa/Romeo, ORCiD, ...



## Sustainability journey:

* Web development:

  * Make it deployable on Azure or AWS, i.e. server agnostic

