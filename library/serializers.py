from library.models import Article, Author, Year, Label, Strategies, KeyWord
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    papers_on_this_db = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = "__all__"

    def get_papers_on_this_db(self, obj):
        return obj.article_set.count()


class YearSerializer(serializers.HyperlinkedModelSerializer):
    papers_on_specific_year = serializers.SerializerMethodField()

    class Meta:
        model = Year
        fields = "__all__"

    def get_papers_on_specific_year(self, obj):
        return obj.article_set.count()


class LabelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ["label"]


class KeyWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyWord
        fields = ["key_word"]


class StrategiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Strategies
        fields = ["strategy_name"]


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(many=True, )
    date = YearSerializer()
    labels = LabelsSerializer(many=True, )
    key_word = KeyWordSerializer(many=True, )
    list_strategies = StrategiesSerializer(many=True)

    class Meta:
        model = Article
        fields = ('key', 'unique_key', 'title', 'author', 'date', 'abstract',
                  'pages', 'journal', 'labels', 'read', 'key_word',
                  'provenance', 'list_strategies')

    def create(self, validated_data):

        # Create the new article attributes
        date = Year.objects.create(year=validated_data['date'].get("year"))
        # create the article
        article = Article(date=date, title=validated_data['title'],
                          abstract=validated_data['abstract'],
                          key=validated_data['key'],
                          pages=validated_data['pages'],
                          journal=validated_data['journal'],
                          provenance=validated_data['provenance'])

        article.save()

        for author in validated_data['author']:
            article.author.add(Author.objects.create(name=author['name']))
        for label in validated_data['labels']:
            article.labels.add(Label.objects.create(label=label['label']))
        for strategy in validated_data['list_strategies']:
            article.list_strategies.add(Strategies.objects.create(
                strategy_name=strategy['strategy_name']))
        for keyword in validated_data['key_word']:
            article.key_word.add(KeyWord.objects.create(key_word=keyword[
                                                                 'key_word']))
        return article
