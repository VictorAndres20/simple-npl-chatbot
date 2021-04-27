from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from src.steps.second_text_preprocess_corpus.nltk_corpus import lem_normalize
from src.steps.third_similar_response.manual_responses import q_response
import random


def get_similar_indexes(flat):
    similar_idx = []
    total = len(flat)
    mean = sum(flat[:-1]) / len(flat[:-1])
    max_mean = flat[-2]
    mean_apx = (mean + max_mean) / 2
    if mean_apx > 0:
        for i, d in enumerate(flat):
            if d > mean_apx:
                similar_idx.append(total - i)
    return similar_idx[:-1]


def response(user_msg, sent_tokens):
    robot_response = ''
    sent_tokens.append(user_msg)
    t_fid_f_vec = TfidfVectorizer(tokenizer=lem_normalize, stop_words=stopwords.words('spanish'))
    t_fid_f = t_fid_f_vec.fit_transform(sent_tokens)

    # eval sim
    vals = cosine_similarity(t_fid_f[-1], t_fid_f)
    sims = vals.argsort()[0]
    flat = vals.flatten()
    flat.sort()
    print(flat)
    # req_tfidf = flat[-2]
    similar_idx = get_similar_indexes(flat)
    # if req_tfidf == 0:
    if len(similar_idx) == 0:
        if random.choice([0, 1]) > 0:
            robot_response = robot_response + 'No te puede entender, puedes repetir? por fis'
        else:
            robot_response = "No te entendí muy bien, pero... "
            robot_response = robot_response + q_response()
    else:
        idx = random.choice(similar_idx) * -1
        robot_response = robot_response + sent_tokens[sims[idx]]

    sent_tokens.remove(user_msg)

    return robot_response
