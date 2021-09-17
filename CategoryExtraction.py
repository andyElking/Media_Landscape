from typing import Dict, List
import json
category_list = json.load(open('allCategoriesList.json'))

def compute_categories_fraction_dict(articles_list: List[dict]):
    category_dict: Dict[str, float] = dict.fromkeys(category_list, 0.0)

    # go over all the articles from this source and add up the occurrences of each category
    for article in articles_list:
        categories: List[dict] = article["categories"]
        for category in categories:
            full_label: str = category["label"]  # get the label of the category from the article
            # now split the label into all three category levels
            split_label = full_label.split('/')
            for i in range(len(split_label)):
                partial_label = "/".join(split_label[:(i + 1)])
                # this returns:
                # Recreation
                # Recreation/Guns
                # Recreation/Guns/Competition_Shooting
                category_dict[partial_label] = category_dict[
                                                   partial_label] + 1.0  # write the number of occurrences back into the dict

    # now divide each category frequency by the total number of articles to get a proportion

    num_articles = float(len(articles_list))
    for ctg in category_dict.keys():
        proportion = category_dict[ctg] / num_articles
        category_dict[ctg] = proportion

    return category_dict


def list_categories(num_iters, articlesFile, level):
    articles_dict: dict = json.load(open(articlesFile))
    category_dict = {"Recreation": True}
    i = 0
    for article in articles_dict.values():
        for category in article["categories"]:
            full_label: str = category["label"]  # get the label of the category from the article
            # now split the label into all three category levels
            split_label = full_label.split('/')
            for i in range(min(len(split_label), level)):
                partial_label = "/".join(split_label[:(i + 1)])
                # as above
                category_dict[partial_label] = True
        # if i == num_iters:
        #     return list(category_dict.keys())
    return list(category_dict.keys())

# l = list_categories(10000,'aljazArticles1000/articles.json',2)
# with open('level2Categories.json', 'w') as fl:
#     json.dump(l, fl)
