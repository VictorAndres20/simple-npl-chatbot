from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from src.steps.second_text_preprocess_corpus.nltk_corpus import lem_normalize


def response(user_msg, sent_tokens):
    robot_response = ''
    sent_tokens.append(user_msg)
    t_fid_f_vec = TfidfVectorizer(tokenizer=lem_normalize, stop_words=stopwords.words('spanish'))
    t_fid_f = t_fid_f_vec.fit_transform(sent_tokens)

    # eval sim
    vals = cosine_similarity(t_fid_f[-1], t_fid_f)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        robot_response = robot_response + 'No te puede entender, puedes repetir? por fis'
    else:
        robot_response = robot_response + sent_tokens[idx]

    sent_tokens.remove(user_msg)

    return robot_response
