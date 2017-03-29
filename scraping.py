import arcas
from tqdm import tqdm

keywords = ['sustainable software', 'replicability', 'reproducibility',
            'dopamine']

pbar = tqdm(total=(len(keywords) * 5))
for p in [arcas.Plos, arcas.Plos, arcas.Arxiv, arcas.Springer]:

    api = p()
    start = 1
    switch = True
    for key in keywords:
        while switch is not False:
            parameters = api.parameters_fix(title=key, records=10, start=start)

            url = api.create_url_search(parameters)
            request = api.make_request(url)
            root = api.get_root(request)
            raw_articles = api.parse(root)
            try:
                for art in raw_articles:
                    article = api.to_dataframe(art)
                    api.export(article, 'data/results_{}_{}_{}.json'.format(
                        api.__class__.__name__, key, start))
            except:
                switch = False
            start += 10
        pbar.update(1)

