from eventregistry import *
from CategoryExtraction import compute_categories_fraction_dict


def CreateSourceArticleDict(articleDict):
    res = {
        "sourceId": articleDict["sourceId"],
        "sourceTitle": articleDict["sourceTitle"],
        "sourceUri": articleDict["sourceUri"],
        "articles": list()
    }
    return res


def SortArticlesBySource(numIters, articlesFile):
    articlesDict: dict = json.load(open(articlesFile))
    i = 0

    for article in articlesDict.values():
        sourceId = article["sourceId"]
        sourceFileName = "SourceArticles10000/" + str(sourceId) + ".json"
        print(sourceFileName)

        if os.path.isfile(sourceFileName):
            f = open(sourceFileName)
            sourceDict = json.load(f)
        else:
            sourceDict = CreateSourceArticleDict(article)

        sourceDict["articles"].append(article)

        with open(sourceFileName, 'w') as fl:
            json.dump(sourceDict, fl)
        i += 1
        if (i == numIters):
            return


#SortArticlesBySource(10000,'aljazArticles1000/articles.json')


def MakeSourceInfoJsons(sourceArticlesDir, sourceInfoDir):

    for filename in os.listdir(sourceArticlesDir):
        sourceArticlesDict: dict = json.load(open(sourceArticlesDir + "/" + filename))
        articles: list = sourceArticlesDict["articles"]

        sourceInfoDict: dict = {
            "sourceId": sourceArticlesDict["sourceId"],
            # "sequential number": j,
            "sourceTitle": sourceArticlesDict["sourceTitle"],
            "sourceUri": sourceArticlesDict["sourceUri"],
            "numArticles": len(articles),
            "avgTitleLength": ComputeAvgTitleLength(articles),
            # "sportsCategoryFraction": FractionArticlesPerCategory("Sports", articles),
            # "societyCategoryFraction": FractionArticlesPerCategory("Society", articles),
            # "scienceCategoryFraction": FractionArticlesPerCategory("Science", articles),
            # "businessCategoryFraction": FractionArticlesPerCategory("Business", articles),
            # "healthCategoryFraction": FractionArticlesPerCategory("Health", articles),
            # "homeCategoryFraction": FractionArticlesPerCategory("Home", articles),
            # "recreationCategoryFraction": FractionArticlesPerCategory("Recreation", articles),
            # "shoppingCategoryFraction": FractionArticlesPerCategory("Shopping", articles),
            # "gamesCategoryFraction": FractionArticlesPerCategory("Games", articles),
            # "artsCategoryFraction": FractionArticlesPerCategory("Arts", articles),
            # "computersCategoryFraction": FractionArticlesPerCategory("Computers", articles)
        }

        # compute the frequency of each category and add it to the dictionary
        ctg_dict = compute_categories_fraction_dict(articles)
        sourceInfoDict.update(ctg_dict)

        sourceInfoFilename = sourceInfoDir + "/" + filename
        with open(sourceInfoFilename, 'w') as fl:
            json.dump(sourceInfoDict, fl)


def ComputeAvgTitleLength(articleList: list):
    sum = 0
    numArticles = len(articleList)
    for article in articleList:
        title: str = article["title"]
        sum += len(title)
    avg = float(sum) / float(numArticles)
    return avg


def FractionArticlesPerCategory(sougthCtg: str, articleList: list):
    totalCount = 0
    for article in articleList:
        categories: list = article["categories"]
        for category in categories:
            if (category["label"].startswith(sougthCtg)):
                totalCount += 1
    return float(totalCount) / float(len(articleList))


MakeSourceInfoJsons("SourceArticles10000", "SourceInfo10000")
