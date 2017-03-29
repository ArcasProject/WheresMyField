# WheresMyField

## The concept

When entering a new research field, how do you know which search terms to use to find the right literature? How do you understand who the key researchers are in your new field? Which journals does the field currently publish in?

Understanding a field takes months of literature searching and meetings. There is a more efficient way to visualise the landscape of a research field. Journal articles are accompanied by freely available structured metadata: journal name, author names, title, abstract. Several services offer entry points to this data. To find research articles by keyword, you can use CORE, Google Scholar, PubMed (for biomedical literature) or other search sites, however these services display the results as a list of articles, and we think that a more intuitive visualisation and overview of the data would be more useful as an entry point. To understanding the research network - who's doing what and where, you could use Web of Science, Microsoft Academic or Yewno Discover. However, none of these services are freely available or open-access.

With 'WheresMyField', we provide a free, open, no-login-required service to help any researcher to understanding the landscape of a research field more quickly. 

## The tool

'Where's my field?' is a web app for researchers to search for a keyword term and understand the surrounding research field in terms of: other keywords that are commonly published with the search term, authors who are publishing in the field, and the journals in which they are publishing. This overview of a field is the knowledge that is commonly acquired through several months of literature searching and work experience within a field. Presenting this overview in a simple visualisation breaks down the barrier of entry to a new field, saves time, and guides deeper research efforts.

There are data sources available that cover a wide field of scholarly literature metadata, such as CORE. The power of being able to access this metadata lies in how we use the data. For this hack, we have created a web app to explore a small database of scholarly literature metadata that was populated by Arcas. Arcas uses a common language to access structured metadata from multiple journals via API calls. 

## Implementation

DIAGRAM OF SOFTWARE ARCHITECTURE

## Roadmap

By building this web app with a modular architecture, we hope that future developers could enhance the features available and add additional features. 

Development should be guided by user desire. Our vision is mocked up on Balsamqiq (The_Vision_in_Balasamiq.xml file) and accompanied by a_user_story.md - do you agree? What would you like to see? What would you proritise? Comments and feedback welcome at roadmap issue.

For example:
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

Ultimately, the power of exploring the literature via the availble metadata rests on the depth of the data available. The web app has been designed to operate agnostic of database, which would allow future development to call in data from various existing aggregator services and original sources, such as:
* CORE (https://core.ac.uk/services)
* Europe PubMedCentral (biomedical literature)
* Jisc's PubRouter service https://pubrouter.jisc.ac.uk/
* SHERPA RoMEO (http://www.sherpa.ac.uk/romeo/index.php)
* ORCID
* Grants data (Gateway)
* UK research data discovery (https://www.jisc.ac.uk/rd/projects/uk-research-data-discovery) and other data repositories or portals
* Symplectic elements (http://symplectic.co.uk/)

