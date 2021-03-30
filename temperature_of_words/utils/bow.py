import pandas as pd
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import joblib
from utils.d_pre import tokenize
from utils.profanity_pred import get_tweet_text
from gensim.models import Word2Vec


def emb_pre(search_word, search_cnt):
    lst = get_tweet_text(search_word, search_cnt)
    rst = pd.DataFrame(np.array(lst)).rename(columns={0: 'text'})
    t_df = tokenize(rst)
    return t_df


def emb_model_gen(search_word, search_cnt=100):
    t_df = emb_pre(search_word, search_cnt)

    num_features = 100

    emb_model = Word2Vec(t_df,
                         size=num_features,
                         iter=100,
                         window=10,
                         min_count=1,
                         seed=42,
                         sample=1e-3,
                         workers=-1,
                         sg=1)

    emb_model.init_sims(replace=True)

    return emb_model
