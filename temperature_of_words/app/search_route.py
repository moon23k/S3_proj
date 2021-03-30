from flask import Flask, render_template, request, Blueprint
from joblib import load
from utils.profanity_pred import get_tweet_text, text_processing
from wordcloud import WordCloud, ImageColorGenerator
from utils.bow import emb_model_gen

bp = Blueprint('search', __name__)
profanity_clf = load("app/profanity_clf")


@bp.route('/search', methods=('GET', 'POST'))
def profanity_check(search_word, search_cnt):
    if request.method == 'POST':
        search_word = request.form.form['text']

        tweets = get_tweet_text(search_word)
        tweets = text_processing(tweets)

    # get the prediction
        profanity_rst = profanity_clf.predict(tweets)

        return render_template('search.html', rst=profanity_rst)
    return '검색어를 입력해주세요'

'''
def get_wordcloud(search_word, search_cnt):
    import matplotlib.pyplot as plt
    model = emb_model_gen(search_word, search_cnt)

    similar_words = model.most_similar(search_word, topn=10)
    wc_text = ' '.join([word[0] for word in similar_words])
    wordcloud = WordCloud(max_font_size=40, background_color='white').generate(wc_text)

    #wordcloud.to_file("models/img/{}_wordcloud.png".format(search_word))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
'''