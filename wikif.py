import urllib.parse, urllib.request, json

def CallWikifier(text, lang="en", threshold=0.8):
    # Prepare the URL.
    data = urllib.parse.urlencode([
        ("text", text), ("lang", lang),
        ("userKey", "tznrrrpqisvzpiybfuztkvpebphurb"),
        ("pageRankSqThreshold", "%g" % threshold), ("applyPageRankSqThreshold", "true"),
        ("nTopDfValuesToIgnore", "200"), ("nWordsToIgnoreFromList", "200"),
        ("wikiDataClasses", "true"), ("wikiDataClassIds", "false"),
        ("support", "false"), ("ranges", "false"), ("minLinkFrequency", "2"),
        ("includeCosines", "true"), ("maxMentionEntropy", "3")
        ])
    url = "http://www.wikifier.org/annotate-article"
    # Call the Wikifier and read the response.
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout = 60) as f:
        response = f.read()
        response = json.loads(response.decode("utf8"))
    # Output the annotations.
    for annotation in response["annotations"]:
        print(f"""{annotation["title"]} ({annotation["url"]}), rank: {annotation["pageRank"]}""")

CallWikifier("""Record numbers of civilians have been killed and injured in Afghanistan in intense fighting since 1 May, when international forces began their final drawdown and the Taliban launched a major offensive.

The heavy toll so far comes largely from battles in rural areas, according to the UN. If the conflict were to spill into more densely populated towns and cities, the consequences could be catastrophic, it says in its report, The Protection of Civilians in Armed Conflict.

Swathes of the country have fallen to the insurgents since they launched their offensive two months ago to coincide with the original deadline authorities set for US and other forces to leave the country. The UN report is the first nationwide account of the impact of the fighting on civilians.

It notes near-record levels of casualties in the first six months of the year, with insurgent groups responsible for well over half of the deaths and injuries. It also says the “acute rise” in the two months since 1 May is of particular concern.

In that period 783 civilians were killed and 1,609 injured, almost equivalent to the toll during the first four months of the year, and the highest figures for May and June since the UN began keeping records in 2009. They are also likely to be the worst since the Taliban were toppled from power in 2001.

“I implore the Taliban and Afghan leaders to take heed of the conflict’s grim and chilling trajectory and its devastating impact on civilians,” said Deborah Lyons, the UN secretary general’s special representative for Afghanistan.

“The report provides a clear warning that unprecedented numbers of Afghan civilians will perish and be maimed this year if the increasing violence is not stemmed.”

Nearly two-thirds of the casualties were caused by insurgent groups, including the regional Isis franchise, the UN said. About a quarter were the responsibility of the government and its allies. The others could not be clearly attributed to any group.

No civilian casualties were attributed to actions of international forces for the first time since the UN began keeping records. The conflict is now almost entirely between Afghans, it said.

Women and girls have been particularly badly hit by the violence. Casualties for both groups reached record highs over the six months of the year, a trend the report described as sickening. The most shocking single incident was perhaps an attack on a girls school in Kabul in which at least 85 people were killed and more than 200 injured, the majority of them schoolgirls.

The increase in civilian casualties ends a four-year period in which they had steadily declined between January and June, despite increasing instability nationwide.

Improvised mines were the leading cause of casualties, responsible for more than one in three deaths and injuries. Recent fighting appears to have led to more being placed on roads and inside homes in areas the Taliban seized.

Because they tend to be activated by whoever happens to step on them or dig them up, they are indiscriminate and may be illegal under international law, the UN said.

We “documented many incidents where the devices were emplaced on the roads leading into areas under the control of anti-government elements, as well as left in and around civilian homes in villages from which they had recently departed,” the report said.

Fighting on the ground caused the second highest number of casualties, and if the battle for control of Afghanistan moves into urban areas the figures could climb further.

“Much of the battlefield action during the most deadly months of May and June took place outside cities, in areas with comparatively low population levels,” the report said.

“The UN is gravely concerned that if intensive military action is undertaken in urban areas with high population densities, the consequences for Afghan civilians could be catastrophic.”

Targeted killings of civilians by insurgents was the third leading cause of casualties, followed by Afghan army airstrikes. The number of airstrikes over the first six months of the year more than tripled from 2020 levels to more than 4,250 missions, and civilian casualties from these attacks doubled.

The UN also raised concern about destruction and looting in areas that came under Taliban control in May and June. Targets included “civilian homes, schools, clinics, electricity and mobile phone towers, city water supplies, bridges, shops, and residential apartment buildings,” the report said.

“The vast majority of incidents of intentional destruction of civilian property … were attributed to or done with the complicity of Taliban fighters after they took control of a new area.”

Lyons called on the Taliban and Afghan leaders to “intensify your efforts at the negotiating table, stop the Afghan-against-Afghan fighting. Protect the Afghan people and give them hope for a better future.”""")